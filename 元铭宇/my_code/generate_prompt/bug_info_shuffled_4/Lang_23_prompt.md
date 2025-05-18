

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

## Test line
assertFalse("registry, hashcode()", emf.hashCode() == other.hashCode());

## Failed test
org.apache.commons.lang3.text.ExtendedMessageFormatTest::testEqualsHashcode

## Error Code Block
```java
    public void testEqualsHashcode() {
        Map<String, ? extends FormatFactory> registry = Collections.singletonMap("testfmt", new LowerCaseFormatFactory());
        Map<String, ? extends FormatFactory> otherRegitry = Collections.singletonMap("testfmt", new UpperCaseFormatFactory());

        String pattern = "Pattern: {0,testfmt}";
        ExtendedMessageFormat emf = new ExtendedMessageFormat(pattern, Locale.US, registry);

        ExtendedMessageFormat other = null;

        // Same object
        assertTrue("same, equals()",   emf.equals(emf));
        assertTrue("same, hashcode()", emf.hashCode() == emf.hashCode());

        // Equal Object
        other = new ExtendedMessageFormat(pattern, Locale.US, registry);
        assertTrue("equal, equals()",   emf.equals(other));
        assertTrue("equal, hashcode()", emf.hashCode() == other.hashCode());

        // Different Class
        other = new OtherExtendedMessageFormat(pattern, Locale.US, registry);
        assertFalse("class, equals()",  emf.equals(other));
        assertTrue("class, hashcode()", emf.hashCode() == other.hashCode()); // same hashcode
        
        // Different pattern
        other = new ExtendedMessageFormat("X" + pattern, Locale.US, registry);
        assertFalse("pattern, equals()",   emf.equals(other));
        assertFalse("pattern, hashcode()", emf.hashCode() == other.hashCode());

        // Different registry
        other = new ExtendedMessageFormat(pattern, Locale.US, otherRegitry);
        assertFalse("registry, equals()",   emf.equals(other));
        assertFalse("registry, hashcode()", emf.hashCode() == other.hashCode());

        // Different Locale
        other = new ExtendedMessageFormat(pattern, Locale.FRANCE, registry);
        assertFalse("locale, equals()",  emf.equals(other));
        assertTrue("locale, hashcode()", emf.hashCode() == other.hashCode()); // same hashcode
    }
```

## Error
junit.framework.AssertionFailedError: registry, hashcode()