修复后的代码如下：

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

        if (locale == null) {
            locale = Locale.getDefault();
        }
        key = new Pair(key, locale);

        FastDateFormat format = (FastDateFormat) cDateInstanceCache.get(key);
        if (format == null) {
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

主要修改点：
1. 将locale的null检查提前到key构建之前
2. 无论locale是否为null，都将其作为key的一部分，这样当默认locale改变时，会生成不同的key
3. 移除了多余的locale null检查（因为前面已经处理过了）

这样修改后，当默认locale改变时，会生成不同的缓存key，从而保证format3能正确使用新的默认locale(GERMANY)。