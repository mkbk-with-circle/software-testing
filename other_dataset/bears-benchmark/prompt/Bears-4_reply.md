修复后的代码如下：

```java
package com.fasterxml.jackson.databind.creators;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.*;

public class InnerClassCreatorTest extends BaseMapTest
{
    static class Something {
        public InnerSomething a;

        @JsonCreator
        public Something(@JsonProperty("a") InnerSomething a) { this.a = a; }

        public Something() { a = new InnerSomething(); }

        static class InnerSomething {  // 添加了static修饰符
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

主要修改是将`InnerSomething`类改为静态内部类（添加了`static`修饰符）。这是因为Jackson在反序列化非静态内部类时需要外部类的实例，这会导致反序列化失败。将内部类改为静态后，它就不再依赖于外部类的实例，可以被正常反序列化。