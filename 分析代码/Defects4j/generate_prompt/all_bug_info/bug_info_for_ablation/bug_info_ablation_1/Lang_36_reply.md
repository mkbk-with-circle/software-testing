I'll help you debug the code. The issue is that the code doesn't properly handle numbers ending with a decimal point (like "2."). Here's the fixed version:

```java
public static Number createNumber(String str) throws NumberFormatException {
    if (str == null) {
        return null;
    }
    if (StringUtils.isBlank(str)) {
        throw new NumberFormatException("A blank string is not a valid number");
    }  
    if (str.startsWith("--")) {
        return null;
    }
    if (str.startsWith("0x") || str.startsWith("-0x")) {
        return createInteger(str);
    }   
    char lastChar = str.charAt(str.length() - 1);
    String mant;
    String dec;
    String exp;
    int decPos = str.indexOf('.');
    int expPos = str.indexOf('e') + str.indexOf('E') + 1;

    if (decPos > -1) {
        if (expPos > -1) {
            if (expPos < decPos) {
                throw new NumberFormatException(str + " is not a valid number.");
            }
            dec = str.substring(decPos + 1, expPos);
        } else {
            dec = str.substring(decPos + 1);
        }
        mant = str.substring(0, decPos);
    } else {
        if (expPos > -1) {
            mant = str.substring(0, expPos);
        } else {
            mant = str;
        }
        dec = null;
    }
    if (!Character.isDigit(lastChar) {
        if (expPos > -1 && expPos < str.length() - 1) {
            exp = str.substring(expPos + 1, str.length() - 1);
        } else {
            exp = null;
        }
        String numeric = str.substring(0, str.length() - 1);
        boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
        switch (lastChar) {
            case 'l' :
            case 'L' :
                if (dec == null
                    && exp == null
                    && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric))) {
                    try {
                        return createLong(numeric);
                    } catch (NumberFormatException nfe) {
                    }
                    return createBigInteger(numeric);
                }
                throw new NumberFormatException(str + " is not a valid number.");
            case 'f' :
            case 'F' :
                try {
                    Float f = NumberUtils.createFloat(numeric);
                    if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                        return f;
                    }
                } catch (NumberFormatException nfe) {
                }
            case 'd' :
            case 'D' :
                try {
                    Double d = NumberUtils.createDouble(numeric);
                    if (!(d.isInfinite() || (d.floatValue() == 0.0D && !allZeros))) {
                        return d;
                    }
                } catch (NumberFormatException nfe) {
                }
                try {
                    return createBigDecimal(numeric);
                } catch (NumberFormatException e) {
                }
            default :
                throw new NumberFormatException(str + " is not a valid number.");
        }
    } else {
        if (expPos > -1 && expPos < str.length() - 1) {
            exp = str.substring(expPos + 1, str.length());
        } else {
            exp = null;
        }
        if (dec == null && exp == null) {
            try {
                return createInteger(str);
            } catch (NumberFormatException nfe) {
            }
            try {
                return createLong(str);
            } catch (NumberFormatException nfe) {
            }
            return createBigInteger(str);
        } else {
            boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
            try {
                if (str.charAt(str.length() - 1) == '.') {
                    str = str.substring(0, str.length() - 1);
                }
                Float f = createFloat(str);
                if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                    return f;
                }
            } catch (NumberFormatException nfe) {
            }
            try {
                Double d = createDouble(str);
                if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {
                    return d;
                }
            } catch (NumberFormatException nfe) {
            }
            return createBigDecimal(str);
        }
    }
}
```

The main change is in the else block where we handle numbers with decimal points. I added a check for strings ending with '.' and remove the trailing decimal point before attempting to parse it as a float or double. This fixes the case where numbers like "2." are passed in.

The fix specifically adds:
```java
if (str.charAt(str.length() - 1) == '.') {
    str = str.substring(0, str.length() - 1);
}
```

before attempting to create the Float or Double values. This ensures that numbers with trailing decimal points are properly handled.