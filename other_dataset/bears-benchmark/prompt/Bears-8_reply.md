The issue appears to be in the `MapSerializer` class where it's not properly handling null checks for the `_valueType` field. The error occurs when trying to check `_valueType.getRawClass()` without first verifying if `_valueType` is null.

Here's the fixed code with the null check added:

```java
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
    
    // If value type is final, it's same as forcing static value typing:
    if (!_valueTypeIsStatic && _valueType != null) {
        _valueTypeIsStatic = _valueType.isFinal();
    } else if (_valueTypeIsStatic && _valueType != null) {
        // also: Object.class can not be handled as static, ever
        if (_valueType.getRawClass() == Object.class) {
            _valueTypeIsStatic = false;
        }
    }
}
```

The main changes are:

1. Moved the static type determination logic into the constructor where it belongs
2. Added null checks for `_valueType` before accessing its methods
3. Restructured the logic to be more defensive against null values

This should prevent the NullPointerException that was occurring when `_valueType` was null while still maintaining all the original functionality. The fix ensures that we only try to access `_valueType` methods when we know `_valueType` is not null.