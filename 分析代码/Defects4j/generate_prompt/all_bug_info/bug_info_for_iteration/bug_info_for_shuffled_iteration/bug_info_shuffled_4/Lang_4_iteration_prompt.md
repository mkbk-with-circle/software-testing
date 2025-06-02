

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

## Test line
assertEquals("Incorrect codepoint consumption", 3, result);

## Failed test
org.apache.commons.lang3.text.translate.LookupTranslatorTest::testLang882

## Error Code Block
```java
    public void testLang882() throws IOException {
        final LookupTranslator lt = new LookupTranslator(new CharSequence[][] { { new StringBuffer("one"), new StringBuffer("two") } });
        final StringWriter out = new StringWriter();
        final int result = lt.translate(new StringBuffer("one"), 0, out);
        assertEquals("Incorrect codepoint consumption", 3, result);
        assertEquals("Incorrect value", "two", out.toString());
    }
```

## Error
junit.framework.AssertionFailedError: Incorrect codepoint consumption expected:<3> but was:<0>
## mistake patch
以下之前你给出的错误的修正代码
```java


public int translate(final CharSequence input, final int index, final Writer out) throws IOException {
    int max = longest;
    if (index + longest > input.length()) {
        max = input.length() - index;
    }
    // descend so as to get a greedy algorithm
    for (int i = max; i >= shortest; i--) {
        final CharSequence subSeq = input.subSequence(index, index + i);
        final CharSequence result = lookupMap.get(subSeq.toString()); // Convert subSeq to String for proper lookup
        if (result != null) {
            out.write(result.toString());
            return i;
        }
    }
    return 0;
}

```
请你继续修正