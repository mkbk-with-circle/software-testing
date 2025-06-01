

## Buggy code
```java
/**
     * Initialize derived fields from defining fields.
     * This is called from constructor and from readObject (de-serialization)
     */
    private void init() {
        thisYear= Calendar.getInstance(timeZone, locale).get(Calendar.YEAR);

        nameValues= new ConcurrentHashMap<Integer, KeyValue[]>();

        StringBuilder regex= new StringBuilder();
        List<Strategy> collector = new ArrayList<Strategy>();

        Matcher patternMatcher= formatPattern.matcher(pattern);
        if(!patternMatcher.lookingAt()) {
            throw new IllegalArgumentException("Invalid pattern");
        }

        currentFormatField= patternMatcher.group();
        Strategy currentStrategy= getStrategy(currentFormatField);
        for(;;) {
            patternMatcher.region(patternMatcher.end(), patternMatcher.regionEnd());
            if(!patternMatcher.lookingAt()) {
                nextStrategy = null;
                break;
            }
            String nextFormatField= patternMatcher.group();
            nextStrategy = getStrategy(nextFormatField);
            if(currentStrategy.addRegex(this, regex)) {
                collector.add(currentStrategy);
            }
            currentFormatField= nextFormatField;
            currentStrategy= nextStrategy;
        }
        if(currentStrategy.addRegex(this, regex)) {
            collector.add(currentStrategy);
        }
        currentFormatField= null;
        strategies= collector.toArray(new Strategy[collector.size()]);
        parsePattern= Pattern.compile(regex.toString());
    }
```

## Failed test
org.apache.commons.lang3.time.FastDateFormat_ParserTest::testLANG_832

## Error
junit.framework.AssertionFailedError: Parsed dates should be equal expected:<null> but was:<Fri Jan 02 21:00:00 PST 1970>

## Error Code Block
```java
    public void testLANG_832() throws Exception {
        testSdfAndFdp("'d'd" ,"d3", false); // OK
        testSdfAndFdp("'d'd'","d3", true); // should fail (unterminated quote)
    }
```

## Test line
testSdfAndFdp("'d'd'","d3", true); // should fail (unterminated quote)