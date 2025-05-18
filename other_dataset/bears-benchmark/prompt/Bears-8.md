## Buggy code
```java
public class MapSerializer
    extends ContainerSerializer<Map<?,?>>
    implements ContextualSerializer
{
    private static final long serialVersionUID = 1L;

    protected final static JavaType UNSPECIFIED_TYPE = TypeFactory.unknownType();

    /**
     * Map-valued property being serialized with this instance
     */
    protected final BeanProperty _property;

    /**
     * Set of entries to omit during serialization, if any
     */
    protected final Set<String> _ignoredEntries;

    /**
     * Whether static types should be used for serialization of values
     * or not (if not, dynamic runtime type is used)
     */
    protected final boolean _valueTypeIsStatic;

    /**
     * Declared type of keys
     */
    protected final JavaType _keyType;

    /**
     * Declared type of contained values
     */
    protected final JavaType _valueType;

    /**
     * Key serializer to use, if it can be statically determined
     */
    protected JsonSerializer<Object> _keySerializer;

    /**
     * Value serializer to use, if it can be statically determined
     */
    protected JsonSerializer<Object> _valueSerializer;

    /**
     * Type identifier serializer used for values, if any.
     */
    protected final TypeSerializer _valueTypeSerializer;

    /**
     * If value type can not be statically determined, mapping from
     * runtime value types to serializers are stored in this object.
     */
    protected PropertySerializerMap _dynamicValueSerializers;

    /**
     * Id of the property filter to use, if any; null if none.
     *
     * @since 2.3
     */
    protected final Object _filterId;

    /**
     * Flag set if output is forced to be sorted by keys (usually due
     * to annotation).
     * 
     * @since 2.4
     */
    protected final boolean _sortKeys;

    /**
     * Value that indicates suppression mechanism to use for <b>values contained</b>;
     * either one of values of {@link com.fasterxml.jackson.annotation.JsonInclude.Include},
     * or actual object to compare against ("default value").
     * Note that inclusion value for Map instance itself is handled by caller (POJO
     * property that refers to the Map value).
     * 
     * @since 2.5
     */
    protected final Object _suppressableValue;

    /*
    /**********************************************************
    /* Life-cycle
    /**********************************************************
     */
    
    /**
     * @since 2.5
     */
    @SuppressWarnings("unchecked")
    protected MapSerializer(Set<String> ignoredEntries,
            JavaType keyType, JavaType valueType, boolean valueTypeIsStatic,
            TypeSerializer vts,
            JsonSerializer<?> keySerializer, JsonSerializer<?> valueSerializer)
    {
        super(Map.class, false);
        _ignoredEntries = ((ignoredEntries == null) || ignoredEntries.isEmpty())
                ? null : ignoredEntries;
        _keyType = keyType;
        _valueType = valueType;
        _valueTypeIsStatic = valueTypeIsStatic;
        _valueTypeSerializer = vts;
        _keySerializer = (JsonSerializer<Object>) keySerializer;
        _valueSerializer = (JsonSerializer<Object>) valueSerializer;
        _dynamicValueSerializers = PropertySerializerMap.emptyForProperties();
        _property = null;
        _filterId = null;
        _sortKeys = false;
        _suppressableValue = null;
    }

    /**
     * @since 2.5
     */
    protected void _ensureOverride() {
        if (getClass() != MapSerializer.class) {
            throw new IllegalStateException("Missing override in class "+getClass().getName());
        }
    }
    
    @SuppressWarnings("unchecked")
    protected MapSerializer(MapSerializer src, BeanProperty property,
            JsonSerializer<?> keySerializer, JsonSerializer<?> valueSerializer,
            Set<String> ignoredEntries)
    {
        super(Map.class, false);
        _ignoredEntries = ((ignoredEntries == null) || ignoredEntries.isEmpty())
                ? null : ignoredEntries;
        _keyType = src._keyType;
        _valueType = src._valueType;
        _valueTypeIsStatic = src._valueTypeIsStatic;
        _valueTypeSerializer = src._valueTypeSerializer;
        _keySerializer = (JsonSerializer<Object>) keySerializer;
        _valueSerializer = (JsonSerializer<Object>) valueSerializer;
        _dynamicValueSerializers = src._dynamicValueSerializers;
        _property = property;
        _filterId = src._filterId;
        _sortKeys = src._sortKeys;
        _suppressableValue = src._suppressableValue;
    }

    @Deprecated // since 2.5
    protected MapSerializer(MapSerializer src, TypeSerializer vts) {
        this(src, vts, src._suppressableValue);
    }

    /**
     * @since 2.5
     */
    protected MapSerializer(MapSerializer src, TypeSerializer vts,
            Object suppressableValue)
    {
        super(Map.class, false);
        _ignoredEntries = src._ignoredEntries;
        _keyType = src._keyType;
        _valueType = src._valueType;
        _valueTypeIsStatic = src._valueTypeIsStatic;
        _valueTypeSerializer = vts;
        _keySerializer = src._keySerializer;
        _valueSerializer = src._valueSerializer;
        _dynamicValueSerializers = src._dynamicValueSerializers;
        _property = src._property;
        _filterId = src._filterId;
        _sortKeys = src._sortKeys;
        // 05-Jun-2015, tatu: For referential, this is same as NON_EMPTY; for others, NON_NULL, so:
        if (suppressableValue == JsonInclude.Include.NON_ABSENT) {
            suppressableValue = _valueType.isReferenceType() ?
                    JsonInclude.Include.NON_EMPTY : JsonInclude.Include.NON_NULL;
        }
        _suppressableValue = suppressableValue;
    }

    protected MapSerializer(MapSerializer src, Object filterId, boolean sortKeys)
    {
        super(Map.class, false);
        _ignoredEntries = src._ignoredEntries;
        _keyType = src._keyType;
        _valueType = src._valueType;
        _valueTypeIsStatic = src._valueTypeIsStatic;
        _valueTypeSerializer = src._valueTypeSerializer;
        _keySerializer = src._keySerializer;
        _valueSerializer = src._valueSerializer;
        _dynamicValueSerializers = src._dynamicValueSerializers;
        _property = src._property;
        _filterId = filterId;
        _sortKeys = sortKeys;
        _suppressableValue = src._suppressableValue;
    }

    @Override
    public MapSerializer _withValueTypeSerializer(TypeSerializer vts) {
        if (_valueTypeSerializer == vts) {
            return this;
        }
        _ensureOverride();
        return new MapSerializer(this, vts, null);
    }

    /**
     * @since 2.4
     */
    public MapSerializer withResolved(BeanProperty property,
            JsonSerializer<?> keySerializer, JsonSerializer<?> valueSerializer,
            Set<String> ignored, boolean sortKeys)
    {
        _ensureOverride();
        MapSerializer ser = new MapSerializer(this, property, keySerializer, valueSerializer, ignored);
        if (sortKeys != ser._sortKeys) {
            ser = new MapSerializer(ser, _filterId, sortKeys);
        }
        return ser;
    }

    @Override
    public MapSerializer withFilterId(Object filterId) {
        if (_filterId == filterId) {
            return this;
        }
        _ensureOverride();
        return new MapSerializer(this, filterId, _sortKeys);
    }

    /**
     * Mutant factory for constructing an instance with different inclusion strategy
     * for content (Map values).
     * 
     * @since 2.5
     */
    public MapSerializer withContentInclusion(Object suppressableValue) {
        if (suppressableValue == _suppressableValue) {
            return this;
        }
        _ensureOverride();
        return new MapSerializer(this, _valueTypeSerializer, suppressableValue);
    }                
    
    /**
     * @since 2.3
     *
     * @deprecated Since 2.8 use the other overload
     */
    @Deprecated // since 2.8
    public static MapSerializer construct(String[] ignoredList, JavaType mapType,
            boolean staticValueType, TypeSerializer vts,
            JsonSerializer<Object> keySerializer, JsonSerializer<Object> valueSerializer,
            Object filterId)
    {
        Set<String> ignoredEntries = (ignoredList == null || ignoredList.length == 0)
                ? null : ArrayBuilders.arrayToSet(ignoredList);
        return construct(ignoredEntries, mapType, staticValueType, vts,
                keySerializer, valueSerializer, filterId);
    }

    /**
     * @since 2.8
     */
    public static MapSerializer construct(Set<String> ignoredEntries, JavaType mapType,
            boolean staticValueType, TypeSerializer vts,
            JsonSerializer<Object> keySerializer, JsonSerializer<Object> valueSerializer,
            Object filterId)
    {
        JavaType keyType, valueType;
        
        if (mapType == null) {
            keyType = valueType = UNSPECIFIED_TYPE;
        } else { 
            keyType = mapType.getKeyType();
            valueType = mapType.getContentType();
        }
        // If value type is final, it's same as forcing static value typing:
        if (!staticValueType) {
            staticValueType = (valueType != null && valueType.isFinal());
        } else {
            // also: Object.class can not be handled as static, ever
            if (valueType.getRawClass() == Object.class) {
                staticValueType = false;
            }
        }
        MapSerializer ser = new MapSerializer(ignoredEntries, keyType, valueType, staticValueType, vts,
                keySerializer, valueSerializer);
        if (filterId != null) {
            ser = ser.withFilterId(filterId);
        }
        return ser;
    }

    /*
    /**********************************************************
    /* Post-processing (contextualization)
    /**********************************************************
     */

    @Override
    public JsonSerializer<?> createContextual(SerializerProvider provider,
            BeanProperty property)
        throws JsonMappingException
    {
        JsonSerializer<?> ser = null;
        JsonSerializer<?> keySer = null;
        final AnnotationIntrospector intr = provider.getAnnotationIntrospector();
        final AnnotatedMember propertyAcc = (property == null) ? null : property.getMember();
        Object suppressableValue = _suppressableValue;

        // First: if we have a property, may have property-annotation overrides
        if ((propertyAcc != null) && (intr != null)) {
            Object serDef = intr.findKeySerializer(propertyAcc);
            if (serDef != null) {
                keySer = provider.serializerInstance(propertyAcc, serDef);
            }
            serDef = intr.findContentSerializer(propertyAcc);
            if (serDef != null) {
                ser = provider.serializerInstance(propertyAcc, serDef);
            }
        }

        JsonInclude.Value inclV = findIncludeOverrides(provider, property, Map.class);
        JsonInclude.Include incl = inclV.getContentInclusion();
        if ((incl != null) && (incl != JsonInclude.Include.USE_DEFAULTS)) {
            suppressableValue = incl;
        }
        if (ser == null) {
            ser = _valueSerializer;
        }
        // [databind#124]: May have a content converter
        ser = findConvertingContentSerializer(provider, property, ser);
        if (ser == null) {
            // 30-Sep-2012, tatu: One more thing -- if explicit content type is annotated,
            //   we can consider it a static case as well.
            // 20-Aug-2013, tatu: Need to avoid trying to access serializer for java.lang.Object tho
            if (_valueTypeIsStatic && !_valueType.isJavaLangObject()) {
                ser = provider.findValueSerializer(_valueType, property);
            }
        } else {
            ser = provider.handleSecondaryContextualization(ser, property);
        }
        if (keySer == null) {
            keySer = _keySerializer;
        }
        if (keySer == null) {
            keySer = provider.findKeySerializer(_keyType, property);
        } else {
            keySer = provider.handleSecondaryContextualization(keySer, property);
        }
        Set<String> ignored = _ignoredEntries;
        boolean sortKeys = false;
        if ((intr != null) && (propertyAcc != null)) {
            JsonIgnoreProperties.Value ignorals = intr.findPropertyIgnorals(propertyAcc);
            if (ignorals != null){
                Set<String> newIgnored = ignorals.findIgnoredForSerialization();
                if ((newIgnored != null) && !newIgnored.isEmpty()) {
                    ignored = (ignored == null) ? new HashSet<String>() : new HashSet<String>(ignored);
                    for (String str : newIgnored) {
                        ignored.add(str);
                    }
                }
            }
            Boolean b = intr.findSerializationSortAlphabetically(propertyAcc);
            sortKeys = (b != null) && b.booleanValue();
        }
        JsonFormat.Value format = findFormatOverrides(provider, property, Map.class);
        if (format != null) {
            Boolean B = format.getFeature(JsonFormat.Feature.WRITE_SORTED_MAP_ENTRIES);
            if (B != null) {
                sortKeys = B.booleanValue();
            }
        }
        MapSerializer mser = withResolved(property, keySer, ser, ignored, sortKeys);
        if (suppressableValue != _suppressableValue) {
            mser = mser.withContentInclusion(suppressableValue);
        }

        // [databind#307]: allow filtering
        if (property != null) {
            AnnotatedMember m = property.getMember();
            if (m != null) {
                Object filterId = intr.findFilterId(m);
                if (filterId != null) {
                    mser = mser.withFilterId(filterId);
                }
            }
        }
        return mser;
    }
    
    /*
    /**********************************************************
    /* Accessors
    /**********************************************************
     */

    @Override
    public JavaType getContentType() {
        return _valueType;
    }

    @Override
    public JsonSerializer<?> getContentSerializer() {
        return _valueSerializer;
    }

    @Override
    public boolean isEmpty(SerializerProvider prov, Map<?,?> value)
    {
        if (value == null || value.isEmpty()) {
            return true;
        }
        // 05-Nove-2015, tatu: Simple cases are cheap, but for recursive
        //   emptiness checking we actually need to see if values are empty as well.
        Object supp = _suppressableValue;

        if ((supp == null) || (supp == JsonInclude.Include.ALWAYS)) {
            return false;
        }
        JsonSerializer<Object> valueSer = _valueSerializer;
        if (valueSer != null) {
            for (Object elemValue : value.values()) {
                if ((elemValue != null) && !valueSer.isEmpty(prov, elemValue)) {
                    return false;
                }
            }
            return true;
        }
        // But if not statically known, try this:
        PropertySerializerMap serializers = _dynamicValueSerializers;
        for (Object elemValue : value.values()) {
            if (elemValue == null) {
                continue;
            }
            Class<?> cc = elemValue.getClass();
            // 05-Nov-2015, tatu: Let's not worry about generic types here, actually;
            //   unlikely to make any difference, but does add significant overhead
            valueSer = serializers.serializerFor(cc);
            if (valueSer == null) {
                try {
                    valueSer = _findAndAddDynamic(serializers, cc, prov);
                } catch (JsonMappingException e) { // Ugh... can not just throw as-is, so...
                    // 05-Nov-2015, tatu: For now, probably best not to assume empty then
                    return false;
                }
                serializers = _dynamicValueSerializers;
            }
            if (!valueSer.isEmpty(prov, elemValue)) {
                return false;
            }
        }
        return true;
    }

    @Override
    public boolean hasSingleElement(Map<?,?> value) {
        return (value.size() == 1);
    }
    
    /*
    /**********************************************************
    /* Extended API
    /**********************************************************
     */

    /**
     * Accessor for currently assigned key serializer. Note that
     * this may return null during construction of <code>MapSerializer</code>:
     * depedencies are resolved during {@link #createContextual} method
     * (which can be overridden by custom implementations), but for some
     * dynamic types, it is possible that serializer is only resolved
     * during actual serialization.
     * 
     * @since 2.0
     */
    public JsonSerializer<?> getKeySerializer() {
        return _keySerializer;
    }
    
    /*
    /**********************************************************
    /* JsonSerializer implementation
    /**********************************************************
     */

    @Override
    public void serialize(Map<?,?> value, JsonGenerator gen, SerializerProvider provider)
        throws IOException
    {
        gen.writeStartObject(value);
        if (!value.isEmpty()) {
            Object suppressableValue = _suppressableValue;
            if (suppressableValue == JsonInclude.Include.ALWAYS) {
                suppressableValue = null;
            } else if (suppressableValue == null) {
                if (!provider.isEnabled(SerializationFeature.WRITE_NULL_MAP_VALUES)) {
                    suppressableValue = JsonInclude.Include.NON_NULL;
                }
            }
            if (_sortKeys || provider.isEnabled(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS)) {
                value = _orderEntries(value, gen, provider, suppressableValue);
            }
            PropertyFilter pf;
            if ((_filterId != null) && (pf = findPropertyFilter(provider, _filterId, value)) != null) {
                serializeFilteredFields(value, gen, provider, pf, suppressableValue);
            } else if (suppressableValue != null) {
                serializeOptionalFields(value, gen, provider, suppressableValue);
            } else if (_valueSerializer != null) {
                serializeFieldsUsing(value, gen, provider, _valueSerializer);
            } else {
                serializeFields(value, gen, provider);
            }
        }
        gen.writeEndObject();
    }

    @Override
    public void serializeWithType(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            TypeSerializer typeSer)
        throws IOException
    {
        typeSer.writeTypePrefixForObject(value, gen);
        // [databind#631]: Assign current value, to be accessible by custom serializers
        gen.setCurrentValue(value);
        if (!value.isEmpty()) {
            Object suppressableValue = _suppressableValue;
            if (suppressableValue == JsonInclude.Include.ALWAYS) {
                suppressableValue = null;
            } else if (suppressableValue == null) {
                if (!provider.isEnabled(SerializationFeature.WRITE_NULL_MAP_VALUES)) {
                    suppressableValue = JsonInclude.Include.NON_NULL;
                }
            }
            if (_sortKeys || provider.isEnabled(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS)) {
                value = _orderEntries(value, gen, provider, suppressableValue);
            }
            PropertyFilter pf;
            if ((_filterId != null) && (pf = findPropertyFilter(provider, _filterId, value)) != null) {
                serializeFilteredFields(value, gen, provider, pf, suppressableValue);
            } else if (suppressableValue != null) {
                serializeOptionalFields(value, gen, provider, suppressableValue);
            } else if (_valueSerializer != null) {
                serializeFieldsUsing(value, gen, provider, _valueSerializer);
            } else {
                serializeFields(value, gen, provider);
            }
        }
        typeSer.writeTypeSuffixForObject(value, gen);
    }

    /*
    /**********************************************************
    /* Secondary serialization methods
    /**********************************************************
     */
    
    /**
     * General-purpose serialization for contents, where we do not necessarily know
     * the value serialization, but 
     * we do know that no value suppression is needed (which simplifies processing a bit)
     */
    public void serializeFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider)
        throws IOException
    {
        // If value type needs polymorphic type handling, some more work needed:
        if (_valueTypeSerializer != null) {
            serializeTypedFields(value, gen, provider, null);
            return;
        }
        final JsonSerializer<Object> keySerializer = _keySerializer;
        final Set<String> ignored = _ignoredEntries;

        PropertySerializerMap serializers = _dynamicValueSerializers;

        for (Map.Entry<?,?> entry : value.entrySet()) {
            Object valueElem = entry.getValue();
            // First, serialize key
            Object keyElem = entry.getKey();

            if (keyElem == null) {
                provider.findNullKeySerializer(_keyType, _property).serialize(null, gen, provider);
            } else {
                // One twist: is entry ignorable? If so, skip
                if ((ignored != null) && ignored.contains(keyElem)) continue;
                keySerializer.serialize(keyElem, gen, provider);
            }

            // And then value
            if (valueElem == null) {
                provider.defaultSerializeNull(gen);
                continue;
            }
            JsonSerializer<Object> serializer = _valueSerializer;
            if (serializer == null) {
                Class<?> cc = valueElem.getClass();
                serializer = serializers.serializerFor(cc);
                if (serializer == null) {
                    if (_valueType.hasGenericTypes()) {
                        serializer = _findAndAddDynamic(serializers,
                                provider.constructSpecializedType(_valueType, cc), provider);
                    } else {
                        serializer = _findAndAddDynamic(serializers, cc, provider);
                    }
                    serializers = _dynamicValueSerializers;
                }
            }
            try {
                serializer.serialize(valueElem, gen, provider);
            } catch (Exception e) {
                // Add reference information
                String keyDesc = ""+keyElem;
                wrapAndThrow(provider, e, value, keyDesc);
            }
        }
    }

    /**
     * Serialization method called when exclusion filtering needs to be applied.
     */
    public void serializeOptionalFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            Object suppressableValue)
        throws IOException
    {
        // If value type needs polymorphic type handling, some more work needed:
        if (_valueTypeSerializer != null) {
            serializeTypedFields(value, gen, provider, suppressableValue);
            return;
        }
        final Set<String> ignored = _ignoredEntries;
        PropertySerializerMap serializers = _dynamicValueSerializers;

        for (Map.Entry<?,?> entry : value.entrySet()) {
            // First find key serializer
            final Object keyElem = entry.getKey();
            JsonSerializer<Object> keySerializer;
            if (keyElem == null) {
                keySerializer = provider.findNullKeySerializer(_keyType, _property);
            } else {
                if (ignored != null && ignored.contains(keyElem)) continue;
                keySerializer = _keySerializer;
            }

            // Then value serializer
            final Object valueElem = entry.getValue();
            JsonSerializer<Object> valueSer;
            if (valueElem == null) {
                if (suppressableValue != null) { // all suppressions include null-suppression
                    continue;
                }
                valueSer = provider.getDefaultNullValueSerializer();
            } else {
                valueSer = _valueSerializer;
                if (valueSer == null) {
                    Class<?> cc = valueElem.getClass();
                    valueSer = serializers.serializerFor(cc);
                    if (valueSer == null) {
                        if (_valueType.hasGenericTypes()) {
                            valueSer = _findAndAddDynamic(serializers,
                                    provider.constructSpecializedType(_valueType, cc), provider);
                        } else {
                            valueSer = _findAndAddDynamic(serializers, cc, provider);
                        }
                        serializers = _dynamicValueSerializers;
                    }
                }
                // also may need to skip non-empty values:
                if ((suppressableValue == JsonInclude.Include.NON_EMPTY)
                        && valueSer.isEmpty(provider, valueElem)) {
                    continue;
                }
            }
            // and then serialize, if all went well
            try {
                keySerializer.serialize(keyElem, gen, provider);
                valueSer.serialize(valueElem, gen, provider);
            } catch (Exception e) {
                String keyDesc = ""+keyElem;
                wrapAndThrow(provider, e, value, keyDesc);
            }
        }
    }
    
    /**
     * Method called to serialize fields, when the value type is statically known,
     * so that value serializer is passed and does not need to be fetched from
     * provider.
     */
    public void serializeFieldsUsing(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            JsonSerializer<Object> ser)
        throws IOException
    {
        final JsonSerializer<Object> keySerializer = _keySerializer;
        final Set<String> ignored = _ignoredEntries;
        final TypeSerializer typeSer = _valueTypeSerializer;

        for (Map.Entry<?,?> entry : value.entrySet()) {
            Object keyElem = entry.getKey();
            if (ignored != null && ignored.contains(keyElem)) continue;

            if (keyElem == null) {
                provider.findNullKeySerializer(_keyType, _property).serialize(null, gen, provider);
            } else {
                keySerializer.serialize(keyElem, gen, provider);
            }
            final Object valueElem = entry.getValue();
            if (valueElem == null) {
                provider.defaultSerializeNull(gen);
            } else {
                try {
                    if (typeSer == null) {
                        ser.serialize(valueElem, gen, provider);
                    } else {
                        ser.serializeWithType(valueElem, gen, provider, typeSer);
                    }
                } catch (Exception e) {
                    String keyDesc = ""+keyElem;
                    wrapAndThrow(provider, e, value, keyDesc);
                }
            }
        }
    }

    /**
     * Helper method used when we have a JSON Filter to use for potentially
     * filtering out Map entries.
     * 
     * @since 2.5
     */
    public void serializeFilteredFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            PropertyFilter filter,
            Object suppressableValue) // since 2.5
        throws IOException
    {
        final Set<String> ignored = _ignoredEntries;

        PropertySerializerMap serializers = _dynamicValueSerializers;
        final MapProperty prop = new MapProperty(_valueTypeSerializer, _property);
        
        for (Map.Entry<?,?> entry : value.entrySet()) {
            // First, serialize key; unless ignorable by key
            final Object keyElem = entry.getKey();
            if (ignored != null && ignored.contains(keyElem)) continue;

            JsonSerializer<Object> keySerializer;
            if (keyElem == null) {
                keySerializer = provider.findNullKeySerializer(_keyType, _property);
            } else {
                keySerializer = _keySerializer;
            }
            // or by value; nulls often suppressed
            final Object valueElem = entry.getValue();

            JsonSerializer<Object> valueSer;
            // And then value
            if (valueElem == null) {
                if (suppressableValue != null) { // all suppressions include null-suppression
                    continue;
                }
                valueSer = provider.getDefaultNullValueSerializer();
            } else {
                valueSer = _valueSerializer;
                if (valueSer == null) {
                    Class<?> cc = valueElem.getClass();
                    valueSer = serializers.serializerFor(cc);
                    if (valueSer == null) {
                        if (_valueType.hasGenericTypes()) {
                            valueSer = _findAndAddDynamic(serializers,
                                    provider.constructSpecializedType(_valueType, cc), provider);
                        } else {
                            valueSer = _findAndAddDynamic(serializers, cc, provider);
                        }
                        serializers = _dynamicValueSerializers;
                    }
                }
                // also may need to skip non-empty values:
                if ((suppressableValue == JsonInclude.Include.NON_EMPTY)
                        && valueSer.isEmpty(provider, valueElem)) {
                    continue;
                }
            }
            // and with that, ask filter to handle it
            prop.reset(keyElem, keySerializer, valueSer);
            try {
                filter.serializeAsField(valueElem, gen, provider, prop);
            } catch (Exception e) {
                String keyDesc = ""+keyElem;
                wrapAndThrow(provider, e, value, keyDesc);
            }
        }
    }

    @Deprecated // since 2.5
    public void serializeFilteredFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            PropertyFilter filter) throws IOException {
        serializeFilteredFields(value, gen, provider, filter,
                provider.isEnabled(SerializationFeature.WRITE_NULL_MAP_VALUES) ? null : JsonInclude.Include.NON_NULL);
    }
    
    /**
     * @since 2.5
     */
    public void serializeTypedFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider,
            Object suppressableValue) // since 2.5
        throws IOException
    {
        final Set<String> ignored = _ignoredEntries;
        PropertySerializerMap serializers = _dynamicValueSerializers;

        for (Map.Entry<?,?> entry : value.entrySet()) {
            Object keyElem = entry.getKey();
            JsonSerializer<Object> keySerializer;
            if (keyElem == null) {
                keySerializer = provider.findNullKeySerializer(_keyType, _property);
            } else {
                // One twist: is entry ignorable? If so, skip
                if (ignored != null && ignored.contains(keyElem)) continue;
                keySerializer = _keySerializer;
            }
            final Object valueElem = entry.getValue();
    
            // And then value
            JsonSerializer<Object> valueSer;
            if (valueElem == null) {
                if (suppressableValue != null) { // all suppression include null suppression
                    continue;
                }
                valueSer = provider.getDefaultNullValueSerializer();
            } else {
                valueSer = _valueSerializer;
                Class<?> cc = valueElem.getClass();
                valueSer = serializers.serializerFor(cc);
                if (valueSer == null) {
                    if (_valueType.hasGenericTypes()) {
                        valueSer = _findAndAddDynamic(serializers,
                                provider.constructSpecializedType(_valueType, cc), provider);
                    } else {
                        valueSer = _findAndAddDynamic(serializers, cc, provider);
                    }
                    serializers = _dynamicValueSerializers;
                }
                // also may need to skip non-empty values:
                if ((suppressableValue == JsonInclude.Include.NON_EMPTY)
                        && valueSer.isEmpty(provider, valueElem)) {
                    continue;
                }
            }
            keySerializer.serialize(keyElem, gen, provider);
            try {
                valueSer.serializeWithType(valueElem, gen, provider, _valueTypeSerializer);
            } catch (Exception e) {
                String keyDesc = ""+keyElem;
                wrapAndThrow(provider, e, value, keyDesc);
            }
        }
    }

    @Deprecated // since 2.5
    protected void serializeTypedFields(Map<?,?> value, JsonGenerator gen, SerializerProvider provider)
        throws IOException {
        serializeTypedFields(value, gen, provider,
                provider.isEnabled(SerializationFeature.WRITE_NULL_MAP_VALUES) ? null : JsonInclude.Include.NON_NULL);
    }

    /*
    /**********************************************************
    /* Schema related functionality
    /**********************************************************
     */
    
    @Override
    public JsonNode getSchema(SerializerProvider provider, Type typeHint)
    {
        //(ryan) even though it's possible to statically determine the "value" type of the map,
        // there's no way to statically determine the keys, so the "Entries" can't be determined.
        return createSchemaNode("object", true);
    }

    @Override
    public void acceptJsonFormatVisitor(JsonFormatVisitorWrapper visitor, JavaType typeHint)
        throws JsonMappingException
    {
        JsonMapFormatVisitor v2 = (visitor == null) ? null : visitor.expectMapFormat(typeHint);        
        if (v2 != null) {
            v2.keyFormat(_keySerializer, _keyType);
            JsonSerializer<?> valueSer = _valueSerializer;
            if (valueSer == null) {
                valueSer = _findAndAddDynamic(_dynamicValueSerializers,
                            _valueType, visitor.getProvider());
            }
            v2.valueFormat(valueSer, _valueType);
        }
    }

    /*
    /**********************************************************
    /* Internal helper methods
    /**********************************************************
     */
    
    protected final JsonSerializer<Object> _findAndAddDynamic(PropertySerializerMap map,
            Class<?> type, SerializerProvider provider) throws JsonMappingException
    {
        PropertySerializerMap.SerializerAndMapResult result = map.findAndAddSecondarySerializer(type, provider, _property);
        // did we get a new map of serializers? If so, start using it
        if (map != result.map) {
            _dynamicValueSerializers = result.map;
        }
        return result.serializer;
    }

    protected final JsonSerializer<Object> _findAndAddDynamic(PropertySerializerMap map,
            JavaType type, SerializerProvider provider) throws JsonMappingException
    {
        PropertySerializerMap.SerializerAndMapResult result = map.findAndAddSecondarySerializer(type, provider, _property);
        if (map != result.map) {
            _dynamicValueSerializers = result.map;
        }
        return result.serializer;
    }

    protected Map<?,?> _orderEntries(Map<?,?> input, JsonGenerator gen,
            SerializerProvider provider, Object suppressableValue) throws IOException
    {
        // minor optimization: may already be sorted?
        if (input instanceof SortedMap<?,?>) {
            return input;
        }
        // [databind#1411]: TreeMap does not like null key... (although note that
        //   check above should prevent this code from being called in that case)
        if (input.containsKey(null)) {
            TreeMap<Object,Object> result = new TreeMap<Object,Object>();
            for (Map.Entry<?,?> entry : input.entrySet()) {
                Object key = entry.getKey();
                if (key == null) {
                    _writeNullKeyedEntry(gen, provider, suppressableValue, entry.getValue());
                    continue;
                } 
                result.put(key, entry.getValue());
            }
            return result;
        }
        return new TreeMap<Object,Object>(input);
    }

    protected void _writeNullKeyedEntry(JsonGenerator gen, SerializerProvider provider,
            Object suppressableValue, Object value) throws IOException
    {
        JsonSerializer<Object> keySerializer = provider.findNullKeySerializer(_keyType, _property);
        JsonSerializer<Object> valueSer;
        if (value == null) {
            if (suppressableValue != null) { // all suppressions include null-suppression
                return;
            }
            valueSer = provider.getDefaultNullValueSerializer();
        } else {
            valueSer = _valueSerializer;
            if (valueSer == null) {
                Class<?> cc = value.getClass();
                valueSer = _dynamicValueSerializers.serializerFor(cc);
                if (valueSer == null) {
                    if (_valueType.hasGenericTypes()) {
                        valueSer = _findAndAddDynamic(_dynamicValueSerializers,
                                provider.constructSpecializedType(_valueType, cc), provider);
                    } else {
                        valueSer = _findAndAddDynamic(_dynamicValueSerializers, cc, provider);
                    }
                }
            }
            // also may need to skip non-empty values:
            if ((suppressableValue == JsonInclude.Include.NON_EMPTY)
                    && valueSer.isEmpty(provider, value)) {
                return;
            }
        }
        // and then serialize, if all went well
        try {
            keySerializer.serialize(null, gen, provider);
            valueSer.serialize(value, gen, provider);
        } catch (Exception e) {
            String keyDesc = "";
            wrapAndThrow(provider, e, value, keyDesc);
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.ser.TestMapSerialization

## Test line
com.fasterxml.jackson.databind.JsonMappingException

## Error
[no message for java.lang.NullPointerException]

## Error Code Block
```java
package com.fasterxml.jackson.databind.ser;

