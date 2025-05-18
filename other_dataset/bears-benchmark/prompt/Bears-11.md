## Buggy code
```java
public class StdKeySerializers
{
    @SuppressWarnings("deprecation")
    protected final static JsonSerializer<Object> DEFAULT_KEY_SERIALIZER = new StdKeySerializer();

    protected final static JsonSerializer<Object> DEFAULT_STRING_SERIALIZER = new StringKeySerializer();

    private StdKeySerializers() { }

    /**
     * @param config Serialization configuration in use, may be needed in choosing
     *    serializer to use
     * @param rawKeyType Type of key values to serialize
     * @param useDefault If no match is found, should we return fallback deserializer
     *    (true), or null (false)?
     */
    public static JsonSerializer<Object> getStdKeySerializer(SerializationConfig config,
            Class<?> rawKeyType, boolean useDefault)
    {
        // 24-Sep-2015, tatu: Important -- should ONLY consider types for which `@JsonValue`
        //    can not be used, since caller has not yet checked for that annotation
        //    This is why Enum types are not handled here quite yet

        // [databind#943: Use a dynamic key serializer if we are not given actual
        // type declaration
        if ((rawKeyType == null) || (rawKeyType == Object.class)) {
            return new Dynamic();
        }
        if (rawKeyType == String.class) {
            return DEFAULT_STRING_SERIALIZER;
        }
        if (rawKeyType.isPrimitive() || Number.class.isAssignableFrom(rawKeyType)) {
            // 28-Jun-2016, tatu: Used to just return DEFAULT_KEY_SERIALIZER, but makes
            //   more sense to use simpler one directly
            return new Default(Default.TYPE_TO_STRING, rawKeyType);
        }
        if (rawKeyType == Class.class) {
            return new Default(Default.TYPE_CLASS, rawKeyType);
        }
        if (Date.class.isAssignableFrom(rawKeyType)) {
            return new Default(Default.TYPE_DATE, rawKeyType);
        }
        if (Calendar.class.isAssignableFrom(rawKeyType)) {
            return new Default(Default.TYPE_CALENDAR, rawKeyType);
        }
        // other JDK types we know convert properly with 'toString()'?
        if (rawKeyType == java.util.UUID.class) {
            return new Default(Default.TYPE_TO_STRING, rawKeyType);
        }
        if (useDefault) {
            return DEFAULT_KEY_SERIALIZER;
        }
        return null;
    }

    /**
     * Method called if no specified key serializer was located; will return a
     * "default" key serializer.
     *
     * @since 2.7
     */
    @SuppressWarnings("unchecked")
    public static JsonSerializer<Object> getFallbackKeySerializer(SerializationConfig config,
            Class<?> rawKeyType)
    {
        if (rawKeyType != null) {
            // 29-Sep-2015, tatu: Odd case here, of `Enum`, which we may get for `EnumMap`; not sure
            //   if that is a bug or feature. Regardless, it seems to require dynamic handling
            //   (compared to getting actual fully typed Enum).
            //  Note that this might even work from the earlier point, but let's play it safe for now
            // 11-Aug-2016, tatu: Turns out we get this if `EnumMap` is the root value because
            //    then there is no static type
            if (rawKeyType == Enum.class) {
                return new Dynamic();
            }
            if (rawKeyType.isEnum()) {
                return EnumKeySerializer.construct(rawKeyType,
                        EnumValues.constructFromName(config, (Class<Enum<?>>) rawKeyType));
            }
        }
        return DEFAULT_KEY_SERIALIZER;
    }

    /**
     * @deprecated since 2.7
     */
    @Deprecated
    public static JsonSerializer<Object> getDefault() {
        return DEFAULT_KEY_SERIALIZER;
    }

    /*
    /**********************************************************
    /* Standard implementations used
    /**********************************************************
     */

    /**
     * This is a "chameleon" style multi-type key serializer for simple
     * standard JDK types.
     *<p>
     * TODO: Should (but does not yet) support re-configuring format used for
     * {@link java.util.Date} and {@link java.util.Calendar} key serializers,
     * as well as alternative configuration of Enum key serializers.
     */
    public static class Default extends StdSerializer<Object> {
        final static int TYPE_DATE = 1;
        final static int TYPE_CALENDAR = 2;
        final static int TYPE_CLASS = 3;
        final static int TYPE_ENUM = 4;
        final static int TYPE_TO_STRING = 5;

        protected final int _typeId;
        
        public Default(int typeId, Class<?> type) {
            super(type, false);
            _typeId = typeId;
        }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider) throws IOException {
            switch (_typeId) {
            case TYPE_DATE:
                provider.defaultSerializeDateKey((Date)value, g);
                break;
            case TYPE_CALENDAR:
                provider.defaultSerializeDateKey(((Calendar) value).getTimeInMillis(), g);
                break;
            case TYPE_CLASS:
                g.writeFieldName(((Class<?>)value).getName());
                break;
            case TYPE_ENUM:
                {
                    String str = provider.isEnabled(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)
                            ? value.toString() : ((Enum<?>) value).name();
                    g.writeFieldName(str);
                }
                break;
            case TYPE_TO_STRING:
            default:
                g.writeFieldName(value.toString());
            }
        }
    }

    /**
     * Key serializer used when key type is not known statically, and actual key
     * serializer needs to be dynamically located.
     */
    public static class Dynamic extends StdSerializer<Object>
    {
        // Important: MUST be transient, to allow serialization of key serializer itself
        protected transient PropertySerializerMap _dynamicSerializers;
        
        public Dynamic() {
            super(String.class, false);
            _dynamicSerializers = PropertySerializerMap.emptyForProperties();
        }

        Object readResolve() {
            // Since it's transient, and since JDK serialization by-passes ctor, need this:
            _dynamicSerializers = PropertySerializerMap.emptyForProperties();
            return this;
        }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider)
                throws IOException
        {
            Class<?> cls = value.getClass();
            PropertySerializerMap m = _dynamicSerializers;
            JsonSerializer<Object> ser = m.serializerFor(cls);
            if (ser == null) {
                ser = _findAndAddDynamic(m, cls, provider);
            }
            ser.serialize(value, g, provider);
        }

        @Override
        public void acceptJsonFormatVisitor(JsonFormatVisitorWrapper visitor, JavaType typeHint) throws JsonMappingException {
            visitStringFormat(visitor, typeHint);
        }

        protected JsonSerializer<Object> _findAndAddDynamic(PropertySerializerMap map,
                Class<?> type, SerializerProvider provider) throws JsonMappingException
        {
            PropertySerializerMap.SerializerAndMapResult result =
                    // null -> for now we won't keep ref or pass BeanProperty; could change
                    map.findAndAddKeySerializer(type, provider, null);
            // did we get a new map of serializers? If so, start using it
            if (map != result.map) {
                _dynamicSerializers = result.map;
            }
            return result.serializer;
        }
    }

    /**
     * Simple and fast key serializer when keys are Strings.
     */
    public static class StringKeySerializer extends StdSerializer<Object>
    {
        public StringKeySerializer() { super(String.class, false); }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider) throws IOException {
            g.writeFieldName((String) value);
        }
    }

    /**
     * Specialized instance to use for Enum keys, as per [databind#1322]
     *
     * @since 2.8
     */
    public static class EnumKeySerializer extends StdSerializer<Object>
    {
        protected final EnumValues _values;

        protected EnumKeySerializer(Class<?> enumType, EnumValues values) {
            super(enumType, false);
            _values = values;
        }

        public static EnumKeySerializer construct(Class<?> enumType,
                EnumValues enumValues)
        {
            return new EnumKeySerializer(enumType, enumValues);
        }
        
        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider serializers)
                throws IOException
        {
            if (serializers.isEnabled(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)) {
                g.writeFieldName(value.toString());
                return;
            }
            Enum<?> en = (Enum<?>) value;
            g.writeFieldName(_values.serializedValueFor(en));
        }
    }
}

public class StdKeySerializers
{
    @SuppressWarnings("deprecation")
    protected final static JsonSerializer<Object> DEFAULT_KEY_SERIALIZER = new StdKeySerializer();

    protected final static JsonSerializer<Object> DEFAULT_STRING_SERIALIZER = new StringKeySerializer();

    private StdKeySerializers() { }

    /**
     * @param config Serialization configuration in use, may be needed in choosing
     *    serializer to use
     * @param rawKeyType Type of key values to serialize
     * @param useDefault If no match is found, should we return fallback deserializer
     *    (true), or null (false)?
     */
    public static JsonSerializer<Object> getStdKeySerializer(SerializationConfig config,
            Class<?> rawKeyType, boolean useDefault)
    {
        // 24-Sep-2015, tatu: Important -- should ONLY consider types for which `@JsonValue`
        //    can not be used, since caller has not yet checked for that annotation
        //    This is why Enum types are not handled here quite yet

        // [databind#943: Use a dynamic key serializer if we are not given actual
        // type declaration
        if ((rawKeyType == null) || (rawKeyType == Object.class)) {
            return new Dynamic();
        }
        if (rawKeyType == String.class) {
            return DEFAULT_STRING_SERIALIZER;
        }
        if (rawKeyType.isPrimitive() || Number.class.isAssignableFrom(rawKeyType)) {
            // 28-Jun-2016, tatu: Used to just return DEFAULT_KEY_SERIALIZER, but makes
            //   more sense to use simpler one directly
            return new Default(Default.TYPE_TO_STRING, rawKeyType);
        }
        if (rawKeyType == Class.class) {
            return new Default(Default.TYPE_CLASS, rawKeyType);
        }
        if (Date.class.isAssignableFrom(rawKeyType)) {
            return new Default(Default.TYPE_DATE, rawKeyType);
        }
        if (Calendar.class.isAssignableFrom(rawKeyType)) {
            return new Default(Default.TYPE_CALENDAR, rawKeyType);
        }
        // other JDK types we know convert properly with 'toString()'?
        if (rawKeyType == java.util.UUID.class) {
            return new Default(Default.TYPE_TO_STRING, rawKeyType);
        }
        if (useDefault) {
            return DEFAULT_KEY_SERIALIZER;
        }
        return null;
    }

    /**
     * Method called if no specified key serializer was located; will return a
     * "default" key serializer.
     *
     * @since 2.7
     */
    @SuppressWarnings("unchecked")
    public static JsonSerializer<Object> getFallbackKeySerializer(SerializationConfig config,
            Class<?> rawKeyType)
    {
        if (rawKeyType != null) {
            // 29-Sep-2015, tatu: Odd case here, of `Enum`, which we may get for `EnumMap`; not sure
            //   if that is a bug or feature. Regardless, it seems to require dynamic handling
            //   (compared to getting actual fully typed Enum).
            //  Note that this might even work from the earlier point, but let's play it safe for now
            // 11-Aug-2016, tatu: Turns out we get this if `EnumMap` is the root value because
            //    then there is no static type
            if (rawKeyType == Enum.class) {
                return new Dynamic();
            }
            if (rawKeyType.isEnum()) {
                return EnumKeySerializer.construct(rawKeyType,
                        EnumValues.constructFromName(config, (Class<Enum<?>>) rawKeyType));
            }
        }
        return DEFAULT_KEY_SERIALIZER;
    }

    /**
     * @deprecated since 2.7
     */
    @Deprecated
    public static JsonSerializer<Object> getDefault() {
        return DEFAULT_KEY_SERIALIZER;
    }

    /*
    /**********************************************************
    /* Standard implementations used
    /**********************************************************
     */

    /**
     * This is a "chameleon" style multi-type key serializer for simple
     * standard JDK types.
     *<p>
     * TODO: Should (but does not yet) support re-configuring format used for
     * {@link java.util.Date} and {@link java.util.Calendar} key serializers,
     * as well as alternative configuration of Enum key serializers.
     */
    public static class Default extends StdSerializer<Object> {
        final static int TYPE_DATE = 1;
        final static int TYPE_CALENDAR = 2;
        final static int TYPE_CLASS = 3;
        final static int TYPE_ENUM = 4;
        final static int TYPE_TO_STRING = 5;

        protected final int _typeId;
        
        public Default(int typeId, Class<?> type) {
            super(type, false);
            _typeId = typeId;
        }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider) throws IOException {
            switch (_typeId) {
            case TYPE_DATE:
                provider.defaultSerializeDateKey((Date)value, g);
                break;
            case TYPE_CALENDAR:
                provider.defaultSerializeDateKey(((Calendar) value).getTimeInMillis(), g);
                break;
            case TYPE_CLASS:
                g.writeFieldName(((Class<?>)value).getName());
                break;
            case TYPE_ENUM:
                {
                    String str = provider.isEnabled(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)
                            ? value.toString() : ((Enum<?>) value).name();
                    g.writeFieldName(str);
                }
                break;
            case TYPE_TO_STRING:
            default:
                g.writeFieldName(value.toString());
            }
        }
    }

    /**
     * Key serializer used when key type is not known statically, and actual key
     * serializer needs to be dynamically located.
     */
    public static class Dynamic extends StdSerializer<Object>
    {
        // Important: MUST be transient, to allow serialization of key serializer itself
        protected transient PropertySerializerMap _dynamicSerializers;
        
        public Dynamic() {
            super(String.class, false);
            _dynamicSerializers = PropertySerializerMap.emptyForProperties();
        }

        Object readResolve() {
            // Since it's transient, and since JDK serialization by-passes ctor, need this:
            _dynamicSerializers = PropertySerializerMap.emptyForProperties();
            return this;
        }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider)
                throws IOException
        {
            Class<?> cls = value.getClass();
            PropertySerializerMap m = _dynamicSerializers;
            JsonSerializer<Object> ser = m.serializerFor(cls);
            if (ser == null) {
                ser = _findAndAddDynamic(m, cls, provider);
            }
            ser.serialize(value, g, provider);
        }

        @Override
        public void acceptJsonFormatVisitor(JsonFormatVisitorWrapper visitor, JavaType typeHint) throws JsonMappingException {
            visitStringFormat(visitor, typeHint);
        }

        protected JsonSerializer<Object> _findAndAddDynamic(PropertySerializerMap map,
                Class<?> type, SerializerProvider provider) throws JsonMappingException
        {
            PropertySerializerMap.SerializerAndMapResult result =
                    // null -> for now we won't keep ref or pass BeanProperty; could change
                    map.findAndAddKeySerializer(type, provider, null);
            // did we get a new map of serializers? If so, start using it
            if (map != result.map) {
                _dynamicSerializers = result.map;
            }
            return result.serializer;
        }
    }

    /**
     * Simple and fast key serializer when keys are Strings.
     */
    public static class StringKeySerializer extends StdSerializer<Object>
    {
        public StringKeySerializer() { super(String.class, false); }

        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider provider) throws IOException {
            g.writeFieldName((String) value);
        }
    }

    /**
     * Specialized instance to use for Enum keys, as per [databind#1322]
     *
     * @since 2.8
     */
    public static class EnumKeySerializer extends StdSerializer<Object>
    {
        protected final EnumValues _values;

        protected EnumKeySerializer(Class<?> enumType, EnumValues values) {
            super(enumType, false);
            _values = values;
        }

        public static EnumKeySerializer construct(Class<?> enumType,
                EnumValues enumValues)
        {
            return new EnumKeySerializer(enumType, enumValues);
        }
        
        @Override
        public void serialize(Object value, JsonGenerator g, SerializerProvider serializers)
                throws IOException
        {
            if (serializers.isEnabled(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)) {
                g.writeFieldName(value.toString());
                return;
            }
            Enum<?> en = (Enum<?>) value;
            g.writeFieldName(_values.serializedValueFor(en));
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.ser.TestEnumSerialization

## Test line
junit.framework.ComparisonFailure

## Error
expected:<{"map":{"[1]":3}}> but was:<{"map":{"[B]":3}}>

## Error Code Block
```java
package com.fasterxml.jackson.databind.ser;

