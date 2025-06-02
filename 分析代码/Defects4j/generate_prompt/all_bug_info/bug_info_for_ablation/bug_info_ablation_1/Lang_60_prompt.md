## Buggy code
```java
/**
     * Checks if the string builder contains the specified char.
     *
     * @param ch  the character to find
     * @return true if the builder contains the character
     */
    public boolean contains(char ch) {
        char[] thisBuf = buffer;
        for (int i = 0; i < thisBuf.length; i++) {
            if (thisBuf[i] == ch) {
                return true;
            }
        }
        return false;
    }
```

## Failed test
org.apache.commons.lang.text.StrBuilderTest::testLang295

## Test line
assertFalse( "The contains(char) method is looking beyond the end of the string", sb.contains('h'));

## Error
junit.framework.AssertionFailedError: The contains(char) method is looking beyond the end of the string

