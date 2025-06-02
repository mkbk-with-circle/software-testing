## Buggy code
```java
public static <T> T[] addAll(T[] array1, T... array2) {
        if (array1 == null) {
            return clone(array2);
        } else if (array2 == null) {
            return clone(array1);
        }
        final Class<?> type1 = array1.getClass().getComponentType();
        T[] joinedArray = (T[]) Array.newInstance(type1, array1.length + array2.length);
        System.arraycopy(array1, 0, joinedArray, 0, array1.length);
            System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
            // Check if problem is incompatible types
        return joinedArray;
    }
```

## Failed test
org.apache.commons.lang3.ArrayUtilsAddTest::testJira567

## Test line
n = ArrayUtils.addAll(new Integer[]{Integer.valueOf(1)}, new Long[]{Long.valueOf(2)});

## Error
java.lang.ArrayStoreException: arraycopy: type mismatch: can not copy java.lang.Long[] into java.lang.Integer[]

