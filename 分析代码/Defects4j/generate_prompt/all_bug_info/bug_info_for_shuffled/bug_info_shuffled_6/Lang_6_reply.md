修复后的代码如下：

```java
/**
     * Translate an input onto a Writer. This is intentionally final as its algorithm is 
     * tightly coupled with the abstract method of this class. 
     *
     * @param input CharSequence that is being translated
     * @param out Writer to translate the text to
     * @throws IOException if and only if the Writer produces an IOException
     */
    public final void translate(CharSequence input, Writer out) throws IOException {
        if (out == null) {
            throw new IllegalArgumentException("The Writer must not be null");
        }
        if (input == null) {
            return;
        }
        int pos = 0;
        int len = input.length();
        while (pos < len) {
            int consumed = translate(input, pos, out);
            if (consumed == 0) {
                char c1 = input.charAt(pos);
                if (Character.isHighSurrogate(c1) && pos + 1 < len) {
                    char c2 = input.charAt(pos + 1);
                    if (Character.isLowSurrogate(c2)) {
                        out.write(new char[]{c1, c2});
                        pos += 2;
                        continue;
                    }
                }
                out.write(c1);
                pos++;
            } else {
                pos += consumed;
            }
        }
    }
```

主要修改点：
1. 移除了原来的Character.codePointAt处理方式，改为直接处理字符
2. 增加了对代理对(surrogate pairs)的显式处理
3. 简化了位置移动逻辑，直接根据consumed值或字符数移动pos
4. 正确处理了高位代理和低位代理的组合情况

这个修复版本能够正确处理代理对(如emoji字符)的情况，避免了原来的StringIndexOutOfBoundsException错误。