修复后的代码需要正确处理高Unicode字符（大于0xFFFF的字符），使用`codePointAt`方法而不是`charAt`方法，因为`char`只能表示0x0000-0xFFFF的字符。以下是修复后的代码：

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
            int c = str.codePointAt(i);
            String entityName = this.entityName(c);
            if (entityName == null) {
                if (c > 0x7F) {
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
            if (c > 0xFFFF) {
                i++; // Skip the next surrogate pair character
            }
        }
    }
```

主要修改点：
1. 将`char c = str.charAt(i)`改为`int c = str.codePointAt(i)`，以支持高Unicode字符
2. 添加了对代理对的处理，当字符大于0xFFFF时，跳过下一个字符（因为高Unicode字符在Java中用两个char表示）
3. 其他逻辑保持不变，但所有字符比较都使用int类型的code point而不是char类型