Here's the fixed code that handles the case of numbers ending with a decimal point (like "2."):

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
    // Handle case where string ends with decimal point
    if (dec != null && dec.isEmpty()) {
        dec = null;
        mant = str.substring(0, decPos);
    }
    if (!Character.isDigit(lastChar)) {
        if (expPos > -1 && expPos < str.length() - 1) {
            exp = str.substring(expPos + 1, str.length() - 1);
        } else {
            exp = null;
        }
        //Requesting a specific type..
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
                        //Too big for a long
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
                    // ignore the bad number
                }
                //$FALL-THROUGH$
            case 'd' :
            case 'D' :
                try {
                    Double d = NumberUtils.createDouble(numeric);
                    if (!(d.isInfinite() || (d.floatValue() == 0.0D && !allZeros))) {
                        return d;
                    }
                } catch (NumberFormatException nfe) {
                    // ignore the bad number
                }
                try {
                    return createBigDecimal(numeric);
                } catch (NumberFormatException e) {
                    // ignore the bad number
                }
                //$FALL-THROUGH$
            default :
                throw new NumberFormatException(str + " is not a valid number.");

        }
    } else {
        //User doesn't have a preference on the return type, so let's start
        //small and go from there...
        if (expPos > -1 && expPos < str.length() - 1) {
            exp = str.substring(expPos + 1, str.length());
        } else {
            exp = null;
        }
        if (dec == null && exp == null) {
            //Must be an int,long,bigint
            try {
                return createInteger(str);
            } catch (NumberFormatException nfe) {
                // ignore the bad number
            }
            try {
                return createLong(str);
            } catch (NumberFormatException nfe) {
                // ignore the bad number
            }
            return createBigInteger(str);

        } else {
            //Must be a float,double,BigDec
            boolean allZeros = isAllZeros(mant) && isAllZeros(exp);
            try {
                Float f = createFloat(str);
                if (!(f.isInfinite() || (f.floatValue() == 0.0F && !allZeros))) {
                    return f;
                }
            } catch (NumberFormatException nfe) {
                // ignore the bad number
            }
            try {
                Double d = createDouble(str);
                if (!(d.isInfinite() || (d.doubleValue() == 0.0D && !allZeros))) {
                    return d;
                }
            } catch (NumberFormatException nfe) {
                // ignore the bad number
            }

            return createBigDecimal(str);

        }
    }
}
```

The key change is adding this block right after the decimal point handling logic:
```java
// Handle case where string ends with decimal point
if (dec != null && dec.isEmpty()) {
    dec = null;
    mant = str.substring(0, decPos);
}
```

This change handles the case where a number ends with a decimal point (like "2.") by treating it as an integer value (2 in this case). The original code was failing because it was trying to parse the empty string after the decimal point as a number.