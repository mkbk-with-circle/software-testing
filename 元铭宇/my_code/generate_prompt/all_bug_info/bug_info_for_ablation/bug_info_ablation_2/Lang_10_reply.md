根据错误信息和代码分析，问题出在`escapeRegex`方法处理单引号时的逻辑。当`unquote`为true时，它会跳过下一个字符，这可能导致日期解析错误。以下是修复后的代码：

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
                    if(i+1 < value.length() && value.charAt(i+1) == '\'') {
                        i++; // skip next quote
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
1. 修改了单引号处理逻辑，只有当遇到连续两个单引号时才跳过下一个字符
2. 当`unquote`为false时，对单引号进行转义
3. 添加了`break`语句确保每个case都能正确终止
4. 移除了直接返回regex的情况，确保所有字符都能被处理

这些修改应该能解决日期解析错误的问题，同时保持原有的转义功能。