## Buggy code
```java
public class POJOPropertiesCollector
{
    /*
    /**********************************************************
    /* Configuration
    /**********************************************************
     */

    /**
     * Configuration settings
     */
    protected final MapperConfig<?> _config;

    /**
     * True if introspection is done for serialization (giving
     * precedence for serialization annotations), or not (false, deserialization)
     */
    protected final boolean _forSerialization;

    /**
     * @since 2.5
     */
    protected final boolean _stdBeanNaming;

    /**
     * Type of POJO for which properties are being collected.
     */
    protected final JavaType _type;

    /**
     * Low-level introspected class information (methods, fields etc)
     */
    protected final AnnotatedClass _classDef;

    protected final VisibilityChecker<?> _visibilityChecker;

    protected final AnnotationIntrospector _annotationIntrospector;

    /**
     * Prefix used by auto-detected mutators ("setters"): usually "set",
     * but differs for builder objects ("with" by default).
     */
    protected final String _mutatorPrefix;
    
    /*
    /**********************************************************
    /* Collected property information
    /**********************************************************
     */

    /**
     * State flag we keep to indicate whether actual property information
     * has been collected or not.
     */
    protected boolean _collected;
    
    /**
     * Set of logical property information collected so far.
     *<p>
     * Since 2.6, this has been constructed (more) lazily, to defer
     * throwing of exceptions for potential conflicts in cases where
     * this may not be an actual problem.
     */
    protected LinkedHashMap<String, POJOPropertyBuilder> _properties;

    protected LinkedList<POJOPropertyBuilder> _creatorProperties ;
    
    protected LinkedList<AnnotatedMember> _anyGetters;

    protected LinkedList<AnnotatedMethod> _anySetters;
    
    protected LinkedList<AnnotatedMember> _anySetterField;

    /**
     * Method(s) marked with 'JsonValue' annotation
     */
    protected LinkedList<AnnotatedMethod> _jsonValueGetters;

    /**
     * Lazily collected list of properties that can be implicitly
     * ignored during serialization; only updated when collecting
     * information for deserialization purposes
     */
    protected HashSet<String> _ignoredPropertyNames;

    /**
     * Lazily collected list of members that were annotated to
     * indicate that they represent mutators for deserializer
     * value injection.
     */
    protected LinkedHashMap<Object, AnnotatedMember> _injectables;
    
    /*
    /**********************************************************
    /* Life-cycle
    /**********************************************************
     */

    protected POJOPropertiesCollector(MapperConfig<?> config, boolean forSerialization,
            JavaType type, AnnotatedClass classDef, String mutatorPrefix)
    {
        _config = config;
        _stdBeanNaming = config.isEnabled(MapperFeature.USE_STD_BEAN_NAMING);
        _forSerialization = forSerialization;
        _type = type;
        _classDef = classDef;
        _mutatorPrefix = (mutatorPrefix == null) ? "set" : mutatorPrefix;
        _annotationIntrospector = config.isAnnotationProcessingEnabled() ?
                _config.getAnnotationIntrospector() : null;
        if (_annotationIntrospector == null) {
            _visibilityChecker = _config.getDefaultVisibilityChecker();
        } else {
            _visibilityChecker = _annotationIntrospector.findAutoDetectVisibility(classDef,
                    _config.getDefaultVisibilityChecker());
        }
    }

    /*
    /**********************************************************
    /* Public API
    /**********************************************************
     */

    public MapperConfig<?> getConfig() {
        return _config;
    }

    public JavaType getType() {
        return _type;
    }
    
    public AnnotatedClass getClassDef() {
        return _classDef;
    }

    public AnnotationIntrospector getAnnotationIntrospector() {
        return _annotationIntrospector;
    }
    
    public List<BeanPropertyDefinition> getProperties() {
        // make sure we return a copy, so caller can remove entries if need be:
        Map<String, POJOPropertyBuilder> props = getPropertyMap();
        return new ArrayList<BeanPropertyDefinition>(props.values());
    }

    public Map<Object, AnnotatedMember> getInjectables() {
        if (!_collected) {
            collectAll();
        }
        return _injectables;
    }
    
    public AnnotatedMethod getJsonValueMethod()
    {
        if (!_collected) {
            collectAll();
        }
        // If @JsonValue defined, must have a single one
        if (_jsonValueGetters != null) {
            if (_jsonValueGetters.size() > 1) {
                reportProblem("Multiple value properties defined ("+_jsonValueGetters.get(0)+" vs "
                        +_jsonValueGetters.get(1)+")");
            }
            // otherwise we won't greatly care
            return _jsonValueGetters.get(0);
        }
        return null;
    }

    public AnnotatedMember getAnyGetter()
    {
        if (!_collected) {
            collectAll();
        }
        if (_anyGetters != null) {
            if (_anyGetters.size() > 1) {
                reportProblem("Multiple 'any-getters' defined ("+_anyGetters.get(0)+" vs "
                        +_anyGetters.get(1)+")");
            }
            return _anyGetters.getFirst();
        }        
        return null;
    }
    
    public AnnotatedMember getAnySetterField()
    {
        if (!_collected) {
            collectAll();
        }
        if (_anySetterField != null) {
            if (_anySetterField.size() > 1) {
                reportProblem("Multiple 'any-Setters' defined ("+_anySetters.get(0)+" vs "
                        +_anySetterField.get(1)+")");
            }
            return _anySetterField.getFirst();
        }
        return null;
    }

    public AnnotatedMethod getAnySetterMethod()
    {
        if (!_collected) {
            collectAll();
        }
        if (_anySetters != null) {
            if (_anySetters.size() > 1) {
                reportProblem("Multiple 'any-setters' defined ("+_anySetters.get(0)+" vs "
                        +_anySetters.get(1)+")");
            }
            return _anySetters.getFirst();
        }
        return null;
    }

    /**
     * Accessor for set of properties that are explicitly marked to be ignored
     * via per-property markers (but NOT class annotations).
     */
    public Set<String> getIgnoredPropertyNames() {
        return _ignoredPropertyNames;
    }

    /**
     * Accessor to find out whether type specified requires inclusion
     * of Object Identifier.
     */
    public ObjectIdInfo getObjectIdInfo()
    {
        if (_annotationIntrospector == null) {
            return null;
        }
        ObjectIdInfo info = _annotationIntrospector.findObjectIdInfo(_classDef);
        if (info != null) { // 2.1: may also have different defaults for refs:
            info = _annotationIntrospector.findObjectReferenceInfo(_classDef, info);
        }
        return info;
    }

    /**
     * Method for finding Class to use as POJO builder, if any.
     */
    public Class<?> findPOJOBuilderClass()
    {
        return _annotationIntrospector.findPOJOBuilder(_classDef);
    }
    
    // for unit tests:
    protected Map<String, POJOPropertyBuilder> getPropertyMap() {
        if (!_collected) {
            collectAll();
        }
        return _properties;
    }

    /*
    /**********************************************************
    /* Public API: main-level collection
    /**********************************************************
     */

    /**
     * Method that orchestrates collection activities, and needs to be called
     * after creating the instance.
     *<p>
     * Since 2.6 has become a no-op and actual collection is done more lazily
     * at point where properties are actually needed.
     * 
     * @deprecated Since 2.6; no need to call
     */
    @Deprecated
    public POJOPropertiesCollector collect() {
        return this;
    }

    /**
     * Internal method that will collect actual property information.
     *
     * @since 2.6
     */
    protected void collectAll()
    {
        LinkedHashMap<String, POJOPropertyBuilder> props = new LinkedHashMap<String, POJOPropertyBuilder>();

        // First: gather basic data
        _addFields(props);
        _addMethods(props);
        // 25-Jan-2016, tatu: Avoid introspecting (constructor-)creators for non-static
        //    inner classes, see [databind#1502]
        if (!_classDef.isNonStaticInnerClass()) {
            _addCreators(props);
        }
        _addInjectables(props);

        // Remove ignored properties, first; this MUST precede annotation merging
        // since logic relies on knowing exactly which accessor has which annotation
        _removeUnwantedProperties(props);

        // then merge annotations, to simplify further processing
        for (POJOPropertyBuilder property : props.values()) {
            property.mergeAnnotations(_forSerialization);
        }
        // and then remove unneeded accessors (wrt read-only, read-write)
        _removeUnwantedAccessor(props);

        // Rename remaining properties
        _renameProperties(props);

        // And use custom naming strategy, if applicable...
        PropertyNamingStrategy naming = _findNamingStrategy();
        if (naming != null) {
            _renameUsing(props, naming);
        }

        /* Sort by visibility (explicit over implicit); drop all but first
         * of member type (getter, setter etc) if there is visibility
         * difference
         */
        for (POJOPropertyBuilder property : props.values()) {
            property.trimByVisibility();
        }

        /* and, if required, apply wrapper name: note, MUST be done after
         * annotations are merged.
         */
        if (_config.isEnabled(MapperFeature.USE_WRAPPER_NAME_AS_PROPERTY_NAME)) {
            _renameWithWrappers(props);
        }
        
        // well, almost last: there's still ordering...
        _sortProperties(props);
        _properties = props;
        _collected = true;
    }

    /*
    /**********************************************************
    /* Overridable internal methods, adding members
    /**********************************************************
     */
    
    /**
     * Method for collecting basic information on all fields found
     */
    protected void _addFields(Map<String, POJOPropertyBuilder> props)
    {
        final AnnotationIntrospector ai = _annotationIntrospector;
        /* 28-Mar-2013, tatu: For deserialization we may also want to remove
         *   final fields, as often they won't make very good mutators...
         *   (although, maybe surprisingly, JVM _can_ force setting of such fields!)
         */
        final boolean pruneFinalFields = !_forSerialization && !_config.isEnabled(MapperFeature.ALLOW_FINAL_FIELDS_AS_MUTATORS);
        final boolean transientAsIgnoral = _config.isEnabled(MapperFeature.PROPAGATE_TRANSIENT_MARKER);
        
        for (AnnotatedField f : _classDef.fields()) {
            String implName = (ai == null) ? null : ai.findImplicitPropertyName(f);
            if (implName == null) {
                implName = f.getName();
            }

            PropertyName pn;

            if (ai == null) {
                pn = null;
            } else if (_forSerialization) {
                /* 18-Aug-2011, tatu: As per existing unit tests, we should only
                 *   use serialization annotation (@JsonSerialize) when serializing
                 *   fields, and similarly for deserialize-only annotations... so
                 *   no fallbacks in this particular case.
                 */
                pn = ai.findNameForSerialization(f);
            } else {
                pn = ai.findNameForDeserialization(f);
            }
            boolean hasName = (pn != null);
            boolean nameExplicit = hasName;

            if (nameExplicit && pn.isEmpty()) { // empty String meaning "use default name", here just means "same as field name"
                pn = _propNameFromSimple(implName);
                nameExplicit = false;
            }
            // having explicit name means that field is visible; otherwise need to check the rules
            boolean visible = (pn != null);
            if (!visible) {
                visible = _visibilityChecker.isFieldVisible(f);
            }
            // and finally, may also have explicit ignoral
            boolean ignored = (ai != null) && ai.hasIgnoreMarker(f);

            // 13-May-2015, tatu: Moved from earlier place (AnnotatedClass) in 2.6
            if (f.isTransient()) {
                // 20-May-2016, tatu: as per [databind#1184] explicit annotation should override
                //    "default" `transient`
                if (!hasName) {
                    visible = false;
                    if (transientAsIgnoral) {
                        ignored = true;
                    }
                }
            }
            /* [databind#190]: this is the place to prune final fields, if they are not
             *  to be used as mutators. Must verify they are not explicitly included.
             *  Also: if 'ignored' is set, need to included until a later point, to
             *  avoid losing ignoral information.
             */
            if (pruneFinalFields && (pn == null) && !ignored && Modifier.isFinal(f.getModifiers())) {
                continue;
            }

            //if field has annotation @JsonAnySetter
            if(f.hasAnnotation(JsonAnySetter.class)) {
            	if (_anySetterField == null) {
            		_anySetterField = new LinkedList<AnnotatedMember>();
            	}
            	_anySetterField.add(f);
            }
            _property(props, implName).addField(f, pn, nameExplicit, visible, ignored);
        }
    }

    /**
     * Method for collecting basic information on constructor(s) found
     */
    protected void _addCreators(Map<String, POJOPropertyBuilder> props)
    {
        // can be null if annotation processing is disabled...
        if (_annotationIntrospector == null) {
            return;
        }
        for (AnnotatedConstructor ctor : _classDef.getConstructors()) {
            if (_creatorProperties == null) {
                _creatorProperties = new LinkedList<POJOPropertyBuilder>();
            }
            for (int i = 0, len = ctor.getParameterCount(); i < len; ++i) {
                _addCreatorParam(props, ctor.getParameter(i));
            }
        }
        for (AnnotatedMethod factory : _classDef.getStaticMethods()) {
            if (_creatorProperties == null) {
                _creatorProperties = new LinkedList<POJOPropertyBuilder>();
            }
            for (int i = 0, len = factory.getParameterCount(); i < len; ++i) {
                _addCreatorParam(props, factory.getParameter(i));
            }
        }
    }

    /**
     * @since 2.4
     */
    protected void _addCreatorParam(Map<String, POJOPropertyBuilder> props,
            AnnotatedParameter param)
    {
        // JDK 8, paranamer, Scala can give implicit name
        String impl = _annotationIntrospector.findImplicitPropertyName(param);
        if (impl == null) {
            impl = "";
        }
        PropertyName pn = _annotationIntrospector.findNameForDeserialization(param);
        boolean expl = (pn != null && !pn.isEmpty());
        if (!expl) {
            if (impl.isEmpty()) {
                /* Important: if neither implicit nor explicit name, can not make use
                 * of this creator parameter -- may or may not be a problem, verified
                 * at a later point.
                 */
                return;
            }
            // Also: if this occurs, there MUST be explicit annotation on creator itself
            if (!_annotationIntrospector.hasCreatorAnnotation(param.getOwner())) {
                return;
            }
            pn = PropertyName.construct(impl);
        }

        // shouldn't need to worry about @JsonIgnore, since creators only added
        // if so annotated

        /* 13-May-2015, tatu: We should try to start with implicit name, similar to how
         *   fields and methods work; but unlike those, we don't necessarily have
         *   implicit name to use (pre-Java8 at least). So:
         */
        POJOPropertyBuilder prop = (expl && impl.isEmpty())
                ? _property(props, pn) : _property(props, impl);
        prop.addCtor(param, pn, expl, true, false);
        _creatorProperties.add(prop);
    }
    
    /**
     * Method for collecting basic information on all fields found
     */
    protected void _addMethods(Map<String, POJOPropertyBuilder> props)
    {
        final AnnotationIntrospector ai = _annotationIntrospector;
        
        for (AnnotatedMethod m : _classDef.memberMethods()) {
            /* For methods, handling differs between getters and setters; and
             * we will also only consider entries that either follow the bean
             * naming convention or are explicitly marked: just being visible
             * is not enough (unlike with fields)
             */
            int argCount = m.getParameterCount();
            if (argCount == 0) { // getters (including 'any getter')
            	_addGetterMethod(props, m, ai);
            } else if (argCount == 1) { // setters
            	_addSetterMethod(props, m, ai);
            } else if (argCount == 2) { // any getter?
                if (ai != null  && ai.hasAnySetterAnnotation(m)) {
                    if (_anySetters == null) {
                        _anySetters = new LinkedList<AnnotatedMethod>();
                    }
                    _anySetters.add(m);
                }
            }
        }
    }

    protected void _addGetterMethod(Map<String, POJOPropertyBuilder> props,
            AnnotatedMethod m, AnnotationIntrospector ai)
    {
        // Very first thing: skip if not returning any value
        if (!m.hasReturnType()) {
            return;
        }
        
        // any getter?
        if (ai != null) {
            if (ai.hasAnyGetterAnnotation(m)) {
                if (_anyGetters == null) {
                    _anyGetters = new LinkedList<AnnotatedMember>();
                }
                _anyGetters.add(m);
                return;
            }
            // @JsonValue?
            if (ai.hasAsValueAnnotation(m)) {
                if (_jsonValueGetters == null) {
                    _jsonValueGetters = new LinkedList<AnnotatedMethod>();
                }
                _jsonValueGetters.add(m);
                return;
            }
        }
        String implName; // from naming convention
        boolean visible;

        PropertyName pn = (ai == null) ? null : ai.findNameForSerialization(m);
        boolean nameExplicit = (pn != null);

        if (!nameExplicit) { // no explicit name; must consider implicit
            implName = (ai == null) ? null : ai.findImplicitPropertyName(m);
            if (implName == null) {
                implName = BeanUtil.okNameForRegularGetter(m, m.getName(), _stdBeanNaming);
            }
            if (implName == null) { // if not, must skip
                implName = BeanUtil.okNameForIsGetter(m, m.getName(), _stdBeanNaming);
                if (implName == null) {
                    return;
                }
                visible = _visibilityChecker.isIsGetterVisible(m);
            } else {
                visible = _visibilityChecker.isGetterVisible(m);
            }
        } else { // explicit indication of inclusion, but may be empty
            // we still need implicit name to link with other pieces
            implName = (ai == null) ? null : ai.findImplicitPropertyName(m);
            if (implName == null) {
                implName = BeanUtil.okNameForGetter(m, _stdBeanNaming);
            }
            // if not regular getter name, use method name as is
            if (implName == null) {
                implName = m.getName();
            }
            if (pn.isEmpty()) {
                // !!! TODO: use PropertyName for implicit names too
                pn = _propNameFromSimple(implName);
                nameExplicit = false;
            }
            visible = true;
        }
        boolean ignore = (ai == null) ? false : ai.hasIgnoreMarker(m);
        _property(props, implName).addGetter(m, pn, nameExplicit, visible, ignore);
    }

    protected void _addSetterMethod(Map<String, POJOPropertyBuilder> props,
            AnnotatedMethod m, AnnotationIntrospector ai)
    {
        String implName; // from naming convention
        boolean visible;
        PropertyName pn = (ai == null) ? null : ai.findNameForDeserialization(m);
        boolean nameExplicit = (pn != null);
        if (!nameExplicit) { // no explicit name; must follow naming convention
            implName = (ai == null) ? null : ai.findImplicitPropertyName(m);
            if (implName == null) {
                implName = BeanUtil.okNameForMutator(m, _mutatorPrefix, _stdBeanNaming);
            }
            if (implName == null) { // if not, must skip
            	return;
            }
            visible = _visibilityChecker.isSetterVisible(m);
        } else { // explicit indication of inclusion, but may be empty
            // we still need implicit name to link with other pieces
            implName = (ai == null) ? null : ai.findImplicitPropertyName(m);
            if (implName == null) {
                implName = BeanUtil.okNameForMutator(m, _mutatorPrefix, _stdBeanNaming);
            }
            // if not regular getter name, use method name as is
            if (implName == null) {
                implName = m.getName();
            }
            if (pn.isEmpty()) {
                // !!! TODO: use PropertyName for implicit names too
                pn = _propNameFromSimple(implName);
                nameExplicit = false;
            }
            visible = true;
        }
        boolean ignore = (ai == null) ? false : ai.hasIgnoreMarker(m);
        _property(props, implName).addSetter(m, pn, nameExplicit, visible, ignore);
    }
    
    protected void _addInjectables(Map<String, POJOPropertyBuilder> props)
    {
        final AnnotationIntrospector ai = _annotationIntrospector;
        if (ai == null) {
            return;
        }
        
        // first fields, then methods
        for (AnnotatedField f : _classDef.fields()) {
            _doAddInjectable(ai.findInjectableValueId(f), f);
        }
        
        for (AnnotatedMethod m : _classDef.memberMethods()) {
            /* for now, only allow injection of a single arg
             * (to be changed in future)
             */
            if (m.getParameterCount() != 1) {
                continue;
            }
            _doAddInjectable(ai.findInjectableValueId(m), m);
        }
    }

    protected void _doAddInjectable(Object id, AnnotatedMember m)
    {
        if (id == null) {
            return;
        }
        if (_injectables == null) {
            _injectables = new LinkedHashMap<Object, AnnotatedMember>();
        }
        AnnotatedMember prev = _injectables.put(id, m);
        if (prev != null) {
            String type = id.getClass().getName();
            throw new IllegalArgumentException("Duplicate injectable value with id '"
                    +String.valueOf(id)+"' (of type "+type+")");
        }
    }

    private PropertyName _propNameFromSimple(String simpleName) {
        return PropertyName.construct(simpleName, null);
    }
    
    /*
    /**********************************************************
    /* Internal methods; removing ignored properties
    /**********************************************************
     */

    /**
     * Method called to get rid of candidate properties that are marked
     * as ignored.
     */
    protected void _removeUnwantedProperties(Map<String, POJOPropertyBuilder> props)
    {
        Iterator<POJOPropertyBuilder> it = props.values().iterator();
        while (it.hasNext()) {
            POJOPropertyBuilder prop = it.next();

            // First: if nothing visible, just remove altogether
            if (!prop.anyVisible()) {
                it.remove();
                continue;
            }
            // Otherwise, check ignorals
            if (prop.anyIgnorals()) {
                // first: if one or more ignorals, and no explicit markers, remove the whole thing
                if (!prop.isExplicitlyIncluded()) {
                    it.remove();
                    _collectIgnorals(prop.getName());
                    continue;
                }
                // otherwise just remove ones marked to be ignored
                prop.removeIgnored();
                if (!_forSerialization && !prop.couldDeserialize()) {
                    _collectIgnorals(prop.getName());
                }
            }
        }
    }

    /**
     * Method called to further get rid of unwanted individual accessors,
     * based on read/write settings and rules for "pulling in" accessors
     * (or not).
     */
    protected void _removeUnwantedAccessor(Map<String, POJOPropertyBuilder> props)
    {
        final boolean inferMutators = _config.isEnabled(MapperFeature.INFER_PROPERTY_MUTATORS);
        Iterator<POJOPropertyBuilder> it = props.values().iterator();

        while (it.hasNext()) {
            POJOPropertyBuilder prop = it.next();
            prop.removeNonVisible(inferMutators);
        }
    }
        
    /**
     * Helper method called to add explicitly ignored properties to a list
     * of known ignored properties; this helps in proper reporting of
     * errors.
     */
    private void _collectIgnorals(String name)
    {
        if (!_forSerialization) {
            if (_ignoredPropertyNames == null) {
                _ignoredPropertyNames = new HashSet<String>();
            }
            _ignoredPropertyNames.add(name);
        }
    }

    /*
    /**********************************************************
    /* Internal methods; renaming properties
    /**********************************************************
     */

    protected void _renameProperties(Map<String, POJOPropertyBuilder> props)
    {
        // With renaming need to do in phases: first, find properties to rename
        Iterator<Map.Entry<String,POJOPropertyBuilder>> it = props.entrySet().iterator();
        LinkedList<POJOPropertyBuilder> renamed = null;
        while (it.hasNext()) {
            Map.Entry<String, POJOPropertyBuilder> entry = it.next();
            POJOPropertyBuilder prop = entry.getValue();

            Collection<PropertyName> l = prop.findExplicitNames();

            // no explicit names? Implicit one is fine as is
            if (l.isEmpty()) {
                continue;
            }
            it.remove(); // need to replace with one or more renamed
            if (renamed == null) {
                renamed = new LinkedList<POJOPropertyBuilder>();
            }
            // simple renaming? Just do it
            if (l.size() == 1) {
                PropertyName n = l.iterator().next();
                renamed.add(prop.withName(n));
                continue;
            }
            // but this may be problematic...
            renamed.addAll(prop.explode(l));

            /*
            String newName = prop.findNewName();
            if (newName != null) {
                if (renamed == null) {
                    renamed = new LinkedList<POJOPropertyBuilder>();
                }
                prop = prop.withSimpleName(newName);
                renamed.add(prop);
                it.remove();
            }
            */
        }
        
        // and if any were renamed, merge back in...
        if (renamed != null) {
            for (POJOPropertyBuilder prop : renamed) {
                String name = prop.getName();
                POJOPropertyBuilder old = props.get(name);
                if (old == null) {
                    props.put(name, prop);
                } else {
                    old.addAll(prop);
                }
                // replace the creatorProperty too, if there is one
                _updateCreatorProperty(prop, _creatorProperties);
            }
        }
    }

    protected void _renameUsing(Map<String, POJOPropertyBuilder> propMap,
            PropertyNamingStrategy naming)
    {
        POJOPropertyBuilder[] props = propMap.values().toArray(new POJOPropertyBuilder[propMap.size()]);
        propMap.clear();
        for (POJOPropertyBuilder prop : props) {
            PropertyName fullName = prop.getFullName();
            String rename = null;
            // As per [databind#428] need to skip renaming if property has
            // explicitly defined name, unless feature  is enabled
            if (!prop.isExplicitlyNamed() || _config.isEnabled(MapperFeature.ALLOW_EXPLICIT_PROPERTY_RENAMING)) {
                if (_forSerialization) {
                    if (prop.hasGetter()) {
                        rename = naming.nameForGetterMethod(_config, prop.getGetter(), fullName.getSimpleName());
                    } else if (prop.hasField()) {
                        rename = naming.nameForField(_config, prop.getField(), fullName.getSimpleName());
                    }
                } else {
                    if (prop.hasSetter()) {
                        rename = naming.nameForSetterMethod(_config, prop.getSetter(), fullName.getSimpleName());
                    } else if (prop.hasConstructorParameter()) {
                        rename = naming.nameForConstructorParameter(_config, prop.getConstructorParameter(), fullName.getSimpleName());
                    } else if (prop.hasField()) {
                        rename = naming.nameForField(_config, prop.getField(), fullName.getSimpleName());
                    } else if (prop.hasGetter()) {
                        /* Plus, when getter-as-setter is used, need to convert that too..
                         * (should we verify that's enabled? For now, assume it's ok always)
                         */
                        rename = naming.nameForGetterMethod(_config, prop.getGetter(), fullName.getSimpleName());
                    }
                }
            }
            final String simpleName;
            if (rename != null && !fullName.hasSimpleName(rename)) {
                prop = prop.withSimpleName(rename);
                simpleName = rename;
            } else {
                simpleName = fullName.getSimpleName();
            }
            /* As per [JACKSON-687], need to consider case where there may already be
             * something in there...
             */
            POJOPropertyBuilder old = propMap.get(simpleName);
            if (old == null) {
                propMap.put(simpleName, prop);
            } else {
                old.addAll(prop);
            }
            // replace the creatorProperty too, if there is one
            _updateCreatorProperty(prop, _creatorProperties);
        }
    }

    protected void _renameWithWrappers(Map<String, POJOPropertyBuilder> props)
    {
        /* 11-Sep-2012, tatu: To support 'MapperFeature.USE_WRAPPER_NAME_AS_PROPERTY_NAME',
         *   need another round of renaming...
         */
        Iterator<Map.Entry<String,POJOPropertyBuilder>> it = props.entrySet().iterator();
        LinkedList<POJOPropertyBuilder> renamed = null;
        while (it.hasNext()) {
            Map.Entry<String, POJOPropertyBuilder> entry = it.next();
            POJOPropertyBuilder prop = entry.getValue();
            AnnotatedMember member = prop.getPrimaryMember();
            if (member == null) {
                continue;
            }
            PropertyName wrapperName = _annotationIntrospector.findWrapperName(member);
            // One trickier part (wrt [Issue#24] of JAXB annotations: wrapper that
            // indicates use of actual property... But hopefully has been taken care
            // of previously
            if (wrapperName == null || !wrapperName.hasSimpleName()) {
                continue;
            }
            if (!wrapperName.equals(prop.getFullName())) {
                if (renamed == null) {
                    renamed = new LinkedList<POJOPropertyBuilder>();
                }
                prop = prop.withName(wrapperName);
                renamed.add(prop);
                it.remove();
            }
        }
        // and if any were renamed, merge back in...
        if (renamed != null) {
            for (POJOPropertyBuilder prop : renamed) {
                String name = prop.getName();
                POJOPropertyBuilder old = props.get(name);
                if (old == null) {
                    props.put(name, prop);
                } else {
                    old.addAll(prop);
                }
            }
        }
    }

    /*
    /**********************************************************
    /* Overridable internal methods, sorting, other stuff
    /**********************************************************
     */
    
    /* First, order by [JACKSON-90] (explicit ordering and/or alphabetic)
     * and then for [JACKSON-170] (implicitly order creator properties before others)
     */
    protected void _sortProperties(Map<String, POJOPropertyBuilder> props)
    {
        // Then how about explicit ordering?
        AnnotationIntrospector intr = _annotationIntrospector;
        Boolean alpha = (intr == null) ? null : intr.findSerializationSortAlphabetically((Annotated) _classDef);
        boolean sort;
        
        if (alpha == null) {
            sort = _config.shouldSortPropertiesAlphabetically();
        } else {
            sort = alpha.booleanValue();
        }
        String[] propertyOrder = (intr == null) ? null : intr.findSerializationPropertyOrder(_classDef);
        
        // no sorting? no need to shuffle, then
        if (!sort && (_creatorProperties == null) && (propertyOrder == null)) {
            return;
        }
        int size = props.size();
        Map<String, POJOPropertyBuilder> all;
        // Need to (re)sort alphabetically?
        if (sort) {
            all = new TreeMap<String,POJOPropertyBuilder>();
        } else {
            all = new LinkedHashMap<String,POJOPropertyBuilder>(size+size);
        }

        for (POJOPropertyBuilder prop : props.values()) {
            all.put(prop.getName(), prop);
        }
        Map<String,POJOPropertyBuilder> ordered = new LinkedHashMap<String,POJOPropertyBuilder>(size+size);
        // Ok: primarily by explicit order
        if (propertyOrder != null) {
            for (String name : propertyOrder) {
                POJOPropertyBuilder w = all.get(name);
                if (w == null) { // will also allow use of "implicit" names for sorting
                    for (POJOPropertyBuilder prop : props.values()) {
                        if (name.equals(prop.getInternalName())) {
                            w = prop;
                            // plus re-map to external name, to avoid dups:
                            name = prop.getName();
                            break;
                        }
                    }
                }
                if (w != null) {
                    ordered.put(name, w);
                }
            }
        }
        // And secondly by sorting Creator properties before other unordered properties
        if (_creatorProperties != null) {
            /* As per [databind#311], this is bit delicate; but if alphabetic ordering
             * is mandated, at least ensure creator properties are in alphabetic
             * order. Related question of creator vs non-creator is punted for now,
             * so creator properties still fully predate non-creator ones.
             */
            Collection<POJOPropertyBuilder> cr;
            if (sort) {
                TreeMap<String, POJOPropertyBuilder> sorted =
                        new TreeMap<String,POJOPropertyBuilder>();
                for (POJOPropertyBuilder prop : _creatorProperties) {
                    sorted.put(prop.getName(), prop);
                }
                cr = sorted.values();
            } else {
                cr = _creatorProperties;
            }
            for (POJOPropertyBuilder prop : cr) {
                // 16-Jan-2016, tatu: Related to [databind#1317], make sure not to accidentally
                //    add back pruned creator properties!
                String name = prop.getName();
                if (all.containsKey(name)) {
                    ordered.put(name, prop);
                }
            }
        }
        // And finally whatever is left (trying to put again will not change ordering)
        ordered.putAll(all);
        
        props.clear();
        props.putAll(ordered);
    }        

    /*
    /**********************************************************
    /* Internal methods; helpers
    /**********************************************************
     */

    protected void reportProblem(String msg) {
        throw new IllegalArgumentException("Problem with definition of "+_classDef+": "+msg);
    }

    protected POJOPropertyBuilder _property(Map<String, POJOPropertyBuilder> props,
            PropertyName name) {
        return _property(props, name.getSimpleName());
    }
    
    // !!! TODO: deprecate, require use of PropertyName
    protected POJOPropertyBuilder _property(Map<String, POJOPropertyBuilder> props,
            String implName)
    {
        POJOPropertyBuilder prop = props.get(implName);
        if (prop == null) {
            prop = new POJOPropertyBuilder(_config, _annotationIntrospector, _forSerialization,
                    PropertyName.construct(implName));
            props.put(implName, prop);
        }
        return prop;
    }

    private PropertyNamingStrategy _findNamingStrategy()
    {
        Object namingDef = (_annotationIntrospector == null)? null
                : _annotationIntrospector.findNamingStrategy(_classDef);
        if (namingDef == null) {
            return _config.getPropertyNamingStrategy();
        }
        if (namingDef instanceof PropertyNamingStrategy) {
            return (PropertyNamingStrategy) namingDef;
        }
        /* Alas, there's no way to force return type of "either class
         * X or Y" -- need to throw an exception after the fact
         */
        if (!(namingDef instanceof Class)) {
            throw new IllegalStateException("AnnotationIntrospector returned PropertyNamingStrategy definition of type "
                    +namingDef.getClass().getName()+"; expected type PropertyNamingStrategy or Class<PropertyNamingStrategy> instead");
        }
        Class<?> namingClass = (Class<?>)namingDef;
        // 09-Nov-2015, tatu: Need to consider pseudo-value of STD, which means "use default"
        if (namingClass == PropertyNamingStrategy.class) {
            return null;
        }
        
        if (!PropertyNamingStrategy.class.isAssignableFrom(namingClass)) {
            throw new IllegalStateException("AnnotationIntrospector returned Class "
                    +namingClass.getName()+"; expected Class<PropertyNamingStrategy>");
        }
        HandlerInstantiator hi = _config.getHandlerInstantiator();
        if (hi != null) {
            PropertyNamingStrategy pns = hi.namingStrategyInstance(_config, _classDef, namingClass);
            if (pns != null) {
                return pns;
            }
        }
        return (PropertyNamingStrategy) ClassUtil.createInstance(namingClass,
                    _config.canOverrideAccessModifiers());
    }

    protected void _updateCreatorProperty(POJOPropertyBuilder prop, List<POJOPropertyBuilder> creatorProperties) {
        if (creatorProperties != null) {
            for (int i = 0, len = creatorProperties.size(); i < len; ++i) {
                if (creatorProperties.get(i).getInternalName().equals(prop.getInternalName())) {
                    creatorProperties.set(i, prop);
                    break;
                }
            }
        }
    }
}

public class POJOPropertyBuilder
    extends BeanPropertyDefinition
    implements Comparable<POJOPropertyBuilder>
{
    /**
     * Whether property is being composed for serialization
     * (true) or deserialization (false)
     */
    protected final boolean _forSerialization;

    protected final MapperConfig<?> _config;

    protected final AnnotationIntrospector _annotationIntrospector;

    /**
     * External name of logical property; may change with
     * renaming (by new instance being constructed using
     * a new name)
     */
    protected final PropertyName _name;

    /**
     * Original internal name, derived from accessor, of this
     * property. Will not be changed by renaming.
     */
    protected final PropertyName _internalName;

    protected Linked<AnnotatedField> _fields;

    protected Linked<AnnotatedParameter> _ctorParameters;

    protected Linked<AnnotatedMethod> _getters;

    protected Linked<AnnotatedMethod> _setters;

    public POJOPropertyBuilder(MapperConfig<?> config, AnnotationIntrospector ai,
            boolean forSerialization, PropertyName internalName) {
        this(config, ai, forSerialization, internalName, internalName);
    }

    protected POJOPropertyBuilder(MapperConfig<?> config, AnnotationIntrospector ai,
            boolean forSerialization, PropertyName internalName, PropertyName name)
    {
        _config = config;
        _annotationIntrospector = ai;
        _internalName = internalName;
        _name = name;
        _forSerialization = forSerialization;
    }

    public POJOPropertyBuilder(POJOPropertyBuilder src, PropertyName newName)
    {
        _config = src._config;
        _annotationIntrospector = src._annotationIntrospector;
        _internalName = src._internalName;
        _name = newName;
        _fields = src._fields;
        _ctorParameters = src._ctorParameters;
        _getters = src._getters;
        _setters = src._setters;
        _forSerialization = src._forSerialization;
    }
    
    /*
    /**********************************************************
    /* Fluent factory methods
    /**********************************************************
     */

    @Override
    public POJOPropertyBuilder withName(PropertyName newName) {
        return new POJOPropertyBuilder(this, newName);
    }

    @Override
    public POJOPropertyBuilder withSimpleName(String newSimpleName)
    {
        PropertyName newName = _name.withSimpleName(newSimpleName);
        return (newName == _name) ? this : new POJOPropertyBuilder(this, newName);
    }
    
    /*
    /**********************************************************
    /* Comparable implementation: sort alphabetically, except
    /* that properties with constructor parameters sorted
    /* before other properties
    /**********************************************************
     */

    @Override
    public int compareTo(POJOPropertyBuilder other)
    {
        // first, if one has ctor params, that should come first:
        if (_ctorParameters != null) {
            if (other._ctorParameters == null) {
                return -1;
            }
        } else if (other._ctorParameters != null) {
            return 1;
        }
        /* otherwise sort by external name (including sorting of
         * ctor parameters)
         */
        return getName().compareTo(other.getName());
    }

    /*
    /**********************************************************
    /* BeanPropertyDefinition implementation, name/type
    /**********************************************************
     */

    @Override
    public String getName() {
        return (_name == null) ? null : _name.getSimpleName();
    }

    @Override
    public PropertyName getFullName() {
        return _name;
    }

    @Override
    public boolean hasName(PropertyName name) {
        return _name.equals(name);
    }

    @Override
    public String getInternalName() { return _internalName.getSimpleName(); }

    @Override
    public PropertyName getWrapperName() {
        /* 13-Mar-2013, tatu: Accessing via primary member SHOULD work,
         *   due to annotation merging. However, I have seen some problems
         *   with this access (for other annotations)... so if this should
         *   occur, try commenting out full traversal code
         */
        AnnotatedMember member = getPrimaryMember();
        return (member == null || _annotationIntrospector == null) ? null
                : _annotationIntrospector.findWrapperName(member);
    	/*
        return fromMemberAnnotations(new WithMember<PropertyName>() {
            @Override
            public PropertyName withMember(AnnotatedMember member) {
                return _annotationIntrospector.findWrapperName(member);
            }
        });
        */
    }

    @Override
    public boolean isExplicitlyIncluded() {
        return _anyExplicits(_fields)
                || _anyExplicits(_getters)
                || _anyExplicits(_setters)
                // 16-Jan-2016, tatu: Creator names are special, in that name should exist too;
                //   reason for this is [databind#1317]. Let's hope this works well, may need
                //   to tweak further if this lowers visibility
//                || _anyExplicits(_ctorParameters)
                || _anyExplicitNames(_ctorParameters)
                ;
    }

    @Override
    public boolean isExplicitlyNamed() {
        return _anyExplicitNames(_fields)
                || _anyExplicitNames(_getters)
                || _anyExplicitNames(_setters)
                || _anyExplicitNames(_ctorParameters)
                ;
    }
    
    /*
    /**********************************************************
    /* BeanPropertyDefinition implementation, accessor access
    /**********************************************************
     */

    @Override
    public boolean hasGetter() { return _getters != null; }

    @Override
    public boolean hasSetter() { return _setters != null; }

    @Override
    public boolean hasField() { return _fields != null; }

    @Override
    public boolean hasConstructorParameter() { return _ctorParameters != null; }

    @Override
    public boolean couldDeserialize() {
        return (_ctorParameters != null) || (_setters != null) || (_fields != null);
    }

    @Override
    public boolean couldSerialize() {
        return (_getters != null) || (_fields != null);
    }

    @Override
    public AnnotatedMethod getGetter()
    {
        // Easy with zero or one getters...
        Linked<AnnotatedMethod> curr = _getters;
        if (curr == null) {
            return null;
        }
        Linked<AnnotatedMethod> next = curr.next;
        if (next == null) {
            return curr.value;
        }
        // But if multiple, verify that they do not conflict...
        for (; next != null; next = next.next) {
            /* [JACKSON-255] Allow masking, i.e. do not report exception if one
             *   is in super-class from the other
             */
            Class<?> currClass = curr.value.getDeclaringClass();
            Class<?> nextClass = next.value.getDeclaringClass();
            if (currClass != nextClass) {
                if (currClass.isAssignableFrom(nextClass)) { // next is more specific
                    curr = next;
                    continue;
                }
                if (nextClass.isAssignableFrom(currClass)) { // current more specific
                    continue;
                }
            }
            /* 30-May-2014, tatu: Three levels of precedence:
             * 
             * 1. Regular getters ("getX")
             * 2. Is-getters ("isX")
             * 3. Implicit, possible getters ("x")
             */
            int priNext = _getterPriority(next.value);
            int priCurr = _getterPriority(curr.value);

            if (priNext != priCurr) {
                if (priNext < priCurr) {
                    curr = next;
                }
                continue;
            }
            throw new IllegalArgumentException("Conflicting getter definitions for property \""+getName()+"\": "
                    +curr.value.getFullName()+" vs "+next.value.getFullName());
        }
        // One more thing; to avoid having to do it again...
        _getters = curr.withoutNext();
        return curr.value;
    }
    
    @Override
    public AnnotatedMethod getSetter()
    {
        // Easy with zero or one getters...
        Linked<AnnotatedMethod> curr = _setters;
        if (curr == null) {
            return null;
        }
        Linked<AnnotatedMethod> next = curr.next;
        if (next == null) {
            return curr.value;
        }
        // But if multiple, verify that they do not conflict...
        for (; next != null; next = next.next) {
            // Allow masking, i.e. do not fail if one is in super-class from the other
            Class<?> currClass = curr.value.getDeclaringClass();
            Class<?> nextClass = next.value.getDeclaringClass();
            if (currClass != nextClass) {
                if (currClass.isAssignableFrom(nextClass)) { // next is more specific
                    curr = next;
                    continue;
                }
                if (nextClass.isAssignableFrom(currClass)) { // current more specific
                    continue;
                }
            }
            AnnotatedMethod nextM = next.value;
            AnnotatedMethod currM = curr.value;

            /* 30-May-2014, tatu: Two levels of precedence:
             * 
             * 1. Regular setters ("setX(...)")
             * 2. Implicit, possible setters ("x(...)")
             */
            int priNext = _setterPriority(nextM);
            int priCurr = _setterPriority(currM);

            if (priNext != priCurr) {
                if (priNext < priCurr) {
                    curr = next;
                }
                continue;
            }
            // 11-Dec-2015, tatu: As per [databind#1033] allow pluggable conflict resolution
            if (_annotationIntrospector != null) {
                AnnotatedMethod pref = _annotationIntrospector.resolveSetterConflict(_config,
                        currM, nextM);
                
                // note: should be one of nextM/currM; but no need to check
                if (pref == currM) {
                    continue;
                }
                if (pref == nextM) {
                    curr = next;
                    continue;
                }
            }
            throw new IllegalArgumentException(String.format(
 "Conflicting setter definitions for property \"%s\": %s vs %s",
 getName(), curr.value.getFullName(), next.value.getFullName()));
        }
        // One more thing; to avoid having to do it again...
        _setters = curr.withoutNext();
        return curr.value;
    }

    @Override
    public AnnotatedField getField()
    {
        if (_fields == null) {
            return null;
        }
        // If multiple, verify that they do not conflict...
        AnnotatedField field = _fields.value;
        Linked<AnnotatedField> next = _fields.next;
        for (; next != null; next = next.next) {
            AnnotatedField nextField = next.value;
            Class<?> fieldClass = field.getDeclaringClass();
            Class<?> nextClass = nextField.getDeclaringClass();
            if (fieldClass != nextClass) {
                if (fieldClass.isAssignableFrom(nextClass)) { // next is more specific
                    field = nextField;
                    continue;
                }
                if (nextClass.isAssignableFrom(fieldClass)) { // getter more specific
                    continue;
                }
            }
            throw new IllegalArgumentException("Multiple fields representing property \""+getName()+"\": "
                    +field.getFullName()+" vs "+nextField.getFullName());
        }
        return field;
    }

    @Override
    public AnnotatedParameter getConstructorParameter()
    {
        if (_ctorParameters == null) {
            return null;
        }
        /* Hmmh. Checking for constructor parameters is trickier; for one,
         * we must allow creator and factory method annotations.
         * If this is the case, constructor parameter has the precedence.
         * 
         * So, for now, just try finding the first constructor parameter;
         * if none, first factory method. And don't check for dups, if we must,
         * can start checking for them later on.
         */
        Linked<AnnotatedParameter> curr = _ctorParameters;
        do {
            if (curr.value.getOwner() instanceof AnnotatedConstructor) {
                return curr.value;
            }
            curr = curr.next;
        } while (curr != null);
        return _ctorParameters.value;
    }

    @Override
    public Iterator<AnnotatedParameter> getConstructorParameters() {
        if (_ctorParameters == null) {
            return ClassUtil.emptyIterator();
        }
        return new MemberIterator<AnnotatedParameter>(_ctorParameters);
    }
    
    @Override
    public AnnotatedMember getAccessor()
    {
        AnnotatedMember m = getGetter();
        if (m == null) {
            m = getField();
        }
        return m;
    }

    @Override
    public AnnotatedMember getMutator()
    {
        AnnotatedMember m = getConstructorParameter();
        if (m == null) {
            m = getSetter();
            if (m == null) {
                m = getField();
            }
        }
        return m;
    }

    @Override
    public AnnotatedMember getNonConstructorMutator() {
        AnnotatedMember m = getSetter();
        if (m == null) {
            m = getField();
        }
        return m;
    }

    @Override
    public AnnotatedMember getPrimaryMember() {
        if (_forSerialization) {
            return getAccessor();
        }
        return getMutator();
    }

    protected int _getterPriority(AnnotatedMethod m)
    {
        final String name = m.getName();
        // [databind#238]: Also, regular getters have precedence over "is-getters"
        if (name.startsWith("get") && name.length() > 3) {
            // should we check capitalization?
            return 1;
        }
        if (name.startsWith("is") && name.length() > 2) {
            return 2;
        }
        return 3;
    }

    protected int _setterPriority(AnnotatedMethod m)
    {
        final String name = m.getName();
        if (name.startsWith("set") && name.length() > 3) {
            // should we check capitalization?
            return 1;
        }
        return 2;
    }

    /*
    /**********************************************************
    /* Implementations of refinement accessors
    /**********************************************************
     */

    @Override
    public Class<?>[] findViews() {
        return fromMemberAnnotations(new WithMember<Class<?>[]>() {
            @Override
            public Class<?>[] withMember(AnnotatedMember member) {
                return _annotationIntrospector.findViews(member);
            }
        });
    }

    @Override
    public AnnotationIntrospector.ReferenceProperty findReferenceType() {
        return fromMemberAnnotations(new WithMember<AnnotationIntrospector.ReferenceProperty>() {
            @Override
            public AnnotationIntrospector.ReferenceProperty withMember(AnnotatedMember member) {
                return _annotationIntrospector.findReferenceType(member);
            }
        });
    }

    @Override
    public boolean isTypeId() {
        Boolean b = fromMemberAnnotations(new WithMember<Boolean>() {
            @Override
            public Boolean withMember(AnnotatedMember member) {
                return _annotationIntrospector.isTypeId(member);
            }
        });
        return (b != null) && b.booleanValue();
    }

    @Override
    public PropertyMetadata getMetadata() {
        final Boolean b = _findRequired();
        final String desc = _findDescription();
        final Integer idx = _findIndex();
        final String def = _findDefaultValue();
        if (b == null && idx == null && def == null) {
            return (desc == null) ? PropertyMetadata.STD_REQUIRED_OR_OPTIONAL
                    : PropertyMetadata.STD_REQUIRED_OR_OPTIONAL.withDescription(desc);
        }
        return PropertyMetadata.construct(b.booleanValue(), desc, idx, def);
    }

    protected Boolean _findRequired() {
       return fromMemberAnnotations(new WithMember<Boolean>() {
            @Override
            public Boolean withMember(AnnotatedMember member) {
                return _annotationIntrospector.hasRequiredMarker(member);
            }
        });
    }
    
    protected String _findDescription() {
        return fromMemberAnnotations(new WithMember<String>() {
            @Override
            public String withMember(AnnotatedMember member) {
                return _annotationIntrospector.findPropertyDescription(member);
            }
        });
    }

    protected Integer _findIndex() {
        return fromMemberAnnotations(new WithMember<Integer>() {
            @Override
            public Integer withMember(AnnotatedMember member) {
                return _annotationIntrospector.findPropertyIndex(member);
            }
        });
    }

    protected String _findDefaultValue() {
        return fromMemberAnnotations(new WithMember<String>() {
            @Override
            public String withMember(AnnotatedMember member) {
                return _annotationIntrospector.findPropertyDefaultValue(member);
            }
        });
    }
    
    @Override
    public ObjectIdInfo findObjectIdInfo() {
        return fromMemberAnnotations(new WithMember<ObjectIdInfo>() {
            @Override
            public ObjectIdInfo withMember(AnnotatedMember member) {
                ObjectIdInfo info = _annotationIntrospector.findObjectIdInfo(member);
                if (info != null) {
                    info = _annotationIntrospector.findObjectReferenceInfo(member, info);
                }
                return info;
            }
        });
    }

    @Override
    public JsonInclude.Value findInclusion() {
        AnnotatedMember a = getAccessor();
        // 16-Apr-2106, tatu: Let's include per-type default inclusion too
        // 17-Aug-2016, tatu: Do NOT include global, or per-type defaults, because
        //    not all of this information (specifically, enclosing type's settings)
        //    is available here
        JsonInclude.Value v = (_annotationIntrospector == null) ?
                null : _annotationIntrospector.findPropertyInclusion(a);
        return (v == null) ? JsonInclude.Value.empty() : v;
    }

    public JsonProperty.Access findAccess() {
        return fromMemberAnnotationsExcept(new WithMember<JsonProperty.Access>() {
            @Override
            public JsonProperty.Access withMember(AnnotatedMember member) {
                return _annotationIntrospector.findPropertyAccess(member);
            }
        }, JsonProperty.Access.AUTO);
    }
    
    /*
    /**********************************************************
    /* Data aggregation
    /**********************************************************
     */
    
    public void addField(AnnotatedField a, PropertyName name, boolean explName, boolean visible, boolean ignored) {
        _fields = new Linked<AnnotatedField>(a, _fields, name, explName, visible, ignored);
    }

    public void addCtor(AnnotatedParameter a, PropertyName name, boolean explName, boolean visible, boolean ignored) {
        _ctorParameters = new Linked<AnnotatedParameter>(a, _ctorParameters, name, explName, visible, ignored);
    }

    public void addGetter(AnnotatedMethod a, PropertyName name, boolean explName, boolean visible, boolean ignored) {
        _getters = new Linked<AnnotatedMethod>(a, _getters, name, explName, visible, ignored);
    }

    public void addSetter(AnnotatedMethod a, PropertyName name, boolean explName, boolean visible, boolean ignored) {
        _setters = new Linked<AnnotatedMethod>(a, _setters, name, explName, visible, ignored);
    }

    /**
     * Method for adding all property members from specified collector into
     * this collector.
     */
    public void addAll(POJOPropertyBuilder src)
    {
        _fields = merge(_fields, src._fields);
        _ctorParameters = merge(_ctorParameters, src._ctorParameters);
        _getters= merge(_getters, src._getters);
        _setters = merge(_setters, src._setters);
    }

    private static <T> Linked<T> merge(Linked<T> chain1, Linked<T> chain2)
    {
        if (chain1 == null) {
            return chain2;
        }
        if (chain2 == null) {
            return chain1;
        }
        return chain1.append(chain2);
    }

    /*
    /**********************************************************
    /* Modifications
    /**********************************************************
     */

    /**
     * Method called to remove all entries that are marked as
     * ignored.
     */
    public void removeIgnored()
    {
        _fields = _removeIgnored(_fields);
        _getters = _removeIgnored(_getters);
        _setters = _removeIgnored(_setters);
        _ctorParameters = _removeIgnored(_ctorParameters);
    }

    /**
     * @param inferMutators Whether mutators can be "pulled in" by visible
     *    accessors or not. 
     */
    public void removeNonVisible(boolean inferMutators)
    {
        /* 07-Jun-2015, tatu: With 2.6, we will allow optional definition
         *  of explicit access type for property; if not "AUTO", it will
         *  dictate how visibility checks are applied.
         */
        JsonProperty.Access acc = findAccess();
        if (acc == null) {
            acc = JsonProperty.Access.AUTO;
        }
        switch (acc) {
        case READ_ONLY:
            // Remove setters, creators for sure, but fields too if deserializing
            _setters = null;
            _ctorParameters = null;
            if (!_forSerialization) {
                _fields = null;
            }
            break;
        case READ_WRITE:
            // no trimming whatsoever?
            break;
        case WRITE_ONLY:
            // remove getters, definitely, but also fields if serializing
            _getters = null;
            if (_forSerialization) {
                _fields = null;
            }
            break;
        default:
        case AUTO: // the default case: base it on visibility
            _getters = _removeNonVisible(_getters);
            _ctorParameters = _removeNonVisible(_ctorParameters);
    
            if (!inferMutators || (_getters == null)) {
                _fields = _removeNonVisible(_fields);
                _setters = _removeNonVisible(_setters);
            }
        }
    }

    /**
     * Mutator that will simply drop any constructor parameters property may have.
     * 
     * @since 2.5
     */
    public void removeConstructors() {
        _ctorParameters = null;
    }
    
    /**
     * Method called to trim unnecessary entries, such as implicit
     * getter if there is an explict one available. This is important
     * for later stages, to avoid unnecessary conflicts.
     */
    public void trimByVisibility()
    {
        _fields = _trimByVisibility(_fields);
        _getters = _trimByVisibility(_getters);
        _setters = _trimByVisibility(_setters);
        _ctorParameters = _trimByVisibility(_ctorParameters);
    }

    @SuppressWarnings("unchecked")
    public void mergeAnnotations(boolean forSerialization)
    {
        if (forSerialization) {
            if (_getters != null) {
                AnnotationMap ann = _mergeAnnotations(0, _getters, _fields, _ctorParameters, _setters);
                _getters = _applyAnnotations(_getters, ann);
            } else if (_fields != null) {
                AnnotationMap ann = _mergeAnnotations(0, _fields, _ctorParameters, _setters);
                _fields = _applyAnnotations(_fields, ann);
            }
        } else { // for deserialization
            if (_ctorParameters != null) {
                AnnotationMap ann = _mergeAnnotations(0, _ctorParameters, _setters, _fields, _getters);
                _ctorParameters = _applyAnnotations(_ctorParameters, ann);
            } else if (_setters != null) {
                AnnotationMap ann = _mergeAnnotations(0, _setters, _fields, _getters);
                _setters = _applyAnnotations(_setters, ann);
            } else if (_fields != null) {
                AnnotationMap ann = _mergeAnnotations(0, _fields, _getters);
                _fields = _applyAnnotations(_fields, ann);
            }
        }
    }

    private AnnotationMap _mergeAnnotations(int index,
            Linked<? extends AnnotatedMember>... nodes)
    {
        AnnotationMap ann = _getAllAnnotations(nodes[index]);
        while (++index < nodes.length) {
            if (nodes[index] != null) {
              return AnnotationMap.merge(ann, _mergeAnnotations(index, nodes));
            }
        }
        return ann;
    }

    /**
     * Replacement, as per [databind#868], of simple access to annotations, which
     * does "deep merge" if an as necessary.
     *<pre>
     * nodes[index].value.getAllAnnotations()
     *</pre>
     * 
     * @since 2.6
     */
    private <T extends AnnotatedMember> AnnotationMap _getAllAnnotations(Linked<T> node) {
        AnnotationMap ann = node.value.getAllAnnotations();
        if (node.next != null) {
            ann = AnnotationMap.merge(ann, _getAllAnnotations(node.next));
        }
        return ann;
    }

    /**
     * Helper method to handle recursive merging of annotations within accessor class,
     * to ensure no annotations are accidentally dropped within chain when non-visible
     * and secondary accessors are pruned later on.
     *<p>
     * See [databind#868] for more information.
     *
     * @since 2.6
     */
    private <T extends AnnotatedMember> Linked<T> _applyAnnotations(Linked<T> node, AnnotationMap ann) {
        @SuppressWarnings("unchecked")
        T value = (T) node.value.withAnnotations(ann);
        if (node.next != null) {
            node = node.withNext(_applyAnnotations(node.next, ann));
        }
        return node.withValue(value);
    }

    private <T> Linked<T> _removeIgnored(Linked<T> node)
    {
        if (node == null) {
            return node;
        }
        return node.withoutIgnored();
    }

    private <T> Linked<T> _removeNonVisible(Linked<T> node)
    {
        if (node == null) {
            return node;
        }
        return node.withoutNonVisible();
    }

    private <T> Linked<T> _trimByVisibility(Linked<T> node)
    {
        if (node == null) {
            return node;
        }
        return node.trimByVisibility();
    }
        
    /*
    /**********************************************************
    /* Accessors for aggregate information
    /**********************************************************
     */

    private <T> boolean _anyExplicits(Linked<T> n)
    {
        for (; n != null; n = n.next) {
            if (n.name != null && n.name.hasSimpleName()) {
                return true;
            }
        }
        return false;
    }

    private <T> boolean _anyExplicitNames(Linked<T> n)
    {
        for (; n != null; n = n.next) {
            if (n.name != null && n.isNameExplicit) {
                return true;
            }
        }
        return false;
    }

    public boolean anyVisible() {
        return _anyVisible(_fields)
            || _anyVisible(_getters)
            || _anyVisible(_setters)
            || _anyVisible(_ctorParameters)
        ;
    }

    private <T> boolean _anyVisible(Linked<T> n)
    {
        for (; n != null; n = n.next) {
            if (n.isVisible) {
                return true;
            }
        }
        return false;
    }
    
    public boolean anyIgnorals() {
        return _anyIgnorals(_fields)
            || _anyIgnorals(_getters)
            || _anyIgnorals(_setters)
            || _anyIgnorals(_ctorParameters)
        ;
    }

    private <T> boolean _anyIgnorals(Linked<T> n)
    {
        for (; n != null; n = n.next) {
            if (n.isMarkedIgnored) {
                return true;
            }
        }
        return false;
    }

    /**
     * Method called to find out set of explicit names for accessors
     * bound together due to implicit name.
     * 
     * @since 2.4
     */
    public Set<PropertyName> findExplicitNames()
    {
        Set<PropertyName> renamed = null;
        renamed = _findExplicitNames(_fields, renamed);
        renamed = _findExplicitNames(_getters, renamed);
        renamed = _findExplicitNames(_setters, renamed);
        renamed = _findExplicitNames(_ctorParameters, renamed);
        if (renamed == null) {
            return Collections.emptySet();
        }
        return renamed;
    }

    /**
     * Method called when a previous call to {@link #findExplicitNames} found
     * multiple distinct explicit names, and the property this builder represents
     * basically needs to be broken apart and replaced by a set of more than
     * one properties.
     * 
     * @since 2.4
     */
    public Collection<POJOPropertyBuilder> explode(Collection<PropertyName> newNames)
    {
        HashMap<PropertyName,POJOPropertyBuilder> props = new HashMap<PropertyName,POJOPropertyBuilder>();
        _explode(newNames, props, _fields);
        _explode(newNames, props, _getters);
        _explode(newNames, props, _setters);
        _explode(newNames, props, _ctorParameters);
        return props.values();
    }

    @SuppressWarnings("unchecked")
    private void _explode(Collection<PropertyName> newNames,
            Map<PropertyName,POJOPropertyBuilder> props,
            Linked<?> accessors)
    {
        final Linked<?> firstAcc = accessors; // clumsy, part 1
        for (Linked<?> node = accessors; node != null; node = node.next) {
            PropertyName name = node.name;
            if (!node.isNameExplicit || name == null) { // no explicit name -- problem!
                // [databind#541] ... but only as long as it's visible
                if (!node.isVisible) {
                    continue;
                }
                
                throw new IllegalStateException("Conflicting/ambiguous property name definitions (implicit name '"
                        +_name+"'): found multiple explicit names: "
                        +newNames+", but also implicit accessor: "+node);
            }
            POJOPropertyBuilder prop = props.get(name);
            if (prop == null) {
                prop = new POJOPropertyBuilder(_config, _annotationIntrospector, _forSerialization,
                        _internalName, name);
                props.put(name, prop);
            }
            // ultra-clumsy, part 2 -- lambdas would be nice here
            if (firstAcc == _fields) {
                Linked<AnnotatedField> n2 = (Linked<AnnotatedField>) node;
                prop._fields = n2.withNext(prop._fields);
            } else if (firstAcc == _getters) {
                Linked<AnnotatedMethod> n2 = (Linked<AnnotatedMethod>) node;
                prop._getters = n2.withNext(prop._getters);
            } else if (firstAcc == _setters) {
                Linked<AnnotatedMethod> n2 = (Linked<AnnotatedMethod>) node;
                prop._setters = n2.withNext(prop._setters);
            } else if (firstAcc == _ctorParameters) {
                Linked<AnnotatedParameter> n2 = (Linked<AnnotatedParameter>) node;
                prop._ctorParameters = n2.withNext(prop._ctorParameters);
            } else {
                throw new IllegalStateException("Internal error: mismatched accessors, property: "+this);
            }
        }
    }
    
    private Set<PropertyName> _findExplicitNames(Linked<? extends AnnotatedMember> node,
            Set<PropertyName> renamed)
    {
        for (; node != null; node = node.next) {
            /* 30-Mar-2014, tatu: Second check should not be needed, but seems like
             *   removing it can cause nasty exceptions with certain version
             *   combinations (2.4 databind, an older module).
             *   So leaving it in for now until this is resolved
             *   (or version beyond 2.4)
             */
            if (!node.isNameExplicit || node.name == null) {
                continue;
            }
            if (renamed == null) {
                renamed = new HashSet<PropertyName>();
            }
            renamed.add(node.name);
        }
        return renamed;
    }
    
    // For trouble-shooting
    @Override
    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("[Property '").append(_name)
          .append("'; ctors: ").append(_ctorParameters)
          .append(", field(s): ").append(_fields)
          .append(", getter(s): ").append(_getters)
          .append(", setter(s): ").append(_setters)
          ;
        sb.append("]");
        return sb.toString();
    }
    
    /*
    /**********************************************************
    /* Helper methods
    /**********************************************************
     */

    /**
     * Helper method used for finding annotation values, from accessors
     * relevant to current usage (deserialization, serialization)
     */
    protected <T> T fromMemberAnnotations(WithMember<T> func)
    {
        T result = null;
        if (_annotationIntrospector != null) {
            if (_forSerialization) {
                if (_getters != null) {
                    result = func.withMember(_getters.value);
                }
            } else {
                if (_ctorParameters != null) {
                    result = func.withMember(_ctorParameters.value);
                }
                if (result == null && _setters != null) {
                    result = func.withMember(_setters.value);
                }
            }
            if (result == null && _fields != null) {
                result = func.withMember(_fields.value);
            }
        }
        return result;
    }

    protected <T> T fromMemberAnnotationsExcept(WithMember<T> func, T defaultValue)
    {
        if (_annotationIntrospector == null) {
            return null;
        }

        // NOTE: here we must ask ALL accessors, but the order varies between
        // serialization, deserialization
        if (_forSerialization) {
            if (_getters != null) {
                T result = func.withMember(_getters.value);
                if ((result != null) && (result != defaultValue)) {
                    return result;
                }
            }
            if (_fields != null) {
                T result = func.withMember(_fields.value);
                if ((result != null) && (result != defaultValue)) {
                    return result;
                }
            }
            if (_ctorParameters != null) {
                T result = func.withMember(_ctorParameters.value);
                if ((result != null) && (result != defaultValue)) {
                    return result;
                }
            }
            if (_setters != null) {
                T result = func.withMember(_setters.value);
                if ((result != null) && (result != defaultValue)) {
                    return result;
                }
            }
            return null;
        }
        if (_ctorParameters != null) {
            T result = func.withMember(_ctorParameters.value);
            if ((result != null) && (result != defaultValue)) {
                return result;
            }
        }
        if (_setters != null) {
            T result = func.withMember(_setters.value);
            if ((result != null) && (result != defaultValue)) {
                return result;
            }
        }
        if (_fields != null) {
            T result = func.withMember(_fields.value);
            if ((result != null) && (result != defaultValue)) {
                return result;
            }
        }
        if (_getters != null) {
            T result = func.withMember(_getters.value);
            if ((result != null) && (result != defaultValue)) {
                return result;
            }
        }
        return null;
    }
    
    /*
    /**********************************************************
    /* Helper classes
    /**********************************************************
     */

    private interface WithMember<T> {
        public T withMember(AnnotatedMember member);
    }

    /**
     * @since 2.5
     */
    protected static class MemberIterator<T extends AnnotatedMember>
        implements Iterator<T>
    {
        private Linked<T> next;
        
        public MemberIterator(Linked<T> first) {
            next = first;
        }
        
        @Override
        public boolean hasNext() {
            return (next != null);
        }

        @Override
        public T next() {
            if (next == null) throw new NoSuchElementException();
            T result = next.value;
            next = next.next;
            return result;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
        
    }
    
    /**
     * Node used for creating simple linked lists to efficiently store small sets
     * of things.
     */
    protected final static class Linked<T>
    {
        public final T value;
        public final Linked<T> next;

        public final PropertyName name;
        public final boolean isNameExplicit;
        public final boolean isVisible;
        public final boolean isMarkedIgnored;
        
        public Linked(T v, Linked<T> n,
                PropertyName name, boolean explName, boolean visible, boolean ignored)
        {
            value = v;
            next = n;
            // ensure that we'll never have missing names
            this.name = (name == null || name.isEmpty()) ? null : name;

            if (explName) {
                if (this.name == null) { // sanity check to catch internal problems
                    throw new IllegalArgumentException("Can not pass true for 'explName' if name is null/empty");
                }
                // 03-Apr-2014, tatu: But how about name-space only override?
                //   Probably should not be explicit? Or, need to merge somehow?
                if (!name.hasSimpleName()) {
                    explName = false;
                }
            }
            
            isNameExplicit = explName;
            isVisible = visible;
            isMarkedIgnored = ignored;
        }

        public Linked<T> withoutNext() {
            if (next == null) {
                return this;
            }
            return new Linked<T>(value, null, name, isNameExplicit, isVisible, isMarkedIgnored);
        }
        
        public Linked<T> withValue(T newValue) {
            if (newValue == value) {
                return this;
            }
            return new Linked<T>(newValue, next, name, isNameExplicit, isVisible, isMarkedIgnored);
        }
        
        public Linked<T> withNext(Linked<T> newNext) {
            if (newNext == next) {
                return this;
            }
            return new Linked<T>(value, newNext, name, isNameExplicit, isVisible, isMarkedIgnored);
        }
        
        public Linked<T> withoutIgnored() {
            if (isMarkedIgnored) {
                return (next == null) ? null : next.withoutIgnored();
            }
            if (next != null) {
                Linked<T> newNext = next.withoutIgnored();
                if (newNext != next) {
                    return withNext(newNext);
                }
            }
            return this;
        }
        
        public Linked<T> withoutNonVisible() {
            Linked<T> newNext = (next == null) ? null : next.withoutNonVisible();
            return isVisible ? withNext(newNext) : newNext;
        }

        /**
         * Method called to append given node(s) at the end of this
         * node chain.
         */
        protected Linked<T> append(Linked<T> appendable) {
            if (next == null) {
                return withNext(appendable);
            }
            return withNext(next.append(appendable));
        }

        public Linked<T> trimByVisibility() {
            if (next == null) {
                return this;
            }
            Linked<T> newNext = next.trimByVisibility();
            if (name != null) { // this already has highest; how about next one?
                if (newNext.name == null) { // next one not, drop it
                    return withNext(null);
                }
                //  both have it, keep
                return withNext(newNext);
            }
            if (newNext.name != null) { // next one has higher, return it...
                return newNext;
            }
            // neither has explicit name; how about visibility?
            if (isVisible == newNext.isVisible) { // same; keep both in current order
                return withNext(newNext);
            }
            return isVisible ? withNext(null) : newNext;
        }
        
        @Override
        public String toString() {
            String msg = value.toString()+"[visible="+isVisible+",ignore="+isMarkedIgnored
                    +",explicitName="+isNameExplicit+"]";
            if (next != null) {
                msg = msg + ", "+next.toString();
            }
            return msg;
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.deser.ReadOrWriteOnlyTest

## Test line
com.fasterxml.jackson.databind.exc.UnrecognizedPropertyException

## Error
Unrecognized field "fullName" (class com.fasterxml.jackson.databind.deser.ReadOrWriteOnlyTest$Pojo935), not marked as ignorable (2 known properties: "lastName", "firstName"])
 at [Source: {"firstName":"Foo","lastName":"Bar","fullName":"Foo Bar"}; line: 1, column: 49] (through reference chain: com.fasterxml.jackson.databind.deser.ReadOrWriteOnlyTest$Pojo935["fullName"])

## Error Code Block
```java
package com.fasterxml.jackson.databind.deser;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.*;

