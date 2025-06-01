

## Buggy code
```java
/**
     * Translate an input onto a Writer. This is intentionally final as its algorithm is 
     * tightly coupled with the abstract method of this class. 
     *
     * @param input CharSequence that is being translated
     * @param out Writer to translate the text to
     * @throws IOException if and only if the Writer produces an IOException
     */
    public final void translate(CharSequence input, Writer out) throws IOException {
        if (out == null) {
            throw new IllegalArgumentException("The Writer must not be null");
        }
        if (input == null) {
            return;
        }
        int pos = 0;
        int len = Character.codePointCount(input, 0, input.length());
        while (pos < len) {
            int consumed = translate(input, pos, out);
            if (consumed == 0) {
                char[] c = Character.toChars(Character.codePointAt(input, pos));
                out.write(c);
            }
            else {
//          // contract with translators is that they have to understand codepoints 
//          // and they just took care of a surrogate pair
            for (int pt = 0; pt < consumed; pt++) {
                    if (pos < len - 2) {
                pos += Character.charCount(Character.codePointAt(input, pos));
                    } else {
                        pos++;
                    }
                }
                pos--;
            }
            pos++;
        }
    }
```

## Test line
assertEquals(input, escaped);

## Failed test
org.apache.commons.lang3.StringEscapeUtilsTest::testLang720

## Error Code Block
```java
    public void testLang720() {
        String input = new StringBuilder("\ud842\udfb7").append("A").toString();
        String escaped = StringEscapeUtils.escapeXml(input);
        assertEquals(input, escaped);
    }
```

## Error
junit.framework.ComparisonFailure: expected:<ð ®·[A]> but was:<ð ®·[?]>
## mistake patch
以下之前你给出的错误的修正代码
```java


/**
     * Translate an input onto a Writer. This is intentionally final as its algorithm is 
     * tightly coupled with the abstract method of this class. 
     *
     * @param input CharSequence that is being translated
     * @param out Writer to translate the text to
     * @throws IOException if and only if the Writer produces an IOException
     */
    public final void translate(CharSequence input, Writer out) throws IOException {
        if (out == null) {
            throw new IllegalArgumentException("The Writer must not be null");
        }
        if (input == null) {
            return;
        }
        int pos = 0;
        int len = input.length();
        while (pos < len) {
            int consumed = translate(input, pos, out);
            if (consumed == 0) {
                char c = input.charAt(pos);
                out.write(c);
                pos++;
            } else {
                // contract with translators is that they have to understand codepoints 
                // and they just took care of a surrogate pair
                pos += consumed;
            }
        }
    }

```
请你继续修正