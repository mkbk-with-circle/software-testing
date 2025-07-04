修复后的代码使用 `Locale.ROOT` 来确保大小写转换不受本地化设置的影响：

```java
/**
 * <p>Checks if String contains a search String irrespective of case,
 * handling <code>null</code>. Case-insensitivity is defined as by
 * {@link String#equalsIgnoreCase(String)}.
 *
 * <p>A <code>null</code> String will return <code>false</code>.</p>
 *
 * <pre>
 * StringUtils.contains(null, *) = false
 * StringUtils.contains(*, null) = false
 * StringUtils.contains("", "") = true
 * StringUtils.contains("abc", "") = true
 * StringUtils.contains("abc", "a") = true
 * StringUtils.contains("abc", "z") = false
 * StringUtils.contains("abc", "A") = true
 * StringUtils.contains("abc", "Z") = false
 * </pre>
 *
 * @param str  the String to check, may be null
 * @param searchStr  the String to find, may be null
 * @return true if the String contains the search String irrespective of
 * case or false if not or <code>null</code> string input
 */
public static boolean containsIgnoreCase(String str, String searchStr) {
    if (str == null || searchStr == null) {
        return false;
    }
    return contains(str.toUpperCase(Locale.ROOT), searchStr.toUpperCase(Locale.ROOT));
}
```