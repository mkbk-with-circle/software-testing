我理解你需要修复原始代码来处理基本类型的类序列化问题。以下是修复后的代码：

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
                        return Class.forName(desc.getName(), false, getClass().getClassLoader());
                    } catch (ClassNotFoundException ex) {
                        // Handle primitive types
                        switch(desc.getName()) {
                            case "byte": return byte.class;
                            case "short": return short.class;
                            case "int": return int.class;
                            case "long": return long.class;
                            case "float": return float.class;
                            case "double": return double.class;
                            case "boolean": return boolean.class;
                            case "char": return char.class;
                            case "void": return void.class;
                            default: throw ex;
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

主要修改点：
1. 使用`Class.forName()`替代原来的`super.resolveClass()`来更好地处理类加载
2. 保留了原始的基本类型处理逻辑
3. 将所有异常捕获并包装为`SerializationException`

这个修改应该能够正确处理基本类型的类序列化和反序列化问题。