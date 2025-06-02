根据测试用例，问题出在高Unicode字符的转义上。原代码在处理大于0x7F的字符时直接使用了char类型，但Java的char类型只能表示到0xFFFF，对于超过这个范围的Unicode字符需要使用代码点(code point)来处理。以下是修复后的代码：

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
            if (Character.isHighSurrogate(c) && i + 1 < len && Character.isLowSurrogate(str.charAt(i + 1))) {
                int codePoint = Character.toCodePoint(c, str.charAt(i + 1));
                writer.write("&#");
                writer.write(Integer.toString(codePoint, 10));
                writer.write(';');
                i++;
            } else {
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
            }
        }
    }
```

修复的关键点：
1. 添加了对代理对(surrogate pairs)的处理，用于支持大于0xFFFF的Unicode字符
2. 当检测到高代理字符(high surrogate)时，会检查下一个字符是否是低代理字符(low surrogate)
3. 如果是代理对，则使用Character.toCodePoint()方法获取完整的代码点
4. 然后写入正确的数字实体引用格式

这样修改后，测试用例中的高Unicode字符(如U+1D362)就能被正确转义为"&#119650;"了。