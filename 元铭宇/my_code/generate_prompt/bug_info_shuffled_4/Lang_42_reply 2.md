根据测试用例，问题出在处理高Unicode字符（大于0xFFFF的字符）时，代码将其拆分为代理对(surrogate pair)而不是作为一个完整的码点处理。以下是修复后的代码：

```java
public void escape(Writer writer, String str) throws IOException {
    int len = str.length();
    for (int i = 0; i < len; i++) {
        char c = str.charAt(i);
        if (Character.isHighSurrogate(c)) {
            if (i + 1 < len) {
                char low = str.charAt(i + 1);
                if (Character.isLowSurrogate(low)) {
                    int codePoint = Character.toCodePoint(c, low);
                    writer.write("&#");
                    writer.write(Integer.toString(codePoint, 10));
                    writer.write(';');
                    i++; // skip the low surrogate
                    continue;
                }
            }
        }
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
```

修复的关键点：
1. 添加了对代理对(surrogate pair)的检测，使用Character.isHighSurrogate()和Character.isLowSurrogate()
2. 当检测到高代理字符时，将其与后续的低代理字符组合成完整的码点(使用Character.toCodePoint())
3. 正确处理高Unicode字符的转义，输出单个十进制实体引用(如"&#119650;")而不是拆分的代理对(如"&#55348;&#57186;")
4. 处理完代理对后跳过下一个字符(i++)，因为低代理字符已经处理过了