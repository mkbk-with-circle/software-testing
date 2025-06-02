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

## Error Code Block
```java
    public void testObjectCycle() {
        ObjectCycle a = new ObjectCycle();
        ObjectCycle b = new ObjectCycle();
        a.obj = b;
        b.obj = a;

        String expected = toBaseString(a) + "[" + toBaseString(b) + "[" + toBaseString(a) + "]]";
        assertEquals(expected, a.toString());
        validateNullToStringStyleRegistry();
    }
```

## mistake patch
以下之前你给出的错误的修正代码
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
        return REGISTRY.get();
    }

```
请你继续修正