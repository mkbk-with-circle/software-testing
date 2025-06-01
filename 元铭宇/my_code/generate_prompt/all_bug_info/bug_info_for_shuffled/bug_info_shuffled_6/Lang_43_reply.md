经过分析，原代码在处理转义引号时存在无限循环问题，导致内存溢出。主要问题是在处理转义引号时没有正确更新循环变量i和pos的位置。以下是修复后的代码：

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
1. 在处理转义引号时，正确更新循环变量i的位置
2. 移除了next(pos)调用，直接使用i来跟踪位置
3. 在switch语句中直接使用c[i]而不是c[pos.getIndex()]
4. 更新pos的位置时使用i+1而不是调用next()
这些修改确保了循环能正确推进并处理转义引号，避免了无限循环和内存溢出的问题。