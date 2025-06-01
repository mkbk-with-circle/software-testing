## Buggy code
```java
/**
     * <p>
     * Returns the registry of objects being traversed by the <code>reflectionToString</code>
     * methods in the current thread.
     * </p>
     *
     * @return Set the registry of objects being traversed
     */
    static Map<Object, Object> getRegistry() {
        return REGISTRY.get() != null ? REGISTRY.get() : Collections.<Object, Object>emptyMap();
    }
```

## Failed test
org.apache.commons.lang3.builder.ToStringBuilderTest::testObjectCycle

## Test line
validateNullToStringStyleRegistry();

## Error
junit.framework.AssertionFailedError: Expected: <null> but was: {}

