我分析了代码和错误，发现主要问题是在处理转义引号时出现了无限循环，导致堆内存耗尽。以下是修复后的代码：

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
            if (escapingOn && pattern.substring(i).startsWith(ESCAPED_QUOTE)) {
                appendTo.append(c, lastHold, i - lastHold).append(
                        QUOTE);
                pos.setIndex(i + ESCAPED_QUOTE.length());
                i = pos.getIndex() - 1; // -1 because loop will increment it
                lastHold = pos.getIndex();
                continue;
            }
            switch (c[i]) {
            case QUOTE:
                pos.setIndex(i + 1);
                return appendTo == null ? null : appendTo.append(c, lastHold,
                        i - lastHold);
            default:
                // do nothing, just continue
            }
        }
        throw new IllegalArgumentException(
                "Unterminated quoted string at position " + start);
    }
```

主要修改点：
1. 移除了`next(pos)`调用，改为直接更新位置索引
2. 在for循环中使用`i`作为索引而不是`pos.getIndex()`
3. 处理转义引号后正确更新循环变量`i`
4. 简化了default case的逻辑

这些修改解决了无限循环的问题，同时保持了原有的功能逻辑。