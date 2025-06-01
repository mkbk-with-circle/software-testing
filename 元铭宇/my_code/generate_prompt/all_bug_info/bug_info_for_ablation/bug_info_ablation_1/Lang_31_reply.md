修复后的代码如下：

```java
/**
     * <p>Checks if the CharSequence contains any character in the given
     * set of characters.</p>
     *
     * <p>A <code>null</code> CharSequence will return <code>false</code>.
     * A <code>null</code> or zero length search array will return <code>false</code>.</p>
     *
     * <pre>
     * StringUtils.containsAny(null, *)                = false
     * StringUtils.containsAny("", *)                  = false
     * StringUtils.containsAny(*, null)                = false
     * StringUtils.containsAny(*, [])                  = false
     * StringUtils.containsAny("zzabyycdxx",['z','a']) = true
     * StringUtils.containsAny("zzabyycdxx",['b','y']) = true
     * StringUtils.containsAny("aba", ['z'])           = false
     * </pre>
     *
     * @param cs  the CharSequence to check, may be null
     * @param searchChars  the chars to search for, may be null
     * @return the <code>true</code> if any of the chars are found,
     * <code>false</code> if no match or null input
     * @since 2.4
     */
    public static boolean containsAny(CharSequence cs, char[] searchChars) {
        if (isEmpty(cs) || ArrayUtils.isEmpty(searchChars)) {
            return false;
        }
        int csLength = cs.length();
        int searchLength = searchChars.length;
        for (int i = 0; i < csLength; i++) {
            char ch = cs.charAt(i);
            for (int j = 0; j < searchLength; j++) {
                if (searchChars[j] == ch) {
                    if (Character.isHighSurrogate(ch)) {
                        if (i < csLength - 1 && searchChars[j] == cs.charAt(i + 1)) {
                            return true;
                        }
                    } else {
                        return true;
                    }
                }
            }
        }
        return false;
    }
```

修复说明：
1. 原代码在处理补充字符(Supplementary Characters)时存在问题，它会错误地将高代理项字符单独匹配
2. 修复后的代码在检测到高代理项字符时，会检查下一个字符是否也匹配，确保正确处理补充字符
3. 对于基本多语言平面(BMP)中的字符，保持原有直接返回true的逻辑
4. 这样修改后，测试用例 `assertEquals(false, StringUtils.containsAny(CharU20000, CharU20001.toCharArray()))` 就能通过，因为这两个不同的补充字符不会错误匹配