## Buggy code
```java
public class ResolvedRecursiveType extends TypeBase
{
    private static final long serialVersionUID = 1L;

    protected JavaType _referencedType;

    public ResolvedRecursiveType(Class<?> erasedType, TypeBindings bindings) {
        super(erasedType, bindings, null, null, 0, null, null, false);
    }

    public void setReference(JavaType ref)
    {
        // sanity check; should not be called multiple times
        if (_referencedType != null) {
            throw new IllegalStateException("Trying to re-set self reference; old value = "+_referencedType+", new = "+ref);
        }
        _referencedType = ref;
    }

    public JavaType getSelfReferencedType() { return _referencedType; }

    @Override
    public StringBuilder getGenericSignature(StringBuilder sb) {
        return _referencedType.getGenericSignature(sb);
    }

    @Override
    public StringBuilder getErasedSignature(StringBuilder sb) {
        return _referencedType.getErasedSignature(sb);
    }

    @Override
    public JavaType withContentType(JavaType contentType) {
        return this;
    }
    
    @Override
    public JavaType withTypeHandler(Object h) {
        return this;
    }

    @Override
    public JavaType withContentTypeHandler(Object h) {
        return this;
    }

    @Override
    public JavaType withValueHandler(Object h) {
        return this;
    }

    @Override
    public JavaType withContentValueHandler(Object h) {
        return this;
    }

    @Override
    public JavaType withStaticTyping() {
        return this;
    }

    @Deprecated // since 2.7
    @Override
    protected JavaType _narrow(Class<?> subclass) {
        return this;
    }

    @Override
    public JavaType refine(Class<?> rawType, TypeBindings bindings,
            JavaType superClass, JavaType[] superInterfaces) {
        return null;
    }

    @Override
    public boolean isContainerType() {
        return false;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(40)
                .append("[recursive type; ");
        if (_referencedType == null) {
            sb.append("UNRESOLVED");
        } else {
            // [databind#1301]: Typically resolves to a loop so short-cut
            //   and only include type-erased class
            sb.append(_referencedType.getRawClass().getName());
        }
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (o == this) return true;
        if (o == null) return false;
        // Do NOT ever match unresolved references
        if (_referencedType == null) {
            return false;
        }
        return (o.getClass() == getClass()
                && _referencedType.equals(((ResolvedRecursiveType) o).getSelfReferencedType()));
    }
}
```

## Failed test
com.fasterxml.jackson.databind.type.RecursiveTypeTest

## Test line
junit.framework.AssertionFailedError

## Error


## Error Code Block
```java
package com.fasterxml.jackson.databind.type;

import java.util.*;

import com.fasterxml.jackson.databind.*;

public class RecursiveTypeTest extends BaseMapTest
{
    // for [databind#1301]
    @SuppressWarnings("serial")
    static class HashTree<K, V> extends HashMap<K, HashTree<K, V>> { }

 // for [databind#938]
    public static interface Ability<T> { }

    // for [databind#1647]
    static interface IFace<T> {}

    // for [databind#1647]
    static class Base implements IFace<Sub> { }

    // for [databind#1647]
    static class Sub extends Base { }

    public static final class ImmutablePair<L, R> implements Map.Entry<L, R>, Ability<ImmutablePair<L, R>> {
        public final L key;
        public final R value;

        public ImmutablePair(final L key, final R value) {
            this.key = key;
            this.value = value;
        }

        @Override
        public L getKey() {
            return key;
        }

        @Override
        public R getValue() {
            return value;
        }

        @Override
        public R setValue(final R value) {
            throw new UnsupportedOperationException();
        }
      
        static <L, R> ImmutablePair<L, R> of(final L left, final R right) {
            return new ImmutablePair<L, R>(left, right);
        }
    }

    // for [databind#1301]
    public void testRecursiveType()
    {
        TypeFactory tf = TypeFactory.defaultInstance();
        JavaType type = tf.constructType(HashTree.class);
        assertNotNull(type);
    }
    
    // for [databind#1301]
    @SuppressWarnings("serial")
    static class DataDefinition extends HashMap<String, DataDefinition> {
        public DataDefinition definition;
        public DataDefinition elements;
        public String regex;
        public boolean required;
        public String type;
    }
    
    private final ObjectMapper MAPPER = new ObjectMapper();

    // [databind#938]
    public void testRecursivePair() throws Exception
    {
        JavaType t = MAPPER.constructType(ImmutablePair.class);

        assertNotNull(t);
        assertEquals(ImmutablePair.class, t.getRawClass());

        List<ImmutablePair<String, Double>> list = new ArrayList<ImmutablePair<String, Double>>();
        list.add(ImmutablePair.of("Hello World!", 123d));
        String json = MAPPER.writeValueAsString(list);

        assertNotNull(json);

        // can not deserialize with current definition, however
    }

    // for [databind#1301]
    public void testJavaTypeToString() throws Exception
    {
        TypeFactory tf = objectMapper().getTypeFactory();
        String desc = tf.constructType(DataDefinition.class).toString();
        assertNotNull(desc);
        // could try comparing exact message, but since it's informational try looser:
        if (!desc.contains("map type")) {
            fail("Description should contain 'map type', did not: "+desc);
        }
        if (!desc.contains("recursive type")) {
            fail("Description should contain 'recursive type', did not: "+desc);
        }
    }

    // for [databind#1647]
    public void testSuperClassWithReferencedJavaType() {
        TypeFactory tf = objectMapper().getTypeFactory();
        tf.constructType(Base.class); // must be constructed before sub to set the cache correctly
        JavaType subType = tf.constructType(Sub.class);
        // baseTypeFromSub should be a ResolvedRecursiveType in this test
        JavaType baseTypeFromSub = subType.getSuperClass();
        assertNotNull(baseTypeFromSub.getSuperClass());
    }
}

```
