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
        int len = input.length();
        while (pos < len) {
            int consumed = translate(input, pos, out);
            if (consumed == 0) {
                char[] c = Character.toChars(Character.codePointAt(input, pos));
                out.write(c);
                pos+= c.length;
                continue;
            }
//          // contract with translators is that they have to understand codepoints 
//          // and they just took care of a surrogate pair
            for (int pt = 0; pt < consumed; pt++) {
                pos += Character.charCount(Character.codePointAt(input, pos));
            }
        }
    }
```

## Failed test
org.apache.commons.lang3.StringUtilsTest::testEscapeSurrogatePairs

## Test line
assertEquals("\uD83D\uDE30", StringEscapeUtils.escapeCsv("\uD83D\uDE30"));

## Error
java.lang.StringIndexOutOfBoundsException: index 2,length 2

