

## Buggy code
```java
/**
     * <p>Gets a date formatter instance using the specified style, time
     * zone and locale.</p>
     * 
     * @param style  date style: FULL, LONG, MEDIUM, or SHORT
     * @param timeZone  optional time zone, overrides time zone of
     *  formatted date
     * @param locale  optional locale, overrides system locale
     * @return a localized standard date formatter
     * @throws IllegalArgumentException if the Locale has no date
     *  pattern defined
     */
    public static synchronized FastDateFormat getDateInstance(int style, TimeZone timeZone, Locale locale) {
        Object key = new Integer(style);
        if (timeZone != null) {
            key = new Pair(key, timeZone);
        }

        if (locale != null) {
            key = new Pair(key, locale);
        }


        FastDateFormat format = (FastDateFormat) cDateInstanceCache.get(key);
        if (format == null) {
            if (locale == null) {
                locale = Locale.getDefault();
            }
            try {
                SimpleDateFormat formatter = (SimpleDateFormat) DateFormat.getDateInstance(style, locale);
                String pattern = formatter.toPattern();
                format = getInstance(pattern, timeZone, locale);
                cDateInstanceCache.put(key, format);
                
            } catch (ClassCastException ex) {
                throw new IllegalArgumentException("No date pattern for locale: " + locale);
            }
        }
        return format;
    }
```

## Error Code Block
```java
    public void test_changeDefault_Locale_DateInstance() {
        Locale realDefaultLocale = Locale.getDefault();
        try {
            Locale.setDefault(Locale.US);
            FastDateFormat format1 = FastDateFormat.getDateInstance(FastDateFormat.FULL, Locale.GERMANY);
            FastDateFormat format2 = FastDateFormat.getDateInstance(FastDateFormat.FULL);
            Locale.setDefault(Locale.GERMANY);
            FastDateFormat format3 = FastDateFormat.getDateInstance(FastDateFormat.FULL);

            assertSame(Locale.GERMANY, format1.getLocale());
            assertSame(Locale.US, format2.getLocale());
            assertSame(Locale.GERMANY, format3.getLocale());
            assertTrue(format1 != format2); // -- junit 3.8 version -- assertFalse(format1 == format2);
            assertTrue(format2 != format3);

        } finally {
            Locale.setDefault(realDefaultLocale);
        }
    }
```

## Test line
assertSame(Locale.GERMANY, format3.getLocale());

## Failed test
org.apache.commons.lang.time.FastDateFormatTest::test_changeDefault_Locale_DateInstance

## Error
junit.framework.AssertionFailedError: expected same:<de_DE> was not:<en_US>
## mistake patch
以下之前你给出的错误的修正代码
```java


/**
     * <p>Gets a date formatter instance using the specified style, time
     * zone and locale.</p>
     * 
     * @param style  date style: FULL, LONG, MEDIUM, or SHORT
     * @param timeZone  optional time zone, overrides time zone of
     *  formatted date
     * @param locale  optional locale, overrides system locale
     * @return a localized standard date formatter
     * @throws IllegalArgumentException if the Locale has no date
     *  pattern defined
     */
    public static synchronized FastDateFormat getDateInstance(int style, TimeZone timeZone, Locale locale) {
        Object key = new Integer(style);
        if (timeZone != null) {
            key = new Pair(key, timeZone);
        }

        if (locale != null) {
            key = new Pair(key, locale);
        }

        FastDateFormat format = (FastDateFormat) cDateInstanceCache.get(key);
        if (format == null) {
            Locale localeToUse = locale != null ? locale : Locale.getDefault();
            try {
                SimpleDateFormat formatter = (SimpleDateFormat) DateFormat.getDateInstance(style, localeToUse);
                String pattern = formatter.toPattern();
                format = getInstance(pattern, timeZone, localeToUse);
                cDateInstanceCache.put(key, format);
                
            } catch (ClassCastException ex) {
                throw new IllegalArgumentException("No date pattern for locale: " + localeToUse);
            }
        }
        return format;
    }

```
请你继续修正