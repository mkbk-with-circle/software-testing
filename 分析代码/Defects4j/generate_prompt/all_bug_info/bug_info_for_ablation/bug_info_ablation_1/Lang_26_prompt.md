## Buggy code
```java
/**
     * <p>Formats a <code>Date</code> object.</p>
     * 
     * @param date  the date to format
     * @return the formatted string
     */
    public String format(Date date) {
        Calendar c = new GregorianCalendar(mTimeZone);
        c.setTime(date);
        return applyRules(c, new StringBuffer(mMaxLengthEstimate)).toString();
    }
```

## Failed test
org.apache.commons.lang3.time.FastDateFormatTest::testLang645

## Test line
assertEquals("fredag, week 53", fdf.format(d));

## Error
junit.framework.ComparisonFailure: expected:<fredag, week [53]> but was:<fredag, week [01]>

