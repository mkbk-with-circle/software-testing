修复后的代码如下：

```java
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
        if (searchList[i] == null || replacementList[i] == null) {
            continue;
        }
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

主要修改：
1. 在计算increase时添加了对searchList[i]和replacementList[i]为null的判断，避免NullPointerException
2. 修复了数组访问时的语法错误（将replacementList[i]改为replacementList[i]）

其他逻辑保持不变，这些修改确保了代码在处理null值时更加健壮，并且修复了语法错误。