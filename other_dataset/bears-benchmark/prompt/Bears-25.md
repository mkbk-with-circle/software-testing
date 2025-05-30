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
                    String key;

                    if (provider.isEnabled(SerializationFeature.WRITE_ENUMS_USING_TO_STRING)) {
                        key = value.toString();
                    } else {
                        Enum<?> e = (Enum<?>) value;
                        if (provider.isEnabled(SerializationFeature.WRITE_ENUMS_USING_INDEX)) {
                            key = String.valueOf(e.ordinal());
                        } else {
                            key = e.name();
                        }
                    }
                    g.writeFieldName(key);
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
            if (serializers.isEnabled(SerializationFeature.WRITE_ENUMS_USING_INDEX)) {
                g.writeFieldName(String.valueOf(en.ordinal()));
                return;
            }
            g.writeFieldName(_values.serializedValueFor(en));
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.ser.KeySerializers1679Test

## Test line
java.lang.StackOverflowError

## Error


## Error Code Block
```java
package com.fasterxml.jackson.databind.ser;

import java.util.*;

import com.fasterxml.jackson.databind.*;

public class KeySerializers1679Test extends BaseMapTest
{
    /*
    /**********************************************************
    /* Unit tests
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();

    // [databind#1679]
    public void testRecursion1679() throws Exception
    {
        Map<Object, Object> objectMap = new HashMap<Object, Object>();
        objectMap.put(new Object(), "foo");
        String json = MAPPER.writeValueAsString(objectMap);
        assertNotNull(json);
    }
}

```
