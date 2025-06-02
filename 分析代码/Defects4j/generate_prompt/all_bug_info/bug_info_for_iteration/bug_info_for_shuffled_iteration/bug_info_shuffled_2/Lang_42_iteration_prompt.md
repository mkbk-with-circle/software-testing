

## Buggy code
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
                if (c > 0x7F) {
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

## Error Code Block
```java
    public void testEscapeHtmlHighUnicode() throws java.io.UnsupportedEncodingException {
        // this is the utf8 representation of the character:
        // COUNTING ROD UNIT DIGIT THREE
        // in unicode
        // codepoint: U+1D362
        byte[] data = new byte[] { (byte)0xF0, (byte)0x9D, (byte)0x8D, (byte)0xA2 };

        String escaped = StringEscapeUtils.escapeHtml( new String(data, "UTF8") );
        String unescaped = StringEscapeUtils.unescapeHtml( escaped );

        assertEquals( "High unicode was not escaped correctly", "&#119650;", escaped);
    }
```

## Test line
assertEquals( "High unicode was not escaped correctly", "&#119650;", escaped);

## Failed test
org.apache.commons.lang.StringEscapeUtilsTest::testEscapeHtmlHighUnicode

## Error
junit.framework.ComparisonFailure: High unicode was not escaped correctly expected:<&#[119650];> but was:<&#[55348;&#57186];>
## mistake patch
以下之前你给出的错误的修正代码
```java


public void escape(Writer writer, String str) throws IOException {
    int len = str.length();
    for (int i = 0; i < len; i++) {
        char c = str.charAt(i);
        if (Character.isHighSurrogate(c) && i + 1 < len && Character.isLowSurrogate(str.charAt(i + 1))) {
            // Handle surrogate pair
            int codePoint = Character.toCodePoint(c, str.charAt(i + 1));
            writer.write("&#");
            writer.write(Integer.toString(codePoint, 10));
            writer.write(';');
            i++; // Skip the next character as we've processed it already
        } else {
            String entityName = this.entityName(c);
            if (entityName == null) {
                if (c > 0x7F) {
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
}

```
运用你给出的修复代码后，编译失败了
请你继续修正