import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentSkipListMap;

import com.fasterxml.jackson.annotation.*;
import com.fasterxml.jackson.annotation.JsonTypeInfo.Id;
import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.*;
import com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

@SuppressWarnings("serial")
public class TestMapSerialization extends BaseMapTest
{
    @JsonSerialize(using=MapSerializer.class)    
    static class PseudoMap extends LinkedHashMap<String,String>
    {
        public PseudoMap(String... values) {
            for (int i = 0, len = values.length; i < len; i += 2) {
                put(values[i], values[i+1]);
            }
        }
    }

    static class MapSerializer extends JsonSerializer<Map<String,String>>
    {
        @Override
        public void serialize(Map<String,String> value,
                JsonGenerator gen, SerializerProvider provider) throws IOException
        {
            // just use standard Map.toString(), output as JSON String
            gen.writeString(value.toString());
        }
    }

    // For [JACKSON-574]
    static class DefaultKeySerializer extends JsonSerializer<Object>
    {
        @Override
        public void serialize(Object value, JsonGenerator jgen, SerializerProvider provider) throws IOException
        {
            jgen.writeFieldName("DEFAULT:"+value);
        }
    }
    
    // [databind#335]
    static class MapOrderingBean {
        @JsonPropertyOrder(alphabetic=true)
        public LinkedHashMap<String,Integer> map;
        
