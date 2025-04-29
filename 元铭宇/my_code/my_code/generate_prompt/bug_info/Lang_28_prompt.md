## Buggy code
```java
public int translate(CharSequence input, int index, Writer out) throws IOException {
        // TODO: Protect from ArrayIndexOutOfBounds
        if(input.charAt(index) == '&' && input.charAt(index + 1) == '#') {
            int start = index + 2;
            boolean isHex = false;

            char firstChar = input.charAt(start);
            if(firstChar == 'x' || firstChar == 'X') {
                start++;
                isHex = true;
            }

            int end = start;
            while(input.charAt(end) != ';') {
                end++;
            }

            int entityValue;
            try {
                if(isHex) {
                    entityValue = Integer.parseInt(input.subSequence(start, end).toString(), 16);
                } else {
                    entityValue = Integer.parseInt(input.subSequence(start, end).toString(), 10);
                }
            } catch(NumberFormatException nfe) {
                return 0;
            }

                out.write(entityValue);
            return 2 + (end - start) + (isHex ? 1 : 0) + 1;
        }
        return 0;
    }
```

## Failed test
org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testSupplementaryUnescaping

## Test line
assertEquals("Failed to unescape numeric entities supplementary characters", expected, result);

## Error
junit.framework.ComparisonFailure: Failed to unescape numeric entities supplementary characters expected:<[ð°¢]> but was:<[à°¢]>

## Error Code Block
```java
    public void testSupplementaryUnescaping() {
        NumericEntityUnescaper neu = new NumericEntityUnescaper();
        String input = "&#68642;";
        String expected = "\uD803\uDC22";

        String result = neu.translate(input);
        assertEquals("Failed to unescape numeric entities supplementary characters", expected, result);
    }
```
