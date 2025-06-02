## Fixed Code
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
        throw new IllegalArgumentException("Cannot store " + type2.getName() + " in " + type1.getName());
    }
    T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);
    System.arraycopy(array1, 0, joinedArray, 0, array1.length);
    System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
    return joinedArray;
}
```

The fix adds a type compatibility check before attempting the array copy operation. It verifies that the component type of the second array is assignable to the component type of the first array. If not, it throws an IllegalArgumentException, which matches the expected behavior in the test case. This prevents the ArrayStoreException by failing fast with a more meaningful error message.