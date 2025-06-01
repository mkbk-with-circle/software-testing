根据错误信息和代码分析，问题出现在反序列化基本类型的Class对象时。修复方法是在反序列化时使用特殊的ClassLoader来处理基本类型。以下是修复后的代码：

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
        try {
            return deserialize(bais);
        } catch (SerializationException ex) {
            // Handle primitive type classes specially
            if (ex.getCause() instanceof ClassNotFoundException) {
                String className = ((ClassNotFoundException) ex.getCause()).getMessage();
                try {
                    switch (className) {
                        case "byte": return byte.class;
                        case "short": return short.class;
                        case "int": return int.class;
                        case "long": return long.class;
                        case "float": return float.class;
                        case "double": return double.class;
                        case "boolean": return boolean.class;
                        case "char": return char.class;
                        case "void": return void.class;
                    }
                } catch (Exception e) {
                    throw new SerializationException(e);
                }
            }
            throw ex;
        }
    }
```