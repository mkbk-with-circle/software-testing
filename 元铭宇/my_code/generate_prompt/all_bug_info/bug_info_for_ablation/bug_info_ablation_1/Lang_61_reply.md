修复后的代码需要确保当搜索的字符串长度超过StringBuilder内容长度时返回-1。原代码中比较的是`strLen > size`，但实际上应该比较`strLen > size - startIndex`，因为是从startIndex开始搜索的。此外，循环的上界应该是`size - strLen`而不是`thisBuf.length - strLen`，因为buffer可能比实际内容大。

以下是修复后的代码：

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
        if (strLen > size - startIndex) {
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