        public MapOrderingBean(String... keys) {
            map = new LinkedHashMap<String,Integer>();
            int ix = 1;
            for (String key : keys) {
                map.put(key, ix++);
            }
        }
    }

    // [databind#565]: Support ser/deser of Map.Entry
    static class StringIntMapEntry implements Map.Entry<String,Integer> {
        public final String k;
        public final Integer v;
        public StringIntMapEntry(String k, Integer v) {
            this.k = k;
            this.v = v;
        }

        @Override
        public String getKey() {
            return k;
        }

        @Override
        public Integer getValue() {
            return v;
        }

        @Override
        public Integer setValue(Integer value) {
            throw new UnsupportedOperationException();
        }
    }

    static class StringIntMapEntryWrapper {
        public StringIntMapEntry value;

        public StringIntMapEntryWrapper(String k, Integer v) {
            value = new StringIntMapEntry(k, v);
        }
    }

    // for [databind#47]
    public static class Wat
    {
        private final String wat;

        @JsonCreator
        Wat(String wat) {
            this.wat = wat;
        }

        @JsonValue
        public String getWat() {
            return wat;
        }

        @Override
        public String toString() {
            return "(String)[Wat: " + wat + "]";
        }
    }

    static class WatMap extends HashMap<Wat,Boolean> { }

