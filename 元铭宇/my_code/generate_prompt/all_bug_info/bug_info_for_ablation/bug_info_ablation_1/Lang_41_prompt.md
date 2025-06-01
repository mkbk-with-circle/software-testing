## Buggy code
```java
/**
     * <p>Gets the class name minus the package name from a String.</p>
     *
     * <p>The string passed in is assumed to be a class name - it is not checked.</p>
     *
     * @param className  the className to get the short name for
     * @return the class name of the class without the package name or an empty string
     */
    public static String getShortClassName(String className) {
        if (className == null) {
            return StringUtils.EMPTY;
        }
        if (className.length() == 0) {
            return StringUtils.EMPTY;
        }


        // Handle array encoding
            // Strip Object type encoding


        int lastDotIdx = className.lastIndexOf(PACKAGE_SEPARATOR_CHAR);
        int innerIdx = className.indexOf(
                INNER_CLASS_SEPARATOR_CHAR, lastDotIdx == -1 ? 0 : lastDotIdx + 1);
        String out = className.substring(lastDotIdx + 1);
        if (innerIdx != -1) {
            out = out.replace(INNER_CLASS_SEPARATOR_CHAR, PACKAGE_SEPARATOR_CHAR);
        }
        return out;
    }
```

## Failed test
org.apache.commons.lang.ClassUtilsTest::test_getShortClassName_Class

## Test line
assertEquals("String[]", ClassUtils.getShortClassName(String[].class));

## Error
junit.framework.ComparisonFailure: expected:<String[[]]> but was:<String[;]>

