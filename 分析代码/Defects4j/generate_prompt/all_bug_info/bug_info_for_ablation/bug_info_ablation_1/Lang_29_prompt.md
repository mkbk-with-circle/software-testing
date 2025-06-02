## Buggy code
```java
/**
     * <p>
     * Converts the given Java version string to an <code>int</code>.
     * </p>
     * 
     * <p>
     * Example return values:
     * </p>
     * <ul>
     * <li><code>120</code> for Java 1.2</li>
     * <li><code>131</code> for Java 1.3.1</li>
     * <li><code>160</code> for Java 1.6.0_20</li>
     * </ul>
     * 
     * <p>
     * Patch releases are not reported.
     * </p>
     * <p>
     * This method is package private instead of private to support unit test invocation.
     * </p>
     * 
     * @return the version, for example 131 for Java 1.3.1
     */
    static float toJavaVersionInt(String version) {
        return toVersionInt(toJavaVersionIntArray(version, JAVA_VERSION_TRIM_SIZE));
    }
```

## Failed test
org.apache.commons.lang3.SystemUtilsTest::testJavaVersionAsInt

## Test line
assertEquals(0, SystemUtils.toJavaVersionInt(null));

## Error
junit.framework.AssertionFailedError: expected:<0> but was:<0.0>

