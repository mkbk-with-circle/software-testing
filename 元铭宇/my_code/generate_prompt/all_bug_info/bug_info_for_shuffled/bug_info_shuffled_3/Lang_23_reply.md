修复后的代码需要确保当registry不同时，hashCode()也应该返回不同的值。问题在于当前的hashCode()实现可能没有考虑registry的影响。以下是修复后的代码：

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
        for (Object element : coll) {
            if (element != null) {
                return true;
            }
        }
        return false;
    }

    @Override
    public int hashCode() {
        int result = super.hashCode();
        result = 31 * result + (registry != null ? registry.hashCode() : 0);
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (!super.equals(obj)) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        ExtendedMessageFormat other = (ExtendedMessageFormat) obj;
        if (registry == null) {
            if (other.registry != null) {
                return false;
            }
        } else if (!registry.equals(other.registry)) {
            return false;
        }
        return true;
    }
```

主要修改点：
1. 改进了containsElements方法，使用更简洁的for-each循环
2. 添加了正确的hashCode()实现，确保考虑了registry的影响
3. 添加了equals()方法的完整实现，确保正确比较registry字段

这些修改将确保当registry不同时，hashCode()也会返回不同的值，从而使测试通过。