    // for [databind#691]
    @JsonTypeInfo(use=JsonTypeInfo.Id.NAME)
    @JsonTypeName("mymap")
    static class MapWithTypedValues extends LinkedHashMap<String,String> { }

    @JsonTypeInfo(use = Id.CLASS)
    public static class Mixin691 { }

    /*
    /**********************************************************
    /* Test methods
    /**********************************************************
     */

    final private ObjectMapper MAPPER = objectMapper();

    public void testUsingObjectWriter() throws IOException
    {
        ObjectWriter w = MAPPER.writerFor(Object.class);
        Map<String,Object> map = new LinkedHashMap<String,Object>();
        map.put("a", 1);
        String json = w.writeValueAsString(map);
        assertEquals(aposToQuotes("{'a':1}"), json);
    }

    public void testMapSerializer() throws IOException
    {
        assertEquals("\"{a=b, c=d}\"", MAPPER.writeValueAsString(new PseudoMap("a", "b", "c", "d")));
    }

    // problems with map entries, values
    public void testMapKeyValueSerialization() throws IOException
    {
        Map<String,String> map = new HashMap<String,String>();
        map.put("a", "b");
        assertEquals("[\"a\"]", MAPPER.writeValueAsString(map.keySet()));
        assertEquals("[\"b\"]", MAPPER.writeValueAsString(map.values()));

        // TreeMap has similar inner class(es):
        map = new TreeMap<String,String>();
        map.put("c", "d");
        assertEquals("[\"c\"]", MAPPER.writeValueAsString(map.keySet()));
        assertEquals("[\"d\"]", MAPPER.writeValueAsString(map.values()));

        // and for [JACKSON-533], same for concurrent maps
        map = new ConcurrentHashMap<String,String>();
        map.put("e", "f");
        assertEquals("[\"e\"]", MAPPER.writeValueAsString(map.keySet()));
        assertEquals("[\"f\"]", MAPPER.writeValueAsString(map.values()));
    }

