## Buggy code
```java
public class JacksonAnnotationIntrospector
    extends AnnotationIntrospector
    implements java.io.Serializable
{
    private static final long serialVersionUID = 1L;

    @SuppressWarnings("unchecked")
    private final static Class<? extends Annotation>[] ANNOTATIONS_TO_INFER_SER = (Class<? extends Annotation>[])
            new Class<?>[] {
        JsonSerialize.class,
        JsonView.class,
        JsonFormat.class,
        JsonTypeInfo.class,
        JsonRawValue.class,
        JsonUnwrapped.class,
        JsonBackReference.class,
        JsonManagedReference.class
    };

    @SuppressWarnings("unchecked")
    private final static Class<? extends Annotation>[] ANNOTATIONS_TO_INFER_DESER = (Class<? extends Annotation>[])
            new Class<?>[] {
        JsonDeserialize.class,
        JsonView.class,
        JsonFormat.class,
        JsonTypeInfo.class,
        JsonUnwrapped.class,
        JsonBackReference.class,
        JsonManagedReference.class,
        JsonMerge.class // since 2.9
    };

    // NOTE: loading of Java7 dependencies is encapsulated by handlers in Java7Support,
    //  here we do not really need any handling; but for extra-safety use try-catch
    private static final Java7Support _java7Helper;
    static {
        Java7Support x = null;
        try {
            x = Java7Support.instance();
        } catch (Throwable t) { }
        _java7Helper = x;
    }
    
    /**
     * Since introspection of annotation types is a performance issue in some
     * use cases (rare, but do exist), let's try a simple cache to reduce
     * need for actual meta-annotation introspection.
     *<p>
     * Non-final only because it needs to be re-created after deserialization.
     *
     * @since 2.7
     */
    protected transient LRUMap<Class<?>,Boolean> _annotationsInside = new LRUMap<Class<?>,Boolean>(48, 48);

    /*
    /**********************************************************
    /* Local configuration settings
    /**********************************************************
     */

    /**
     * See {@link #setConstructorPropertiesImpliesCreator(boolean)} for
     * explanation.
     *<p>
     * Defaults to true.
     * 
     * @since 2.7.4
     */
    protected boolean _cfgConstructorPropertiesImpliesCreator = true;

    /*
    /**********************************************************
    /* Life-cycle
    /**********************************************************
     */

    public JacksonAnnotationIntrospector() { }

    @Override
    public Version version() {
        return com.fasterxml.jackson.databind.cfg.PackageVersion.VERSION;
    }

    protected Object readResolve() {
        if (_annotationsInside == null) {
            _annotationsInside = new LRUMap<Class<?>,Boolean>(48, 48);
        }
        return this;
    }

    /*
    /**********************************************************
    /* Configuration
    /**********************************************************
     */

    /**
     * Method for changing behavior of {@link java.beans.ConstructorProperties}:
     * if set to `true`, existence DOES indicate that the given constructor should
     * be considered a creator; `false` that it should NOT be considered a creator
     * without explicit use of <code>JsonCreator</code> annotation.
     *<p>
     * Default setting is `true`
     *
     * @since 2.7.4
     */
    public JacksonAnnotationIntrospector setConstructorPropertiesImpliesCreator(boolean b)
    {
        _cfgConstructorPropertiesImpliesCreator = b;
        return this;
    }
    
    /*
    /**********************************************************
    /* General annotation properties
    /**********************************************************
     */

    /**
     * Annotations with meta-annotation {@link JacksonAnnotationsInside}
     * are considered bundles.
     */
    @Override
    public boolean isAnnotationBundle(Annotation ann) {
        // 22-Sep-2015, tatu: Caching here has modest effect on JavaSE, and only
        //   mostly in degenerate cases where introspection used more often than
        //   it should (like recreating ObjectMapper once per read/write).
        //   But it may be more beneficial on platforms like Android (should verify)
        Class<?> type = ann.annotationType();
        Boolean b = _annotationsInside.get(type);
        if (b == null) {
            b = type.getAnnotation(JacksonAnnotationsInside.class) != null;
            _annotationsInside.putIfAbsent(type, b);
        }
        return b.booleanValue();
    }

    /*
    /**********************************************************
    /* General annotations
    /**********************************************************
     */

    /**
     * Since 2.6, we have supported use of {@link JsonProperty} for specifying
     * explicit serialized name
     */
    @Override
    @Deprecated // since 2.8
    public String findEnumValue(Enum<?> value)
    {
        // 11-Jun-2015, tatu: As per [databind#677], need to allow explicit naming.
        //   Unfortunately can not quite use standard AnnotatedClass here (due to various
        //   reasons, including odd representation JVM uses); has to do for now
        try {
            // We know that values are actually static fields with matching name so:
            Field f = value.getClass().getField(value.name());
            if (f != null) {
                JsonProperty prop = f.getAnnotation(JsonProperty.class);
                if (prop != null) {
                    String n = prop.value();
                    if (n != null && !n.isEmpty()) {
                        return n;
                    }
                }
            }
        } catch (SecurityException e) {
            // 17-Sep-2015, tatu: Anything we could/should do here?
        } catch (NoSuchFieldException e) {
            // 17-Sep-2015, tatu: should not really happen. But... can we do anything?
        }
        return value.name();
    }

    @Override // since 2.7
    public String[] findEnumValues(Class<?> enumType, Enum<?>[] enumValues, String[] names) {
        HashMap<String,String> expl = null;
        for (Field f : ClassUtil.getDeclaredFields(enumType)) {
            if (!f.isEnumConstant()) {
                continue;
            }
            JsonProperty prop = f.getAnnotation(JsonProperty.class);
            if (prop == null) {
                continue;
            }
            String n = prop.value();
            if (n.isEmpty()) {
                continue;
            }
            if (expl == null) {
                expl = new HashMap<String,String>();
            }
            expl.put(f.getName(), n);
        }
        // and then stitch them together if and as necessary
        if (expl != null) {
            for (int i = 0, end = enumValues.length; i < end; ++i) {
                String defName = enumValues[i].name();
                String explValue = expl.get(defName);
                if (explValue != null) {
                    names[i] = explValue;
                }
            }
        }
        return names;
    }

    /**
     * Finds the Enum value that should be considered the default value, if possible.
     * <p>
     * This implementation relies on {@link JsonEnumDefaultValue} annotation to determine the default value if present.
     *
     * @param enumCls The Enum class to scan for the default value.
     * @return null if none found or it's not possible to determine one.
     * @since 2.8
     */
    @Override
    public Enum<?> findDefaultEnumValue(Class<Enum<?>> enumCls) {
        return ClassUtil.findFirstAnnotatedEnumValue(enumCls, JsonEnumDefaultValue.class);
    }

    /*
    /**********************************************************
    /* General class annotations
    /**********************************************************
     */

    @Override
    public PropertyName findRootName(AnnotatedClass ac)
    {
        JsonRootName ann = _findAnnotation(ac, JsonRootName.class);
        if (ann == null) {
            return null;
        }
        String ns = ann.namespace();
        if (ns != null && ns.length() == 0) {
            ns = null;
        }
        return PropertyName.construct(ann.value(), ns);
    }

    @Override // since 2.8
    public JsonIgnoreProperties.Value findPropertyIgnorals(Annotated a)
    {
        JsonIgnoreProperties v = _findAnnotation(a, JsonIgnoreProperties.class);
        if (v == null) {
            return JsonIgnoreProperties.Value.empty();
        }
        return JsonIgnoreProperties.Value.from(v);
    }

    @Override
    public Boolean isIgnorableType(AnnotatedClass ac) {
        JsonIgnoreType ignore = _findAnnotation(ac, JsonIgnoreType.class);
        return (ignore == null) ? null : ignore.value();
    }
 
    @Override
    public Object findFilterId(Annotated a) {
        JsonFilter ann = _findAnnotation(a, JsonFilter.class);
        if (ann != null) {
            String id = ann.value();
            // Empty String is same as not having annotation, to allow overrides
            if (id.length() > 0) {
                return id;
            }
        }
        return null;
    }

    @Override
    public Object findNamingStrategy(AnnotatedClass ac)
    {
        JsonNaming ann = _findAnnotation(ac, JsonNaming.class);
        return (ann == null) ? null : ann.value();
    }

    @Override
    public String findClassDescription(AnnotatedClass ac) {
        JsonClassDescription ann = _findAnnotation(ac, JsonClassDescription.class);
        return (ann == null) ? null : ann.value();
    }

    /*
    /**********************************************************
    /* Property auto-detection
    /**********************************************************
     */

    @Override
    public VisibilityChecker<?> findAutoDetectVisibility(AnnotatedClass ac,
        VisibilityChecker<?> checker)
    {
        JsonAutoDetect ann = _findAnnotation(ac, JsonAutoDetect.class);
        return (ann == null) ? checker : checker.with(ann);
    }

    /*
    /**********************************************************
    /* General member (field, method/constructor) annotations
    /**********************************************************
     */

    @Override
    public String findImplicitPropertyName(AnnotatedMember m) {
        PropertyName n = _findConstructorName(m);
        return (n == null) ? null : n.getSimpleName();
    }

    @Override
    public List<PropertyName> findPropertyAliases(Annotated m) {
        JsonAlias ann = _findAnnotation(m, JsonAlias.class);
        if (ann == null) {
            return null;
        }
        String[] strs = ann.value();
        final int len = strs.length;
        if (len == 0) {
            return Collections.emptyList();
        }
        List<PropertyName> result = new ArrayList<>(len);
        for (int i = 0; i < len; ++i) {
            result.add(PropertyName.construct(strs[i]));
        }
        return result;
    }

    @Override
    public boolean hasIgnoreMarker(AnnotatedMember m) {
        return _isIgnorable(m);
    }

    @Override
    public Boolean hasRequiredMarker(AnnotatedMember m)
    {
        JsonProperty ann = _findAnnotation(m, JsonProperty.class);
        if (ann != null) {
            return ann.required();
        }
        return null;
    }

    @Override
    public JsonProperty.Access findPropertyAccess(Annotated m) {
        JsonProperty ann = _findAnnotation(m, JsonProperty.class);
        if (ann != null) {
            return ann.access();
        }
        return null;
    }

    @Override
    public String findPropertyDescription(Annotated ann) {
        JsonPropertyDescription desc = _findAnnotation(ann, JsonPropertyDescription.class);
        return (desc == null) ? null : desc.value();
    }

    @Override
    public Integer findPropertyIndex(Annotated ann) {
        JsonProperty prop = _findAnnotation(ann, JsonProperty.class);
        if (prop != null) {
          int ix = prop.index();
          if (ix != JsonProperty.INDEX_UNKNOWN) {
               return Integer.valueOf(ix);
          }
        }
        return null;
    }
    
    @Override
    public String findPropertyDefaultValue(Annotated ann) {
        JsonProperty prop = _findAnnotation(ann, JsonProperty.class);
        if (prop == null) {
            return null;
        }
        String str = prop.defaultValue();
        // Since annotations do not allow nulls, need to assume empty means "none"
        return str.isEmpty() ? null : str;
    }
    
    @Override
    public JsonFormat.Value findFormat(Annotated ann) {
        JsonFormat f = _findAnnotation(ann, JsonFormat.class);
        return (f == null)  ? null : new JsonFormat.Value(f);
    }

    @Override        
    public ReferenceProperty findReferenceType(AnnotatedMember member)
    {
        JsonManagedReference ref1 = _findAnnotation(member, JsonManagedReference.class);
        if (ref1 != null) {
            return AnnotationIntrospector.ReferenceProperty.managed(ref1.value());
        }
        JsonBackReference ref2 = _findAnnotation(member, JsonBackReference.class);
        if (ref2 != null) {
            return AnnotationIntrospector.ReferenceProperty.back(ref2.value());
        }
        return null;
    }

    @Override
    public NameTransformer findUnwrappingNameTransformer(AnnotatedMember member)
    {
        JsonUnwrapped ann = _findAnnotation(member, JsonUnwrapped.class);
        // if not enabled, just means annotation is not enabled; not necessarily
        // that unwrapping should not be done (relevant when using chained introspectors)
        if (ann == null || !ann.enabled()) {
            return null;
        }
        String prefix = ann.prefix();
        String suffix = ann.suffix();
        return NameTransformer.simpleTransformer(prefix, suffix);
    }

    @Override // since 2.9
    public JacksonInject.Value findInjectableValue(AnnotatedMember m) {
        JacksonInject ann = _findAnnotation(m, JacksonInject.class);
        if (ann == null) {
            return null;
        }
        // Empty String means that we should use name of declared value class.
        JacksonInject.Value v = JacksonInject.Value.from(ann);
        if (!v.hasId()) {
            Object id;
            // slight complication; for setters, type 
            if (!(m instanceof AnnotatedMethod)) {
                id = m.getRawType().getName();
            } else {
                AnnotatedMethod am = (AnnotatedMethod) m;
                if (am.getParameterCount() == 0) { // getter
                    id = m.getRawType().getName();
                } else { // setter
                    id = am.getRawParameterType(0).getName();
                }
            }
            v = v.withId(id);
        }
        return v;
    }

    @Override
    @Deprecated // since 2.9
    public Object findInjectableValueId(AnnotatedMember m) {
        JacksonInject.Value v = findInjectableValue(m);
        return (v == null) ? null : v.getId();
    }

    @Override
    public Class<?>[] findViews(Annotated a)
    {
        JsonView ann = _findAnnotation(a, JsonView.class);
        return (ann == null) ? null : ann.value();
    }

    @Override // since 2.7
    public AnnotatedMethod resolveSetterConflict(MapperConfig<?> config,
            AnnotatedMethod setter1, AnnotatedMethod setter2)
    {
        Class<?> cls1 = setter1.getRawParameterType(0);
        Class<?> cls2 = setter2.getRawParameterType(0);
        
        // First: prefer primitives over non-primitives
        // 11-Dec-2015, tatu: TODO, perhaps consider wrappers for primitives too?
        if (cls1.isPrimitive()) {
            if (!cls2.isPrimitive()) {
                return setter1;
            }
        } else if (cls2.isPrimitive()) {
            return setter2;
        }
        
        if (cls1 == String.class) {
            if (cls2 != String.class) {
                return setter1;
            }
        } else if (cls2 == String.class) {
            return setter2;
        }

        return null;
    }

    /*
    /**********************************************************
    /* Annotations for Polymorphic Type handling
    /**********************************************************
     */

    @Override
    public TypeResolverBuilder<?> findTypeResolver(MapperConfig<?> config,
            AnnotatedClass ac, JavaType baseType)
    {
        return _findTypeResolver(config, ac, baseType);
    }

    @Override
    public TypeResolverBuilder<?> findPropertyTypeResolver(MapperConfig<?> config,
            AnnotatedMember am, JavaType baseType)
    {
        /* As per definition of @JsonTypeInfo, should only apply to contents of container
         * (collection, map) types, not container types themselves:
         */
        // 17-Apr-2016, tatu: For 2.7.4 make sure ReferenceType also included
        if (baseType.isContainerType() || baseType.isReferenceType()) {
            return null;
        }
        // No per-member type overrides (yet)
        return _findTypeResolver(config, am, baseType);
    }

    @Override
    public TypeResolverBuilder<?> findPropertyContentTypeResolver(MapperConfig<?> config,
            AnnotatedMember am, JavaType containerType)
    {
        /* First: let's ensure property is a container type: caller should have
         * verified but just to be sure
         */
        if (containerType.getContentType() == null) {
            throw new IllegalArgumentException("Must call method with a container or reference type (got "+containerType+")");
        }
        return _findTypeResolver(config, am, containerType);
    }
    
    @Override
    public List<NamedType> findSubtypes(Annotated a)
    {
        JsonSubTypes t = _findAnnotation(a, JsonSubTypes.class);
        if (t == null) return null;
        JsonSubTypes.Type[] types = t.value();
        ArrayList<NamedType> result = new ArrayList<NamedType>(types.length);
        for (JsonSubTypes.Type type : types) {
            result.add(new NamedType(type.value(), type.name()));
        }
        return result;
    }

    @Override        
    public String findTypeName(AnnotatedClass ac)
    {
        JsonTypeName tn = _findAnnotation(ac, JsonTypeName.class);
        return (tn == null) ? null : tn.value();
    }

    @Override
    public Boolean isTypeId(AnnotatedMember member) {
        return _hasAnnotation(member, JsonTypeId.class);
    }

    /*
    /**********************************************************
    /* Annotations for Object Id handling
    /**********************************************************
     */

    @Override
    public ObjectIdInfo findObjectIdInfo(Annotated ann) {
        JsonIdentityInfo info = _findAnnotation(ann, JsonIdentityInfo.class);
        if (info == null || info.generator() == ObjectIdGenerators.None.class) {
            return null;
        }
        // In future may need to allow passing namespace?
        PropertyName name = PropertyName.construct(info.property());
        return new ObjectIdInfo(name, info.scope(), info.generator(), info.resolver());
    }

    @Override
    public ObjectIdInfo findObjectReferenceInfo(Annotated ann, ObjectIdInfo objectIdInfo) {
        JsonIdentityReference ref = _findAnnotation(ann, JsonIdentityReference.class);
        if (ref == null) {
            return objectIdInfo;
        }
        if (objectIdInfo == null) {
            objectIdInfo = ObjectIdInfo.empty();
        }
        return objectIdInfo.withAlwaysAsId(ref.alwaysAsId());
    }

    /*
    /**********************************************************
    /* Serialization: general annotations
    /**********************************************************
    */

    @Override
    public Object findSerializer(Annotated a)
    {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonSerializer> serClass = ann.using();
            if (serClass != JsonSerializer.None.class) {
                return serClass;
            }
        }
        
        /* 18-Oct-2010, tatu: [JACKSON-351] @JsonRawValue handled just here, for now;
         *  if we need to get raw indicator from other sources need to add
         *  separate accessor within {@link AnnotationIntrospector} interface.
         */
        JsonRawValue annRaw =  _findAnnotation(a, JsonRawValue.class);
        if ((annRaw != null) && annRaw.value()) {
            // let's construct instance with nominal type:
            Class<?> cls = a.getRawType();
            return new RawSerializer<Object>(cls);
        }       
        return null;
    }

    @Override
    public Object findKeySerializer(Annotated a)
    {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonSerializer> serClass = ann.keyUsing();
            if (serClass != JsonSerializer.None.class) {
                return serClass;
            }
        }
        return null;
    }

    @Override
    public Object findContentSerializer(Annotated a)
    {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonSerializer> serClass = ann.contentUsing();
            if (serClass != JsonSerializer.None.class) {
                return serClass;
            }
        }
        return null;
    }

    @Override
    public Object findNullSerializer(Annotated a)
    {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonSerializer> serClass = ann.nullsUsing();
            if (serClass != JsonSerializer.None.class) {
                return serClass;
            }
        }
        return null;
    }

    @Override
    public JsonInclude.Value findPropertyInclusion(Annotated a)
    {
        JsonInclude inc = _findAnnotation(a, JsonInclude.class);
        JsonInclude.Value value = (inc == null) ? JsonInclude.Value.empty() : JsonInclude.Value.from(inc);

        // only consider deprecated variant if we didn't have non-deprecated one:
        if (value.getValueInclusion() == JsonInclude.Include.USE_DEFAULTS) {
            value = _refinePropertyInclusion(a, value);
        }
        return value;
    }

    @SuppressWarnings("deprecation")
    private JsonInclude.Value _refinePropertyInclusion(Annotated a, JsonInclude.Value value) {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        if (ann != null) {
            switch (ann.include()) {
            case ALWAYS:
                return value.withValueInclusion(JsonInclude.Include.ALWAYS);
            case NON_NULL:
                return value.withValueInclusion(JsonInclude.Include.NON_NULL);
            case NON_DEFAULT:
                return value.withValueInclusion(JsonInclude.Include.NON_DEFAULT);
            case NON_EMPTY:
                return value.withValueInclusion(JsonInclude.Include.NON_EMPTY);
            case DEFAULT_INCLUSION:
            default:
            }
        }
        return value;
    }

    @Override
    public JsonSerialize.Typing findSerializationTyping(Annotated a)
    {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        return (ann == null) ? null : ann.typing();
    }

    @Override
    public Object findSerializationConverter(Annotated a) {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        return (ann == null) ? null : _classIfExplicit(ann.converter(), Converter.None.class);
    }

    @Override
    public Object findSerializationContentConverter(AnnotatedMember a) {
        JsonSerialize ann = _findAnnotation(a, JsonSerialize.class);
        return (ann == null) ? null : _classIfExplicit(ann.contentConverter(), Converter.None.class);
    }

    /*
    /**********************************************************
    /* Serialization: type refinements
    /**********************************************************
     */
    
    @Override
    public JavaType refineSerializationType(final MapperConfig<?> config,
            final Annotated a, final JavaType baseType) throws JsonMappingException
    {
        JavaType type = baseType;
        final TypeFactory tf = config.getTypeFactory();

        final JsonSerialize jsonSer = _findAnnotation(a, JsonSerialize.class);
        
        // Ok: start by refining the main type itself; common to all types

        final Class<?> serClass = (jsonSer == null) ? null : _classIfExplicit(jsonSer.as());
        if (serClass != null) {
            if (type.hasRawClass(serClass)) {
                // 30-Nov-2015, tatu: As per [databind#1023], need to allow forcing of
                //    static typing this way
                type = type.withStaticTyping();
            } else {
                Class<?> currRaw = type.getRawClass();
                try {
                    // 11-Oct-2015, tatu: For deser, we call `TypeFactory.constructSpecializedType()`,
                    //   may be needed here too in future?
                    if (serClass.isAssignableFrom(currRaw)) { // common case
                        type = tf.constructGeneralizedType(type, serClass);
                    } else if (currRaw.isAssignableFrom(serClass)) { // specialization, ok as well
                        type = tf.constructSpecializedType(type, serClass);
                    } else {
                        throw new JsonMappingException(null,
                                String.format("Can not refine serialization type %s into %s; types not related",
                                        type, serClass.getName()));
                    }
                } catch (IllegalArgumentException iae) {
                    throw new JsonMappingException(null,
                            String.format("Failed to widen type %s with annotation (value %s), from '%s': %s",
                                    type, serClass.getName(), a.getName(), iae.getMessage()),
                                    iae);
                }
            }
        }
        // Then further processing for container types

        // First, key type (for Maps, Map-like types):
        if (type.isMapLikeType()) {
            JavaType keyType = type.getKeyType();
            final Class<?> keyClass = (jsonSer == null) ? null : _classIfExplicit(jsonSer.keyAs());
            if (keyClass != null) {
                if (keyType.hasRawClass(keyClass)) {
                    keyType = keyType.withStaticTyping();
                } else {
                    Class<?> currRaw = keyType.getRawClass();
                    try {
                        // 19-May-2016, tatu: As per [databind#1231], [databind#1178] may need to actually
                        //   specialize (narrow) type sometimes, even if more commonly opposite
                        //   is needed.
                        if (keyClass.isAssignableFrom(currRaw)) { // common case
                            keyType = tf.constructGeneralizedType(keyType, keyClass);
                        } else if (currRaw.isAssignableFrom(keyClass)) { // specialization, ok as well
                            keyType = tf.constructSpecializedType(keyType, keyClass);
                        } else {
                            throw new JsonMappingException(null,
                                    String.format("Can not refine serialization key type %s into %s; types not related",
                                            keyType, keyClass.getName()));
                        }
                    } catch (IllegalArgumentException iae) {
                        throw new JsonMappingException(null,
                                String.format("Failed to widen key type of %s with concrete-type annotation (value %s), from '%s': %s",
                                        type, keyClass.getName(), a.getName(), iae.getMessage()),
                                        iae);
                    }
                }
                type = ((MapLikeType) type).withKeyType(keyType);
            }
        }

        JavaType contentType = type.getContentType();
        if (contentType != null) { // collection[like], map[like], array, reference
            // And then value types for all containers:
           final Class<?> contentClass = (jsonSer == null) ? null : _classIfExplicit(jsonSer.contentAs());
           if (contentClass != null) {
               if (contentType.hasRawClass(contentClass)) {
                   contentType = contentType.withStaticTyping();
               } else {
                   // 03-Apr-2016, tatu: As per [databind#1178], may need to actually
                   //   specialize (narrow) type sometimes, even if more commonly opposite
                   //   is needed.
                   Class<?> currRaw = contentType.getRawClass();
                   try {
                       if (contentClass.isAssignableFrom(currRaw)) { // common case
                           contentType = tf.constructGeneralizedType(contentType, contentClass);
                       } else if (currRaw.isAssignableFrom(contentClass)) { // specialization, ok as well
                           contentType = tf.constructSpecializedType(contentType, contentClass);
                       } else {
                           throw new JsonMappingException(null,
                                   String.format("Can not refine serialization content type %s into %s; types not related",
                                           contentType, contentClass.getName()));
                       }
                   } catch (IllegalArgumentException iae) { // shouldn't really happen
                       throw new JsonMappingException(null,
                               String.format("Internal error: failed to refine value type of %s with concrete-type annotation (value %s), from '%s': %s",
                                       type, contentClass.getName(), a.getName(), iae.getMessage()),
                                       iae);
                   }
               }
               type = type.withContentType(contentType);
           }
        }
        return type;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findSerializationType(Annotated am) {
        return null;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findSerializationKeyType(Annotated am, JavaType baseType) {
        return null;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findSerializationContentType(Annotated am, JavaType baseType) {
        return null;
    }

    /*
    /**********************************************************
    /* Serialization: class annotations
    /**********************************************************
     */

    @Override
    public String[] findSerializationPropertyOrder(AnnotatedClass ac) {
        JsonPropertyOrder order = _findAnnotation(ac, JsonPropertyOrder.class);
        return (order == null) ? null : order.value();
    }

    @Override
    public Boolean findSerializationSortAlphabetically(Annotated ann) {
        return _findSortAlpha(ann);
    }

    private final Boolean _findSortAlpha(Annotated ann) {
        JsonPropertyOrder order = _findAnnotation(ann, JsonPropertyOrder.class);
        // 23-Jun-2015, tatu: as per [databind#840], let's only consider
        //  `true` to have any significance.
        if ((order != null) && order.alphabetic()) {
            return Boolean.TRUE;
        }
        return null;
    }

    @Override
    public void findAndAddVirtualProperties(MapperConfig<?> config, AnnotatedClass ac,
            List<BeanPropertyWriter> properties) {
        JsonAppend ann = _findAnnotation(ac, JsonAppend.class);
        if (ann == null) {
            return;
        }
        final boolean prepend = ann.prepend();
        JavaType propType = null;

        // First: any attribute-backed properties?
        JsonAppend.Attr[] attrs = ann.attrs();
        for (int i = 0, len = attrs.length; i < len; ++i) {
            if (propType == null) {
                propType = config.constructType(Object.class);
            }
            BeanPropertyWriter bpw = _constructVirtualProperty(attrs[i],
                    config, ac, propType);
            if (prepend) {
                properties.add(i, bpw);
            } else {
                properties.add(bpw);
            }
        }

        // Then: general-purpose virtual properties?
        JsonAppend.Prop[] props = ann.props();
        for (int i = 0, len = props.length; i < len; ++i) {
            BeanPropertyWriter bpw = _constructVirtualProperty(props[i],
                    config, ac);
            if (prepend) {
                properties.add(i, bpw);
            } else {
                properties.add(bpw);
            }
        }
    }

    protected BeanPropertyWriter _constructVirtualProperty(JsonAppend.Attr attr,
            MapperConfig<?> config, AnnotatedClass ac, JavaType type)
    {
        PropertyMetadata metadata = attr.required() ?
                    PropertyMetadata.STD_REQUIRED : PropertyMetadata.STD_OPTIONAL;
        // could add Index, Description in future, if those matter
        String attrName = attr.value();

        // allow explicit renaming; if none, default to attribute name
        PropertyName propName = _propertyName(attr.propName(), attr.propNamespace());
        if (!propName.hasSimpleName()) {
            propName = PropertyName.construct(attrName);
        }
        // now, then, we need a placeholder for member (no real Field/Method):
        AnnotatedMember member = new VirtualAnnotatedMember(ac, ac.getRawType(),
                attrName, type);
        // and with that and property definition
        SimpleBeanPropertyDefinition propDef = SimpleBeanPropertyDefinition.construct(config,
                member, propName, metadata, attr.include());
        // can construct the property writer
        return AttributePropertyWriter.construct(attrName, propDef,
                ac.getAnnotations(), type);
    }

    protected BeanPropertyWriter _constructVirtualProperty(JsonAppend.Prop prop,
            MapperConfig<?> config, AnnotatedClass ac)
    {
        PropertyMetadata metadata = prop.required() ?
                    PropertyMetadata.STD_REQUIRED : PropertyMetadata.STD_OPTIONAL;
        PropertyName propName = _propertyName(prop.name(), prop.namespace());
        JavaType type = config.constructType(prop.type());
        // now, then, we need a placeholder for member (no real Field/Method):
        AnnotatedMember member = new VirtualAnnotatedMember(ac, ac.getRawType(),
                propName.getSimpleName(), type);
        // and with that and property definition
        SimpleBeanPropertyDefinition propDef = SimpleBeanPropertyDefinition.construct(config,
                member, propName, metadata, prop.include());

        Class<?> implClass = prop.value();

        HandlerInstantiator hi = config.getHandlerInstantiator();
        VirtualBeanPropertyWriter bpw = (hi == null) ? null
                : hi.virtualPropertyWriterInstance(config, implClass);
        if (bpw == null) {
            bpw = (VirtualBeanPropertyWriter) ClassUtil.createInstance(implClass,
                    config.canOverrideAccessModifiers());
        }

        // one more thing: give it necessary contextual information
        return bpw.withConfig(config, ac, propDef, type);
    }

    /*
    /**********************************************************
    /* Serialization: property annotations
    /**********************************************************
     */

    @Override
    public PropertyName findNameForSerialization(Annotated a)
    {
        JsonGetter jg = _findAnnotation(a, JsonGetter.class);
        if (jg != null) {
            return PropertyName.construct(jg.value());
        }
        JsonProperty pann = _findAnnotation(a, JsonProperty.class);
        if (pann != null) {
            return PropertyName.construct(pann.value());
        }
        if (_hasOneOf(a, ANNOTATIONS_TO_INFER_SER)) {
            return PropertyName.USE_DEFAULT;
        }
        return null;
    }

    @Override // since 2.9
    public Boolean hasAsValue(Annotated a) {
        JsonValue ann = _findAnnotation(a, JsonValue.class);
        if (ann == null) {
            return null;
        }
        return ann.value();
    }

    @Override // since 2.9
    public Boolean hasAnyGetter(Annotated a) {
        JsonAnyGetter ann = _findAnnotation(a, JsonAnyGetter.class);
        if (ann == null) {
            return null;
        }
        return ann.enabled();
    }

    @Override
    @Deprecated // since 2.9
    public boolean hasAnyGetterAnnotation(AnnotatedMethod am) {
        // No dedicated disabling; regular @JsonIgnore used if needs to be ignored (handled separately)
        return _hasAnnotation(am, JsonAnyGetter.class);
    }

    @Override
    @Deprecated // since 2.9
    public boolean hasAsValueAnnotation(AnnotatedMethod am) {
        JsonValue ann = _findAnnotation(am, JsonValue.class);
        // value of 'false' means disabled...
        return (ann != null) && ann.value();
    }

    /*
    /**********************************************************
    /* Deserialization: general annotations
    /**********************************************************
     */

    @Override
    public Object findDeserializer(Annotated a)
    {
        JsonDeserialize ann = _findAnnotation(a, JsonDeserialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonDeserializer> deserClass = ann.using();
            if (deserClass != JsonDeserializer.None.class) {
                return deserClass;
            }
        }
        return null;
    }

    @Override
    public Object findKeyDeserializer(Annotated a)
    {
        JsonDeserialize ann = _findAnnotation(a, JsonDeserialize.class);
        if (ann != null) {
            Class<? extends KeyDeserializer> deserClass = ann.keyUsing();
            if (deserClass != KeyDeserializer.None.class) {
                return deserClass;
            }
        }
        return null;
    }

    @Override
    public Object findContentDeserializer(Annotated a)
    {
        JsonDeserialize ann = _findAnnotation(a, JsonDeserialize.class);
        if (ann != null) {
            @SuppressWarnings("rawtypes")
            Class<? extends JsonDeserializer> deserClass = ann.contentUsing();
            if (deserClass != JsonDeserializer.None.class) {
                return deserClass;
            }
        }
        return null;
    }

    @Override
    public Object findDeserializationConverter(Annotated a)
    {
        JsonDeserialize ann = _findAnnotation(a, JsonDeserialize.class);
        return (ann == null) ? null : _classIfExplicit(ann.converter(), Converter.None.class);
    }

    @Override
    public Object findDeserializationContentConverter(AnnotatedMember a)
    {
        JsonDeserialize ann = _findAnnotation(a, JsonDeserialize.class);
        return (ann == null) ? null : _classIfExplicit(ann.contentConverter(), Converter.None.class);
    }

    /*
    /**********************************************************
    /* Deserialization: type modifications
    /**********************************************************
     */

    @Override
    public JavaType refineDeserializationType(final MapperConfig<?> config,
            final Annotated a, final JavaType baseType) throws JsonMappingException
    {
        JavaType type = baseType;
        final TypeFactory tf = config.getTypeFactory();

        final JsonDeserialize jsonDeser = _findAnnotation(a, JsonDeserialize.class);
        
        // Ok: start by refining the main type itself; common to all types
        final Class<?> valueClass = (jsonDeser == null) ? null : _classIfExplicit(jsonDeser.as());
        if ((valueClass != null) && !type.hasRawClass(valueClass)) {
            try {
                type = tf.constructSpecializedType(type, valueClass);
            } catch (IllegalArgumentException iae) {
                throw new JsonMappingException(null,
                        String.format("Failed to narrow type %s with annotation (value %s), from '%s': %s",
                                type, valueClass.getName(), a.getName(), iae.getMessage()),
                                iae);
            }
        }
        // Then further processing for container types

        // First, key type (for Maps, Map-like types):
        if (type.isMapLikeType()) {
            JavaType keyType = type.getKeyType();
            final Class<?> keyClass = (jsonDeser == null) ? null : _classIfExplicit(jsonDeser.keyAs());
            if (keyClass != null) {
                try {
                    keyType = tf.constructSpecializedType(keyType, keyClass);
                    type = ((MapLikeType) type).withKeyType(keyType);
                } catch (IllegalArgumentException iae) {
                    throw new JsonMappingException(null,
                            String.format("Failed to narrow key type of %s with concrete-type annotation (value %s), from '%s': %s",
                                    type, keyClass.getName(), a.getName(), iae.getMessage()),
                                    iae);
                }
            }
        }
        JavaType contentType = type.getContentType();
        if (contentType != null) { // collection[like], map[like], array, reference
            // And then value types for all containers:
            final Class<?> contentClass = (jsonDeser == null) ? null : _classIfExplicit(jsonDeser.contentAs());
            if (contentClass != null) {
                try {
                    contentType = tf.constructSpecializedType(contentType, contentClass);
                    type = type.withContentType(contentType);
                } catch (IllegalArgumentException iae) {
                    throw new JsonMappingException(null,
                            String.format("Failed to narrow value type of %s with concrete-type annotation (value %s), from '%s': %s",
                                    type, contentClass.getName(), a.getName(), iae.getMessage()),
                            iae);
                }
            }
        }
        return type;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findDeserializationContentType(Annotated am, JavaType baseContentType) {
        return null;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findDeserializationType(Annotated am, JavaType baseType) {
        return null;
    }

    @Override
    @Deprecated // since 2.7
    public Class<?> findDeserializationKeyType(Annotated am, JavaType baseKeyType) {
        return null;
    }

    /*
    /**********************************************************
    /* Deserialization: Class annotations
    /**********************************************************
     */

    @Override
    public Object findValueInstantiator(AnnotatedClass ac)
    {
        JsonValueInstantiator ann = _findAnnotation(ac, JsonValueInstantiator.class);
        // no 'null' marker yet, so:
        return (ann == null) ? null : ann.value();
    }

    @Override
    public Class<?> findPOJOBuilder(AnnotatedClass ac)
    {
        JsonDeserialize ann = _findAnnotation(ac, JsonDeserialize.class);
        return (ann == null) ? null : _classIfExplicit(ann.builder());
    }

    @Override
    public JsonPOJOBuilder.Value findPOJOBuilderConfig(AnnotatedClass ac)
    {
        JsonPOJOBuilder ann = _findAnnotation(ac, JsonPOJOBuilder.class);
        return (ann == null) ? null : new JsonPOJOBuilder.Value(ann);
    }
    
    /*
    /**********************************************************
    /* Deserialization: property annotations
    /**********************************************************
     */

    @Override
    public PropertyName findNameForDeserialization(Annotated a)
    {
        // @JsonSetter has precedence over @JsonProperty, being more specific
        // @JsonDeserialize implies that there is a property, but no name
        JsonSetter js = _findAnnotation(a, JsonSetter.class);
        if (js != null) {
            return PropertyName.construct(js.value());
        }
        JsonProperty pann = _findAnnotation(a, JsonProperty.class);
        if (pann != null) {
            return PropertyName.construct(pann.value());
        }
        if (_hasOneOf(a, ANNOTATIONS_TO_INFER_DESER)) {
            return PropertyName.USE_DEFAULT;
        }
        return null;
    }

    @Override
    public Boolean hasAnySetter(Annotated a) {
        JsonAnySetter ann = _findAnnotation(a, JsonAnySetter.class);
        return (ann == null) ? null : ann.enabled();
    }

    @Override
    public JsonSetter.Value findSetterInfo(Annotated a) {
        return JsonSetter.Value.from(_findAnnotation(a, JsonSetter.class));
    }

    @Override // since 2.9
    public Boolean findMergeInfo(Annotated a) {
        JsonMerge ann = _findAnnotation(a, JsonMerge.class);
        return (ann == null) ? null : ann.value().asBoolean();
    }

    @Override
    @Deprecated // since 2.9
    public boolean hasAnySetterAnnotation(AnnotatedMethod am) {
        return _hasAnnotation(am, JsonAnySetter.class);
    }

    @Override
    @Deprecated // since 2.9
    public boolean hasCreatorAnnotation(Annotated a)
    {
        /* No dedicated disabling; regular @JsonIgnore used if needs to be
         * ignored (and if so, is handled prior to this method getting called)
         */
         JsonCreator ann = _findAnnotation(a, JsonCreator.class);
         if (ann != null) {
             return (ann.mode() != JsonCreator.Mode.DISABLED);
         }
         // 19-Apr-2016, tatu: As per [databind#1197], [databind#1122] (and some related),
         //    may or may not consider it a creator
         if (_cfgConstructorPropertiesImpliesCreator ) {
             if (a instanceof AnnotatedConstructor) {
                 if (_java7Helper != null) {
                     Boolean b = _java7Helper.hasCreatorAnnotation(a);
                     if (b != null) {
                         return b.booleanValue();
                     }
                 }
             }
         }
         return false;
    }

    @Override
    @Deprecated // since 2.9
    public JsonCreator.Mode findCreatorBinding(Annotated a) {
        JsonCreator ann = _findAnnotation(a, JsonCreator.class);
        return (ann == null) ? null : ann.mode();
    }

    @Override
    public JsonCreator.Mode findCreatorAnnotation(MapperConfig<?> config, Annotated a) {
        JsonCreator ann = _findAnnotation(a, JsonCreator.class);
        if (ann != null) {
            return ann.mode();
        }

        if (_cfgConstructorPropertiesImpliesCreator
                && config.isEnabled(MapperFeature.INFER_CREATOR_FROM_CONSTRUCTOR_PROPERTIES)
            ) {
            if (a instanceof AnnotatedConstructor) {
                if (_java7Helper != null) {
                    Boolean b = _java7Helper.hasCreatorAnnotation(a);
                    if ((b != null) && b.booleanValue()) {
                        // 13-Sep-2016, tatu: Judgment call, but I don't think JDK ever implies
                        //    use of delegate; assumes as-properties implicitly
                        return JsonCreator.Mode.PROPERTIES;
                    }
                }
            }
        }
        return null;
    }

    /*
    /**********************************************************
    /* Helper methods
    /**********************************************************
     */

    protected boolean _isIgnorable(Annotated a)
    {
        JsonIgnore ann = _findAnnotation(a, JsonIgnore.class);
        if (ann != null) {
            return ann.value();
        }
        if (_java7Helper != null) {
            Boolean b = _java7Helper.findTransient(a);
            if (b != null) {
                return b.booleanValue();
            }
        }
        return false;
    }

    protected Class<?> _classIfExplicit(Class<?> cls) {
        if (cls == null || ClassUtil.isBogusClass(cls)) {
            return null;
        }
        return cls;
    }

    protected Class<?> _classIfExplicit(Class<?> cls, Class<?> implicit) {
        cls = _classIfExplicit(cls);
        return (cls == null || cls == implicit) ? null : cls;
    }

    protected PropertyName _propertyName(String localName, String namespace) {
        if (localName.isEmpty()) {
            return PropertyName.USE_DEFAULT;
        }
        if (namespace == null || namespace.isEmpty()) {
            return PropertyName.construct(localName);
        }
        return PropertyName.construct(localName, namespace);
    }

    protected PropertyName _findConstructorName(Annotated a)
    {
        if (a instanceof AnnotatedParameter) {
            AnnotatedParameter p = (AnnotatedParameter) a;
            AnnotatedWithParams ctor = p.getOwner();

            if (ctor != null) {
                if (_java7Helper != null) {
                    PropertyName name = _java7Helper.findConstructorName(p);
                    if (name != null) {
                        return name;
                    }
                }
            }
        }
        return null;
    }

    /**
     * Helper method called to construct and initialize instance of {@link TypeResolverBuilder}
     * if given annotated element indicates one is needed.
     */
    @SuppressWarnings("deprecation")
    protected TypeResolverBuilder<?> _findTypeResolver(MapperConfig<?> config,
            Annotated ann, JavaType baseType)
    {
        // First: maybe we have explicit type resolver?
        TypeResolverBuilder<?> b;
        JsonTypeInfo info = _findAnnotation(ann, JsonTypeInfo.class);
        JsonTypeResolver resAnn = _findAnnotation(ann, JsonTypeResolver.class);
        
        if (resAnn != null) {
            if (info == null) {
                return null;
            }
            /* let's not try to force access override (would need to pass
             * settings through if we did, since that's not doable on some
             * platforms)
             */
            b = config.typeResolverBuilderInstance(ann, resAnn.value());
        } else { // if not, use standard one, if indicated by annotations
            if (info == null) {
                return null;
            }
            // bit special; must return 'marker' to block use of default typing:
            if (info.use() == JsonTypeInfo.Id.NONE) {
                return _constructNoTypeResolverBuilder();
            }
            b = _constructStdTypeResolverBuilder();
        }
        // Does it define a custom type id resolver?
        JsonTypeIdResolver idResInfo = _findAnnotation(ann, JsonTypeIdResolver.class);
        TypeIdResolver idRes = (idResInfo == null) ? null
                : config.typeIdResolverInstance(ann, idResInfo.value());
        if (idRes != null) {
            idRes.init(baseType);
        }
        b = b.init(info.use(), idRes);
        /* 13-Aug-2011, tatu: One complication; external id
         *   only works for properties; so if declared for a Class, we will need
         *   to map it to "PROPERTY" instead of "EXTERNAL_PROPERTY"
         */
        JsonTypeInfo.As inclusion = info.include();
        if (inclusion == JsonTypeInfo.As.EXTERNAL_PROPERTY && (ann instanceof AnnotatedClass)) {
            inclusion = JsonTypeInfo.As.PROPERTY;
        }
        b = b.inclusion(inclusion);
        b = b.typeProperty(info.property());
        Class<?> defaultImpl = info.defaultImpl();

        // 08-Dec-2014, tatu: To deprecate `JsonTypeInfo.None` we need to use other placeholder(s);
        //   and since `java.util.Void` has other purpose (to indicate "deser as null"), we'll instead
        //   use `JsonTypeInfo.class` itself. But any annotation type will actually do, as they have no
        //   valid use (can not instantiate as default)
        if (defaultImpl != JsonTypeInfo.None.class && !defaultImpl.isAnnotation()) {
            b = b.defaultImpl(defaultImpl);
        }
        b = b.typeIdVisibility(info.visible());
        return b;
    }

    /**
     * Helper method for constructing standard {@link TypeResolverBuilder}
     * implementation.
     */
    protected StdTypeResolverBuilder _constructStdTypeResolverBuilder() {
        return new StdTypeResolverBuilder();
    }

    /**
     * Helper method for dealing with "no type info" marker; can't be null
     * (as it'd be replaced by default typing)
     */
    protected StdTypeResolverBuilder _constructNoTypeResolverBuilder() {
        return StdTypeResolverBuilder.noTypeInfoBuilder();
    }

    /*
    /**********************************************************
    /* Helper classes
    /**********************************************************
     */
}
```

## Failed test
com.fasterxml.jackson.databind.introspect.TypeCoercion1592Test

## Test line
com.fasterxml.jackson.databind.exc.InvalidDefinitionException

## Error
Invalid definition for property "i" (of type com.fasterxml.jackson.databind.introspect.TypeCoercion1592Test$Bean1592): Can not refine serialization type [simple type, class int] into java.lang.Integer; types not related

## Error Code Block
```java
package com.fasterxml.jackson.databind.introspect;

import com.fasterxml.jackson.databind.*;

import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

// [databind#1592]: allow "coercion" between primitive/wrapper (mostly just ignoring)
public class TypeCoercion1592Test extends BaseMapTest
{
    static class Bean1592
    {
        @JsonSerialize(as=Integer.class)
        public int i;

        @JsonDeserialize(as=Long.class)
        public long l;
    }

    /*
    /**********************************************************
    /* Test methods
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();

    public void testTypeCoercion1592() throws Exception
    {
        // first, serialize
        MAPPER.writeValueAsString(new Bean1592());
        Bean1592 result = MAPPER.readValue("{}", Bean1592.class);
        assertNotNull(result);
    }
}

```
