Here's the fixed code that handles the case when both array and element are null by throwing an IllegalArgumentException:

```java
public static <T> T[] add(T[] array, T element) {
    if (array == null && element == null) {
        throw new IllegalArgumentException("Arguments cannot both be null");
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

The fix adds a check at the beginning of the method to throw an IllegalArgumentException when both arguments are null, which matches the documented behavior in the method's javadoc. This prevents the ClassCastException that would occur when trying to create an Object array and cast it to a String array when both inputs are null.