修复后的代码需要确保在字符串被删除后，indexOf方法能正确返回-1而不是错误的位置。问题出在循环的边界条件上，应该使用size而不是buffer.length来计算len。以下是修复后的代码：

```java
/**
     * Searches the string builder to find the first reference to the specified
     * string starting searching from the given index.
     * <p>
     * Note that a null input string will return -1, whereas the JDK throws an exception.
     * 
     * @param str  the string to find, null returns -1
     * @param startIndex  the index to start at, invalid index rounded to edge
     * @return the first index of the string, or -1 if not found
     */
    public int indexOf(String str, int startIndex) {
        startIndex = (startIndex < 0 ? 0 : startIndex);
        if (str == null || startIndex >= size) {
            return -1;
        }
        int strLen = str.length();
        if (strLen == 1) {
            return indexOf(str.charAt(0), startIndex);
        }
        if (strLen == 0) {
            return startIndex;
        }
        if (strLen > size) {
            return -1;
        }
        char[] thisBuf = buffer;
        int len = size - strLen + 1;  // Changed from thisBuf.length to size
        outer:
        for (int i = startIndex; i < len; i++) {
            for (int j = 0; j < strLen; j++) {
                if (str.charAt(j) != thisBuf[i + j]) {
                    continue outer;
                }
            }
            return i;
        }
        return -1;
    }
```

关键修改是将`len = thisBuf.length - strLen`改为`len = size - strLen + 1`，这样循环会在实际字符串内容范围内进行搜索，而不是在整个buffer数组范围内搜索。