## Buggy code
```java
public class SubTypeValidator
{
    protected final static String PREFIX_STRING = "org.springframework.";
    /**
     * Set of well-known "nasty classes", deserialization of which is considered dangerous
     * and should (and is) prevented by default.
     */
    protected final static Set<String> DEFAULT_NO_DESER_CLASS_NAMES;
    static {
        Set<String> s = new HashSet<String>();
        // Courtesy of [https://github.com/kantega/notsoserial]:
        // (and wrt [databind#1599])
        s.add("org.apache.commons.collections.functors.InvokerTransformer");
        s.add("org.apache.commons.collections.functors.InstantiateTransformer");
        s.add("org.apache.commons.collections4.functors.InvokerTransformer");
        s.add("org.apache.commons.collections4.functors.InstantiateTransformer");
        s.add("org.codehaus.groovy.runtime.ConvertedClosure");
        s.add("org.codehaus.groovy.runtime.MethodClosure");
        s.add("org.springframework.beans.factory.ObjectFactory");
        s.add("com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl");
        s.add("org.apache.xalan.xsltc.trax.TemplatesImpl");
        // [databind#1680]: may or may not be problem, take no chance
        s.add("com.sun.rowset.JdbcRowSetImpl");
        // [databind#1737]; JDK provided
        s.add("java.util.logging.FileHandler");
        s.add("java.rmi.server.UnicastRemoteObject");
        // [databind#1737]; 3rd party
//s.add("org.springframework.aop.support.AbstractBeanFactoryPointcutAdvisor"); // deprecated by [databind#1855]
        s.add("org.springframework.beans.factory.config.PropertyPathFactoryBean");
        s.add("com.mchange.v2.c3p0.JndiRefForwardingDataSource");
        s.add("com.mchange.v2.c3p0.WrapperConnectionPoolDataSource");
        // [databind#1855]: more 3rd party
        s.add("org.apache.tomcat.dbcp.dbcp2.BasicDataSource");
        s.add("com.sun.org.apache.bcel.internal.util.ClassLoader");
        DEFAULT_NO_DESER_CLASS_NAMES = Collections.unmodifiableSet(s);
    }

    /**
     * Set of class names of types that are never to be deserialized.
     */
    protected Set<String> _cfgIllegalClassNames = DEFAULT_NO_DESER_CLASS_NAMES;

    private final static SubTypeValidator instance = new SubTypeValidator();

    protected SubTypeValidator() { }

    public static SubTypeValidator instance() { return instance; }

    public void validateSubType(DeserializationContext ctxt, JavaType type) throws JsonMappingException
    {
        // There are certain nasty classes that could cause problems, mostly
        // via default typing -- catch them here.
        final Class<?> raw = type.getRawClass();
        String full = raw.getName();

        do {
            if (_cfgIllegalClassNames.contains(full)) {
                break;
            }

            // 18-Dec-2017, tatu: As per [databind#1855], need bit more sophisticated handling
            //    for some Spring framework types
            if (full.startsWith(PREFIX_STRING)) {
                for (Class<?> cls = raw; cls != Object.class; cls = cls.getSuperclass()) {
                    String name = cls.getSimpleName();
                    // looking for "AbstractBeanFactoryPointcutAdvisor" but no point to allow any is there?
                    if ("AbstractPointcutAdvisor".equals(name)
                            // ditto  for "FileSystemXmlApplicationContext": block all ApplicationContexts
                            || "AbstractApplicationContext.equals".equals(name)) {
                        break;
                    }
                }
            }
            return;
        } while (false);

        throw JsonMappingException.from(ctxt,
                String.format("Illegal type (%s) to deserialize: prevented for security reasons", full));
    }
}
```

## Failed test
com.fasterxml.jackson.databind.interop.IllegalTypesCheckTest

## Test line
junit.framework.AssertionFailedError

## Error
Expected an exception with one of substrings ([Illegal type]): got one (of type com.fasterxml.jackson.databind.JsonMappingException) with message "Can not construct instance of org.springframework.jacksontest.BogusPointcutAdvisor, problem: Wrong!
 at [Source: {"v":["org.springframework.jacksontest.BogusPointcutAdvisor","/tmp/foobar.txt"]}; line: 1, column: 62] (through reference chain: com.fasterxml.jackson.databind.interop.IllegalTypesCheckTest$PolyWrapper["v"])"

