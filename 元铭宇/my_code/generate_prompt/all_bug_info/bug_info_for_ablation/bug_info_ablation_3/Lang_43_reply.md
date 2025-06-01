The issue appears to be an infinite loop caused by incorrect index handling in the loop. Here's the fixed code:

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
        for (int i = pos.getIndex(); i < pattern.length(); i = pos.getIndex()) {
            if (escapingOn && pattern.substring(i).startsWith(ESCAPED_QUOTE)) {
                appendTo.append(c, lastHold, i - lastHold).append(
                        QUOTE);
                pos.setIndex(i + ESCAPED_QUOTE.length());
                lastHold = pos.getIndex();
                continue;
            }
            switch (c[i]) {
            case QUOTE:
                next(pos);
                return appendTo == null ? null : appendTo.append(c, lastHold,
                        pos.getIndex() - lastHold - 1);
            default:
                next(pos);
            }
        }
        throw new IllegalArgumentException(
                "Unterminated quoted string at position " + start);
    }
```

Key changes made:
1. Changed the loop increment to use `i = pos.getIndex()` instead of relying on the for-loop increment
2. Used `i` instead of `pos.getIndex()` in the switch statement to avoid confusion
3. Fixed the length calculation in the final append by subtracting 1 to account for the quote position
4. Used `i` instead of `pos.getIndex()` in the escaped quote handling for consistency

These changes prevent the infinite loop that was causing the OutOfMemoryError while maintaining the original functionality.