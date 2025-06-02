Based on the error description, the issue occurs when trying to use the 'validateOnCheckout' property which doesn't have a corresponding setter method. The fix involves modifying the `setBeanProps()` method in `StdSchedulerFactory` to handle this case more gracefully.

Here's the fixed code for the `setBeanProps()` method:

```java
private void setBeanProps(Object obj, Properties props)
    throws NoSuchMethodException, IllegalAccessException,
        java.lang.reflect.InvocationTargetException,
        IntrospectionException, SchedulerConfigException {
    props.remove("class");
    props.remove(PoolingConnectionProvider.POOLING_PROVIDER);

    BeanInfo bi = Introspector.getBeanInfo(obj.getClass());
    PropertyDescriptor[] propDescs = bi.getPropertyDescriptors();
    PropertiesParser pp = new PropertiesParser(props);

    java.util.Enumeration<Object> keys = props.keys();
    while (keys.hasMoreElements()) {
        String name = (String) keys.nextElement();
        String c = name.substring(0, 1).toUpperCase(Locale.US);
        String methName = "set" + c + name.substring(1);

        java.lang.reflect.Method setMeth = getSetMethod(methName, propDescs);

        try {
            if (setMeth == null) {
                // Skip properties that don't have setters rather than throwing exception
                continue;
            }

            Class<?>[] params = setMeth.getParameterTypes();
            if (params.length != 1) {
                throw new NoSuchMethodException(
                    "No 1-argument setter for property '" + name + "'");
            }
            
            // does the property value reference another property's value? If so, swap to look at its value
            PropertiesParser refProps = pp;
            String refName = pp.getStringProperty(name);
            if(refName != null && refName.startsWith("$@")) {
                refName =  refName.substring(2);
                refProps = cfg;
            }
            else
                refName = name;
            
            if (params[0].equals(int.class)) {
                setMeth.invoke(obj, new Object[]{Integer.valueOf(refProps.getIntProperty(refName))});
            } else if (params[0].equals(long.class)) {
                setMeth.invoke(obj, new Object[]{Long.valueOf(refProps.getLongProperty(refName))});
            } else if (params[0].equals(float.class)) {
                setMeth.invoke(obj, new Object[]{Float.valueOf(refProps.getFloatProperty(refName))});
            } else if (params[0].equals(double.class)) {
                setMeth.invoke(obj, new Object[]{Double.valueOf(refProps.getDoubleProperty(refName))});
            } else if (params[0].equals(boolean.class)) {
                setMeth.invoke(obj, new Object[]{Boolean.valueOf(refProps.getBooleanProperty(refName))});
            } else if (params[0].equals(String.class)) {
                setMeth.invoke(obj, new Object[]{refProps.getStringProperty(refName)});
            } else {
                throw new NoSuchMethodException(
                        "No primitive-type setter for property '" + name
                                + "'");
            }
        } catch (NumberFormatException nfe) {
            throw new SchedulerConfigException("Could not parse property '"
                    + name + "' into correct data type: " + nfe.toString());
        }
    }
}
```

The key change is that instead of throwing an exception when a setter method is not found (`if (setMeth == null)`), we now simply continue to the next property. This makes the method more tolerant of properties that may be valid for some implementations but not others.

This change allows the configuration to include properties like 'validateOnCheckout' that may be valid for certain connection pool implementations but not others, without causing the scheduler initialization to fail. The properties will simply be ignored if there's no corresponding setter method on the target object.