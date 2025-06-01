根据测试用例和错误信息，问题在于当输入字符串完全匹配时，`translate`方法没有正确处理最长匹配的情况。修复后的代码如下：

```java
public int translate(final CharSequence input, final int index, final Writer out) throws IOException {
    int max = longest;
    if (index + longest > input.length()) {
        max = input.length() - index;
    }
    // descend so as to get a greedy algorithm
    for (int i = max; i >= shortest; i--) {
        if (index + i > input.length()) {
            continue;
        }
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

主要修改是添加了对`index + i > input.length()`的检查，确保不会尝试获取超出输入长度的子序列。这样当输入完全匹配时（如测试用例中的"one"），方法会正确返回匹配的长度3。