import java.io.*;
import java.util.*;

import com.fasterxml.jackson.annotation.*;

import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.jsontype.TypeSerializer;
import com.fasterxml.jackson.databind.module.SimpleModule;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;
import com.fasterxml.jackson.databind.ser.std.ToStringSerializer;

/**
 * Unit tests for verifying serialization of simple basic non-structured
 * types; primitives (and/or their wrappers), Strings.
 */
public class TestEnumSerialization
    extends BaseMapTest
{
    /*
    /**********************************************************
    /* Helper enums
    /**********************************************************
     */

    /**
     * Test enumeration for verifying Enum serialization functionality.
     */
    protected enum TestEnum {
        A, B, C;
        private TestEnum() { }

        @Override public String toString() { return name().toLowerCase(); }
    }

    /**
     * Alternative version that forces use of "toString-serializer".
     */
    @JsonSerialize(using=ToStringSerializer.class)
    protected enum AnnotatedTestEnum {
        A2, B2, C2;
        private AnnotatedTestEnum() { }

        @Override public String toString() { return name().toLowerCase(); }
    }

    protected enum EnumWithJsonValue {
        A("foo"), B("bar");
        private final String name;
        private EnumWithJsonValue(String n) {
            name = n;
        }

        @Override
        public String toString() { return name; }

        @JsonValue
        public String external() { return "value:"+name; }
    }

    protected static interface ToStringMixin {
        @Override
        @JsonValue public String toString();
    }

    protected static enum SerializableEnum implements JsonSerializable
    {
        A, B, C;

        private SerializableEnum() { }

        @Override
        public void serializeWithType(JsonGenerator jgen, SerializerProvider provider, TypeSerializer typeSer)
                throws IOException, JsonProcessingException
        {
            serialize(jgen, provider);
        }

        @Override
        public void serialize(JsonGenerator jgen, SerializerProvider provider) throws IOException, JsonProcessingException
        {
            jgen.writeString("foo");
        }
    }

    protected static enum LowerCaseEnum {
        A, B, C;
        private LowerCaseEnum() { }
        @Override
        public String toString() { return name().toLowerCase(); }
    }

    static class MapBean {
        public Map<TestEnum,Integer> map = new HashMap<TestEnum,Integer>();
        
        public void add(TestEnum key, int value) {
            map.put(key, Integer.valueOf(value));
        }
    }

    static enum NOT_OK {
        V1("v1"); 
        protected String key;
        // any runtime-persistent annotation is fine
        NOT_OK(@JsonProperty String key) { this.key = key; }
    }

    static enum OK {
        V1("v1");
        protected String key;
        OK(String key) { this.key = key; }
    }

    @SuppressWarnings({ "rawtypes", "serial" })
    static class LowerCasingEnumSerializer extends StdSerializer<Enum>
    {
        public LowerCasingEnumSerializer() { super(Enum.class); }
        @Override
        public void serialize(Enum value, JsonGenerator jgen,
                SerializerProvider provider) throws IOException {
            jgen.writeString(value.name().toLowerCase());
        }
    }

    static enum MyEnum594 {
        VALUE_WITH_A_REALLY_LONG_NAME_HERE("longValue");

        private final String key;
        private MyEnum594(String k) { key = k; }

        @JsonValue
        public String getKey() { return key; }
    }

    static class MyStuff594 {
        public Map<MyEnum594,String> stuff = new EnumMap<MyEnum594,String>(MyEnum594.class);
        
        public MyStuff594(String value) {
            stuff.put(MyEnum594.VALUE_WITH_A_REALLY_LONG_NAME_HERE, value);
        }
    }

    public class MyBean661 {
        private Map<Foo661, String> foo = new EnumMap<Foo661, String>(Foo661.class);

        public MyBean661(String value) {
            foo.put(Foo661.FOO, value);
        }

        @JsonAnyGetter
        @JsonSerialize(keyUsing = Foo661.Serializer.class)
        public Map<Foo661, String> getFoo() {
            return foo;
        }
    }

    enum Foo661 {
        FOO;
        public static class Serializer extends JsonSerializer<Foo661> {
            @Override
            public void serialize(Foo661 value, JsonGenerator jgen, SerializerProvider provider) 
                    throws IOException {
                jgen.writeFieldName("X-"+value.name());
            }
        }
    }

    protected static enum LC749Enum {
        A, B, C;
        private LC749Enum() { }
        @Override
        public String toString() { return name().toLowerCase(); }
    }

    // for [databind#1322]
    protected enum EnumWithJsonProperty {
        @JsonProperty("aleph")
        A;
    }

    /*
    /**********************************************************
    /* Tests
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();
    
    public void testSimple() throws Exception
    {
        assertEquals("\"B\"", MAPPER.writeValueAsString(TestEnum.B));
    }

    public void testEnumSet() throws Exception
    {
        StringWriter sw = new StringWriter();
        EnumSet<TestEnum> value = EnumSet.of(TestEnum.B);
        MAPPER.writeValue(sw, value);
        assertEquals("[\"B\"]", sw.toString());
    }

    /**
     * Whereas regular Enum serializer uses enum names, some users
     * prefer calling toString() instead. So let's verify that
     * this can be done using annotation for enum class.
     */
    public void testEnumUsingToString() throws Exception
    {
        StringWriter sw = new StringWriter();
        MAPPER.writeValue(sw, AnnotatedTestEnum.C2);
        assertEquals("\"c2\"", sw.toString());
    }

    // Test [JACKSON-214]
    public void testSubclassedEnums() throws Exception
    {
        assertEquals("\"B\"", MAPPER.writeValueAsString(EnumWithSubClass.B));
    }

    public void testEnumsWithJsonValue() throws Exception {
        assertEquals("\"value:bar\"", MAPPER.writeValueAsString(EnumWithJsonValue.B));
    }

    public void testEnumsWithJsonValueUsingMixin() throws Exception
    {
        // can't share, as new mix-ins are added
        ObjectMapper m = new ObjectMapper();
        m.addMixIn(TestEnum.class, ToStringMixin.class);
        assertEquals("\"b\"", m.writeValueAsString(TestEnum.B));
    }

    // [databind#601]
    public void testEnumsWithJsonValueInMap() throws Exception
    {
        EnumMap<EnumWithJsonValue,String> input = new EnumMap<EnumWithJsonValue,String>(EnumWithJsonValue.class);
        input.put(EnumWithJsonValue.B, "x");
        // 24-Sep-2015, tatu: SHOULD actually use annotated method, as per:
        assertEquals("{\"value:bar\":\"x\"}", MAPPER.writeValueAsString(input));
    }

    /**
     * Test for ensuring that @JsonSerializable is used with Enum types as well
     * as with any other types.
     */
    public void testSerializableEnum() throws Exception
    {
        assertEquals("\"foo\"", MAPPER.writeValueAsString(SerializableEnum.A));
    }

    // [JACKSON-212]
    public void testToStringEnum() throws Exception
    {
        ObjectMapper m = new ObjectMapper();
        m.configure(SerializationFeature.WRITE_ENUMS_USING_TO_STRING, true);
        assertEquals("\"b\"", m.writeValueAsString(LowerCaseEnum.B));

        // [databind#749] but should also be able to dynamically disable
        assertEquals("\"B\"",
                m.writer().without(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)
                    .writeValueAsString(LowerCaseEnum.B));
    }

    public void testToStringEnumWithEnumMap() throws Exception
    {
        ObjectMapper m = new ObjectMapper();
        m.enable(SerializationFeature.WRITE_ENUMS_USING_TO_STRING);
        EnumMap<LowerCaseEnum,String> enums = new EnumMap<LowerCaseEnum,String>(LowerCaseEnum.class);
        enums.put(LowerCaseEnum.C, "value");
        assertEquals("{\"c\":\"value\"}", m.writeValueAsString(enums));
    }

    public void testMapWithEnumKeys() throws Exception
    {
        MapBean bean = new MapBean();
        bean.add(TestEnum.B, 3);

        // By default Enums serialized using `name()`
        String json = MAPPER.writeValueAsString(bean);
        assertEquals("{\"map\":{\"B\":3}}", json);

        // but can change
        json = MAPPER.writer()
                .with(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)
                .writeValueAsString(bean);
        assertEquals("{\"map\":{\"b\":3}}", json);

        // [databind#1570]
        json = MAPPER.writer()
                .with(SerializationFeature.WRITE_ENUMS_USING_INDEX)
                .writeValueAsString(bean);
        assertEquals(aposToQuotes("{'map':{'"+TestEnum.B.ordinal()+"':3}}"), json);
    }

    public void testAsIndex() throws Exception
    {
        // By default, serialize using name
        ObjectMapper m = new ObjectMapper();
        assertFalse(m.isEnabled(SerializationFeature.WRITE_ENUMS_USING_INDEX));
        assertEquals(quote("B"), m.writeValueAsString(TestEnum.B));

        // but we can change (dynamically, too!) it to be number-based
        m.enable(SerializationFeature.WRITE_ENUMS_USING_INDEX);
        assertEquals("1", m.writeValueAsString(TestEnum.B));
    }

    // [JACKSON-757]
    public void testAnnotationsOnEnumCtor() throws Exception
    {
        assertEquals(quote("V1"), MAPPER.writeValueAsString(OK.V1));
        assertEquals(quote("V1"), MAPPER.writeValueAsString(NOT_OK.V1));
        assertEquals(quote("V2"), MAPPER.writeValueAsString(NOT_OK2.V2));
    }

    // [Issue#227]
    public void testGenericEnumSerializer() throws Exception
    {
        // By default, serialize using name
        ObjectMapper m = new ObjectMapper();
        SimpleModule module = new SimpleModule("foobar");
        module.addSerializer(Enum.class, new LowerCasingEnumSerializer());
        m.registerModule(module);
        assertEquals(quote("b"), m.writeValueAsString(TestEnum.B));
    }

    // [databind#594]
    public void testJsonValueForEnumMapKey() throws Exception {
        assertEquals(aposToQuotes("{'stuff':{'longValue':'foo'}}"),
                MAPPER.writeValueAsString(new MyStuff594("foo")));
    }

    // [databind#661]
    public void testCustomEnumMapKeySerializer() throws Exception {
        String json = MAPPER.writeValueAsString(new MyBean661("abc"));
        assertEquals(aposToQuotes("{'X-FOO':'abc'}"), json);
    }

    // [databind#749]

    public void testEnumMapSerDefault() throws Exception {
        final ObjectMapper mapper = new ObjectMapper();
        EnumMap<LC749Enum, String> m = new EnumMap<LC749Enum, String>(LC749Enum.class);
        m.put(LC749Enum.A, "value");
        assertEquals("{\"A\":\"value\"}", mapper.writeValueAsString(m));
    }
    
    public void testEnumMapSerDisableToString() throws Exception {
        final ObjectMapper mapper = new ObjectMapper();
        ObjectWriter w = mapper.writer().without(SerializationFeature.WRITE_ENUMS_USING_TO_STRING);
        EnumMap<LC749Enum, String> m = new EnumMap<LC749Enum, String>(LC749Enum.class);
        m.put(LC749Enum.A, "value");
        assertEquals("{\"A\":\"value\"}", w.writeValueAsString(m));
    }

    public void testEnumMapSerEnableToString() throws Exception {
        final ObjectMapper mapper = new ObjectMapper();
        ObjectWriter w = mapper.writer().with(SerializationFeature.WRITE_ENUMS_USING_TO_STRING);
        EnumMap<LC749Enum, String> m = new EnumMap<LC749Enum, String>(LC749Enum.class);
        m.put(LC749Enum.A, "value");
        assertEquals("{\"a\":\"value\"}", w.writeValueAsString(m));
    }

    // [databind#1322]
    public void testEnumsWithJsonProperty() throws Exception {
        assertEquals(quote("aleph"), MAPPER.writeValueAsString(EnumWithJsonProperty.A));
    }

    // [databind#1535]
    public void testEnumKeysWithJsonProperty() throws Exception {
        Map<EnumWithJsonProperty,Integer> input = new HashMap<EnumWithJsonProperty,Integer>();
        input.put(EnumWithJsonProperty.A, 13);
        assertEquals(aposToQuotes("{'aleph':13}"), MAPPER.writeValueAsString(input));
    }

    // [databind#1322]
    public void testEnumsWithJsonPropertyInSet() throws Exception
    {
        assertEquals("[\"aleph\"]",
                MAPPER.writeValueAsString(EnumSet.of(EnumWithJsonProperty.A)));
    }

    // [databind#1322]
    public void testEnumsWithJsonPropertyAsKey() throws Exception
    {
        EnumMap<EnumWithJsonProperty,String> input = new EnumMap<EnumWithJsonProperty,String>(EnumWithJsonProperty.class);
        input.put(EnumWithJsonProperty.A, "b");
        assertEquals("{\"aleph\":\"b\"}", MAPPER.writeValueAsString(input));
    }
}

// [JACKSON-757], non-inner enum
enum NOT_OK2 {
    V2("v2"); 
    protected String key;
    // any runtime-persistent annotation is fine
    NOT_OK2(@JsonProperty String key) { this.key = key; }
}

```
