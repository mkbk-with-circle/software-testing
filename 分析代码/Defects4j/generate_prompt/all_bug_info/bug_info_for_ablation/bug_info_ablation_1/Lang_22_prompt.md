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

## Failed test
org.apache.commons.lang3.math.FractionTest::testReducedFactory_int_int

## Test line
assertEquals(Integer.MIN_VALUE / 2, f.getNumerator());

## Error
junit.framework.AssertionFailedError: expected:<-1073741824> but was:<-2147483648>

