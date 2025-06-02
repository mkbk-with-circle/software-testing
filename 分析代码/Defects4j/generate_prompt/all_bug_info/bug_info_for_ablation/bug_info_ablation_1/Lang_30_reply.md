The bug occurs when handling supplementary Unicode characters (characters outside the BMP - Basic Multilingual Plane). The current code doesn't properly handle these characters which are represented as surrogate pairs in Java. Here's the fixed version:

```java
public static int indexOfAny(CharSequence cs, char[] searchChars) {
    if (isEmpty(cs) || ArrayUtils.isEmpty(searchChars)) {
        return INDEX_NOT_FOUND;
    }
    int csLen = cs.length();
    int searchLen = searchChars.length;
    for (int i = 0; i < csLen; i++) {
        char ch = cs.charAt(i);
        for (int j = 0; j < searchLen; j++) {
            if (searchChars[j] == ch) {
                // Check if we're in the middle of a surrogate pair
                if (Character.isHighSurrogate(ch)) {
                    if (j < searchLen - 1 && searchChars[j+1] == cs.charAt(i+1)) {
                        return i;
                    }
                } else {
                    return i;
                }
            }
        }
    }
    return INDEX_NOT_FOUND;
}
```

The fix adds proper handling of surrogate pairs by:
1. Checking if the current character is a high surrogate (first part of a surrogate pair)
2. If it is, we also check the next character in both the searchChars and the input string
3. Only returning the index if both parts of the surrogate pair match

This ensures that supplementary characters are properly compared as pairs rather than as individual surrogate characters.