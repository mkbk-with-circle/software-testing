## Buggy code
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
						// ch is a supplementary character
						// ch is in the Basic Multilingual Plane
						return true;
				}
			}
		}
		return false;
	}
```

## Failed test
org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsAnyCharArrayWithSupplementaryChars

## Test line
assertEquals(false, StringUtils.containsAny(CharU20000, CharU20001.toCharArray()));

## Error
junit.framework.AssertionFailedError: expected:<false> but was:<true>

