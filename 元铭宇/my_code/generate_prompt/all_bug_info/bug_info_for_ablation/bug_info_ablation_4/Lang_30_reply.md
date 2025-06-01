修复后的代码如下：

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
            for (int j = 0; j < searchLen; j++) {
                if (searchChars[j] == ch) {
                    return i;
                }
            }
        }
        return INDEX_NOT_FOUND;
    }
```

主要修改：
1. 删除了多余的注释行 `// ch is a supplementary character`，因为这个注释与代码逻辑无关
2. 保持了原有的缩进格式一致性

原代码逻辑本身是正确的，只是包含了一条无关的注释。修复后的代码功能完全相同，但更加简洁。