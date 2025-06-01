修复后的代码如下：

```java
/**
     * Escape constant fields into regular expression
     * @param regex The destination regex
     * @param value The source field
     * @param unquote If true, replace two success quotes ('') with single quote (')
     * @return The <code>StringBuilder</code>
     */
    private static StringBuilder escapeRegex(StringBuilder regex, String value, boolean unquote) {
        boolean wasWhite = false;
        for(int i = 0; i < value.length(); ++i) {
            char c = value.charAt(i);
            if(Character.isWhitespace(c)) {
                if(!wasWhite) {
                    wasWhite = true;
                    regex.append("\\s*+");
                }
                continue;
            }
            wasWhite = false;
            switch(c) {
            case '\'':
                if(unquote) {
                    if(++i < value.length()) {
                        c = value.charAt(i);
                        if(c != '\'') {
                            regex.append('\\');
                            i--; // go back one position since we advanced i but didn't use this character
                            c = '\'';
                        }
                    } else {
                        regex.append('\\');
                        i--; // go back one position since we advanced i past the end
                        c = '\'';
                    }
                } else {
                    regex.append('\\');
                }
                break;
            case '?':
            case '[':
            case ']':
            case '(':
            case ')':
            case '{':
            case '}':
            case '\\':
            case '|':
            case '*':
            case '+':
            case '^':
            case '$':
            case '.':
                regex.append('\\');
                break;
            }
            regex.append(c);
        }
        return regex;
    }
```

主要修复内容：
1. 修正了处理单引号时的逻辑，当unquote为true时正确处理连续两个单引号的情况
2. 为switch语句中的case添加了break语句，防止case穿透
3. 改进了索引越界处理，确保在到达字符串末尾时正确处理
4. 添加了当遇到单引号但不进行unquote时的转义处理