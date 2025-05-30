## Buggy code
```java
public class BeanPropertyMap
    implements Iterable<SettableBeanProperty>,
        java.io.Serializable
{
    private static final long serialVersionUID = 2L;

    /**
     * @since 2.5
     */
    protected final boolean _caseInsensitive;

    private int _hashMask;

    /**
     * Number of entries stored in the hash area.
     */
    private int _size;
    
    private int _spillCount;

    /**
     * Hash area that contains key/property pairs in adjacent elements.
     */
    private Object[] _hashArea;

    /**
     * Array of properties in the exact order they were handed in. This is
     * used by as-array serialization, deserialization.
     */
    private SettableBeanProperty[] _propsInOrder;

    public BeanPropertyMap(boolean caseInsensitive, Collection<SettableBeanProperty> props)
    {
        _caseInsensitive = caseInsensitive;
        _propsInOrder = props.toArray(new SettableBeanProperty[props.size()]);
        init(props);
    }

    /**
     * @since 2.8
     */
    protected BeanPropertyMap(BeanPropertyMap base, boolean caseInsensitive)
    {
        _caseInsensitive = caseInsensitive;

        // 16-May-2016, tatu: Alas, not enough to just change flag, need to re-init
        //    as well.
        _propsInOrder = Arrays.copyOf(base._propsInOrder, base._propsInOrder.length);
        init(Arrays.asList(_propsInOrder));
    }

    /**
     * Mutant factory method that constructs a new instance if desired case-insensitivity
     * state differs from the state of this instance; if states are the same, returns
     * <code>this</code>.
     *
     * @since 2.8
     */
    public BeanPropertyMap withCaseInsensitivity(boolean state) {
        if (_caseInsensitive == state) {
            return this;
        }
        return new BeanPropertyMap(this, state);
    }

    protected void init(Collection<SettableBeanProperty> props)
    {
        _size = props.size();
        
        // First: calculate size of primary hash area
        final int hashSize = findSize(_size);
        _hashMask = hashSize-1;

        // and allocate enough to contain primary/secondary, expand for spillovers as need be
        int alloc = (hashSize + (hashSize>>1)) * 2;
        Object[] hashed = new Object[alloc];
        int spillCount = 0;

        for (SettableBeanProperty prop : props) {
            // Due to removal, renaming, theoretically possible we'll have "holes" so:
            if (prop == null) {
                continue;
            }
            
            String key = getPropertyName(prop);
            int slot = _hashCode(key);
            int ix = (slot<<1);

            // primary slot not free?
            if (hashed[ix] != null) {
                // secondary?
                ix = (hashSize + (slot >> 1)) << 1;
                if (hashed[ix] != null) {
                    // ok, spill over.
                    ix = ((hashSize + (hashSize >> 1) ) << 1) + spillCount;
                    spillCount += 2;
                    if (ix >= hashed.length) {
                        hashed = Arrays.copyOf(hashed, hashed.length + 4);
                    }
                }
            }
//System.err.println(" add '"+key+" at #"+(ix>>1)+"/"+size+" (hashed at "+slot+")");             
            hashed[ix] = key;
            hashed[ix+1] = prop;
        }
/*
for (int i = 0; i < hashed.length; i += 2) {
System.err.printf("#%02d: %s\n", i>>1, (hashed[i] == null) ? "-" : hashed[i]);
}
*/
        _hashArea = hashed;
        _spillCount = spillCount;
    }
    
    private final static int findSize(int size)
    {
        if (size <= 5) {
            return 8;
        }
        if (size <= 12) {
            return 16;
        }
        int needed = size + (size >> 2); // at most 80% full
        int result = 32;
        while (result < needed) {
            result += result;
        }
        return result;
    }
    
    /**
     * @since 2.6
     */
    public static BeanPropertyMap construct(Collection<SettableBeanProperty> props, boolean caseInsensitive) {
        return new BeanPropertyMap(caseInsensitive, props);
    }
    
    /**
     * Fluent copy method that creates a new instance that is a copy
     * of this instance except for one additional property that is
     * passed as the argument.
     * Note that method does not modify this instance but constructs
     * and returns a new one.
     */
    public BeanPropertyMap withProperty(SettableBeanProperty newProp)
    {
        // First: may be able to just replace?
        String key = getPropertyName(newProp);

        for (int i = 1, end = _hashArea.length; i < end; i += 2) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[i];
            if ((prop != null) && prop.getName().equals(key)) {
                _hashArea[i] = newProp;
                _propsInOrder[_findFromOrdered(prop)] = newProp;
                return this;
            }
        }
        // If not, append
        final int slot = _hashCode(key);
        final int hashSize = _hashMask+1;
        int ix = (slot<<1);
        
        // primary slot not free?
        if (_hashArea[ix] != null) {
            // secondary?
            ix = (hashSize + (slot >> 1)) << 1;
            if (_hashArea[ix] != null) {
                // ok, spill over.
                ix = ((hashSize + (hashSize >> 1) ) << 1) + _spillCount;
                _spillCount += 2;
                if (ix >= _hashArea.length) {
                    _hashArea = Arrays.copyOf(_hashArea, _hashArea.length + 4);
                    // Uncomment for debugging only
                    /*
for (int i = 0; i < _hashArea.length; i += 2) {
    if (_hashArea[i] != null) {
        System.err.println("Property #"+(i/2)+" '"+_hashArea[i]+"'...");
    }
}
System.err.println("And new propr #"+slot+" '"+key+"'");
*/
                
                }
            }
        }
        _hashArea[ix] = key;
        _hashArea[ix+1] = newProp;

        int last = _propsInOrder.length;
        _propsInOrder = Arrays.copyOf(_propsInOrder, last+1);
        _propsInOrder[last] = newProp;

        // should we just create a new one? Or is resetting ok?
        
        return this;
    }

    public BeanPropertyMap assignIndexes()
    {
        // order is arbitrary, but stable:
        int index = 0;
        for (int i = 1, end = _hashArea.length; i < end; i += 2) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[i];
            if (prop != null) {
                prop.assignIndex(index++);
            }
        }
        return this;
    }

    /**
     * Mutant factory method for constructing a map where all entries use given
     * prefix
     */
    public BeanPropertyMap renameAll(NameTransformer transformer)
    {
        if (transformer == null || (transformer == NameTransformer.NOP)) {
            return this;
        }
        // Try to retain insertion ordering as well
        final int len = _propsInOrder.length;
        ArrayList<SettableBeanProperty> newProps = new ArrayList<SettableBeanProperty>(len);

        for (int i = 0; i < len; ++i) {
            SettableBeanProperty prop = _propsInOrder[i];
            
            // What to do with holes? For now, retain
            if (prop == null) {
                newProps.add(prop);
                continue;
            }
            newProps.add(_rename(prop, transformer));
        }
        // should we try to re-index? Ordering probably changed but caller probably doesn't want changes...
        return new BeanPropertyMap(_caseInsensitive, newProps);
    }

    /**
     * Mutant factory method that will use this instance as the base, and
     * construct an instance that is otherwise same except for excluding
     * properties with specified names.
     *
     * @since 2.8
     */
    public BeanPropertyMap withoutProperties(Collection<String> toExclude)
    {
        if (toExclude.isEmpty()) {
            return this;
        }
        final int len = _propsInOrder.length;
        ArrayList<SettableBeanProperty> newProps = new ArrayList<SettableBeanProperty>(len);

        for (int i = 0; i < len; ++i) {
            SettableBeanProperty prop = _propsInOrder[i];
            // 01-May-2015, tatu: Not 100% sure if existing `null`s should be retained;
            //   or, if entries to ignore should be retained as nulls. For now just
            //   prune them out
            if (prop != null) { // may contain holes, too, check.
                if (!toExclude.contains(prop.getName())) {
                    newProps.add(prop);
                }
            }
        }
        // should we try to re-index? Apparently no need
        return new BeanPropertyMap(_caseInsensitive, newProps);
    }
    
    /**
     * Specialized method that can be used to replace an existing entry
     * (note: entry MUST exist; otherwise exception is thrown) with
     * specified replacement.
     */
    public void replace(SettableBeanProperty newProp)
    {
        String key = getPropertyName(newProp);
        int ix = _findIndexInHash(key);
        
        if (ix >= 0) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[ix];
            _hashArea[ix] = newProp;
            // also, replace in in-order
            _propsInOrder[_findFromOrdered(prop)] = newProp;
            return;
        }
        
        throw new NoSuchElementException("No entry '"+key+"' found, can't replace");
    }

    private List<SettableBeanProperty> properties() {
        ArrayList<SettableBeanProperty> p = new ArrayList<SettableBeanProperty>(_size);
        for (int i = 1, end = _hashArea.length; i < end; i += 2) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[i];
            if (prop != null) {
                p.add(prop);
            }
        }
        return p;
    }

    /**
     * Accessor for traversing over all contained properties.
     */
    @Override
    public Iterator<SettableBeanProperty> iterator() {
        return properties().iterator();
    }

    /**
     * Method that will re-create initial insertion-ordering of
     * properties contained in this map. Note that if properties
     * have been removed, array may contain nulls; otherwise
     * it should be consecutive.
     * 
     * @since 2.1
     */
    public SettableBeanProperty[] getPropertiesInInsertionOrder() {
        return _propsInOrder;
    }

    // Confining this case insensitivity to this function (and the find method) in case we want to
    // apply a particular locale to the lower case function.  For now, using the default.
    protected final String getPropertyName(SettableBeanProperty prop) {
        return _caseInsensitive ? prop.getName().toLowerCase() : prop.getName();
    }

    /**
     * @since 2.3
     */
    public SettableBeanProperty find(int index)
    {
        // note: will scan the whole area, including primary, secondary and
        // possible spill-area
        for (int i = 1, end = _hashArea.length; i < end; i += 2) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[i];
            if ((prop != null) && (index == prop.getPropertyIndex())) {
                return prop;
            }
        }
        return null;
    }

    public SettableBeanProperty find(String key)
    {
        if (key == null) {
            throw new IllegalArgumentException("Can not pass null property name");
        }
        if (_caseInsensitive) {
            key = key.toLowerCase();
        }
            
        // inlined `_hashCode(key)`
        int slot = key.hashCode() & _hashMask;
//        int h = key.hashCode();
//        int slot = (h + (h >> 13)) & _hashMask;

        int ix = (slot<<1);
        Object match = _hashArea[ix];
        if ((match == key) || key.equals(match)) {
            return (SettableBeanProperty) _hashArea[ix+1];
        }
        return _find2(key, slot, match);
    }

    private final SettableBeanProperty _find2(String key, int slot, Object match)
    {
        if (match == null) {
            return null;
        }
        // no? secondary?
        int hashSize = _hashMask+1;
        int ix = hashSize + (slot>>1) << 1;
        match = _hashArea[ix];
        if (key.equals(match)) {
            return (SettableBeanProperty) _hashArea[ix+1];
        }
        if (match != null) { // _findFromSpill(...)
            int i = (hashSize + (hashSize>>1)) << 1;
            for (int end = i + _spillCount; i < end; i += 2) {
                match = _hashArea[i];
                if ((match == key) || key.equals(match)) {
                    return (SettableBeanProperty) _hashArea[i+1];
                }
            }
        }
        return null;
    }
    
    /*
    /**********************************************************
    /* Public API
    /**********************************************************
     */

    public int size() { return _size; }

    /**
     * Specialized method for removing specified existing entry.
     * NOTE: entry MUST exist, otherwise an exception is thrown.
     */
    public void remove(SettableBeanProperty propToRm) {
        ArrayList<SettableBeanProperty> props = new ArrayList<SettableBeanProperty>(_size);
        String key = getPropertyName(propToRm);
        boolean found = false;

        for (int i = 1, end = _hashArea.length; i < end; i += 2) {
            SettableBeanProperty prop = (SettableBeanProperty) _hashArea[i];
            if (prop == null) {
                continue;
            }
            if (!found) {
                found = key.equals(prop.getName());
                if (found) {
                    // need to leave a hole here
                    _propsInOrder[_findFromOrdered(prop)] = null;
                    continue;
                }
            }
            props.add(prop);
        }
        if (!found) {
            throw new NoSuchElementException("No entry '"+propToRm.getName()+"' found, can't remove");
        }
        init(props);
    }

    /**
     * Convenience method that tries to find property with given name, and
     * if it is found, call {@link SettableBeanProperty#deserializeAndSet}
     * on it, and return true; or, if not found, return false.
     * Note, too, that if deserialization is attempted, possible exceptions
     * are wrapped if and as necessary, so caller need not handle those.
     * 
     * @since 2.5
     */
    public boolean findDeserializeAndSet(JsonParser p, DeserializationContext ctxt,
            Object bean, String key) throws IOException
    {
        final SettableBeanProperty prop = find(key);
        if (prop == null) {
            return false;
        }
        try {
            prop.deserializeAndSet(p, ctxt, bean);
        } catch (Exception e) {
            wrapAndThrow(e, bean, key, ctxt);
        }
        return true;
    }

    @Override
    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("Properties=[");
        int count = 0;

        Iterator<SettableBeanProperty> it = iterator();
        while (it.hasNext()) {
            SettableBeanProperty prop = it.next();
            if (count++ > 0) {
                sb.append(", ");
            }
            sb.append(prop.getName());
            sb.append('(');
            sb.append(prop.getType());
            sb.append(')');
        }
        sb.append(']');
        return sb.toString();
    }
    
    /*
    /**********************************************************
    /* Helper methods
    /**********************************************************
     */

    protected SettableBeanProperty _rename(SettableBeanProperty prop, NameTransformer xf)
    {
        if (prop == null) {
            return prop;
        }
        String newName = xf.transform(prop.getName());
        prop = prop.withSimpleName(newName);
        JsonDeserializer<?> deser = prop.getValueDeserializer();
        if (deser != null) {
            @SuppressWarnings("unchecked")
            JsonDeserializer<Object> newDeser = (JsonDeserializer<Object>)
                deser.unwrappingDeserializer(xf);
            if (newDeser != deser) {
                prop = prop.withValueDeserializer(newDeser);
            }
        }
        return prop;
    }

    protected void wrapAndThrow(Throwable t, Object bean, String fieldName, DeserializationContext ctxt)
        throws IOException
    {
        // inlined 'throwOrReturnThrowable'
        while (t instanceof InvocationTargetException && t.getCause() != null) {
            t = t.getCause();
        }
        // Errors to be passed as is
        if (t instanceof Error) {
            throw (Error) t;
        }
        // StackOverflowErrors are tricky ones; need to be careful...
        boolean wrap = (ctxt == null) || ctxt.isEnabled(DeserializationFeature.WRAP_EXCEPTIONS);
        // Ditto for IOExceptions; except we may want to wrap JSON exceptions
        if (t instanceof IOException) {
            if (!wrap || !(t instanceof JsonProcessingException)) {
                throw (IOException) t;
            }
        } else if (!wrap) { // allow disabling wrapping for unchecked exceptions
            if (t instanceof RuntimeException) {
                throw (RuntimeException) t;
            }
        }
        throw JsonMappingException.wrapWithPath(t, bean, fieldName);
    }

    /**
     * Helper method used to find exact location of a property with name
     * given exactly, not subject to case changes, within hash area.
     * Expectation is that such property SHOULD exist, although no
     * exception is thrown.
     *
     * @since 2.7
     */
    private final int _findIndexInHash(String key)
    {
        final int slot = _hashCode(key);
        int ix = (slot<<1);
        
        // primary match?
        if (key.equals(_hashArea[ix])) {
            return ix+1;
        }
        // no? secondary?
        int hashSize = _hashMask+1;
        ix = hashSize + (slot>>1) << 1;
        if (key.equals(_hashArea[ix])) {
            return ix+1;
        }
        // perhaps spill then
        int i = (hashSize + (hashSize>>1)) << 1;
        for (int end = i + _spillCount; i < end; i += 2) {
            if (key.equals(_hashArea[i])) {
                return i+1;
            }
        }
        return -1;
    }
    
    private final int _findFromOrdered(SettableBeanProperty prop) {
        for (int i = 0, end = _propsInOrder.length; i < end; ++i) {
            if (_propsInOrder[i] == prop) {
                return i;
            }
        }
        throw new IllegalStateException("Illegal state: property '"+prop.getName()+"' missing from _propsInOrder");
    }

    // Offlined version for convenience if we want to change hashing scheme
    private final int _hashCode(String key) {
        // This method produces better hash, fewer collisions... yet for some
        // reason produces slightly worse performance. Very strange.

        // 05-Aug-2015, tatu: ... still true?

        /*
        int h = key.hashCode();
        return (h + (h >> 13)) & _hashMask;
        */
        return key.hashCode() & _hashMask;
    }
}
```

