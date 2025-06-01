我分析了代码和测试用例，发现主要问题是循环中的索引处理不正确导致无限循环。以下是修复后的代码：

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
                appendTo.append(c, lastHold, i - lastHold).append(QUOTE);
                pos.setIndex(i + ESCAPED_QUOTE.length());
                i = pos.getIndex() - 1;  // -1 because loop will increment it
                lastHold = pos.getIndex();
                continue;
            }
            if (c[i] == QUOTE) {
                pos.setIndex(i + 1);
                return appendTo == null ? null : appendTo.append(c, lastHold,
                        i - lastHold);
            }
        }
        throw new IllegalArgumentException(
                "Unterminated quoted string at position " + start);
    }
```

主要修改：
1. 移除了switch语句，改用简单的if判断，因为default分支什么都不做
2. 使用当前循环索引i而不是pos.getIndex()来访问字符数组
3. 正确处理了转义引号后的索引更新
4. 确保每次循环都能推进索引位置，避免无限循环

这个修改应该能正确处理测试用例中的转义引号情况，同时避免内存溢出错误。