根据测试用例和错误信息，当输入数组和元素都为null时，应该抛出IllegalArgumentException异常。以下是修复后的代码：

```java
public static <T> T[] add(T[] array, T element) {
    if (array == null && element == null) {
        throw new IllegalArgumentException("Both arguments are null");
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

主要修改是在方法开始时添加了对两个参数都为null的检查，并抛出IllegalArgumentException异常，这与方法注释中的描述一致。这样就能通过测试用例testLANG571的验证。