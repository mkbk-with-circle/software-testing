

## Error
java.lang.ClassCastException: class [Ljava.lang.Object; cannot be cast to class [Ljava.lang.String; ([Ljava.lang.Object; and [Ljava.lang.String; are in module java.base of loader 'bootstrap')

## Error Code Block
```java
    public void testLANG571(){
        String[] stringArray=null;
        String aString=null;
        try {
            @SuppressWarnings("unused")
            String[] sa = ArrayUtils.add(stringArray, aString);
            fail("Should have caused IllegalArgumentException");
        } catch (IllegalArgumentException iae){
            //expected
        }
        try {
            @SuppressWarnings("unused")
            String[] sa = ArrayUtils.add(stringArray, 0, aString);
            fail("Should have caused IllegalArgumentException");
        } catch (IllegalArgumentException iae){
            //expected
        }
    }
```

## Test line
String[] sa = ArrayUtils.add(stringArray, aString);

## Failed test
org.apache.commons.lang3.ArrayUtilsAddTest::testLANG571

## Buggy code
```java
/**
     * <p>Copies the given array and adds the given element at the end of the new array.</p>
     *
     * <p>The new array contains the same elements of the input
     * array plus the given element in the last position. The component type of
     * the new array is the same as that of the input array.</p>
     *
     * <p>If the input array is <code>null</code>, a new one element array is returned
     *  whose component type is the same as the element, unless the element itself is null,
     *  in which case the return type is Object[]</p>
     *
     * <pre>
     * ArrayUtils.add(null, null)      = [null]
     * ArrayUtils.add(null, "a")       = ["a"]
     * ArrayUtils.add(["a"], null)     = ["a", null]
     * ArrayUtils.add(["a"], "b")      = ["a", "b"]
     * ArrayUtils.add(["a", "b"], "c") = ["a", "b", "c"]
     * </pre>
     *
     * @param array  the array to "add" the element to, may be <code>null</code>
     * @param element  the object to add, may be <code>null</code>
     * @return A new array containing the existing elements plus the new element
     * The returned array type will be that of the input array (unless null),
     * in which case it will have the same type as the element.
     * If both are null, an IllegalArgumentException is thrown
     * @since 2.1
     * @throws IllegalArgumentException if both arguments are null
     */
    public static <T> T[] add(T[] array, T element) {
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
## mistake patch
以下之前你给出的错误的修正代码
```java


/**
     * <p>Copies the given array and adds the given element at the end of the new array.</p>
     *
     * <p>The new array contains the same elements of the input
     * array plus the given element in the last position. The component type of
     * the new array is the same as that of the input array.</p>
     *
     * <p>If the input array is <code>null</code>, a new one element array is returned
     *  whose component type is the same as the element, unless the element itself is null,
     *  in which case the return type is Object[]</p>
     *
     * <pre>
     * ArrayUtils.add(null, null)      = [null]
     * ArrayUtils.add(null, "a")       = ["a"]
     * ArrayUtils.add(["a"], null)     = ["a", null]
     * ArrayUtils.add(["a"], "b")      = ["a", "b"]
     * ArrayUtils.add(["a", "b"], "c") = ["a", "b", "c"]
     * </pre>
     *
     * @param array  the array to "add" the element to, may be <code>null</code>
     * @param element  the object to add, may be <code>null</code>
     * @return A new array containing the existing elements plus the new element
     * The returned array type will be that of the input array (unless null),
     * in which case it will have the same type as the element.
     * If both are null, an IllegalArgumentException is thrown
     * @since 2.1
     * @throws IllegalArgumentException if both arguments are null
     */
    public static <T> T[] add(T[] array, T element) {
        if (array == null && element == null) {
            throw new IllegalArgumentException("Arguments cannot both be null");
        }
        Class<?> type;
        if (array != null){
            type = array.getClass().getComponentType();
        } else if (element != null) {
            type = element.getClass();
        } else {
            type = Object.class;
        }
        @SuppressWarnings("unchecked") // type must be T
        T[] newArray = (T[]) Array.newInstance(type, array == null ? 1 : array.length + 1);
        if (array != null) {
            System.arraycopy(array, 0, newArray, 0, array.length);
        }
        newArray[newArray.length - 1] = element;
        return newArray;
    }

```
请你继续修正