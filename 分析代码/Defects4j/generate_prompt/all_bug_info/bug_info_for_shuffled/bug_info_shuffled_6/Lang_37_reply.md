修复后的代码需要检查数组类型是否兼容，如果不兼容则抛出IllegalArgumentException。以下是修复后的代码：

```java
public static <T> T[] addAll(T[] array1, T... array2) {
    if (array1 == null) {
        return clone(array2);
    } else if (array2 == null) {
        return clone(array1);
    }
    final Class<?> type1 = array1.getClass().getComponentType();
    final Class<?> type2 = array2.getClass().getComponentType();
    if (!type1.isAssignableFrom(type2)) {
        throw new IllegalArgumentException("Cannot store " + type2.getName() + " in " + type1.getName() + " array");
    }
    T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);
    System.arraycopy(array1, 0, joinedArray, 0, array1.length);
    System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
    return joinedArray;
}
```

主要修改：
1. 添加了类型检查，使用`isAssignableFrom`方法验证array2的元素类型是否可以赋值给array1的元素类型
2. 如果不兼容，抛出IllegalArgumentException
3. 只有当类型兼容时才进行数组合并操作

这样修改后，当尝试将Long数组添加到Integer数组时，会抛出IllegalArgumentException，符合测试用例的预期。