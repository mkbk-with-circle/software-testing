The bug occurs when handling high Unicode characters (those above 0xFFFF). The current code writes them as surrogate pairs (two separate characters) instead of as a single Unicode code point. Here's the fixed version:

```java
/**
     * <p>
     * Escapes the characters in the <code>String</code> passed and writes the result to the <code>Writer</code>
     * passed.
     * </p>
     * 
     * @param writer
     *            The <code>Writer</code> to write the results of the escaping to. Assumed to be a non-null value.
     * @param str
     *            The <code>String</code> to escape. Assumed to be a non-null value.
     * @throws IOException
     *             when <code>Writer</code> passed throws the exception from calls to the {@link Writer#write(int)}
     *             methods.
     * 
     * @see #escape(String)
     * @see Writer
     */
    public void escape(Writer writer, String str) throws IOException {
        int len = str.length();
        for (int i = 0; i < len; i++) {
            char c = str.charAt(i);
            String entityName = this.entityName(c);
            if (entityName == null) {
                if (c >= Character.MIN_SURROGATE && c <= Character.MAX_SURROGATE && i + 1 < len) {
                    // Handle surrogate pairs
                    int codePoint = str.codePointAt(i);
                    writer.write("&#");
                    writer.write(Integer.toString(codePoint, 10));
                    writer.write(';');
                    i++; // Skip the next surrogate char
                } else if (c > 0x7F) {
                    writer.write("&#");
                    writer.write(Integer.toString(c, 10));
                    writer.write(';');
                } else {
                    writer.write(c);
                }
            } else {
                writer.write('&');
                writer.write(entityName);
                writer.write(';');
            }
        }
    }
```

The key changes are:
1. Added handling for surrogate pairs using `Character.MIN_SURROGATE` and `Character.MAX_SURROGATE` checks
2. Used `codePointAt()` to get the full Unicode code point for surrogate pairs
3. Incremented the loop counter when we process a surrogate pair to skip the next char
4. Maintained the existing behavior for non-surrogate characters

This will now correctly handle high Unicode characters by outputting their full code point value rather than their surrogate pair components.