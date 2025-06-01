根据测试用例，当字符串被删除后，查找该字符串应该返回-1，但当前代码返回了6，说明删除操作后indexOf仍然找到了已删除的字符串。问题在于代码没有考虑buffer中实际有效数据的大小(size)，而是使用了buffer数组的完整长度。以下是修复后的代码：

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

主要修改：
1. 将 `int len = thisBuf.length - strLen;` 改为 `int len = size - strLen;`，使用实际有效数据大小(size)而不是buffer数组的完整长度
2. 将循环条件 `i < len` 改为 `i <= len`，确保能检查到字符串末尾的可能匹配