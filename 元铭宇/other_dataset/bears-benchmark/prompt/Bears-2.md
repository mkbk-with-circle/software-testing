## Buggy code
```java
public class StdKeyDeserializer extends KeyDeserializer
    implements java.io.Serializable
{
    private static final long serialVersionUID = 1L;

    public final static int TYPE_BOOLEAN = 1;
    public final static int TYPE_BYTE = 2;
    public final static int TYPE_SHORT = 3;
    public final static int TYPE_CHAR = 4;
    public final static int TYPE_INT = 5;
    public final static int TYPE_LONG = 6;
    public final static int TYPE_FLOAT = 7;
    public final static int TYPE_DOUBLE = 8;
    public final static int TYPE_LOCALE = 9;
    public final static int TYPE_DATE = 10;
    public final static int TYPE_CALENDAR = 11;
    public final static int TYPE_UUID = 12;
    public final static int TYPE_URI = 13;
    public final static int TYPE_URL = 14;
    public final static int TYPE_CLASS = 15;
    public final static int TYPE_CURRENCY = 16;

    final protected int _kind;
    final protected Class<?> _keyClass;

    /**
     * Some types that are deserialized using a helper deserializer.
     */
    protected final FromStringDeserializer<?> _deser;
    
    protected StdKeyDeserializer(int kind, Class<?> cls) {
        this(kind, cls, null);
    }

    protected StdKeyDeserializer(int kind, Class<?> cls, FromStringDeserializer<?> deser) {
        _kind = kind;
        _keyClass = cls;
        _deser = deser;
    }

    public static StdKeyDeserializer forType(Class<?> raw)
    {
        int kind;

        // first common types:
        if (raw == String.class || raw == Object.class) {
            return StringKD.forType(raw);
        } else if (raw == UUID.class) {
            kind = TYPE_UUID;
        } else if (raw == Integer.class) {
            kind = TYPE_INT;
        } else if (raw == Long.class) {
            kind = TYPE_LONG;
        } else if (raw == Date.class) {
            kind = TYPE_DATE;
        } else if (raw == Calendar.class) {
            kind = TYPE_CALENDAR;
        // then less common ones...
        } else if (raw == Boolean.class) {
            kind = TYPE_BOOLEAN;
        } else if (raw == Byte.class) {
            kind = TYPE_BYTE;
        } else if (raw == Character.class) {
            kind = TYPE_CHAR;
        } else if (raw == Short.class) {
            kind = TYPE_SHORT;
        } else if (raw == Float.class) {
            kind = TYPE_FLOAT;
        } else if (raw == Double.class) {
            kind = TYPE_DOUBLE;
        } else if (raw == URI.class) {
            kind = TYPE_URI;
        } else if (raw == URL.class) {
            kind = TYPE_URL;
        } else if (raw == Class.class) {
            kind = TYPE_CLASS;
        } else if (raw == Locale.class) {
            FromStringDeserializer<?> deser = FromStringDeserializer.findDeserializer(Locale.class);
            return new StdKeyDeserializer(TYPE_LOCALE, raw, deser);
        } else if (raw == Currency.class) {
            FromStringDeserializer<?> deser = FromStringDeserializer.findDeserializer(Currency.class);
            return new StdKeyDeserializer(TYPE_CURRENCY, raw, deser);
        } else {
            return null;
        }
        return new StdKeyDeserializer(kind, raw);
    }
    
    @Override
    public Object deserializeKey(String key, DeserializationContext ctxt)
        throws IOException
    {
        if (key == null) { // is this even legal call?
            return null;
        }
        try {
            Object result = _parse(key, ctxt);
            if (result != null) {
                return result;
            }
        } catch (Exception re) {
            throw ctxt.weirdKeyException(_keyClass, key, "not a valid representation: "+re.getMessage());
        }
        if (_keyClass.isEnum() && ctxt.getConfig().isEnabled(DeserializationFeature.READ_UNKNOWN_ENUM_VALUES_AS_NULL)) {
            return null;
        }
        throw ctxt.weirdKeyException(_keyClass, key, "not a valid representation");
    }

    public Class<?> getKeyClass() { return _keyClass; }

    protected Object _parse(String key, DeserializationContext ctxt) throws Exception
    {
        switch (_kind) {
        case TYPE_BOOLEAN:
            if ("true".equals(key)) {
                return Boolean.TRUE;
            }
            if ("false".equals(key)) {
                return Boolean.FALSE;
            }
            throw ctxt.weirdKeyException(_keyClass, key, "value not 'true' or 'false'");
        case TYPE_BYTE:
            {
                int value = _parseInt(key);
                // as per [JACKSON-804], allow range up to 255, inclusive
                if (value < Byte.MIN_VALUE || value > 255) {
                    throw ctxt.weirdKeyException(_keyClass, key, "overflow, value can not be represented as 8-bit value");
                }
                return Byte.valueOf((byte) value);
            }
        case TYPE_SHORT:
            {
                int value = _parseInt(key);
                if (value < Short.MIN_VALUE || value > Short.MAX_VALUE) {
                    throw ctxt.weirdKeyException(_keyClass, key, "overflow, value can not be represented as 16-bit value");
                }
                return Short.valueOf((short) value);
            }
        case TYPE_CHAR:
            if (key.length() == 1) {
                return Character.valueOf(key.charAt(0));
            }
            throw ctxt.weirdKeyException(_keyClass, key, "can only convert 1-character Strings");
        case TYPE_INT:
            return _parseInt(key);

        case TYPE_LONG:
            return _parseLong(key);

        case TYPE_FLOAT:
            // Bounds/range checks would be tricky here, so let's not bother even trying...
            return Float.valueOf((float) _parseDouble(key));
        case TYPE_DOUBLE:
            return _parseDouble(key);
        case TYPE_LOCALE:
            try {
                return _deser._deserialize(key, ctxt);
            } catch (IOException e) {
                throw ctxt.weirdKeyException(_keyClass, key, "unable to parse key as locale");
            }
        case TYPE_CURRENCY:
            try {
                return _deser._deserialize(key, ctxt);
            } catch (IOException e) {
                throw ctxt.weirdKeyException(_keyClass, key, "unable to parse key as currency");
            }
        case TYPE_DATE:
            return ctxt.parseDate(key);
        case TYPE_CALENDAR:
            java.util.Date date = ctxt.parseDate(key);
            return (date == null)  ? null : ctxt.constructCalendar(date);
        case TYPE_UUID:
            return UUID.fromString(key);
        case TYPE_URI:
            return URI.create(key);
        case TYPE_URL:
            return new URL(key);
        case TYPE_CLASS:
            try {
                return ctxt.findClass(key);
            } catch (Exception e) {
                throw ctxt.weirdKeyException(_keyClass, key, "unable to parse key as Class");
            }
        }
        return null;
    }

    /*
    /**********************************************************
    /* Helper methods for sub-classes
    /**********************************************************
     */

    protected int _parseInt(String key) throws IllegalArgumentException {
        return Integer.parseInt(key);
    }

    protected long _parseLong(String key) throws IllegalArgumentException {
        return Long.parseLong(key);
    }

    protected double _parseDouble(String key) throws IllegalArgumentException {
        return NumberInput.parseDouble(key);
    }

    /*
    /**********************************************************
    /* First: the standard "String as String" deserializer
    /**********************************************************
     */

    @JacksonStdImpl
    final static class StringKD extends StdKeyDeserializer
    {
        private static final long serialVersionUID = 1L;
        private final static StringKD sString = new StringKD(String.class);
        private final static StringKD sObject = new StringKD(Object.class);
        
        private StringKD(Class<?> nominalType) { super(-1, nominalType); }

        public static StringKD forType(Class<?> nominalType)
        {
            if (nominalType == String.class) {
                return sString;
            }
            if (nominalType == Object.class) {
                return sObject;
            }
            return new StringKD(nominalType);
        }

        @Override
        public Object deserializeKey(String key, DeserializationContext ctxt) throws IOException, JsonProcessingException {
            return key;
        }
    }    

    /*
    /**********************************************************
    /* Key deserializer implementations; other
    /**********************************************************
     */

    /**
     * Key deserializer that wraps a "regular" deserializer (but one
     * that must recognize FIELD_NAMEs as text!) to reuse existing
     * handlers as key handlers.
     */
    final static class DelegatingKD
        extends KeyDeserializer // note: NOT the std one
        implements java.io.Serializable
    {
        private static final long serialVersionUID = 1L;

        final protected Class<?> _keyClass;

        protected final JsonDeserializer<?> _delegate;
        
        protected DelegatingKD(Class<?> cls, JsonDeserializer<?> deser) {
            _keyClass = cls;
            _delegate = deser;
        }

        @Override
        public final Object deserializeKey(String key, DeserializationContext ctxt)
            throws IOException, JsonProcessingException
        {
            if (key == null) { // is this even legal call?
                return null;
            }
            try {
                // Ugh... should not have to give parser which may or may not be correct one...
                Object result = _delegate.deserialize(ctxt.getParser(), ctxt);
                if (result != null) {
                    return result;
                }
            } catch (Exception re) {
                throw ctxt.weirdKeyException(_keyClass, key, "not a valid representation: "+re.getMessage());
            }
            throw ctxt.weirdKeyException(_keyClass, key, "not a valid representation");
        }

        public Class<?> getKeyClass() { return _keyClass; }
    }
     
    @JacksonStdImpl
    final static class EnumKD extends StdKeyDeserializer
    {
        private static final long serialVersionUID = 1L;

        protected final EnumResolver _byNameResolver;

        protected final AnnotatedMethod _factory;

        /**
         * Lazily constructed alternative in case there is need to
         * use 'toString()' method as the source.
         *
         * @since 2.7.3
         */
        protected EnumResolver _byToStringResolver;
        
        protected EnumKD(EnumResolver er, AnnotatedMethod factory) {
            super(-1, er.getEnumClass());
            _byNameResolver = er;
            _factory = factory;
        }

        @Override
        public Object _parse(String key, DeserializationContext ctxt) throws JsonMappingException
        {
            if (_factory != null) {
                try {
                    return _factory.call1(key);
                } catch (Exception e) {
                    ClassUtil.unwrapAndThrowAsIAE(e);
                }
            }
            EnumResolver res = ctxt.isEnabled(DeserializationFeature.READ_ENUMS_USING_TO_STRING)
                    ? _getToStringResolver() : _byNameResolver;
            Enum<?> e = res.findEnum(key);
            if ((e == null) && !ctxt.getConfig().isEnabled(DeserializationFeature.READ_UNKNOWN_ENUM_VALUES_AS_NULL)) {
                throw ctxt.weirdKeyException(_keyClass, key, "not one of values excepted for Enum class: "
                        +res.getEnumIds());
            }
            return e;
        }

        private EnumResolver _getToStringResolver()
        {
            EnumResolver res = _byToStringResolver;
            if (res == null) {
                synchronized (this) {
                    res = EnumResolver.constructUnsafeUsingToString(_byNameResolver.getEnumClass());
                }
            }
            return res;
        }
    }
    
    /**
     * Key deserializer that calls a single-string-arg constructor
     * to instantiate desired key type.
     */
    final static class StringCtorKeyDeserializer extends StdKeyDeserializer
    {
        private static final long serialVersionUID = 1L;

        protected final Constructor<?> _ctor;

        public StringCtorKeyDeserializer(Constructor<?> ctor) {
            super(-1, ctor.getDeclaringClass());
            _ctor = ctor;
        }

        @Override
        public Object _parse(String key, DeserializationContext ctxt) throws Exception
        {
            return _ctor.newInstance(key);
        }
    }

    /**
     * Key deserializer that calls a static no-args factory method
     * to instantiate desired key type.
     */
    final static class StringFactoryKeyDeserializer extends StdKeyDeserializer
    {
        private static final long serialVersionUID = 1L;

        final Method _factoryMethod;

        public StringFactoryKeyDeserializer(Method fm) {
            super(-1, fm.getDeclaringClass());
            _factoryMethod = fm;
        }

        @Override
        public Object _parse(String key, DeserializationContext ctxt) throws Exception
        {
            return _factoryMethod.invoke(null, key);
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.deser.TestMapDeserialization

## Test line
com.fasterxml.jackson.databind.JsonMappingException

## Error
Can not find a (Map) Key deserializer for type [simple type, class java.lang.CharSequence]
 at [Source: {"a":"b"}; line: 1, column: 1]

## Error Code Block
```java
package com.fasterxml.jackson.databind.deser;