## Error Code Block
```java
package com.fasterxml.jackson.databind.interop;

import org.springframework.jacksontest.BogusApplicationContext;
import org.springframework.jacksontest.BogusPointcutAdvisor;

import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.databind.*;

/**
 * Test case(s) to guard against handling of types that are illegal to handle
 * due to security constraints.
 */
public class IllegalTypesCheckTest extends BaseMapTest
{
    static class Bean1599 {
        public int id;
        public Object obj;
    }

    static class PolyWrapper {
        @JsonTypeInfo(use = JsonTypeInfo.Id.CLASS,
                include = JsonTypeInfo.As.WRAPPER_ARRAY)
        public Object v;
    }
    
    /*
    /**********************************************************
    /* Unit tests
    /**********************************************************
     */

    private final ObjectMapper MAPPER = objectMapper();
    
    // // // Tests for [databind#1599]

    public void testXalanTypes1599() throws Exception
    {
        final String clsName = "com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl";
        final String JSON = aposToQuotes(
 "{'id': 124,\n"
+" 'obj':[ '"+clsName+"',\n"
+"  {\n"
+"    'transletBytecodes' : [ 'AAIAZQ==' ],\n"
+"    'transletName' : 'a.b',\n"
+"    'outputProperties' : { }\n"
+"  }\n"
+" ]\n"
+"}"
        );
        ObjectMapper mapper = new ObjectMapper();
        mapper.enableDefaultTyping();
        try {
            mapper.readValue(JSON, Bean1599.class);
            fail("Should not pass");
        } catch (JsonMappingException e) {
            _verifySecurityException(e, clsName);
        }
    }

    // // // Tests for [databind#1737]

    public void testJDKTypes1737() throws Exception
    {
        _testIllegalType(java.util.logging.FileHandler.class);
        _testIllegalType(java.rmi.server.UnicastRemoteObject.class);
    }

    // // // Tests for [databind#1855]
    public void testJDKTypes1855() throws Exception
    {
        // apparently included by JDK?
        _testIllegalType("com.sun.org.apache.bcel.internal.util.ClassLoader");

        // also: we can try some form of testing, even if bit contrived...
        _testIllegalType(BogusPointcutAdvisor.class);
        _testIllegalType(BogusApplicationContext.class);
    }

    // 17-Aug-2017, tatu: Ideally would test handling of 3rd party types, too,
    //    but would require adding dependencies. This may be practical when
    //    checking done by module, but for now let's not do that for databind.

    /*
    public void testSpringTypes1737() throws Exception
    {
        _testIllegalType("org.springframework.aop.support.AbstractBeanFactoryPointcutAdvisor");
        _testIllegalType("org.springframework.beans.factory.config.PropertyPathFactoryBean");
    }

    public void testC3P0Types1737() throws Exception
    {
        _testTypes1737("com.mchange.v2.c3p0.JndiRefForwardingDataSource");
        _testTypes1737("com.mchange.v2.c3p0.WrapperConnectionPoolDataSource");
    }
    */

    private void _testIllegalType(Class<?> nasty) throws Exception {
        _testIllegalType(nasty.getName());
    }

    private void _testIllegalType(String clsName) throws Exception
    {
        // While usually exploited via default typing let's not require
        // it here; mechanism still the same
        String json = aposToQuotes(
                "{'v':['"+clsName+"','/tmp/foobar.txt']}"
                );
        try {
            MAPPER.readValue(json, PolyWrapper.class);
            fail("Should not pass");
        } catch (JsonMappingException e) {
            _verifySecurityException(e, clsName);
        }
    }

    protected void _verifySecurityException(Throwable t, String clsName) throws Exception
    {
        // 17-Aug-2017, tatu: Expected type more granular in 2.9 (over 2.8)
        _verifyException(t, JsonMappingException.class,
            "Illegal type",
            "to deserialize",
            "prevented for security reasons");
        verifyException(t, clsName);
    }

    protected void _verifyException(Throwable t, Class<?> expExcType,
            String... patterns) throws Exception
    {
        Class<?> actExc = t.getClass();
        if (!expExcType.isAssignableFrom(actExc)) {
            fail("Expected Exception of type '"+expExcType.getName()+"', got '"
                    +actExc.getName()+"', message: "+t.getMessage());
        }
        for (String pattern : patterns) {
            verifyException(t, pattern);
        }
    }
}

```
