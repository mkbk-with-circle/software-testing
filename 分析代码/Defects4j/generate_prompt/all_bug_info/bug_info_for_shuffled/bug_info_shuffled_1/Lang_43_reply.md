修复后的代码如下：

```java
/**
     * Consume a quoted string, adding it to <code>appendTo</code> if
     * specified.
     * 
     * @param pattern pattern to parse
     * @param pos current parse position
     * @param appendTo optional StringBuffer to append
     * @param escapingOn whether to process escaped quotes
     * @return <code>appendTo</code>
     */
    private StringBuffer appendQuotedString(String pattern, ParsePosition pos,
            StringBuffer appendTo, boolean escapingOn) {
        int start = pos.getIndex();
        char[] c = pattern.toCharArray();
        if (escapingOn && c[start] == QUOTE) {
            return appendTo == null ? null : appendTo.append(QUOTE);
        }
        int lastHold = start;
        for (int i = pos.getIndex(); i < pattern.length(); i++) {
            if (escapingOn && pattern.substring(i, Math.min(i + ESCAPED_QUOTE.length(), pattern.length())).startsWith(ESCAPED_QUOTE)) {
                appendTo.append(c, lastHold, i - lastHold).append(
                        QUOTE);
                pos.setIndex(i + ESCAPED_QUOTE.length());
                i = pos.getIndex() - 1;
                lastHold = pos.getIndex();
                continue;
            }
            switch (c[i]) {
            case QUOTE:
                next(pos);
                return appendTo == null ? null : appendTo.append(c, lastHold,
                        pos.getIndex() - lastHold);
            default:
                next(pos);
            }
        }
        throw new IllegalArgumentException(
                "Unterminated quoted string at position " + start);
    }
```

主要修改点：
1. 修复了`pattern.substring(i)`可能导致的内存溢出问题，改为使用`pattern.substring(i, Math.min(i + ESCAPED_QUOTE.length(), pattern.length()))`来限制子字符串长度
2. 将`c[pos.getIndex()]`改为`c[i]`以保持索引一致性
3. 在处理转义引号后，更新循环变量`i`的值以避免无限循环
4. 修正了append操作中的位置计算，使用`i - lastHold`而不是`pos.getIndex() - lastHold`

这些修改解决了内存溢出问题并确保了正确处理转义引号的情况。