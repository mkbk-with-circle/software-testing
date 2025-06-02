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

主要修复点：
1. 在转义引号处理部分，使用循环变量i而不是pos.getIndex()来计算要追加的字符长度
2. 在处理转义引号后，更新循环变量i以保持同步
3. 在switch语句中使用循环变量i而不是pos.getIndex()来检查当前字符
4. 移除了next(pos)调用，直接通过设置pos.setIndex()来更新位置
5. 在default情况下不再调用next(pos)，让循环自然递增i

这些修改确保了位置指针和循环变量保持同步，并正确处理了转义字符和引号。