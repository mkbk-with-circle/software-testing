

## Error
org.apache.commons.lang.SerializationException: java.io.NotSerializableException: org.apache.commons.lang.time.FastDateFormat$PaddedNumberField

## Error Code Block
```java
    public void testLang303() {
        FastDateFormat format = FastDateFormat.getInstance("yyyy/MM/dd");
        format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );
    }
```

## Test line
format = (FastDateFormat) SerializationUtils.deserialize( SerializationUtils.serialize( format ) );

## Failed test
org.apache.commons.lang.time.FastDateFormatTest::testLang303

## Buggy code
```java
/**
         * {@inheritDoc}
         */
        public String toString() {
            return "[" + mObj1 + ':' + mObj2 + ']';
        }
```
## mistake patch
以下之前你给出的错误的修正代码
```java


public void testLang303() {
    FastDateFormat format = FastDateFormat.getInstance("yyyy/MM/dd");
    // Clone the format to avoid serialization issues
    FastDateFormat cloned = (FastDateFormat) format.clone();
    format = (FastDateFormat) SerializationUtils.deserialize(SerializationUtils.serialize(cloned));
}

```
运用你给出的修复代码后，编译失败了
请你继续修正