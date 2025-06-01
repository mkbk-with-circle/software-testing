根据测试用例和错误信息，问题在于`deleteFirst("three")`之后，`indexOf("three")`仍然返回6而不是-1。这表明`deleteFirst()`方法没有正确更新内部缓冲区或大小。修复的关键是确保`deleteFirst()`方法正确更新字符串构建器的状态。

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
        if (strLen > size) {
            return -1;
        }
        char[] thisBuf = buffer;
        int len = size - strLen;  // Changed from thisBuf.length to size
        outer:
        for (int i = startIndex; i <= len; i++) {  // Changed < to <=
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
1. 将循环条件中的`len`计算从`thisBuf.length - strLen`改为`size - strLen`，使用实际大小而不是缓冲区长度
2. 将外层循环的条件从`i < len`改为`i <= len`，确保能检查到字符串末尾的匹配

这些修改确保`indexOf()`方法只搜索字符串构建器的有效内容区域，并且能够正确检测到字符串末尾的匹配。