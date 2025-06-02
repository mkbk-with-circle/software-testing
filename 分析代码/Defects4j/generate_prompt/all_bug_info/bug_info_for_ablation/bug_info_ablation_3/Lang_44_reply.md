The bug occurs when trying to process an empty string after removing the last character. Here's the fixed code with proper checks:

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
    if (!Character.isDigit(lastChar)) {
        if (expPos > -1 && expPos < val.length() - 1) {
            exp = val.substring(expPos + 1, val.length() - 1);
        } else {
            exp = null;
        }
        String numeric = val.substring(0, val.length() - 1);
        boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
        switch (lastChar) {
            case 'l' :
            case 'L' :
                if (dec == null
                    && exp == null
                    && (numeric.length() > 0 
                        && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric)))) {
                    try {
                        return createLong(numeric);
                    } catch (NumberFormatException nfe) {
                        //Too big for a long
                    }
                    return createBigInteger(numeric);
                }
                throw new NumberFormatException(val + " is not a valid number.");
            case 'f' :
            case 'F' :
                try {
                    Float f = NumberUtils.createFloat(numeric);
                    if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                        return f;
                    }
                } catch (NumberFormatException e) {
                    // ignore the bad number
                }
                //Fall through
            case 'd' :
            case 'D' :
                try {
                    Double d = NumberUtils.createDouble(numeric);
                    if (!(d.isInfinite() || (d.floatValue() == 0.0D && !allZeros))) {
                        return d;
                    }
                } catch (NumberFormatException nfe) {
                    // empty catch
                }
                try {
                    return createBigDecimal(numeric);
                } catch (NumberFormatException e) {
                    // empty catch
                }
                //Fall through
            default :
                throw new NumberFormatException(val + " is not a valid number.");
        }
    } else {
        if (expPos > -1 && expPos < val.length() - 1) {
            exp = val.substring(expPos + 1, val.length());
        } else {
            exp = null;
        }
        if (dec == null && exp == null) {
            try {
                return createInteger(val);
            } catch (NumberFormatException nfe) {
                // empty catch
            }
            try {
                return createLong(val);
            } catch (NumberFormatException nfe) {
                // empty catch
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
                // empty catch
            }
            try {
                Double d = createDouble(val);
                if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {
                    return d;
                }
            } catch (NumberFormatException nfe) {
                // empty catch
            }
            return createBigDecimal(val);
        }
    }
}
```

The main fix was adding a check for `numeric.length() > 0` before trying to access `numeric.charAt(0)` in the 'L' case handler. This prevents the StringIndexOutOfBoundsException when the input string is a single character that gets removed (like "L" would become an empty string after removing the last character).