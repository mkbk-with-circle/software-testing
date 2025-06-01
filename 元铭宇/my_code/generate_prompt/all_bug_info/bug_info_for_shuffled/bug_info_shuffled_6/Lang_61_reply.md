修复后的代码需要确保在字符串被删除后，查找该字符串会返回-1。原代码的问题在于它使用了buffer.length而不是size来计算长度，这可能导致访问到已删除的内容。以下是修复后的代码：

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
        int len = size - strLen;
        outer:
        for (int i = startIndex; i <= len; i++) {
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

主要修改点：
1. 将`int len = thisBuf.length - strLen;`改为`int len = size - strLen;`，使用实际的字符串长度(size)而不是缓冲区长度(buffer.length)
2. 将循环条件`i < len`改为`i <= len`，确保能检查到字符串末尾的可能性

这些修改确保了我们只在有效的字符串范围内进行搜索，而不会访问到已被删除的内容。