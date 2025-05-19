## Buggy code
```java

```

## Failed test
com.fasterxml.jackson.databind.creators.InnerClassCreatorTest

## Test line
java.lang.IllegalStateException

## Error
Internal error: no creator index for property 'a' (of type com.fasterxml.jackson.databind.deser.impl.InnerClassProperty)

## Error Code Block
```java
package com.fasterxml.jackson.databind.creators;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.*;

// for [databind#1501]
public class InnerClassCreatorTest extends BaseMapTest
{
    static class Something {
        public InnerSomething a;

        // important: must name the parameter (param names module, or explicit)
        @JsonCreator
        public Something(@JsonProperty("a") InnerSomething a) { this.a = a; }

        public Something() { a = new InnerSomething(); }

        class InnerSomething {
            @JsonCreator
            public InnerSomething() { }
        }
    }

    public void testIssue1501() throws Exception
    {
        ObjectMapper mapper = new ObjectMapper();
        mapper.disable(SerializationFeature.FAIL_ON_EMPTY_BEANS);
        String ser = mapper.writeValueAsString(new Something());
        mapper.readValue(ser, Something.class);
    }
}

```
