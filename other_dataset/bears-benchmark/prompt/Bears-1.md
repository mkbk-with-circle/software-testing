## Buggy code
```java
public class CreatorCollector
{
    // Since 2.5
    protected final static int C_DEFAULT = 0;
    protected final static int C_STRING = 1;
    protected final static int C_INT = 2;
    protected final static int C_LONG = 3;
    protected final static int C_DOUBLE = 4;
    protected final static int C_BOOLEAN = 5;
    protected final static int C_DELEGATE = 6;
    protected final static int C_PROPS = 7;
    protected final static int C_ARRAY_DELEGATE = 8;

    protected final static String[] TYPE_DESCS = new String[] {
        "default",
        "String", "int", "long", "double", "boolean",
        "delegate", "property-based"
    };

    /// Type of bean being created
    final protected BeanDescription _beanDesc;

    final protected boolean _canFixAccess;

    /**
     * @since 2.7
     */
    final protected boolean _forceAccess;
    
    /**
     * Set of creators we have collected so far
     * 
     * @since 2.5
     */
    protected final AnnotatedWithParams[] _creators = new AnnotatedWithParams[9];

    /**
     * Bitmask of creators that were explicitly marked as creators; false for auto-detected
     * (ones included base on naming and/or visibility, not annotation)
     * 
     * @since 2.5
     */
    protected int _explicitCreators = 0;

    protected boolean _hasNonDefaultCreator = false;

    // when there are injectable values along with delegate:
    protected SettableBeanProperty[] _delegateArgs;

    protected SettableBeanProperty[] _arrayDelegateArgs;

    protected SettableBeanProperty[] _propertyBasedArgs;

    protected AnnotatedParameter _incompleteParameter;

    /*
    /**********************************************************
    /* Life-cycle
    /**********************************************************
     */
    
    public CreatorCollector(BeanDescription beanDesc, MapperConfig<?> config)
    {
        _beanDesc = beanDesc;
        _canFixAccess = config.canOverrideAccessModifiers();
        _forceAccess = config.isEnabled(MapperFeature.OVERRIDE_PUBLIC_ACCESS_MODIFIERS);
    }

    public ValueInstantiator constructValueInstantiator(DeserializationConfig config)
    {
        final JavaType delegateType = _computeDelegateType(_creators[C_DELEGATE], _delegateArgs);
        final JavaType arrayDelegateType = _computeDelegateType(_creators[C_ARRAY_DELEGATE], _arrayDelegateArgs);
        final JavaType type = _beanDesc.getType();

        // Any non-standard creator will prevent; with one exception: int-valued constructor
        // that standard containers have can be ignored
        if (!_hasNonDefaultCreator) {
            /* 10-May-2014, tatu: If we have nothing special, and we are dealing with one
             *   of "well-known" types, can create a non-reflection-based instantiator.
             */
            final Class<?> rawType = type.getRawClass();
            if (rawType == Collection.class || rawType == List.class || rawType == ArrayList.class) {
                return new Vanilla(Vanilla.TYPE_COLLECTION);
            }
            if (rawType == Map.class || rawType == LinkedHashMap.class) {
                return new Vanilla(Vanilla.TYPE_MAP);
            }
            if (rawType == HashMap.class) {
                return new Vanilla(Vanilla.TYPE_HASH_MAP);
            }
        }
        
        StdValueInstantiator inst = new StdValueInstantiator(config, type);
        inst.configureFromObjectSettings(_creators[C_DEFAULT],
                _creators[C_DELEGATE], delegateType, _delegateArgs,
                _creators[C_PROPS], _propertyBasedArgs);
        inst.configureFromArraySettings(_creators[C_ARRAY_DELEGATE], arrayDelegateType, _arrayDelegateArgs);
        inst.configureFromStringCreator(_creators[C_STRING]);
        inst.configureFromIntCreator(_creators[C_INT]);
        inst.configureFromLongCreator(_creators[C_LONG]);
        inst.configureFromDoubleCreator(_creators[C_DOUBLE]);
        inst.configureFromBooleanCreator(_creators[C_BOOLEAN]);
        inst.configureIncompleteParameter(_incompleteParameter);
        return inst;
    }
    
    /*
    /**********************************************************
    /* Setters
    /**********************************************************
     */
    
    /**
     * Method called to indicate the default creator: no-arguments
     * constructor or factory method that is called to instantiate
     * a value before populating it with data. Default creator is
     * only used if no other creators are indicated.
     * 
     * @param creator Creator method; no-arguments constructor or static
     *   factory method.
     */
    public void setDefaultCreator(AnnotatedWithParams creator) {
        _creators[C_DEFAULT] = _fixAccess(creator);
    }
    
    public void addStringCreator(AnnotatedWithParams creator, boolean explicit) {
        verifyNonDup(creator, C_STRING, explicit);
    }
    public void addIntCreator(AnnotatedWithParams creator, boolean explicit) {
        verifyNonDup(creator, C_INT, explicit);
    }
    public void addLongCreator(AnnotatedWithParams creator, boolean explicit) {
        verifyNonDup(creator, C_LONG, explicit);
    }
    public void addDoubleCreator(AnnotatedWithParams creator, boolean explicit) {
        verifyNonDup(creator, C_DOUBLE, explicit);
    }
    public void addBooleanCreator(AnnotatedWithParams creator, boolean explicit) {
        verifyNonDup(creator, C_BOOLEAN, explicit);
    }

    public void addDelegatingCreator(AnnotatedWithParams creator, boolean explicit,
            SettableBeanProperty[] injectables)
    {
        if (creator.getParameterType(0).isCollectionLikeType()) {
            verifyNonDup(creator, C_ARRAY_DELEGATE, explicit);
            _arrayDelegateArgs = injectables;
        } else {
            verifyNonDup(creator, C_DELEGATE, explicit);
            _delegateArgs = injectables;
        }
    }
    
    public void addPropertyCreator(AnnotatedWithParams creator, boolean explicit,
            SettableBeanProperty[] properties)
    {
        verifyNonDup(creator, C_PROPS, explicit);
        // Better ensure we have no duplicate names either...
        if (properties.length > 1) {
            HashMap<String,Integer> names = new HashMap<String,Integer>();
            for (int i = 0, len = properties.length; i < len; ++i) {
                String name = properties[i].getName();
                /* [Issue-13]: Need to consider Injectables, which may not have
                 *   a name at all, and need to be skipped
                 */
                if (name.length() == 0 && properties[i].getInjectableValueId() != null) {
                    continue;
                }
                Integer old = names.put(name, Integer.valueOf(i));
                if (old != null) {
                    throw new IllegalArgumentException("Duplicate creator property \""+name+"\" (index "+old+" vs "+i+")");
                }
            }
        }
        _propertyBasedArgs = properties;
    }

    public void addIncompeteParameter(AnnotatedParameter parameter) {
        if (_incompleteParameter == null) {
            _incompleteParameter = parameter;
        }
    }

    // Bunch of methods deprecated in 2.5, to be removed from 2.6 or later
    
    @Deprecated // since 2.5
    public void addStringCreator(AnnotatedWithParams creator) {
        addStringCreator(creator, false);
    }
    @Deprecated // since 2.5
    public void addIntCreator(AnnotatedWithParams creator) {
        addBooleanCreator(creator, false);
    }
    @Deprecated // since 2.5
    public void addLongCreator(AnnotatedWithParams creator) {
        addBooleanCreator(creator, false);
    }
    @Deprecated // since 2.5
    public void addDoubleCreator(AnnotatedWithParams creator) {
        addBooleanCreator(creator, false);
    }
    @Deprecated // since 2.5
    public void addBooleanCreator(AnnotatedWithParams creator) {
        addBooleanCreator(creator, false);
    }

    @Deprecated // since 2.5
    public void addDelegatingCreator(AnnotatedWithParams creator, CreatorProperty[] injectables) {
        addDelegatingCreator(creator, false, injectables);
    }

    @Deprecated // since 2.5
    public void addPropertyCreator(AnnotatedWithParams creator, CreatorProperty[] properties) {
        addPropertyCreator(creator, false, properties);
    }

    /*
    /**********************************************************
    /* Accessors
    /**********************************************************
     */

    /**
     * @since 2.1
     */
    public boolean hasDefaultCreator() {
        return _creators[C_DEFAULT] != null;
    }

    /**
     * @since 2.6
     */
    public boolean hasDelegatingCreator() {
        return _creators[C_DELEGATE] != null;
    }

    /**
     * @since 2.6
     */
    public boolean hasPropertyBasedCreator() {
        return _creators[C_PROPS] != null;
    }
    
    /*
    /**********************************************************
    /* Helper methods
    /**********************************************************
     */

    private JavaType _computeDelegateType(AnnotatedWithParams creator,
            SettableBeanProperty[] delegateArgs)
    {
        if (!_hasNonDefaultCreator || (creator == null)) {
            return null;
        }
        // need to find type...
        int ix = 0;
        if (delegateArgs != null) {
            for (int i = 0, len = delegateArgs.length; i < len; ++i) {
                if (delegateArgs[i] == null) { // marker for delegate itself
                    ix = i;
                    break;
                }
            }
        }
        return creator.getParameterType(ix);
    }

    private <T extends AnnotatedMember> T _fixAccess(T member)
    {
        if (member != null && _canFixAccess) {
            ClassUtil.checkAndFixAccess((Member) member.getAnnotated(), _forceAccess);
        }
        return member;
    }

    protected void verifyNonDup(AnnotatedWithParams newOne, int typeIndex, boolean explicit)
    {
        final int mask = (1 << typeIndex);
        _hasNonDefaultCreator = true;
        AnnotatedWithParams oldOne = _creators[typeIndex];
        // already had an explicitly marked one?
        if (oldOne != null) {
            boolean verify;

            if ((_explicitCreators & mask) != 0) { // already had explicitly annotated, leave as-is
                // but skip, if new one not annotated
                if (!explicit) {
                    return;
                }
                // both explicit: verify
                verify = true;
            } else {
                // otherwise only verify if neither explicitly annotated.
                verify = !explicit;
            }

            // one more thing: ok to override in sub-class
            if (verify && (oldOne.getClass() == newOne.getClass())) {
                // [databind#667]: avoid one particular class of bogus problems
                Class<?> oldType = oldOne.getRawParameterType(0);
                Class<?> newType = newOne.getRawParameterType(0);

                if (oldType == newType) {
                    throw new IllegalArgumentException("Conflicting "+TYPE_DESCS[typeIndex]
                            +" creators: already had explicitly marked "+oldOne+", encountered "+newOne);
                }
                // otherwise, which one to choose?
                if (newType.isAssignableFrom(oldType)) {
                    // new type more generic, use old
                    return;
                }
                // new type more specific, use it
            }
        }
        if (explicit) {
            _explicitCreators |= mask;
        }
        _creators[typeIndex] = _fixAccess(newOne);
    }

    /*
    /**********************************************************
    /* Helper class(es)
    /**********************************************************
     */

    protected final static class Vanilla
        extends ValueInstantiator
        implements java.io.Serializable
    {
        private static final long serialVersionUID = 1L;

        public final static int TYPE_COLLECTION = 1;
        public final static int TYPE_MAP = 2;
        public final static int TYPE_HASH_MAP = 3;

        private final int _type;
        
        public Vanilla(int t) {
            _type = t;
        }
        
        
        @Override
        public String getValueTypeDesc() {
            switch (_type) {
            case TYPE_COLLECTION: return ArrayList.class.getName();
            case TYPE_MAP: return LinkedHashMap.class.getName();
            case TYPE_HASH_MAP: return HashMap.class.getName();
            }
            return Object.class.getName();
        }

        @Override
        public boolean canInstantiate() { return true; }

        @Override
        public boolean canCreateUsingDefault() {  return true; }

        @Override
        public Object createUsingDefault(DeserializationContext ctxt) throws IOException {
            switch (_type) {
            case TYPE_COLLECTION: return new ArrayList<Object>();
            case TYPE_MAP: return new LinkedHashMap<String,Object>();
            case TYPE_HASH_MAP: return new HashMap<String,Object>();
            }
            throw new IllegalStateException("Unknown type "+_type);
        }
    }
}
```

