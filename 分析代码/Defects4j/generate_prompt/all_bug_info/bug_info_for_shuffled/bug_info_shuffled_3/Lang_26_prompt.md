

## Error Code Block
```java
    public void testLang645() {
        Locale locale = new Locale("sv", "SE");

        Calendar cal = Calendar.getInstance();
        cal.set(2010, 0, 1, 12, 0, 0);
        Date d = cal.getTime();

        FastDateFormat fdf = FastDateFormat.getInstance("EEEE', week 'ww", locale);

        assertEquals("fredag, week 53", fdf.format(d));
    }
```

## Test line
assertEquals("fredag, week 53", fdf.format(d));

## Failed test
org.apache.commons.lang3.time.FastDateFormatTest::testLang645

## Error
junit.framework.ComparisonFailure: expected:<fredag, week [53]> but was:<fredag, week [01]>

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