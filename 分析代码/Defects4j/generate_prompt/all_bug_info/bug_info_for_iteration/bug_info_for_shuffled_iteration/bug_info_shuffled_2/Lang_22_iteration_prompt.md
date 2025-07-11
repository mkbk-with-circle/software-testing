

## Buggy code
```java
/**
     * <p>Gets the greatest common divisor of the absolute value of
     * two numbers, using the "binary gcd" method which avoids
     * division and modulo operations.  See Knuth 4.5.2 algorithm B.
     * This algorithm is due to Josef Stein (1961).</p>
     *
     * @param u  a non-zero number
     * @param v  a non-zero number
     * @return the greatest common divisor, never zero
     */
    private static int greatestCommonDivisor(int u, int v) {
        // From Commons Math:
        //if either operand is abs 1, return 1:
        if (Math.abs(u) <= 1 || Math.abs(v) <= 1) {
            return 1;
        }
        // keep u and v negative, as negative integers range down to
        // -2^31, while positive numbers can only be as large as 2^31-1
        // (i.e. we can't necessarily negate a negative number without
        // overflow)
        if (u>0) { u=-u; } // make u negative
        if (v>0) { v=-v; } // make v negative
        // B1. [Find power of 2]
        int k=0;
        while ((u&1)==0 && (v&1)==0 && k<31) { // while u and v are both even...
            u/=2; v/=2; k++; // cast out twos.
        }
        if (k==31) {
            throw new ArithmeticException("overflow: gcd is 2^31");
        }
        // B2. Initialize: u and v have been divided by 2^k and at least
        //     one is odd.
        int t = ((u&1)==1) ? v : -(u/2)/*B3*/;
        // t negative: u was odd, v may be even (t replaces v)
        // t positive: u was even, v is odd (t replaces u)
        do {
            /* assert u<0 && v<0; */
            // B4/B3: cast out twos from t.
            while ((t&1)==0) { // while t is even..
                t/=2; // cast out twos
            }
            // B5 [reset max(u,v)]
            if (t>0) {
                u = -t;
            } else {
                v = t;
            }
            // B6/B3. at this point both u and v should be odd.
            t = (v - u)/2;
            // |u| larger: t positive (replace u)
            // |v| larger: t negative (replace v)
        } while (t!=0);
        return -u*(1<<k); // gcd is u*2^k
    }
```

## Error Code Block
```java
    public void testReducedFactory_int_int() {
        Fraction f = null;
        
        // zero
        f = Fraction.getReducedFraction(0, 1);
        assertEquals(0, f.getNumerator());
        assertEquals(1, f.getDenominator());
        
        // normal
        f = Fraction.getReducedFraction(1, 1);
        assertEquals(1, f.getNumerator());
        assertEquals(1, f.getDenominator());
        
        f = Fraction.getReducedFraction(2, 1);
        assertEquals(2, f.getNumerator());
        assertEquals(1, f.getDenominator());
        
        // improper
        f = Fraction.getReducedFraction(22, 7);
        assertEquals(22, f.getNumerator());
        assertEquals(7, f.getDenominator());
        
        // negatives
        f = Fraction.getReducedFraction(-6, 10);
        assertEquals(-3, f.getNumerator());
        assertEquals(5, f.getDenominator());
        
        f = Fraction.getReducedFraction(6, -10);
        assertEquals(-3, f.getNumerator());
        assertEquals(5, f.getDenominator());
        
        f = Fraction.getReducedFraction(-6, -10);
        assertEquals(3, f.getNumerator());
        assertEquals(5, f.getDenominator());
        
        // zero denominator
        try {
            f = Fraction.getReducedFraction(1, 0);
            fail("expecting ArithmeticException");
        } catch (ArithmeticException ex) {}
        
        try {
            f = Fraction.getReducedFraction(2, 0);
            fail("expecting ArithmeticException");
        } catch (ArithmeticException ex) {}
        
        try {
            f = Fraction.getReducedFraction(-3, 0);
            fail("expecting ArithmeticException");
        } catch (ArithmeticException ex) {}

        // reduced        
        f = Fraction.getReducedFraction(0, 2);
        assertEquals(0, f.getNumerator());
        assertEquals(1, f.getDenominator());
        
        f = Fraction.getReducedFraction(2, 2);
        assertEquals(1, f.getNumerator());
        assertEquals(1, f.getDenominator());
        
        f = Fraction.getReducedFraction(2, 4);
        assertEquals(1, f.getNumerator());
        assertEquals(2, f.getDenominator());
        
        f = Fraction.getReducedFraction(15, 10);
        assertEquals(3, f.getNumerator());
        assertEquals(2, f.getDenominator());
        
        f = Fraction.getReducedFraction(121, 22);
        assertEquals(11, f.getNumerator());
        assertEquals(2, f.getDenominator());
        
        // Extreme values 
        // OK, can reduce before negating
        f = Fraction.getReducedFraction(-2, Integer.MIN_VALUE);
        assertEquals(1, f.getNumerator());
        assertEquals(-(Integer.MIN_VALUE / 2), f.getDenominator());
        
        // Can't reduce, negation will throw
        try { 
            f = Fraction.getReducedFraction(-7, Integer.MIN_VALUE);  
            fail("Expecting ArithmeticException");
        } catch (ArithmeticException ex) {}      

        // LANG-662
        f = Fraction.getReducedFraction(Integer.MIN_VALUE, 2);
        assertEquals(Integer.MIN_VALUE / 2, f.getNumerator());
        assertEquals(1, f.getDenominator());
    }
```

## Test line
assertEquals(Integer.MIN_VALUE / 2, f.getNumerator());

## Failed test
org.apache.commons.lang3.math.FractionTest::testReducedFactory_int_int

## Error
junit.framework.AssertionFailedError: expected:<-1073741824> but was:<-2147483648>
## mistake patch
以下之前你给出的错误的修正代码
```java


private static int greatestCommonDivisor(int u, int v) {
    // From Commons Math:
    //if either operand is abs 1, return 1:
    if (Math.abs(u) <= 1 || Math.abs(v) <= 1) {
        return 1;
    }
    // keep u and v negative, as negative integers range down to
    // -2^31, while positive numbers can only be as large as 2^31-1
    // (i.e. we can't necessarily negate a negative number without
    // overflow)
    if (u>0) { u=-u; } // make u negative
    if (v>0) { v=-v; } // make v negative
    // B1. [Find power of 2]
    int k=0;
    while ((u&1)==0 && (v&1)==0 && k<31) { // while u and v are both even...
        u/=2; v/=2; k++; // cast out twos.
    }
    if (k==31) {
        throw new ArithmeticException("overflow: gcd is 2^31");
    }
    // B2. Initialize: u and v have been divided by 2^k and at least
    //     one is odd.
    int t = ((u&1)==1) ? v : -(u/2)/*B3*/;
    // t negative: u was odd, v may be even (t replaces v)
    // t positive: u was even, v is odd (t replaces u)
    do {
        /* assert u<0 && v<0; */
        // B4/B3: cast out twos from t.
        while ((t&1)==0) { // while t is even..
            t/=2; // cast out twos
        }
        // B5 [reset max(u,v)]
        if (t>0) {
            u = -t;
        } else {
            v = t;
        }
        // B6/B3. at this point both u and v should be odd.
        t = (v - u)/2;
        // |u| larger: t positive (replace u)
        // |v| larger: t negative (replace v)
    } while (t!=0);
    return -u*(1<<k); // gcd is u*2^k
}

```
请你继续修正