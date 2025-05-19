Here's the fix for the NPE issue in `ApiClientImpl`. The problem occurs when handling null responses in `executeOnAll()`. I'll modify the code to check for null responses before processing them:

```java
private T handleResponse(Request request, Response response) throws IOException, APIException {
    // Add null check at the beginning
    if (response == null) {
        throw new APIException(request, new IllegalStateException("Received null response from server"));
    }

    // TODO: once we switch to jackson we can take the media type into account automatically
    final MediaType responseContentType;
    if (response.getContentType() == null) {
        responseContentType = MediaType.JSON_UTF_8;
    } else {
        responseContentType = MediaType.parse(response.getContentType());
    }

    if (!responseContentType.is(mediaType.withoutParameters())) {
        LOG.error("Accept header was {} but response is {}. Failing.", mediaType, responseContentType);
        throw new APIException(request, response);
    }
    if (responseClass.equals(String.class)) {
        return responseClass.cast(response.getResponseBody("UTF-8"));
    }

    final boolean responseCodeIsExpected = expectedResponseCodes.contains(response.getStatusCode());
    final boolean responseCodeIsSuccessful = response.getStatusCode() >= 200 && response.getStatusCode() < 300;
    if (responseCodeIsExpected || responseCodeIsSuccessful) {
        T result;
        try {
            if (response.getResponseBody().isEmpty()) {
                return null;
            }

            if (responseContentType.is(MediaType.JSON_UTF_8.withoutParameters())) {
                result = deserializeJson(response, responseClass);
            } else {
                LOG.error("Cannot deserialize content type {} expected {}, failing.", responseContentType, mediaType);
                throw new APIException(request, response);
            }

            if (result == null) {
                throw new APIException(request, response);
            }

            return result;
        } catch (Exception e) {
            LOG.error("Caught Exception while deserializing JSON request: ", e);
            LOG.debug("Response from backend was: " + response.getResponseBody("UTF-8"));

            throw new APIException(request, response, e);
        }
    } else {
        throw new APIException(request, response);
    }
}
```

And in the `executeOnAll()` method, we should also add a null check before processing the response:

```java
@Override
public Map<Node, T> executeOnAll() throws APIException {
    HashMap<Node, T> results = Maps.newHashMap();
    if (node == null && nodes == null) {
        nodes = serverNodes.all();
    }

    final Set<RequestContext> requestContexts = Sets.newHashSetWithExpectedSize(nodes.size());
    final Collection<Response> responses = Lists.newArrayList();

    ensureAuthentication();
    for (Node currentNode : nodes) {
        final URL url = prepareUrl(currentNode);
        try {
            final AsyncHttpClient.BoundRequestBuilder requestBuilder = requestBuilderForUrl(url);
            requestBuilder.addHeader(HttpHeaders.ACCEPT, mediaType.toString());

            // we need to build the request in case we have to throw an APIException in handleResponse()
            final Request request = requestBuilder.build();
            if (LOG.isDebugEnabled()) {
                LOG.debug("API Request: {}", request);
            }
            final ListenableFuture<Response> future = requestBuilder.execute(new AsyncCompletionHandler<Response>() {
                @Override
                public Response onCompleted(Response response) throws Exception {
                    responses.add(response);
                    return response;
                }
            });
            requestContexts.add(new RequestContext(currentNode, request, future));
        } catch (IOException e) {
            LOG.error("Cannot execute request", e);
            currentNode.markFailure();
        }
    }

    // Set 200 OK as standard if not defined.
    ensureExpectedResponseCodes();

    for (RequestContext context : requestContexts) {
        final Node node = context.node;
        final ListenableFuture<Response> future = context.listenableFuture;
        try {
            final Response response = future.get(timeoutValue, timeoutUnit);
            if (response != null) {  // Add null check here
                node.touch();
                final T result = handleResponse(context.request, response);
                results.put(node, result);
            } else {
                node.markFailure();
                throw new APIException(context.request, new IllegalStateException("Received null response from server"));
            }
        } catch (InterruptedException e) {
            LOG.error("API call Interrupted", e);
            node.markFailure();
        } catch (ExecutionException e) {
            if (e.getCause() instanceof ConnectException) {
                LOG.error("{}", e.getCause().getMessage());
            } else {
                LOG.error("API call failed to execute.", e);
            }
            node.markFailure();
        } catch (IOException e) {
            LOG.error("API failed due to IO error", e);
            node.markFailure();
        } catch (TimeoutException e) {
            LOG.error("API call timed out", e);
            node.markFailure();
        }
    }

    return results;
}
```

The changes add proper null checks for responses before processing them, which should prevent the NPE. When a null response is encountered, it will mark the node as failed and throw an appropriate APIException.