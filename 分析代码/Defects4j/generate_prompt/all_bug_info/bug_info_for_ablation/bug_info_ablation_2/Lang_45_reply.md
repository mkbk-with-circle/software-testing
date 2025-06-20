Here's the fixed code. The main issue was that the code didn't properly handle cases where the upper limit was larger than the string length. I've added additional checks to ensure we don't try to substring beyond the string's length.

```java
public static String abbreviate(String str, int lower, int upper, String appendToEnd) {
    // initial parameter checks
    if (str == null) {
        return null;
    }
    if (str.length() == 0) {
        return StringUtils.EMPTY;
    }

    // if the lower value is greater than the length of the string,
    // set to the length of the string
    if (lower > str.length()) {
        lower = str.length();
    }
    // if the upper value is -1 (i.e. no limit) or is greater
    // than the length of the string, set to the length of the string
    if (upper == -1 || upper > str.length()) {
        upper = str.length();
    }
    // if upper is less than lower, raise it to lower
    if (upper < lower) {
        upper = lower;
    }

    StringBuffer result = new StringBuffer();
    int index = StringUtils.indexOf(str, " ", lower);
    if (index == -1) {
        result.append(str.substring(0, Math.min(upper, str.length())));
        // only if abbreviation has occured do we append the appendToEnd value
        if (upper != str.length()) {
            result.append(StringUtils.defaultString(appendToEnd));
        }
    } else if (index > upper) {
        result.append(str.substring(0, Math.min(upper, str.length())));
        result.append(StringUtils.defaultString(appendToEnd));
    } else {
        result.append(str.substring(0, Math.min(index, str.length())));
        result.append(StringUtils.defaultString(appendToEnd));
    }
    return result.toString();
}
```

Key changes made:
1. Added a check to handle when lower limit is greater than string length
2. Added Math.min() when doing substring operations to ensure we don't exceed string length
3. Maintained all the original functionality while making it more robust against edge cases

The fixed code should now handle all the test cases without throwing StringIndexOutOfBoundsException.