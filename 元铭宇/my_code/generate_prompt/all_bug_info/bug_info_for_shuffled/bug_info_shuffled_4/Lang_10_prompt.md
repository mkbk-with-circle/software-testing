

## Buggy code
```java
/**
     * Escape constant fields into regular expression
     * @param regex The destination regex
     * @param value The source field
     * @param unquote If true, replace two success quotes ('') with single quote (')
     * @return The <code>StringBuilder</code>
     */
    private static StringBuilder escapeRegex(StringBuilder regex, String value, boolean unquote) {
        boolean wasWhite= false;
        for(int i= 0; i<value.length(); ++i) {
            char c= value.charAt(i);
            if(Character.isWhitespace(c)) {
                if(!wasWhite) {
                    wasWhite= true;
                    regex.append("\\s*+");
                }
                continue;
            }
            wasWhite= false;
            switch(c) {
            case '\'':
                if(unquote) {
                    if(++i==value.length()) {
                        return regex;
                    }
                    c= value.charAt(i);
                }
                break;
            case '?':
            case '[':
            case ']':
            case '(':
            case ')':
            case '{':
            case '}':
            case '\\':
            case '|':
            case '*':
            case '+':
            case '^':
            case '$':
            case '.':
                regex.append('\\');
            }
            regex.append(c);
        }
        return regex;
    }
```

## Test line
testSdfAndFdp("M E","3  Tue", true);

## Failed test
org.apache.commons.lang3.time.FastDateFormat_ParserTest::testLANG_831

## Error Code Block
```java
    public void testLANG_831() throws Exception {
        testSdfAndFdp("M E","3  Tue", true);
    }
```

## Error
junit.framework.AssertionFailedError: Parsed dates should be equal expected:<null> but was:<Mon Mar 02 21:00:00 PST 1970>