    // For [JACKSON-574]
    public void testDefaultKeySerializer() throws IOException
    {
        ObjectMapper m = new ObjectMapper();
        m.getSerializerProvider().setDefaultKeySerializer(new DefaultKeySerializer());
        Map<String,String> map = new HashMap<String,String>();
        map.put("a", "b");
        assertEquals("{\"DEFAULT:a\":\"b\"}", m.writeValueAsString(map));
    }

    // sort Map entries by key
    public void testOrderByKey() throws IOException
    {
        ObjectMapper m = new ObjectMapper();
        assertFalse(m.isEnabled(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS));
        LinkedHashMap<String,Integer> map = new LinkedHashMap<String,Integer>();
        map.put("b", 3);
        map.put("a", 6);
        // by default, no (re)ordering:
        assertEquals("{\"b\":3,\"a\":6}", m.writeValueAsString(map));
        // but can be changed
        ObjectWriter sortingW =  m.writer(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS);
        assertEquals("{\"a\":6,\"b\":3}", sortingW.writeValueAsString(map));
    }

    // related to [databind#1411]
    public void testOrderByWithNulls() throws IOException
    {
        ObjectWriter sortingW = MAPPER.writer(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS);
        // 16-Oct-2016, tatu: but mind the null key, if any
        Map<String,Integer> mapWithNullKey = new LinkedHashMap<String,Integer>();
        mapWithNullKey.put(null, 1);
        mapWithNullKey.put("b", 2);
        // 16-Oct-2016, tatu: By default, null keys are not accepted...
        try {
            /*String json =*/ sortingW.writeValueAsString(mapWithNullKey);
            //assertEquals(aposToQuotes("{'':1,'b':2}"), json);
        } catch (JsonMappingException e) {
            verifyException(e, "Null key for a Map not allowed");
        }
    }

