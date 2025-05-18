

## Failed test
org.apache.commons.lang3.SerializationUtilsTest::testPrimitiveTypeClassSerialization

## Error
org.apache.commons.lang3.SerializationException: ClassNotFoundException while reading cloned object data

## Error Code Block
```java
    public void testPrimitiveTypeClassSerialization() {
        Class<?>[] primitiveTypes = { byte.class, short.class, int.class, long.class, float.class, double.class,
                boolean.class, char.class, void.class };

        for (Class<?> primitiveType : primitiveTypes) {
            Class<?> clone = SerializationUtils.clone(primitiveType);
            assertEquals(primitiveType, clone);
        }
    }
```

## Test line
Class<?> clone = SerializationUtils.clone(primitiveType);

## Buggy code
```java
/**
     * <p>Deserializes a single {@code Object} from an array of bytes.</p>
     *
     * @param objectData  the serialized object, must not be null
     * @return the deserialized object
     * @throws IllegalArgumentException if {@code objectData} is {@code null}
     * @throws SerializationException (runtime) if the serialization fails
     */
    public static Object deserialize(byte[] objectData) {
        if (objectData == null) {
            throw new IllegalArgumentException("The byte[] must not be null");
        }
        ByteArrayInputStream bais = new ByteArrayInputStream(objectData);
        return deserialize(bais);
    }
```