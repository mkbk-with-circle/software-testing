## Buggy code
```java
/**
     * <p>Tests for order.</p>
     *
     * <p>The default ordering is numeric by value, but this
     * can be overridden by subclasses.</p>
     *
     * <p>NOTE: From v2.2 the enums must be of the same type.
     * If the parameter is in a different class loader than this instance,
     * reflection is used to compare the values.</p>
     *
     * @see java.lang.Comparable#compareTo(Object)
     * @param other  the other object to compare to
     * @return -ve if this is less than the other object, +ve if greater than,
     *  <code>0</code> of equal
     * @throws ClassCastException if other is not an <code>Enum</code>
     * @throws NullPointerException if other is <code>null</code>
     */
    public int compareTo(Object other) {
        return iValue - ((ValuedEnum) other).iValue;
    }
```





