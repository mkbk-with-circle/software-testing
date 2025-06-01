

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

## Test line
assertEquals(0, SystemUtils.toJavaVersionInt(null));

## Failed test
org.apache.commons.lang3.SystemUtilsTest::testJavaVersionAsInt

## Error Code Block
```java
    public void testJavaVersionAsInt() {
        assertEquals(0, SystemUtils.toJavaVersionInt(null));
        assertEquals(0, SystemUtils.toJavaVersionInt(""));
        assertEquals(0, SystemUtils.toJavaVersionInt("0"));
        assertEquals(110, SystemUtils.toJavaVersionInt("1.1"));
        assertEquals(120, SystemUtils.toJavaVersionInt("1.2"));
        assertEquals(130, SystemUtils.toJavaVersionInt("1.3.0"));
        assertEquals(131, SystemUtils.toJavaVersionInt("1.3.1"));
        assertEquals(140, SystemUtils.toJavaVersionInt("1.4.0"));
        assertEquals(141, SystemUtils.toJavaVersionInt("1.4.1"));
        assertEquals(142, SystemUtils.toJavaVersionInt("1.4.2"));
        assertEquals(150, SystemUtils.toJavaVersionInt("1.5.0"));
        assertEquals(160, SystemUtils.toJavaVersionInt("1.6.0"));
        assertEquals(131, SystemUtils.toJavaVersionInt("JavaVM-1.3.1"));
        assertEquals(131, SystemUtils.toJavaVersionInt("1.3.1 subset"));
        // This used to return 0f in [lang] version 2.5:
        assertEquals(130, SystemUtils.toJavaVersionInt("XXX-1.3.x"));
    }
```

## Error
junit.framework.AssertionFailedError: expected:<0> but was:<0.0>
## mistake patch
以下之前你给出的错误的修正代码
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
    static int toJavaVersionInt(String version) {
        return (int)toVersionInt(toJavaVersionIntArray(version, JAVA_VERSION_TRIM_SIZE));
    }

```
运用你给出的修复代码后，编译失败了
请你继续修正