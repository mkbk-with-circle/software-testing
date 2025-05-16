## Buggy code
```java
package org.apereo.cas.authentication;

import org.apache.http.HttpResponse;
import org.apereo.cas.authentication.principal.Principal;
import org.apereo.cas.configuration.model.support.mfa.MultifactorAuthenticationProviderBypassProperties;
import org.apereo.cas.services.MultifactorAuthenticationProvider;
import org.apereo.cas.services.RegisteredService;
import org.apereo.cas.util.CollectionUtils;
import org.apereo.cas.util.HttpUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;

/**
 * This is {@link RestMultifactorAuthenticationProviderBypass}.
 *
 * @author Misagh Moayyed
 * @since 5.2.0
 */
public class RestMultifactorAuthenticationProviderBypass extends DefaultMultifactorAuthenticationProviderBypass {
    private static final Logger LOGGER = LoggerFactory.getLogger(RestMultifactorAuthenticationProviderBypass.class);
    private static final long serialVersionUID = -7553888418344342672L;

    public RestMultifactorAuthenticationProviderBypass(final MultifactorAuthenticationProviderBypassProperties bypassProperties) {
        super(bypassProperties);
    }

    @Override
    public boolean shouldMultifactorAuthenticationProviderExecute(final Authentication authentication, final RegisteredService registeredService,
                                                                  final MultifactorAuthenticationProvider provider,
                                                                  final HttpServletRequest request) {
        try {
            final Principal principal = authentication.getPrincipal();
            final MultifactorAuthenticationProviderBypassProperties.Rest rest = bypassProperties.getRest();
            LOGGER.debug("Evaluating multifactor authentication bypass properties for principal [{}], "
                            + "service [{}] and provider [{}] via REST endpoint [{}]",
                    principal.getId(), registeredService, provider, rest.getUrl());

            final Map<String, String> parameters = CollectionUtils.wrap("principal", CollectionUtils.wrap(principal.getId()),
                    "provider", CollectionUtils.wrap(provider.getId()));
            if (registeredService != null) {
                parameters.put("service", registeredService.getServiceId());
            }

            final HttpResponse response = HttpUtils.execute(rest.getUrl(), rest.getMethod(),
                    rest.getBasicAuthUsername(), rest.getBasicAuthPassword(), parameters);
            return response.getStatusLine().getStatusCode() == HttpStatus.ACCEPTED.value();
        } catch (final Exception e) {
            LOGGER.error(e.getMessage(), e);
        }
        return super.shouldMultifactorAuthenticationProviderExecute(authentication, registeredService, provider, request);
    }
}

```

## Error
Fix the REST mfa bypass call

## Error Description
Currently, the parameters are added as lists which generates the following error:

```java
2018-01-03 13:04:13,374 ERROR [org.apereo.cas.util.HttpUtils] - <java.util.ArrayList cannot be cast to java.lang.String>
java.lang.ClassCastException: java.util.ArrayList cannot be cast to java.lang.String
  at java.util.HashMap.forEach(HashMap.java:1280) ~[?:1.8.0_77]
  at org.apereo.cas.util.HttpUtils.buildHttpUri(HttpUtils.java:81) ~[cas-server-core-util-5.2.1.jar:5.2.1]
  at org.apereo.cas.util.HttpUtils.execute(HttpUtils.java:69) ~[cas-server-core-util-5.2.1.jar:5.2.1]
  at org.apereo.cas.authentication.RestMultifactorAuthenticationProviderBypass.shouldMultifactorAuthenticationProviderExecute(RestMultifactorAuthenticationProviderBypass.java:48) ~[cas-server-core-authentication-mfa-5.2.1.
````
This PR fixes this bug.
