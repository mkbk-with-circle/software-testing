Here's the fixed code that handles null elements in the array by checking for null before accessing the array element's length:

```java
public static String join(Object[] array, char separator, int startIndex, int endIndex) {
    if (array == null) {
        return null;
    }
    int noOfItems = (endIndex - startIndex);
    if (noOfItems <= 0) {
        return EMPTY;
    }
    
    final int bufSize = noOfItems * 16;  // default initial size
    StringBuilder buf = new StringBuilder(bufSize);

    for (int i = startIndex; i < endIndex; i++) {
        if (i > startIndex) {
            buf.append(separator);
        }
        if (array[i] != null) {
            buf.append(array[i]);
        }
    }
    return buf.toString();
}
```

The main changes are:
1. Removed the problematic length calculation that could cause NPE when array[startIndex] is null
2. Used a simpler initial buffer size calculation (number of items * 16)
3. Kept the same null handling logic in the main loop where null elements are skipped

This change ensures the code won't throw NullPointerException when handling arrays containing null elements while maintaining all other functionality.