    // [Databind#335]
    public void testOrderByKeyViaProperty() throws IOException
    {
        MapOrderingBean input = new MapOrderingBean("c", "b", "a");
        String json = MAPPER.writeValueAsString(input);
        assertEquals(aposToQuotes("{'map':{'a':3,'b':2,'c':1}}"), json);
    }        

    // [Databind#565]
    public void testMapEntry() throws IOException
    {
        StringIntMapEntry input = new StringIntMapEntry("answer", 42);
        String json = MAPPER.writeValueAsString(input);
        assertEquals(aposToQuotes("{'answer':42}"), json);

        StringIntMapEntry[] array = new StringIntMapEntry[] { input };
        json = MAPPER.writeValueAsString(array);
        assertEquals(aposToQuotes("[{'answer':42}]"), json);

        // and maybe with bit of extra typing?
        ObjectMapper mapper = new ObjectMapper().enableDefaultTyping(DefaultTyping.NON_FINAL);
        json = mapper.writeValueAsString(input);
        assertEquals(aposToQuotes("['"+StringIntMapEntry.class.getName()+"',{'answer':42}]"),
                json);
    }        

    public void testMapEntryWrapper() throws IOException
    {
        StringIntMapEntryWrapper input = new StringIntMapEntryWrapper("answer", 42);
        String json = MAPPER.writeValueAsString(input);
        assertEquals(aposToQuotes("{'value':{'answer':42}}"), json);
    }

