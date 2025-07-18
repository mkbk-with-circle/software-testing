

## Error
java.lang.NullPointerException

## Error Code Block
```java
    public void testReplace_StringStringArrayStringArray() {

        
        //JAVADOC TESTS START
        assertNull(StringUtils.replaceEach(null, new String[]{"a"}, new String[]{"b"}));
        assertEquals(StringUtils.replaceEach("", new String[]{"a"}, new String[]{"b"}),"");
        assertEquals(StringUtils.replaceEach("aba", null, null),"aba");
        assertEquals(StringUtils.replaceEach("aba", new String[0], null),"aba");
        assertEquals(StringUtils.replaceEach("aba", null, new String[0]),"aba");
        assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, null),"aba");

        assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, new String[]{""}),"b");
        assertEquals(StringUtils.replaceEach("aba", new String[]{null}, new String[]{"a"}),"aba");
        assertEquals(StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"w", "t"}),"wcte");
        assertEquals(StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"d", "t"}),"dcte");
        //JAVADOC TESTS END

        assertEquals("bcc", StringUtils.replaceEach("abc", new String[]{"a", "b"}, new String[]{"b", "c"}));
        assertEquals("q651.506bera", StringUtils.replaceEach("d216.102oren",
            new String[]{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", 
                "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
            new String[]{"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", 
                "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "N", "O", "P", "Q", 
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", 
                "H", "I", "J", "K", "L", "M", "5", "6", "7", "8", "9", "1", "2", "3", "4"}));

        // Test null safety inside arrays - LANG-552
        assertEquals(StringUtils.replaceEach("aba", new String[]{"a"}, new String[]{null}),"aba");
        assertEquals(StringUtils.replaceEach("aba", new String[]{"a", "b"}, new String[]{"c", null}),"cbc");
    }
```

## Test line
assertEquals(StringUtils.replaceEach("aba", new String[]{"a", "b"}, new String[]{"c", null}),"cbc");

## Failed test
org.apache.commons.lang3.StringUtilsTest::testReplace_StringStringArrayStringArray

