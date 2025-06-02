I'll help fix the race condition in `ProducerImpl.closeAsync()`. The issue occurs when the connection is being closed at the same time as the producer, leading to a potential NPE. Here's the fixed code:

```java
@Override
public CompletableFuture<Void> closeAsync() {
    final State currentState = getAndUpdateState(state -> {
        if (state == State.Closed) {
            return state;
        }
        return State.Closing;
    });

    if (currentState == State.Closed || currentState == State.Closing) {
        return CompletableFuture.completedFuture(null);
    }

    Timeout timeout = sendTimeout;
    if (timeout != null) {
        timeout.cancel();
        sendTimeout = null;
    }

    stats.cancelStatsTimeout();

    ClientCnx cnx = getClientCnx();
    if (cnx == null || currentState != State.Ready) {
        log.info("[{}] [{}] Closed Producer (not connected)", topic, producerName);
        synchronized (this) {
            setState(State.Closed);
            client.cleanupProducer(this);
            PulsarClientException ex = new PulsarClientException.AlreadyClosedException(
                    "Producer was already closed");
            pendingMessages.forEach(msg -> {
                msg.callback.sendComplete(ex);
                msg.cmd.release();
                msg.recycle();
            });
            pendingMessages.clear();
        }

        return CompletableFuture.completedFuture(null);
    }

    long requestId = client.newRequestId();
    ByteBuf cmd = Commands.newCloseProducer(producerId, requestId);

    CompletableFuture<Void> closeFuture = new CompletableFuture<>();
    cnx.sendRequestWithId(cmd, requestId).handle((v, exception) -> {
        cnx.removeProducer(producerId);
        if (exception == null || !cnx.ctx().channel().isActive()) {
            // Either we've received the success response for the close producer command from the broker, or the
            // connection did break in the meantime. In any case, the producer is gone.
            synchronized (ProducerImpl.this) {
                log.info("[{}] [{}] Closed Producer", topic, producerName);
                setState(State.Closed);
                pendingMessages.forEach(msg -> {
                    msg.cmd.release();
                    msg.recycle();
                });
                pendingMessages.clear();
            }

            closeFuture.complete(null);
            client.cleanupProducer(this);
        } else {
            closeFuture.completeExceptionally(exception);
        }

        return null;
    });

    return closeFuture;
}
```

The key changes are:

1. Read the `cnx` variable just once at the beginning of the method and store it in a local variable to avoid potential race conditions where the connection could be nulled out between checks
2. Use the local `cnx` variable consistently throughout the method
3. The rest of the logic remains the same, but is now protected against NPEs due to concurrent connection closures

This change ensures that even if the connection is being closed concurrently, we'll either:
- Complete the close operation successfully if we got the connection reference before it was closed
- Handle the failure in the future callback if the connection was closed during the operation