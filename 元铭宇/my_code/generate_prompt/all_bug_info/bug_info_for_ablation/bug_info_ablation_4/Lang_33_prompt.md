## Buggy code
```java
/**
     * <p>Converts an array of <code>Object</code> in to an array of <code>Class</code> objects.
     * If any of these objects is null, a null element will be inserted into the array.</p>
     *
     * <p>This method returns <code>null</code> for a <code>null</code> input array.</p>
     *
     * @param array an <code>Object</code> array
     * @return a <code>Class</code> array, <code>null</code> if null array input
     * @since 2.4
     */
    public static Class<?>[] toClass(Object[] array) {
        if (array == null) {
            return null;
        } else if (array.length == 0) {
            return ArrayUtils.EMPTY_CLASS_ARRAY;
        }
        Class<?>[] classes = new Class[array.length];
        for (int i = 0; i < array.length; i++) {
            classes[i] = array[i].getClass();
        }
        return classes;
    }
```





