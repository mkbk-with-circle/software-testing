## Buggy code
```java
public int translate(CharSequence input, int index, Writer out) throws IOException {
        int seqEnd = input.length();
        // Uses -2 to ensure there is something after the &#
        if(input.charAt(index) == '&' && index < seqEnd - 1 && input.charAt(index + 1) == '#') {
            int start = index + 2;
            boolean isHex = false;

            char firstChar = input.charAt(start);
            if(firstChar == 'x' || firstChar == 'X') {
                start++;
                isHex = true;

                // Check there's more than just an x after the &#
            }

            int end = start;
            // Note that this supports character codes without a ; on the end
            while(input.charAt(end) != ';') 
            {
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
            System.err.println("FAIL: " + input.subSequence(start, end) + "[" + start +"]["+ end +"]");
                return 0;
            }

            if(entityValue > 0xFFFF) {
                char[] chrs = Character.toChars(entityValue);
                out.write(chrs[0]);
                out.write(chrs[1]);
            } else {
                out.write(entityValue);
            }


            return 2 + (end - start) + (isHex ? 1 : 0) + 1;
        }
        return 0;
    }
```

## Failed test
org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testUnfinishedEntity

## Test line
String result = neu.translate(input);

## Error
java.lang.StringIndexOutOfBoundsException: String index out of range: 19

