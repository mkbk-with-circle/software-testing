Here's the fixed code:

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
            if (escapingOn && pattern.substring(i, i + (ESCAPED_QUOTE.length() > pattern.length() - i ? pattern.length() - i : ESCAPED_QUOTE.length())).startsWith(ESCAPED_QUOTE)) {
                appendTo.append(c, lastHold, i - lastHold).append(
                        QUOTE);
                pos.setIndex(i + ESCAPED_QUOTE.length());
                lastHold = pos.getIndex();
                i = pos.getIndex() - 1;
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

The main changes are:
1. Fixed the substring bounds checking to prevent StringIndexOutOfBoundsException
2. Changed `c[pos.getIndex()]` to `c[i]` to use the loop counter instead of the position index
3. Added `i = pos.getIndex() - 1` to properly sync the loop counter after processing an escaped quote
4. Updated the append position calculation to use `i` instead of `pos.getIndex()`

These changes prevent the infinite loop that was causing the OutOfMemoryError while maintaining the original functionality.