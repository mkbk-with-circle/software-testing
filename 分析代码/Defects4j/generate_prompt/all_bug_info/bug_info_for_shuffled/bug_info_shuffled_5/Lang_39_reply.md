修复后的代码如下：

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

主要修改点：
1. 在计算increase时增加了对searchList[i]和replacementList[i]是否为null的检查
2. 在追加替换字符串时增加了对replacementList[replaceIndex]是否为null的检查

这些修改确保了当replacementList中包含null值时不会抛出NullPointerException，同时保持了原有的功能逻辑。