## Buggy code
```java
/**
     * <p>
     * Replaces all occurrences of Strings within another String.
     * </p>
     * 
     * <p>
     * A <code>null</code> reference passed to this method is a no-op, or if
     * any "search string" or "string to replace" is null, that replace will be
     * ignored. 
     * </p>
     * 
     * <pre>
     *  StringUtils.replaceEach(null, *, *, *) = null
     *  StringUtils.replaceEach("", *, *, *) = ""
     *  StringUtils.replaceEach("aba", null, null, *) = "aba"
     *  StringUtils.replaceEach("aba", new String[0], null, *) = "aba"
     *  StringUtils.replaceEach("aba", null, new String[0], *) = "aba"
     *  StringUtils.replaceEach("aba", new String[]{"a"}, null, *) = "aba"
     *  StringUtils.replaceEach("aba", new String[]{"a"}, new String[]{""}, *) = "b"
     *  StringUtils.replaceEach("aba", new String[]{null}, new String[]{"a"}, *) = "aba"
     *  StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"w", "t"}, *) = "wcte"
     *  (example of how it repeats)
     *  StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"d", "t"}, false) = "dcte"
     *  StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"d", "t"}, true) = "tcte"
     *  StringUtils.replaceEach("abcde", new String[]{"ab", "d"}, new String[]{"d", "ab"}, *) = IllegalArgumentException
     * </pre>
     * 
     * @param text
     *            text to search and replace in, no-op if null
     * @param searchList
     *            the Strings to search for, no-op if null
     * @param replacementList
     *            the Strings to replace them with, no-op if null
     * @param repeat if true, then replace repeatedly 
     *       until there are no more possible replacements or timeToLive < 0
     * @param timeToLive
     *            if less than 0 then there is a circular reference and endless
     *            loop
     * @return the text with any replacements processed, <code>null</code> if
     *         null String input
     * @throws IllegalArgumentException
     *             if the search is repeating and there is an endless loop due
     *             to outputs of one being inputs to another
     * @throws IndexOutOfBoundsException
     *             if the lengths of the arrays are not the same (null is ok,
     *             and/or size 0)
     * @since 2.4
     */
    private static String replaceEach(String text, String[] searchList, String[] replacementList, 
                                      boolean repeat, int timeToLive) 
    {

        // mchyzer Performance note: This creates very few new objects (one major goal)
        // let me know if there are performance requests, we can create a harness to measure

        if (text == null || text.length() == 0 || searchList == null || 
            searchList.length == 0 || replacementList == null || replacementList.length == 0) 
        {
            return text;
        }

        // if recursing, this shouldnt be less than 0
        if (timeToLive < 0) {
            throw new IllegalStateException("TimeToLive of " + timeToLive + " is less than 0: " + text);
        }

        int searchLength = searchList.length;
        int replacementLength = replacementList.length;

        // make sure lengths are ok, these need to be equal
        if (searchLength != replacementLength) {
            throw new IllegalArgumentException("Search and Replace array lengths don't match: "
                + searchLength
                + " vs "
                + replacementLength);
        }

        // keep track of which still have matches
        boolean[] noMoreMatchesForReplIndex = new boolean[searchLength];

        // index on index that the match was found
        int textIndex = -1;
        int replaceIndex = -1;
        int tempIndex = -1;

        // index of replace array that will replace the search string found
        // NOTE: logic duplicated below START
        for (int i = 0; i < searchLength; i++) {
            if (noMoreMatchesForReplIndex[i] || searchList[i] == null || 
                searchList[i].length() == 0 || replacementList[i] == null) 
            {
                continue;
            }
            tempIndex = text.indexOf(searchList[i]);

            // see if we need to keep searching for this
            if (tempIndex == -1) {
                noMoreMatchesForReplIndex[i] = true;
            } else {
                if (textIndex == -1 || tempIndex < textIndex) {
                    textIndex = tempIndex;
                    replaceIndex = i;
                }
            }
        }
        // NOTE: logic mostly below END

        // no search strings found, we are done
        if (textIndex == -1) {
            return text;
        }

        int start = 0;

        // get a good guess on the size of the result buffer so it doesnt have to double if it goes over a bit
        int increase = 0;

        // count the replacement text elements that are larger than their corresponding text being replaced
        for (int i = 0; i < searchList.length; i++) {
            int greater = replacementList[i].length() - searchList[i].length();
            if (greater > 0) {
                increase += 3 * greater; // assume 3 matches
            }
        }
        // have upper-bound at 20% increase, then let Java take over
        increase = Math.min(increase, text.length() / 5);

        StringBuilder buf = new StringBuilder(text.length() + increase);

        while (textIndex != -1) {

            for (int i = start; i < textIndex; i++) {
                buf.append(text.charAt(i));
            }
            buf.append(replacementList[replaceIndex]);

            start = textIndex + searchList[replaceIndex].length();

            textIndex = -1;
            replaceIndex = -1;
            tempIndex = -1;
            // find the next earliest match
            // NOTE: logic mostly duplicated above START
            for (int i = 0; i < searchLength; i++) {
                if (noMoreMatchesForReplIndex[i] || searchList[i] == null || 
                    searchList[i].length() == 0 || replacementList[i] == null) 
                {
                    continue;
                }
                tempIndex = text.indexOf(searchList[i], start);

                // see if we need to keep searching for this
                if (tempIndex == -1) {
                    noMoreMatchesForReplIndex[i] = true;
                } else {
                    if (textIndex == -1 || tempIndex < textIndex) {
                        textIndex = tempIndex;
                        replaceIndex = i;
                    }
                }
            }
            // NOTE: logic duplicated above END

        }
        int textLength = text.length();
        for (int i = start; i < textLength; i++) {
            buf.append(text.charAt(i));
        }
        String result = buf.toString();
        if (!repeat) {
            return result;
        }

        return replaceEach(result, searchList, replacementList, repeat, timeToLive - 1);
    }
```
## mistake patch
以下之前你给出的错误的修正代码
```java


private static String replaceEach(String text, String[] searchList, String[] replacementList, 
                                  boolean repeat, int timeToLive) 
{
    if (text == null || text.length() == 0 || searchList == null || 
        searchList.length == 0 || replacementList == null || replacementList.length == 0) 
    {
        return text;
    }

    if (timeToLive < 0) {
        throw new IllegalStateException("TimeToLive of " + timeToLive + " is less than 0: " + text);
    }

    int searchLength = searchList.length;
    int replacementLength = replacementList.length;

    if (searchLength != replacementLength) {
        throw new IllegalArgumentException("Search and Replace array lengths don't match: "
            + searchLength
            + " vs "
            + replacementLength);
    }

    boolean[] noMoreMatchesForReplIndex = new boolean[searchLength];

    int textIndex = -1;
    int replaceIndex = -1;
    int tempIndex = -1;

    for (int i = 0; i < searchLength; i++) {
        if (noMoreMatchesForReplIndex[i] || searchList[i] == null || 
            searchList[i].length() == 0 || replacementList[i] == null) 
        {
            continue;
        }
        tempIndex = text.indexOf(searchList[i]);

        if (tempIndex == -1) {
            noMoreMatchesForReplIndex[i] = true;
        } else {
            if (textIndex == -1 || tempIndex < textIndex) {
                textIndex = tempIndex;
                replaceIndex = i;
            }
        }
    }

    if (textIndex == -1) {
        return text;
    }

    int start = 0;
    int increase = 0;

    for (int i = 0; i < searchList.length; i++) {
        if (searchList[i] != null && replacementList[i] != null) {
            int greater = replacementList[i].length() - searchList[i].length();
            if (greater > 0) {
                increase += 3 * greater;
            }
        }
    }
    increase = Math.min(increase, text.length() / 5);

    StringBuilder buf = new StringBuilder(text.length() + increase);

    while (textIndex != -1) {
        for (int i = start; i < textIndex; i++) {
            buf.append(text.charAt(i));
        }
        if (replacementList[replaceIndex] != null) {
            buf.append(replacementList[replaceIndex]);
        }

        start = textIndex + searchList[replaceIndex].length();

        textIndex = -1;
        replaceIndex = -1;
        tempIndex = -1;
        for (int i = 0; i < searchLength; i++) {
            if (noMoreMatchesForReplIndex[i] || searchList[i] == null || 
                searchList[i].length() == 0 || replacementList[i] == null) 
            {
                continue;
            }
            tempIndex = text.indexOf(searchList[i], start);

            if (tempIndex == -1) {
                noMoreMatchesForReplIndex[i] = true;
            } else {
                if (textIndex == -1 || tempIndex < textIndex) {
                    textIndex = tempIndex;
                    replaceIndex = i;
                }
            }
        }
    }
    int textLength = text.length();
    for (int i = start; i < textLength; i++) {
        buf.append(text.charAt(i));
    }
    String result = buf.toString();
    if (!repeat) {
        return result;
    }

    return replaceEach(result, searchList, replacementList, repeat, timeToLive - 1);
}

```
运用你给出的修复代码后，编译失败了
请你继续修正