import java.io.IOException;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

@SuppressWarnings("serial")
public class TestMapDeserialization
    extends BaseMapTest
{
    static enum Key {
        KEY1, KEY2, WHATEVER;
    }

    static class BrokenMap
        extends HashMap<Object,Object>
    {
        // No default ctor, nor @JsonCreators
        public BrokenMap(boolean dummy) { super(); }
    }

    @JsonDeserialize(using=MapDeserializer.class)
    static class CustomMap extends LinkedHashMap<String,String> { }

    static class MapDeserializer extends StdDeserializer<CustomMap>
    {
        public MapDeserializer() { super(CustomMap.class); }
        @Override
        public CustomMap deserialize(JsonParser jp, DeserializationContext ctxt)
            throws IOException
        {
            CustomMap result = new CustomMap();
            result.put("x", jp.getText());
            return result;
        }
    }

    static class KeyType {
        protected String value;
        
        private KeyType(String v, boolean bogus) {
            value = v;
        }

        @JsonCreator
        public static KeyType create(String v) {
            return new KeyType(v, true);
        }
    }

    // Issue #142
    public static class EnumMapContainer {
        @JsonTypeInfo(use=JsonTypeInfo.Id.CLASS, include=JsonTypeInfo.As.PROPERTY, property="@class")
        public EnumMap<KeyEnum,ITestType> testTypes;
    }

    public static class ListContainer {
        public List<ITestType> testTypes;
    }

    @JsonTypeInfo(use=JsonTypeInfo.Id.CLASS, include=JsonTypeInfo.As.PROPERTY, property="@class")
    public static interface ITestType { }

    public static enum KeyEnum {
        A, B
    }
    public static enum ConcreteType implements ITestType {
        ONE, TWO;
    }

    static class ClassStringMap extends HashMap<Class<?>,String> { }
    
    /*
    /**********************************************************
    /* Test methods, untyped (Object valued) maps
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();

    public void testUntypedMap() throws Exception
    {
        // to get "untyped" default map-to-map, pass Object.class
        String JSON = "{ \"foo\" : \"bar\", \"crazy\" : true, \"null\" : null }";

        // Not a guaranteed cast theoretically, but will work:
        @SuppressWarnings("unchecked")
        Map<String,Object> result = (Map<String,Object>)MAPPER.readValue(JSON, Object.class);
        assertNotNull(result);
        assertTrue(result instanceof Map<?,?>);

        assertEquals(3, result.size());

        assertEquals("bar", result.get("foo"));
        assertEquals(Boolean.TRUE, result.get("crazy"));
        assertNull(result.get("null"));

        // Plus, non existing:
        assertNull(result.get("bar"));
        assertNull(result.get(3));
    }

    public void testBigUntypedMap() throws Exception
    {
        Map<String,Object> map = new LinkedHashMap<String,Object>();
        for (int i = 0; i < 1100; ++i) {
            if ((i & 1) == 0) {
                map.put(String.valueOf(i), Integer.valueOf(i));
            } else {
                Map<String,Object> map2 = new LinkedHashMap<String,Object>();
                map2.put("x", Integer.valueOf(i));
                map.put(String.valueOf(i), map2);
            }
        }
        String json = MAPPER.writeValueAsString(map);
        Object bound = MAPPER.readValue(json, Object.class);
        assertEquals(map, bound);
    }
    
    /**
     * Let's also try another way to express "gimme a Map" deserialization;
     * this time by specifying a Map class, to reduce need to cast
     */
    public void testUntypedMap2() throws Exception
    {
        // to get "untyped" default map-to-map, pass Object.class
        String JSON = "{ \"a\" : \"x\" }";

        @SuppressWarnings("unchecked")
        HashMap<String,Object> result = /*(HashMap<String,Object>)*/ MAPPER.readValue(JSON, HashMap.class);
        assertNotNull(result);
        assertTrue(result instanceof Map<?,?>);

        assertEquals(1, result.size());

        assertEquals("x", result.get("a"));
    }

    /**
     * Unit test for [JACKSON-185]
     */
    public void testUntypedMap3() throws Exception
    {
        String JSON = "{\"a\":[{\"a\":\"b\"},\"value\"]}";
        Map<?,?> result = MAPPER.readValue(JSON, Map.class);
        assertTrue(result instanceof Map<?,?>);
        assertEquals(1, result.size());
        Object ob = result.get("a");
        assertNotNull(ob);
        Collection<?> list = (Collection<?>)ob;
        assertEquals(2, list.size());

        JSON = "{ \"var1\":\"val1\", \"var2\":\"val2\", "
            +"\"subvars\": ["
            +" {  \"subvar1\" : \"subvar2\", \"x\" : \"y\" }, "
            +" { \"a\":1 } ]"
            +" }"
            ;
        result = MAPPER.readValue(JSON, Map.class);
        assertTrue(result instanceof Map<?,?>);
        assertEquals(3, result.size());
    }

    private static final String UNTYPED_MAP_JSON =
            "{ \"double\":42.0, \"string\":\"string\","
            +"\"boolean\":true, \"list\":[\"list0\"],"
            +"\"null\":null }";
    
    static class ObjectWrapperMap extends HashMap<String, ObjectWrapper> { }
    
    public void testSpecialMap() throws IOException
    {
       final ObjectWrapperMap map = MAPPER.readValue(UNTYPED_MAP_JSON, ObjectWrapperMap.class);
       assertNotNull(map);
       _doTestUntyped(map);
    }

    public void testGenericMap() throws IOException
    {
        final Map<String, ObjectWrapper> map = MAPPER.readValue
            (UNTYPED_MAP_JSON,
             new TypeReference<Map<String, ObjectWrapper>>() { });
       _doTestUntyped(map);
    }
    
    private void _doTestUntyped(final Map<String, ObjectWrapper> map)
    {
        ObjectWrapper w = map.get("double");
        assertNotNull(w);
        assertEquals(Double.valueOf(42), w.getObject());
        assertEquals("string", map.get("string").getObject());
        assertEquals(Boolean.TRUE, map.get("boolean").getObject());
        assertEquals(Collections.singletonList("list0"), map.get("list").getObject());
        assertTrue(map.containsKey("null"));
        assertNull(map.get("null"));
        assertEquals(5, map.size());
    }
    
    // [JACKSON-620]: allow "" to mean 'null' for Maps
    public void testFromEmptyString() throws Exception
    {
        ObjectMapper m = new ObjectMapper();
        m.configure(DeserializationFeature.ACCEPT_EMPTY_STRING_AS_NULL_OBJECT, true);
        Map<?,?> result = m.readValue(quote(""), Map.class);
        assertNull(result);
    }

    /*
    /**********************************************************
    /* Test methods, typed maps
    /**********************************************************
     */

    public void testExactStringIntMap() throws Exception
    {
        // to get typing, must use type reference
        String JSON = "{ \"foo\" : 13, \"bar\" : -39, \n \"\" : 0 }";
        Map<String,Integer> result = MAPPER.readValue
            (JSON, new TypeReference<HashMap<String,Integer>>() { });

        assertNotNull(result);
        assertEquals(HashMap.class, result.getClass());
        assertEquals(3, result.size());

        assertEquals(Integer.valueOf(13), result.get("foo"));
        assertEquals(Integer.valueOf(-39), result.get("bar"));
        assertEquals(Integer.valueOf(0), result.get(""));
        assertNull(result.get("foobar"));
        assertNull(result.get(" "));
    }

    /**
     * Let's also check that it is possible to do type conversions
     * to allow use of non-String Map keys.
     */
    public void testIntBooleanMap() throws Exception
    {
        // to get typing, must use type reference
        String JSON = "{ \"1\" : true, \"-1\" : false }";
        Map<String,Integer> result = MAPPER.readValue
            (JSON, new TypeReference<HashMap<Integer,Boolean>>() { });

        assertNotNull(result);
        assertEquals(HashMap.class, result.getClass());
        assertEquals(2, result.size());

        assertEquals(Boolean.TRUE, result.get(Integer.valueOf(1)));
        assertEquals(Boolean.FALSE, result.get(Integer.valueOf(-1)));
        assertNull(result.get("foobar"));
        assertNull(result.get(0));
    }

    public void testExactStringStringMap() throws Exception
    {
        // to get typing, must use type reference
        String JSON = "{ \"a\" : \"b\" }";
        Map<String,Integer> result = MAPPER.readValue
            (JSON, new TypeReference<TreeMap<String,String>>() { });

        assertNotNull(result);
        assertEquals(TreeMap.class, result.getClass());
        assertEquals(1, result.size());

        assertEquals("b", result.get("a"));
        assertNull(result.get("b"));
    }

    /**
     * Unit test that verifies that it's ok to have incomplete
     * information about Map class itself, as long as it's something
     * we good guess about: for example, <code>Map.Class</code> will
     * be replaced by something like <code>HashMap.class</code>,
     * if given.
     */
    public void testGenericStringIntMap() throws Exception
    {
        // to get typing, must use type reference; but with abstract type
        String JSON = "{ \"a\" : 1, \"b\" : 2, \"c\" : -99 }";
        Map<String,Integer> result = MAPPER.readValue
            (JSON, new TypeReference<Map<String,Integer>>() { });
        assertNotNull(result);
        assertTrue(result instanceof Map<?,?>);
        assertEquals(3, result.size());

        assertEquals(Integer.valueOf(-99), result.get("c"));
        assertEquals(Integer.valueOf(2), result.get("b"));
        assertEquals(Integer.valueOf(1), result.get("a"));

        assertNull(result.get(""));
    }

    // [Databind#540]
    public void testMapFromEmptyArray() throws Exception
    {
        final String JSON = "  [\n]";
        assertFalse(MAPPER.isEnabled(DeserializationFeature.ACCEPT_EMPTY_ARRAY_AS_NULL_OBJECT));
        // first, verify default settings which do not accept empty Array
        ObjectMapper mapper = new ObjectMapper();
        try {
            mapper.readValue(JSON, Map.class);
            fail("Should not accept Empty Array for Map by default");
        } catch (JsonProcessingException e) {
            verifyException(e, "START_ARRAY token");
        }
        // should be ok to enable dynamically:
        ObjectReader r = MAPPER.readerFor(Map.class)
                .with(DeserializationFeature.ACCEPT_EMPTY_ARRAY_AS_NULL_OBJECT);

        Map<?,?> result = r.readValue(JSON);
        assertNull(result);

        EnumMap<?,?> result2 = r.forType(new TypeReference<EnumMap<Key,String>>() { })
                .readValue(JSON);
        assertNull(result2);
    }

    /*
    /**********************************************************
    /* Test methods, maps with enums
    /**********************************************************
     */

    public void testEnumMap() throws Exception
    {
        String JSON = "{ \"KEY1\" : \"\", \"WHATEVER\" : null }";

        // to get typing, must use type reference
        EnumMap<Key,String> result = MAPPER.readValue
            (JSON, new TypeReference<EnumMap<Key,String>>() { });

        assertNotNull(result);
        assertEquals(EnumMap.class, result.getClass());
        assertEquals(2, result.size());

        assertEquals("", result.get(Key.KEY1));
        // null should be ok too...
        assertTrue(result.containsKey(Key.WHATEVER));
        assertNull(result.get(Key.WHATEVER));

        // plus we have nothing for this key
        assertFalse(result.containsKey(Key.KEY2));
        assertNull(result.get(Key.KEY2));
    }

    public void testMapWithEnums() throws Exception
    {
        String JSON = "{ \"KEY2\" : \"WHATEVER\" }";

        // to get typing, must use type reference
        Map<Enum<?>,Enum<?>> result = MAPPER.readValue
            (JSON, new TypeReference<Map<Key,Key>>() { });

        assertNotNull(result);
        assertTrue(result instanceof Map<?,?>);
        assertEquals(1, result.size());

        assertEquals(Key.WHATEVER, result.get(Key.KEY2));
        assertNull(result.get(Key.WHATEVER));
        assertNull(result.get(Key.KEY1));
    }

    public void testEnumPolymorphicSerializationTest() throws Exception 
    {
        ObjectMapper mapper = new ObjectMapper();
        List<ITestType> testTypesList = new ArrayList<ITestType>();
        testTypesList.add(ConcreteType.ONE);
        testTypesList.add(ConcreteType.TWO);
        ListContainer listContainer = new ListContainer();
        listContainer.testTypes = testTypesList;
        String json = mapper.writeValueAsString(listContainer);
        listContainer = mapper.readValue(json, ListContainer.class);
        EnumMapContainer enumMapContainer = new EnumMapContainer();
        EnumMap<KeyEnum,ITestType> testTypesMap = new EnumMap<KeyEnum,ITestType>(KeyEnum.class);
        testTypesMap.put(KeyEnum.A, ConcreteType.ONE);
        testTypesMap.put(KeyEnum.B, ConcreteType.TWO);
        enumMapContainer.testTypes = testTypesMap;
        
        json = mapper.writeValueAsString(enumMapContainer);
        enumMapContainer = mapper.readValue(json, EnumMapContainer.class);
    }

    /*
    /**********************************************************
    /* Test methods, maps with Date
    /**********************************************************
     */
    public void testDateMap() throws Exception
    {
    	 Date date1=new Date(123456000L);
    	 DateFormat fmt = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz", Locale.US);
         
    	 String JSON = "{ \""+  fmt.format(date1)+"\" : \"\", \""+new Date(0).getTime()+"\" : null }";
    	 HashMap<Date,String> result=  MAPPER.readValue
    	            (JSON, new TypeReference<HashMap<Date,String>>() { });
    	 
    	 assertNotNull(result);
    	 assertEquals(HashMap.class, result.getClass());
    	 assertEquals(2, result.size());
    	 
    	 assertTrue(result.containsKey(date1));
    	 assertEquals("", result.get(new Date(123456000L)));

    	 assertTrue(result.containsKey(new Date(0)));
    	 assertNull(result.get(new Date(0)));
    }

    /*
    /**********************************************************
    /* Test methods, maps with various alternative key types
    /**********************************************************
     */

    public void testCalendarMap() throws Exception
    {
        // 18-Jun-2015, tatu: Should be safest to use default timezone that mapper would use
        TimeZone tz = MAPPER.getSerializationConfig().getTimeZone();        
        Calendar c = Calendar.getInstance(tz);

        c.setTimeInMillis(123456000L);
        DateFormat fmt = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz", Locale.US);
        String JSON = "{ \""+fmt.format(c.getTime())+"\" : \"\", \""+new Date(0).getTime()+"\" : null }";
        HashMap<Calendar,String> result = MAPPER.readValue
                (JSON, new TypeReference<HashMap<Calendar,String>>() { });

        assertNotNull(result);
        assertEquals(HashMap.class, result.getClass());
        assertEquals(2, result.size());

        assertTrue(result.containsKey(c));
        assertEquals("", result.get(c));
        c.setTimeInMillis(0);
        assertTrue(result.containsKey(c));
        assertNull(result.get(c));
    }

    public void testUUIDKeyMap() throws Exception
    {
         UUID key = UUID.nameUUIDFromBytes("foobar".getBytes("UTF-8"));
         String JSON = "{ \""+key+"\":4}";
         Map<UUID,Object> result = MAPPER.readValue(JSON, new TypeReference<Map<UUID,Object>>() { });
         assertNotNull(result);
         assertEquals(1, result.size());
         Object ob = result.keySet().iterator().next();
         assertNotNull(ob);
         assertEquals(UUID.class, ob.getClass());
         assertEquals(key, ob);
    }

    public void testLocaleKeyMap() throws Exception {
        Locale key = Locale.CHINA;
        String JSON = "{ \"" + key + "\":4}";
        Map<Locale, Object> result = MAPPER.readValue(JSON, new TypeReference<Map<Locale, Object>>() {
        });
        assertNotNull(result);
        assertEquals(1, result.size());
        Object ob = result.keySet().iterator().next();
        assertNotNull(ob);
        assertEquals(Locale.class, ob.getClass());
        assertEquals(key, ob);
    }

    public void testCurrencyKeyMap() throws Exception {
        Currency key = Currency.getInstance("USD");
        String JSON = "{ \"" + key + "\":4}";
        Map<Currency, Object> result = MAPPER.readValue(JSON, new TypeReference<Map<Currency, Object>>() {
        });
        assertNotNull(result);
        assertEquals(1, result.size());
        Object ob = result.keySet().iterator().next();
        assertNotNull(ob);
        assertEquals(Currency.class, ob.getClass());
        assertEquals(key, ob);
    }

    // Test confirming that @JsonCreator may be used with Map Key types
    public void testKeyWithCreator() throws Exception
    {
        // first, key should deserialize normally:
        KeyType key = MAPPER.readValue(quote("abc"), KeyType.class);
        assertEquals("abc", key.value);

        Map<KeyType,Integer> map = MAPPER.readValue("{\"foo\":3}", new TypeReference<Map<KeyType,Integer>>() {} );
        assertEquals(1, map.size());
        key = map.keySet().iterator().next();
        assertEquals("foo", key.value);
    }

    public void testClassKeyMap() throws Exception {
        ClassStringMap map = MAPPER.readValue(aposToQuotes("{'java.lang.String':'foo'}"),
                ClassStringMap.class);
        assertNotNull(map);
        assertEquals(1, map.size());
        assertEquals("foo", map.get(String.class));
    }

    public void testcharSequenceKeyMap() throws Exception {
        String JSON = aposToQuotes("{'a':'b'}");
        Map<CharSequence,String> result = MAPPER.readValue(JSON, new TypeReference<Map<CharSequence,String>>() { });
        assertNotNull(result);
        assertEquals(1, result.size());
        assertEquals("b", result.get("a"));
    }

    /*
    /**********************************************************
    /* Test methods, annotated Maps
    /**********************************************************
     */

    /**
     * Simple test to ensure that @JsonDeserialize.using is
     * recognized
     */
    public void testMapWithDeserializer() throws Exception
    {
        CustomMap result = MAPPER.readValue(quote("xyz"), CustomMap.class);
        assertEquals(1, result.size());
        assertEquals("xyz", result.get("x"));
    }

    /*
    /**********************************************************
    /* Test methods, annotated Map.Entry
    /**********************************************************
     */

    public void testMapEntrySimpleTypes() throws Exception
    {
        List<Map.Entry<String,Long>> stuff = MAPPER.readValue(aposToQuotes("[{'a':15},{'b':42}]"),
                new TypeReference<List<Map.Entry<String,Long>>>() { });
        assertNotNull(stuff);
        assertEquals(2, stuff.size());
        assertNotNull(stuff.get(1));
        assertEquals("b", stuff.get(1).getKey());
        assertEquals(Long.valueOf(42), stuff.get(1).getValue());
    }

    public void testMapEntryWithStringBean() throws Exception
    {
        List<Map.Entry<Integer,StringWrapper>> stuff = MAPPER.readValue(aposToQuotes("[{'28':'Foo'},{'13':'Bar'}]"),
                new TypeReference<List<Map.Entry<Integer,StringWrapper>>>() { });
        assertNotNull(stuff);
        assertEquals(2, stuff.size());
        assertNotNull(stuff.get(1));
        assertEquals(Integer.valueOf(13), stuff.get(1).getKey());
        
        StringWrapper sw = stuff.get(1).getValue();
        assertEquals("Bar", sw.str);
    }

    public void testMapEntryFail() throws Exception
    {
        try {
            /*List<Map.Entry<Integer,StringWrapper>> stuff =*/ MAPPER.readValue(aposToQuotes("[{'28':'Foo','13':'Bar'}]"),
                    new TypeReference<List<Map.Entry<Integer,StringWrapper>>>() { });
            fail("Should not have passed");
        } catch (Exception e) {
            verifyException(e, "more than one entry in JSON");
        }
    }

    /*
    /**********************************************************
    /* Test methods, other exotic Map types
    /**********************************************************
     */
    
    // [databind#810]
    public void testReadProperties() throws Exception
    {
        Properties props = MAPPER.readValue(aposToQuotes("{'a':'foo', 'b':123, 'c':true}"),
                Properties.class);
        assertEquals(3, props.size());
        assertEquals("foo", props.getProperty("a"));
        assertEquals("123", props.getProperty("b"));
        assertEquals("true", props.getProperty("c"));
    }

    // JDK singletonMap
    public void testSingletonMapRoundtrip() throws Exception
    {
        final TypeReference<?> type = new TypeReference<Map<String,IntWrapper>>() { };

        String json = MAPPER.writeValueAsString(Collections.singletonMap("value", new IntWrapper(5)));
        Map<String,IntWrapper> result = MAPPER.readValue(json, type);
        assertNotNull(result);
        assertEquals(1, result.size());
        IntWrapper w = result.get("value");
        assertNotNull(w);
        assertEquals(5, w.i);
    }

    /*
    /**********************************************************
    /* Error tests
    /**********************************************************
     */

    public void testMapError() throws Exception
    {
        try {
            Object result = MAPPER.readValue("[ 1, 2 ]", 
                                             new TypeReference<Map<String,String>>() { });
            fail("Expected an exception, but got result value: "+result);
        } catch (JsonMappingException jex) {
            verifyException(jex, "START_ARRAY");
        }
    }

    public void testNoCtorMap() throws Exception
    {
        try {
            BrokenMap result = MAPPER.readValue("{ \"a\" : 3 }", BrokenMap.class);
            // should never get here; assert added to remove compiler warning
            assertNull(result);
        } catch (JsonMappingException e) {
            // instead, should get this exception:
            verifyException(e, "no default constructor found");
        }
    }
}

```
