修复后的代码需要正确处理高Unicode字符（大于0xFFFF的字符）。原代码在处理高Unicode字符时没有考虑代理对(surrogate pairs)的情况，导致将单个字符错误地拆分为两个字符输出。以下是修复后的代码：

```java
/**
     * <p>
     * Escapes the characters in the <code>String</code> passed and writes the result to the <code>Writer</code>
     * passed.
     * </p>
     * 
     * @param writer
     *            The <code>Writer</code> to write the results of the escaping to. Assumed to be a non-null value.
     * @param str
     *            The <code>String</code> to escape. Assumed to be a non-null value.
     * @throws IOException
     *             when <code>Writer</code> passed throws the exception from calls to the {@link Writer#write(int)}
     *             methods.
     * 
     * @see #escape(String)
     * @see Writer
     */
    public void escape(Writer writer, String str) throws IOException {
        int len = str.length();
        for (int i = 0; i < len; i++) {
            char c = str.charAt(i);
            String entityName = this.entityName(c);
            if (entityName == null) {
                if (Character.isHighSurrogate(c) && i + 1 < len && Character.isLowSurrogate(str.charAt(i + 1))) {
                    int codePoint = Character.toCodePoint(c, str.charAt(i + 1));
                    writer.write("&#");
                    writer.write(Integer.toString(codePoint, 10));
                    writer.write(';');
                    i++; // Skip the low surrogate
                } else if (c > 0x7F) {
                    writer.write("&#");
                    writer.write(Integer.toString(c, 10));
                    writer.write(';');
                } else {
                    writer.write(c);
                }
            } else {
                writer.write('&');
                writer.write(entityName);
                writer.write(';');
            }
        }
    }
```

主要修改是添加了对代理对(surrogate pairs)的处理，当遇到高代理字符时，会检查下一个字符是否是低代理字符，如果是，则使用Character.toCodePoint()方法将它们组合成一个完整的Unicode码点，然后进行转义输出。这样可以正确处理大于0xFFFF的Unicode字符。