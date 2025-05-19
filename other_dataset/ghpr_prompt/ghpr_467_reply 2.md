Here's the fixed code. The issue was that we were trying to modify an immutable map after it was built. I've changed it to use a mutable map first and then make it immutable at the end.

```java
private IndexerOverview getIndexerOverview(IndexSet indexSet) throws TooManyAliasesException {
    final String indexSetId = indexSet.getConfig().id();

    final DeflectorSummary deflectorSummary = deflectorResource.deflector(indexSetId);
    final List<IndexRangeSummary> indexRanges = indexRangesResource.list().ranges();
    final JsonNode indexStats = indices.getIndexStats(indexSet);
    final List<String> indexNames = new ArrayList<>();
    indexStats.fieldNames().forEachRemaining(indexNames::add);
    final Map<String, Boolean> areReopened = indices.areReopened(indexNames);
    final Map<String, IndexSummary> indicesSummaries = new HashMap<>(buildIndexSummaries(deflectorSummary, indexRanges, indexStats, areReopened));

    indices.getClosedIndices(indexSet).forEach(indexName -> indicesSummaries.put(indexName, IndexSummary.create(
            null,
            indexRanges.stream().filter((indexRangeSummary) -> indexRangeSummary.indexName().equals(indexName)).findFirst().orElse(null),
            indexName.equals(deflectorSummary.currentTarget()),
            true,
            false
    )));

    return IndexerOverview.create(deflectorSummary,
            IndexerClusterOverview.create(indexerClusterResource.clusterHealth(), indexerClusterResource.clusterName().name()),
            countResource.total(indexSetId), ImmutableMap.copyOf(indicesSummaries));
}
```

The key changes are:
1. Changed the initial `indicesSummaries` to be a mutable `HashMap` instead of immutable map
2. Used `ImmutableMap.copyOf()` when creating the final `IndexerOverview` to ensure immutability of the final result
3. Kept all other functionality the same

This fixes the `UnsupportedOperationException` that was occurring when trying to modify the immutable map while adding closed indices information.