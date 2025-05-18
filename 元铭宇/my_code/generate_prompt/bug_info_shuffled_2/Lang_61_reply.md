我理解了这个问题。当字符串被删除后，`indexOf`方法仍然返回了原来的索引位置，这是因为代码中的`len`计算有误。修复后的代码应该使用`size`而不是`buffer.length`来计算最大可能的索引位置。以下是修复后的代码：

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
1. 将`len`的计算从`thisBuf.length - strLen`改为`size - strLen`，这样会使用实际的字符串长度而不是底层buffer的长度
2. 将循环条件从`i < len`改为`i <= len`，确保能检查到字符串末尾的可能性

这样修改后，当字符串被删除后，`indexOf`方法会正确返回-1而不是原来的索引位置。