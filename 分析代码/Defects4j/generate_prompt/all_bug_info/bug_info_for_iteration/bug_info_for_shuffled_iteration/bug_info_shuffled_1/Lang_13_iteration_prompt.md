

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
## mistake patch
以下之前你给出的错误的修正代码
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
        try {
            ByteArrayInputStream bais = new ByteArrayInputStream(objectData);
            ObjectInputStream in = new ObjectInputStream(bais) {
                @Override
                protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException, ClassNotFoundException {
                    try {
                        return super.resolveClass(desc);
                    } catch (ClassNotFoundException e) {
                        // Handle primitive types
                        switch (desc.getName()) {
                            case "byte": return byte.class;
                            case "short": return short.class;
                            case "int": return int.class;
                            case "long": return long.class;
                            case "float": return float.class;
                            case "double": return double.class;
                            case "boolean": return boolean.class;
                            case "char": return char.class;
                            case "void": return void.class;
                            default: throw e;
                        }
                    }
                }
            };
            return in.readObject();
        } catch (Exception e) {
            throw new SerializationException(e);
        }
    }

```
运用你给出的修复代码后，编译失败了
请你继续修正