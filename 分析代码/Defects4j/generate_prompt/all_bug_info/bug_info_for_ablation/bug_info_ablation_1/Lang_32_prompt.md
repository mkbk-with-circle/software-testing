## Buggy code
```java
protected Set<IDKey> initialValue() {
            return new HashSet<IDKey>();
        }
```

## Failed test
org.apache.commons.lang3.builder.HashCodeBuilderTest::testReflectionObjectCycle

## Test line
assertNull(HashCodeBuilder.getRegistry());

## Error
junit.framework.AssertionFailedError: Expected: <null> but was: []

