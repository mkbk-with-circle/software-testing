## Fixed code
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
        if (array != null) {
            type = array.getClass().getComponentType();
        } else if (element != null) {
            type = element.getClass();
        } else {
            throw new IllegalArgumentException("Arguments cannot both be null");
        }
        @SuppressWarnings("unchecked") // type must be T
        T[] newArray = (T[]) java.lang.reflect.Array.newInstance(type, array != null ? array.length + 1 : 1);
        if (array != null) {
            System.arraycopy(array, 0, newArray, 0, array.length);
        }
        newArray[newArray.length - 1] = element;
        return newArray;
    }
```

The main issues fixed are:

1. Changed `array.getClass()` to `array.getClass().getComponentType()` to get the actual component type of the array rather than the array type itself
2. Replaced the `copyArrayGrow1` call with direct array creation using `Array.newInstance()`
3. Added proper array copying when the input array isn't null
4. Added proper null check throwing IllegalArgumentException when both arguments are null
5. Fixed the array creation to handle both cases (null and non-null input arrays)

This should now handle all cases correctly without any ClassCastExceptions.