

## Buggy code
```java
/**
         * {@inheritDoc}
         */
        public String toString() {
            return "[" + mObj1 + ':' + mObj2 + ']';
        }
```

## Test line
format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );

## Failed test
org.apache.commons.lang.time.FastDateFormatTest::testLang303

## Error Code Block
```java
    public void testLang303() {
        FastDateFormat format = FastDateFormat.getInstance("yyyy/MM/dd");
        format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );
    }
```

## Error
org.apache.commons.lang.SerializationException: java.io.NotSerializableException: org.apache.commons.lang.time.FastDateFormat$PaddedNumberField