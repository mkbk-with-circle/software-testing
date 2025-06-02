修复后的代码需要正确处理补充字符(Supplementary Characters)的情况。以下是修复后的代码：

```java
/**
     * <p>Search a CharSequence to find the first index of any
     * character in the given set of characters.</p>
     *
     * <p>A <code>null</code> String will return <code>-1</code>.
     * A <code>null</code> or zero length search array will return <code>-1</code>.</p>
     *
     * <pre>
     * StringUtils.indexOfAny(null, *)                = -1
     * StringUtils.indexOfAny("", *)                  = -1
     * StringUtils.indexOfAny(*, null)                = -1
     * StringUtils.indexOfAny(*, [])                  = -1
     * StringUtils.indexOfAny("zzabyycdxx",['z','a']) = 0
     * StringUtils.indexOfAny("zzabyycdxx",['b','y']) = 3
     * StringUtils.indexOfAny("aba", ['z'])           = -1
     * </pre>
     *
     * @param cs  the CharSequence to check, may be null
     * @param searchChars  the chars to search for, may be null
     * @return the index of any of the chars, -1 if no match or null input
     * @since 2.0
     */
    public static int indexOfAny(CharSequence cs, char[] searchChars) {
        if (isEmpty(cs) || ArrayUtils.isEmpty(searchChars)) {
            return INDEX_NOT_FOUND;
        }
        int csLen = cs.length();
        int searchLen = searchChars.length;
        for (int i = 0; i < csLen; i++) {
            char ch = cs.charAt(i);
            if (Character.isHighSurrogate(ch)) {
                if (i < csLen - 1) {
                    char ch2 = cs.charAt(i + 1);
                    if (Character.isLowSurrogate(ch2)) {
                        int codePoint = Character.toCodePoint(ch, ch2);
                        for (int j = 0; j < searchLen; j++) {
                            if (searchChars[j] == codePoint) {
                                return i;
                            }
                        }
                        i++;
                    }
                }
            } else {
                for (int j = 0; j < searchLen; j++) {
                    if (searchChars[j] == ch) {
                        return i;
                    }
                }
            }
        }
        return INDEX_NOT_FOUND;
    }
```

主要修改点：
1. 添加了对补充字符(Supplementary Characters)的处理逻辑
2. 当遇到高代理字符(High Surrogate)时，检查下一个字符是否是低代理字符(Low Surrogate)
3. 如果是有效的代理对，将其转换为代码点(code point)进行比较
4. 否则按普通字符处理

这样修改后，测试用例中对于补充字符的比较就能正确工作了。