## Failed test
com.fasterxml.jackson.databind.struct.TestUnwrapped

## Test line
java.util.NoSuchElementException

## Error
No entry 'businessAddress' found, can't remove

## Error Code Block
```java
package com.fasterxml.jackson.databind.struct;

import com.fasterxml.jackson.annotation.*;

import com.fasterxml.jackson.databind.*;

/**
 * Unit tests for verifying that basic {@link JsonUnwrapped} annotation
 * handling works as expected; some more advanced tests are separated out
 * to more specific test classes (like prefix/suffix handling).
 */
public class TestUnwrapped extends BaseMapTest
{
    static class Unwrapping {
        public String name;
        @JsonUnwrapped
        public Location location;

        public Unwrapping() { }
        public Unwrapping(String str, int x, int y) {
            name = str;
            location = new Location(x, y);
        }
    }

    static class DeepUnwrapping
    {
        @JsonUnwrapped
        public Unwrapping unwrapped;

        public DeepUnwrapping() { }
        public DeepUnwrapping(String str, int x, int y) {
            unwrapped = new Unwrapping(str, x, y);
        }
    }
    
    static class UnwrappingWithCreator {
        public String name;

        @JsonUnwrapped
        public Location location;

        @JsonCreator
        public UnwrappingWithCreator(@JsonProperty("name") String n) {
            name = n;
        }
    }
    
    final static class Location {
        public int x;
        public int y;

        public Location() { }
        public Location(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    // Class with two unwrapped properties
    static class TwoUnwrappedProperties {
        @JsonUnwrapped
        public Location location;
        @JsonUnwrapped
        public Name name;

        public TwoUnwrappedProperties() { }
    }

    static class Name {
        public String first, last;
    }

    // [databind#615]
    static class Parent {
        @JsonUnwrapped
        public Child c1;

        public Parent() { }
        public Parent(String str) { c1 = new Child(str); }
    }

    static class Child {
        public String field;

        public Child() { }
        public Child(String f) { field = f; }
    }

    static class Inner {
        public String animal;
    }

    static class Outer {
        // @JsonProperty
        @JsonUnwrapped
        private Inner inner;
    }

    // [databind#1493]: case-insensitive handling
    static class Person {
        @JsonUnwrapped(prefix = "businessAddress.")
        public Address businessAddress;
    }

    static class Address {
        public String street;
        public String addon;
        public String zip;
        public String town;    
        public String country;
    }

    /*
    /**********************************************************
    /* Tests, serialization
    /**********************************************************
     */

    private final ObjectMapper MAPPER = new ObjectMapper();

    public void testSimpleUnwrappingSerialize() throws Exception {
        assertEquals("{\"name\":\"Tatu\",\"x\":1,\"y\":2}",
                MAPPER.writeValueAsString(new Unwrapping("Tatu", 1, 2)));
    }

    public void testDeepUnwrappingSerialize() throws Exception {
        assertEquals("{\"name\":\"Tatu\",\"x\":1,\"y\":2}",
                MAPPER.writeValueAsString(new DeepUnwrapping("Tatu", 1, 2)));
    }

    /*
    /**********************************************************
    /* Tests, deserialization
    /**********************************************************
     */

    public void testSimpleUnwrappedDeserialize() throws Exception
    {
        Unwrapping bean = MAPPER.readValue("{\"name\":\"Tatu\",\"y\":7,\"x\":-13}",
                Unwrapping.class);
        assertEquals("Tatu", bean.name);
        Location loc = bean.location;
        assertNotNull(loc);
        assertEquals(-13, loc.x);
        assertEquals(7, loc.y);
    }

    public void testDoubleUnwrapping() throws Exception
    {
        TwoUnwrappedProperties bean = MAPPER.readValue("{\"first\":\"Joe\",\"y\":7,\"last\":\"Smith\",\"x\":-13}",
                TwoUnwrappedProperties.class);
        Location loc = bean.location;
        assertNotNull(loc);
        assertEquals(-13, loc.x);
        assertEquals(7, loc.y);
        Name name = bean.name;
        assertNotNull(name);
        assertEquals("Joe", name.first);
        assertEquals("Smith", name.last);
    }

    public void testDeepUnwrapping() throws Exception
    {
        DeepUnwrapping bean = MAPPER.readValue("{\"x\":3,\"name\":\"Bob\",\"y\":27}",
                DeepUnwrapping.class);
        Unwrapping uw = bean.unwrapped;
        assertNotNull(uw);
        assertEquals("Bob", uw.name);
        Location loc = uw.location;
        assertNotNull(loc);
        assertEquals(3, loc.x);
        assertEquals(27, loc.y);
    }

    public void testUnwrappedDeserializeWithCreator() throws Exception
    {
        UnwrappingWithCreator bean = MAPPER.readValue("{\"x\":1,\"y\":2,\"name\":\"Tatu\"}",
                UnwrappingWithCreator.class);
        assertEquals("Tatu", bean.name);
        Location loc = bean.location;
        assertNotNull(loc);
        assertEquals(1, loc.x);
        assertEquals(2, loc.y);
    }

    public void testIssue615() throws Exception
    {
        Parent input = new Parent("name");
        String json = MAPPER.writeValueAsString(input);
        Parent output = MAPPER.readValue(json, Parent.class);
        assertEquals("name", output.c1.field);
    }

    public void testUnwrappedAsPropertyIndicator() throws Exception
    {
        Inner inner = new Inner();
        inner.animal = "Zebra";

        Outer outer = new Outer();
        outer.inner = inner;

        String actual = MAPPER.writeValueAsString(outer);

        assertTrue(actual.contains("animal"));
        assertTrue(actual.contains("Zebra"));
        assertFalse(actual.contains("inner"));
    }

    // [databind#1493]: case-insensitive handling
    public void testCaseInsensitiveUnwrap() throws Exception
    {
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(MapperFeature.ACCEPT_CASE_INSENSITIVE_PROPERTIES);
        Person p = mapper.readValue("{ }", Person.class);
        assertNotNull(p);
    }
}

```