## Failed test
com.fasterxml.jackson.databind.creators.Creator1476Test

## Test line
com.fasterxml.jackson.databind.JsonMappingException

## Error
Could not find creator property with name 'intField' (in class com.fasterxml.jackson.databind.creators.Creator1476Test$SimplePojo)
 at [Source: { "intField": 1, "stringField": "foo" }; line: 1, column: 1]

## Error Code Block
```java
package com.fasterxml.jackson.databind.creators;

import com.fasterxml.jackson.annotation.*;

import com.fasterxml.jackson.databind.*;

public class Creator1476Test extends BaseMapTest
{
    static final class SimplePojo {
        private final int intField;
        private final String stringField;

        public SimplePojo(@JsonProperty("intField") int intField) {
          this(intField, "empty");
        }

        public SimplePojo(@JsonProperty("stringField") String stringField) {
          this(-1, stringField);
        }

        @JsonCreator
        public SimplePojo(@JsonProperty("intField") int intField, @JsonProperty("stringField") String stringField) {
          this.intField = intField;
          this.stringField = stringField;
        }

        public int getIntField() {
          return intField;
        }

        public String getStringField() {
          return stringField;
        }
    }

    public void testConstructorChoice() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        SimplePojo pojo = mapper.readValue("{ \"intField\": 1, \"stringField\": \"foo\" }", SimplePojo.class);

        assertEquals(1, pojo.getIntField());
        assertEquals("foo", pojo.getStringField());
    }
}

```
