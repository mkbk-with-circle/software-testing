

## Buggy code
```java
/**
     * Appends an object to the builder padding on the left to a fixed width.
     * The <code>toString</code> of the object is used.
     * If the object is larger than the length, the left hand side is lost.
     * If the object is null, the null text value is used.
     * 
     * @param obj  the object to append, null uses null text
     * @param width  the fixed field width, zero or negative has no effect
     * @param padChar  the pad character to use
     * @return this, to enable chaining
     */
    public StrBuilder appendFixedWidthPadLeft(Object obj, int width, char padChar) {
        if (width > 0) {
            ensureCapacity(size + width);
            String str = (obj == null ? getNullText() : obj.toString());
            int strLen = str.length();
            if (strLen >= width) {
                str.getChars(strLen - width, strLen, buffer, size);
            } else {
                int padLen = width - strLen;
                for (int i = 0; i < padLen; i++) {
                    buffer[size + i] = padChar;
                }
                str.getChars(0, strLen, buffer, size + padLen);
            }
            size += width;
        }
        return this;
    }
```

## Failed test
org.apache.commons.lang.text.StrBuilderTest::testLang412Left

## Error
java.lang.NullPointerException

## Error Code Block
```java
    public void testLang412Left() {
        StrBuilder sb = new StrBuilder();
        sb.appendFixedWidthPadLeft(null, 10, '*');
        assertEquals( "Failed to invoke appendFixedWidthPadLeft correctly", "**********", sb.toString());
    }
```

## Test line
sb.appendFixedWidthPadLeft(null, 10, '*');
## mistake patch
以下之前你给出的错误的修正代码
```java


/**
     * Appends an object to the builder padding on the left to a fixed width.
     * The <code>toString</code> of the object is used.
     * If the object is larger than the length, the left hand side is lost.
     * If the object is null, the null text value is used.
     * 
     * @param obj  the object to append, null uses null text
     * @param width  the fixed field width, zero or negative has no effect
     * @param padChar  the pad character to use
     * @return this, to enable chaining
     */
    public StrBuilder appendFixedWidthPadLeft(Object obj, int width, char padChar) {
        if (width > 0) {
            ensureCapacity(size + width);
            String nullText = getNullText();
            String str = (obj == null ? (nullText == null ? "null" : nullText) : obj.toString());
            int strLen = str.length();
            if (strLen >= width) {
                str.getChars(strLen - width, strLen, buffer, size);
            } else {
                int padLen = width - strLen;
                for (int i = 0; i < padLen; i++) {
                    buffer[size + i] = padChar;
                }
                str.getChars(0, strLen, buffer, size + padLen);
            }
            size += width;
        }
        return this;
    }

```
请你继续修正