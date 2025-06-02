## Buggy code
```java
/**
         * {@inheritDoc}
         */
        public String toString() {
            return "[" + mObj1 + ':' + mObj2 + ']';
        }
```

## Failed test
org.apache.commons.lang.time.FastDateFormatTest::testLang303

## Test line
format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );

## Error
org.apache.commons.lang.SerializationException: java.io.NotSerializableException: org.apache.commons.lang.time.FastDateFormat$PaddedNumberField

