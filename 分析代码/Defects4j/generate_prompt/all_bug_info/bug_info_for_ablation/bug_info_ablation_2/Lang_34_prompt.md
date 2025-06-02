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
