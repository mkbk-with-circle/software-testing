根据测试用例和错误信息，问题出在`escapeRegex`方法处理空格和引号的逻辑上。测试用例"M E"和"3  Tue"需要正确匹配空格模式。以下是修复后的代码：

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
                    regex.append("\\s+");
                }
                continue;
            }
            wasWhite = false;
            switch(c) {
            case '\'':
                if(unquote) {
                    if(++i == value.length()) {
                        return regex;
                    }
                    c = value.charAt(i);
                    if(c != '\'') {
                        regex.append('\\');
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
1. 将`\\s*+`改为`\\s+`，因为`*`表示0次或多次匹配，而`+`表示1次或多次匹配，这样能更准确地匹配输入中的多个空格
2. 在引号处理逻辑中添加了对非连续引号情况的处理
3. 在switch语句的每个case后添加了`break`语句以确保逻辑正确
4. 改进了代码格式，使变量赋值更清晰易读

这些修改应该能解决测试用例中的日期解析问题。