public class ReadOrWriteOnlyTest extends BaseMapTest
{
    // for [databind#935], verify read/write-only cases
    static class ReadXWriteY {
        @JsonProperty(access=JsonProperty.Access.READ_ONLY)
        public int x = 1;

        @JsonProperty(access=JsonProperty.Access.WRITE_ONLY)
        public int y = 2;

        public void setX(int x) {
            throw new Error("Should NOT set x");
        }

        public int getY() {
            throw new Error("Should NOT get y");
        }
    }

    public static class Pojo935
    {
        private String firstName = "Foo";
        private String lastName = "Bar";

        @JsonProperty(access = JsonProperty.Access.READ_ONLY)
        public String getFullName() {
            return firstName + " " + lastName;
        }

        public String getFirstName() {
            return firstName;
        }

        public void setFirstName(String n) {
            firstName = n;
        }

        public String getLastName() {
            return lastName;
        }

        public void setLastName(String n) {
            lastName = n;
        }
    }    

    /*
    /**********************************************************
    /* Test methods
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();

    // [databind#935]
    public void testReadOnlyAndWriteOnly() throws Exception
    {
        String json = MAPPER.writeValueAsString(new ReadXWriteY());
        assertEquals("{\"x\":1}", json);

        ReadXWriteY result = MAPPER.readValue("{\"x\":5, \"y\":6}", ReadXWriteY.class);
        assertNotNull(result);
        assertEquals(1, result.x);
        assertEquals(6, result.y);
    }

    public void testReadOnly935() throws Exception
    {
        String json = MAPPER.writeValueAsString(new Pojo935());
        Pojo935 result = MAPPER.readValue(json, Pojo935.class);
        assertNotNull(result);
    }
}

```
