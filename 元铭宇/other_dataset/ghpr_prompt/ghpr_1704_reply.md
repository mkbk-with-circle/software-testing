Here's the fixed code with null check for inputConsumers in the close() method:

```java
@Override
public void close() throws Exception {
    if (inputConsumers != null) {
        inputConsumers.forEach(consumer -> {
            try {
                consumer.close();
            } catch (PulsarClientException e) {
            }
        });
    }
}
```

The fix adds a null check for `inputConsumers` before attempting to iterate over it. This prevents the NullPointerException that could occur if `close()` was called before `open()` or if `open()` failed to initialize the `inputConsumers` list.