    // [databind#47]
    public void testMapJsonValueKey47() throws Exception
    {
        WatMap input = new WatMap();
        input.put(new Wat("3"), true);

        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(input);
        assertEquals(aposToQuotes("{'3':true}"), json);
    }    

    // [databind#682]
    public void testClassKey() throws IOException
    {
        Map<Class<?>,Integer> map = new LinkedHashMap<Class<?>,Integer>();
        map.put(String.class, 2);
        String json = MAPPER.writeValueAsString(map);
        assertEquals(aposToQuotes("{'java.lang.String':2}"), json);
    }

    // [databind#691]
    public void testNullJsonMapping691() throws Exception
    {
        MapWithTypedValues input = new MapWithTypedValues();
        input.put("id", "Test");
        input.put("NULL", null);

        String json = MAPPER.writeValueAsString(input);

        assertEquals(aposToQuotes("{'@type':'mymap','id':'Test','NULL':null}"),
                json);
    }    

    // [databind#691]
    public void testNullJsonInTypedMap691() throws Exception {
        Map<String, String> map = new HashMap<String, String>();
        map.put("NULL", null);
    
        ObjectMapper mapper = new ObjectMapper();
        mapper.addMixIn(Object.class, Mixin691.class);
        String json = mapper.writeValueAsString(map);
        assertEquals("{\"@class\":\"java.util.HashMap\",\"NULL\":null}", json);
    }

    // [databind#1513]
    public void testConcurrentMaps() throws Exception
    {
        final ObjectWriter w = MAPPER.writer(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS);

        Map<String,String> input = new ConcurrentSkipListMap<String,String>();
        input.put("x", "y");
        input.put("a", "b");
        String json = w.writeValueAsString(input);
        assertEquals(aposToQuotes("{'a':'b','x':'y'}"), json);

        input = new ConcurrentHashMap<String,String>();
        input.put("x", "y");
        input.put("a", "b");
        json = w.writeValueAsString(input);
        assertEquals(aposToQuotes("{'a':'b','x':'y'}"), json);

        // One more: while not technically concurrent map at all, exhibits same issue
        input = new Hashtable<String,String>();
        input.put("x", "y");
        input.put("a", "b");
        json = w.writeValueAsString(input);
        assertEquals(aposToQuotes("{'a':'b','x':'y'}"), json);
    }
}

```
