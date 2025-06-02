根据测试用例和错误信息，问题出在`registry`不同时哈希码应该不同。当前的`containsElements`方法并没有被直接用于哈希码计算，但我们需要确保哈希码计算考虑了注册表(registry)的内容。修复的关键是确保`hashCode()`方法正确考虑了registry的内容。

以下是修复后的代码：

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

修复的关键点：
1. 改进了`containsElements`方法，使用更简洁的for-each循环
2. 添加了正确的`hashCode()`实现，确保考虑了registry的内容
3. 添加了完整的`equals()`方法实现，确保与`hashCode()`保持一致

这样修改后，当registry不同时，哈希码也会不同，从而通过测试用例。