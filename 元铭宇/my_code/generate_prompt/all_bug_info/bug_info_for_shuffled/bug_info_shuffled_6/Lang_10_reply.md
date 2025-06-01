根据测试用例和错误信息，问题出在处理带引号的文本时没有正确处理转义字符。修复后的代码如下：

```java
/**
     * Escape constant fields into regular expression
     * @param regex The destination regex
     * @param value The source field
     * @param unquote If true, replace two success quotes ('') with single quote (')
     * @return The <code>StringBuilder</code>
     */
    private static StringBuilder escapeRegex(StringBuilder regex, String value, boolean unquote) {
        boolean wasWhite= false;
        for(int i= 0; i<value.length(); ++i) {
            char c= value.charAt(i);
            if(Character.isWhitespace(c)) {
                if(!wasWhite) {
                    wasWhite= true;
                    regex.append("\\s*+");
                }
                continue;
            }
            wasWhite= false;
            switch(c) {
            case '\'':
                if(unquote) {
                    if(++i<value.length()) {
                        c= value.charAt(i);
                        if(c != '\'') {
                            regex.append('\\');
                        }
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

主要修改点：
1. 修复了处理引号时的逻辑，当unquote为true时，正确处理连续两个引号的情况
2. 为所有case添加了break语句确保逻辑正确
3. 修改了引号处理的条件判断，确保不会越界访问字符串
4. 当遇到单个引号时，确保正确添加转义字符