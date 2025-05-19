## Buggy code
```java
package com.taobao.arthas.core.command.express;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

import ognl.ClassResolver;

/**
 *
 * @author hengyunabc 2018-10-18
 * @see ognl.DefaultClassResolver
 */
public class ClassLoaderClassResolver implements ClassResolver {

    private ClassLoader classLoader;

    private Map<String, Class<?>> classes = new ConcurrentHashMap<String, Class<?>>(101);

    public ClassLoaderClassResolver(ClassLoader classLoader) {
        this.classLoader = classLoader;
    }

    @Override
    public Class<?> classForName(String className, @SuppressWarnings("rawtypes") Map context)
                    throws ClassNotFoundException {
        Class<?> result = null;

        if ((result = classes.get(className)) == null) {
            try {
                result = classLoader.loadClass(className);
            } catch (ClassNotFoundException ex) {
                if (className.indexOf('.') == -1) {
                    result = Class.forName("java.lang." + className);
                    classes.put("java.lang." + className, result);
                }
            }
            classes.put(className, result);
        }
        return result;
    }

}

```

## Error
fix class loader npe

## Error Description
If ognl express's class cann't find, throws java.lang.NullPointerException, it confusing.
![image](https://user-images.githubusercontent.com/48389485/55677542-5fa33a80-591c-11e9-986c-482f55dcac56.png)

Fix to throw java.lang.ClassNotFoundException.
![image](https://user-images.githubusercontent.com/48389485/55677547-76e22800-591c-11e9-9888-fd996ea44bc6.png)

![image](https://user-images.githubusercontent.com/48389485/55677537-4ef2c480-591c-11e9-835b-a1c18b0cf872.png)

