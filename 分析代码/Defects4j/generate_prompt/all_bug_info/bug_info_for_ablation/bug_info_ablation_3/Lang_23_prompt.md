## Buggy code
```java
/**
     * Learn whether the specified Collection contains non-null elements.
     * @param coll to check
     * @return <code>true</code> if some Object was found, <code>false</code> otherwise.
     */
    private boolean containsElements(Collection<?> coll) {
        if (coll == null || coll.size() == 0) {
            return false;
        }
        for (Iterator<?> iter = coll.iterator(); iter.hasNext();) {
            if (iter.next() != null) {
                return true;
            }
        }
        return false;
    }
```



## Error
junit.framework.AssertionFailedError: registry, hashcode()


