## Buggy code
```java
public int translate(final CharSequence input, final int index, final Writer out) throws IOException {
        int max = longest;
        if (index + longest > input.length()) {
            max = input.length() - index;
        }
        // descend so as to get a greedy algorithm
        for (int i = max; i >= shortest; i--) {
            final CharSequence subSeq = input.subSequence(index, index + i);
            final CharSequence result = lookupMap.get(subSeq);
            if (result != null) {
                out.write(result.toString());
                return i;
            }
        }
        return 0;
    }
```



## Error
junit.framework.AssertionFailedError: Incorrect codepoint consumption expected:<3> but was:<0>


