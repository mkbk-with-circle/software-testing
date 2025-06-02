修复后的代码如下：

```java
public static Number createNumber(String val) throws NumberFormatException {
    if (val == null) {
        return null;
    }
    if (val.length() == 0) {
        throw new NumberFormatException("\"\" is not a valid number.");
    }
    if (val.startsWith("--")) {
        return null;
    }
    if (val.startsWith("0x") || val.startsWith("-0x")) {
        return createInteger(val);
    }   
    char lastChar = val.charAt(val.length() - 1);
    String mant;
    String dec;
    String exp;
    int decPos = val.indexOf('.');
    int expPos = val.indexOf('e') + val.indexOf('E') + 1;

    if (decPos > -1) {
        if (expPos > -1) {
            if (expPos < decPos) {
                throw new NumberFormatException(val + " is not a valid number.");
            }
            dec = val.substring(decPos + 1, expPos);
        } else {
            dec = val.substring(decPos + 1);
        }
        mant = val.substring(0, decPos);
    } else {
        if (expPos > -1) {
            mant = val.substring(0, expPos);
        } else {
            mant = val;
        }
        dec = null;
    }
    if (!Character.isDigit(lastChar) && lastChar != '.') {
        if (expPos > -1 && expPos < val.length() - 1) {
            exp = val.substring(expPos + 1, val.length() - 1);
        } else {
            exp = null;
        }
        String numeric = val.substring(0, val.length() - 1);
        boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
        switch (lastChar) {
            case 'l':
            case 'L':
                if (dec == null
                    && exp == null
                    && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric))) {
                    try {
                        return createLong(numeric);
                    } catch (NumberFormatException nfe) {
                        return createBigInteger(numeric);
                    }
                }
                throw new NumberFormatException(val + " is not a valid number.");
            case 'f':
            case 'F':
                try {
                    Float f = createFloat(numeric);
                    if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                        return f;
                    }
                } catch (NumberFormatException e) {
                }
            case 'd':
            case 'D':
                try {
                    Double d = createDouble(numeric);
                    if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {
                        return d;
                    }
                } catch (NumberFormatException nfe) {
                }
                try {
                    return createBigDecimal(numeric);
                } catch (NumberFormatException e) {
                }
            default:
                throw new NumberFormatException(val + " is not a valid number.");
        }
    } else {
        if (expPos > -1 && expPos < val.length() - 1) {
            exp = val.substring(expPos + 1);
        } else {
            exp = null;
        }
        if (dec == null && exp == null) {
            try {
                return createInteger(val);
            } catch (NumberFormatException nfe) {
            }
            try {
                return createLong(val);
            } catch (NumberFormatException nfe) {
            }
            return createBigInteger(val);
        } else {
            boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
            try {
                Float f = createFloat(val);
                if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                    return f;
                }
            } catch (NumberFormatException nfe) {
            }
            try {
                Double d = createDouble(val);
                if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {
                    return d;
                }
            } catch (NumberFormatException nfe) {
            }
            return createBigDecimal(val);
        }
    }
}
```

主要修复点：
1. 在检查最后一个字符是否为数字时，添加了对小数点'.'的判断，因为数字可能以小数点结尾
2. 修复了指数部分提取时的错误，当有类型后缀时，指数部分应该从expPos+1到val.length()-1
3. 当没有类型后缀时，指数部分应该从expPos+1到val.length()
4. 移除了NumberUtils的冗余调用，直接使用createFloat和createDouble方法
5. 修复了代码格式问题，如case语句后的空格等

注意：此代码假设存在以下辅助方法：
- isAllZeros()
- isDigits()
- createInteger()
- createLong()
- createBigInteger()
- createFloat()
- createDouble()
- createBigDecimal()