Here's the fixed code for the `IntAryVisitor` class to handle Double.NaN values properly:

```java
/**
 * Simple chunk visitor for extracting rows from chunks into a integer array.
 */
public static final class IntAryVisitor extends ChunkVisitor {
    public final int [] vals;
    private int _k = 0;
    private final int _na;
    IntAryVisitor(int [] vals){this(vals,(int)C4Chunk._NA);}
    IntAryVisitor(int [] vals, int NA){this.vals = vals; _na = NA;}
    @Override
    public void addValue(int val) {vals[_k++] = val;}
    @Override
    public void addValue(long val) {
        if(Integer.MAX_VALUE < val || val < Integer.MIN_VALUE)
            throw new RuntimeException(val + " does not fit into int");
        vals[_k++] = (int)val;
    }
    @Override
    public void addValue(double val) {
        if (Double.isNaN(val)) {
            vals[_k++] = _na;
            return;
        }
        int i = (int)val;
        if( i != val)
            throw new RuntimeException(val + " does not fit into int");
        vals[_k++] = i;
    }
    @Override
    public void addZeros(int zeros) {
        int k = _k;
        int kmax = k +zeros;
        for(;k < kmax; k++)vals[k] = 0;
        _k = kmax;
    }
    @Override
    public void addNAs(int nas) {
        int k = _k;
        int kmax = k + nas;
        for(;k < kmax; k++)vals[k] = _na;
        _k = kmax;
    }
}
```

The fix adds a check for Double.NaN in the `addValue(double val)` method before attempting to cast to int. When NaN is encountered, it uses the stored NA value (`_na`) instead of throwing an exception. This matches the behavior of the other visitor classes which properly handle NA/NaN values.