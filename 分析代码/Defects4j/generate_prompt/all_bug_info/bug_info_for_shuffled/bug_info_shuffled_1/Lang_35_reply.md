修复后的代码需要在处理两个参数都为null时抛出IllegalArgumentException异常。以下是修复后的代码：

```java
public static <T> T[] add(T[] array, T element) {
    if (array == null && element == null) {
        throw new IllegalArgumentException("Both arguments cannot be null");
    }
    Class<?> type;
    if (array != null){
        type = array.getClass();
    } else if (element != null) {
        type = element.getClass();
    } else {
        type = Object.class;
    }
    @SuppressWarnings("unchecked") // type must be T
    T[] newArray = (T[]) copyArrayGrow1(array, type);
    newArray[newArray.length - 1] = element;
    return newArray;
}
```

主要修改是在方法开头添加了对两个参数都为null的检查，并抛出IllegalArgumentException异常。这符合测试用例的预期行为。