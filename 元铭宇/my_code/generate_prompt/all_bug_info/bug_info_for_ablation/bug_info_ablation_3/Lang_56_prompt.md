## Buggy code
```java
/**
         * {@inheritDoc}
         */
        public String toString() {
            return "[" + mObj1 + ':' + mObj2 + ']';
        }
```



## Error
org.apache.commons.lang.SerializationException: java.io.NotSerializableException: org.apache.commons.lang.time.FastDateFormat$PaddedNumberField


