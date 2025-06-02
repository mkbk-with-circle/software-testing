The issue occurs when trying to remove a property with a case-insensitive name match. The problem is in the `remove()` method where it checks for property name equality without considering case sensitivity. Here's the fixed version of the `remove()` method:

```java
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
            String propName = getPropertyName(prop);
            found = key.equals(propName);
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
```

The key changes are:
1. Instead of directly comparing with `prop.getName()`, we now use `getPropertyName(prop)` to get the properly cased version of the property name
2. This ensures the case sensitivity setting is respected when comparing property names

This change makes the removal operation consistent with how properties are looked up elsewhere in the class, where case sensitivity is properly handled through the `getPropertyName()` method.