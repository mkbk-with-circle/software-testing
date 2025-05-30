## Buggy code
```java
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.bookkeeper.mledger.impl;

import static com.google.common.base.Preconditions.checkArgument;
import static com.google.common.base.Preconditions.checkNotNull;
import static org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.createManagedLedgerException;
import static org.apache.bookkeeper.mledger.util.SafeRun.safeRun;

import com.google.common.collect.Lists;
import com.google.common.primitives.Longs;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.PooledByteBufAllocator;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import org.apache.bookkeeper.client.api.BKException;
import org.apache.bookkeeper.client.api.LedgerEntry;
import org.apache.bookkeeper.client.api.ReadHandle;
import org.apache.bookkeeper.mledger.AsyncCallbacks.ReadEntriesCallback;
import org.apache.bookkeeper.mledger.AsyncCallbacks.ReadEntryCallback;
import org.apache.bookkeeper.mledger.ManagedLedgerException;
import org.apache.bookkeeper.mledger.util.RangeCache;
import org.apache.bookkeeper.mledger.util.RangeCache.Weighter;
import org.apache.commons.lang3.tuple.Pair;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Cache data payload for entries of all ledgers.
 */
public class EntryCacheImpl implements EntryCache {

    private final EntryCacheManager manager;
    private final ManagedLedgerImpl ml;
    private final RangeCache<PositionImpl, EntryImpl> entries;

    private static final double MB = 1024 * 1024;

    private static final Weighter<EntryImpl> entryWeighter = EntryImpl::getLength;

    public EntryCacheImpl(EntryCacheManager manager, ManagedLedgerImpl ml) {
        this.manager = manager;
        this.ml = ml;
        this.entries = new RangeCache<>(entryWeighter);

        if (log.isDebugEnabled()) {
            log.debug("[{}] Initialized managed-ledger entry cache", ml.getName());
        }
    }

    @Override
    public String getName() {
        return ml.getName();
    }

    public final static PooledByteBufAllocator ALLOCATOR = new PooledByteBufAllocator(true, // preferDirect
            0, // nHeapArenas,
            PooledByteBufAllocator.defaultNumDirectArena(), // nDirectArena
            PooledByteBufAllocator.defaultPageSize(), // pageSize
            PooledByteBufAllocator.defaultMaxOrder(), // maxOrder
            PooledByteBufAllocator.defaultTinyCacheSize(), // tinyCacheSize
            PooledByteBufAllocator.defaultSmallCacheSize(), // smallCacheSize
            PooledByteBufAllocator.defaultNormalCacheSize(), // normalCacheSize,
            true // Use cache for all threads
    );

    @Override
    public boolean insert(EntryImpl entry) {
        if (!manager.hasSpaceInCache()) {
            if (log.isDebugEnabled()) {
                log.debug("[{}] Skipping cache while doing eviction: {} - size: {}", ml.getName(), entry.getPosition(),
                        entry.getLength());
            }
            return false;
        }

        if (log.isDebugEnabled()) {
            log.debug("[{}] Adding entry to cache: {} - size: {}", ml.getName(), entry.getPosition(),
                    entry.getLength());
        }

        // Copy the entry into a buffer owned by the cache. The reason is that the incoming entry is retaining a buffer
        // from netty, usually allocated in 64Kb chunks. So if we just retain the entry without copying it, we might
        // retain actually the full 64Kb even for a small entry
        int size = entry.getLength();
        ByteBuf cachedData = null;
        try {
            cachedData = ALLOCATOR.directBuffer(size, size);
        } catch (Throwable t) {
            log.warn("[{}] Failed to allocate buffer for entry cache: {}", ml.getName(), t.getMessage(), t);
            return false;
        }

        if (size > 0) {
            ByteBuf entryBuf = entry.getDataBuffer();
            int readerIdx = entryBuf.readerIndex();
            cachedData.writeBytes(entryBuf);
            entryBuf.readerIndex(readerIdx);
        }

        PositionImpl position = entry.getPosition();
        EntryImpl cacheEntry = EntryImpl.create(position, cachedData);
        cachedData.release();
        if (entries.put(position, cacheEntry)) {
            manager.entryAdded(entry.getLength());
            return true;
        } else {
            // entry was not inserted into cache, we need to discard it
            cacheEntry.release();
            return false;
        }
    }

    @Override
    public void invalidateEntries(final PositionImpl lastPosition) {
        final PositionImpl firstPosition = PositionImpl.get(-1, 0);

        Pair<Integer, Long> removed = entries.removeRange(firstPosition, lastPosition, true);
        int entriesRemoved = removed.getLeft();
        long sizeRemoved = removed.getRight();
        if (log.isDebugEnabled()) {
            log.debug("[{}] Invalidated entries up to {} - Entries removed: {} - Size removed: {}", ml.getName(),
                    lastPosition, entriesRemoved, sizeRemoved);
        }

        manager.entriesRemoved(sizeRemoved);
    }

    @Override
    public void invalidateAllEntries(long ledgerId) {
        final PositionImpl firstPosition = PositionImpl.get(ledgerId, 0);
        final PositionImpl lastPosition = PositionImpl.get(ledgerId + 1, 0);

        Pair<Integer, Long> removed = entries.removeRange(firstPosition, lastPosition, false);
        int entriesRemoved = removed.getLeft();
        long sizeRemoved = removed.getRight();
        if (log.isDebugEnabled()) {
            log.debug("[{}] Invalidated all entries on ledger {} - Entries removed: {} - Size removed: {}",
                    ml.getName(), ledgerId, entriesRemoved, sizeRemoved);
        }

        manager.entriesRemoved(sizeRemoved);
    }

    @Override
    public void asyncReadEntry(ReadHandle lh, PositionImpl position, final ReadEntryCallback callback,
            final Object ctx) {
        if (log.isDebugEnabled()) {
            log.debug("[{}] Reading entry ledger {}: {}", ml.getName(), lh.getId(), position.getEntryId());
        }
        EntryImpl entry = entries.get(position);
        if (entry != null) {
            EntryImpl cachedEntry = EntryImpl.create(entry);
            entry.release();
            manager.mlFactoryMBean.recordCacheHit(cachedEntry.getLength());
            callback.readEntryComplete(cachedEntry, ctx);
        } else {
            lh.readAsync(position.getEntryId(), position.getEntryId()).whenCompleteAsync(
                    (ledgerEntries, exception) -> {
                        if (exception != null) {
                            ml.invalidateLedgerHandle(lh, exception);
                            callback.readEntryFailed(createManagedLedgerException(exception), ctx);
                            return;
                        }

                        try {
                            Iterator<LedgerEntry> iterator = ledgerEntries.iterator();
                            if (iterator.hasNext()) {
                                LedgerEntry ledgerEntry = iterator.next();
                                EntryImpl returnEntry = EntryImpl.create(ledgerEntry);

                                manager.mlFactoryMBean.recordCacheMiss(1, returnEntry.getLength());
                                ml.mbean.addReadEntriesSample(1, returnEntry.getLength());
                                callback.readEntryComplete(returnEntry, ctx);
                            } else {
                                // got an empty sequence
                                callback.readEntryFailed(new ManagedLedgerException("Could not read given position"),
                                                         ctx);
                            }
                        } finally {
                            ledgerEntries.close();
                        }
                    }, ml.getExecutor().chooseThread(ml.getName()));
        }
    }

    @Override
    @SuppressWarnings({ "unchecked", "rawtypes" })
    public void asyncReadEntry(ReadHandle lh, long firstEntry, long lastEntry, boolean isSlowestReader,
            final ReadEntriesCallback callback, Object ctx) {
        final long ledgerId = lh.getId();
        final int entriesToRead = (int) (lastEntry - firstEntry) + 1;
        final PositionImpl firstPosition = PositionImpl.get(lh.getId(), firstEntry);
        final PositionImpl lastPosition = PositionImpl.get(lh.getId(), lastEntry);

        if (log.isDebugEnabled()) {
            log.debug("[{}] Reading entries range ledger {}: {} to {}", ml.getName(), ledgerId, firstEntry, lastEntry);
        }

        Collection<EntryImpl> cachedEntries = entries.getRange(firstPosition, lastPosition);

        if (cachedEntries.size() == entriesToRead) {
            long totalCachedSize = 0;
            final List<EntryImpl> entriesToReturn = Lists.newArrayListWithExpectedSize(entriesToRead);

            // All entries found in cache
            for (EntryImpl entry : cachedEntries) {
                entriesToReturn.add(EntryImpl.create(entry));
                totalCachedSize += entry.getLength();
                entry.release();
            }

            manager.mlFactoryMBean.recordCacheHits(entriesToReturn.size(), totalCachedSize);
            if (log.isDebugEnabled()) {
                log.debug("[{}] Ledger {} -- Found in cache entries: {}-{}", ml.getName(), ledgerId, firstEntry,
                        lastEntry);
            }

            callback.readEntriesComplete((List) entriesToReturn, ctx);

        } else {
            if (!cachedEntries.isEmpty()) {
                cachedEntries.forEach(entry -> entry.release());
            }

            // Read all the entries from bookkeeper
            lh.readAsync(firstEntry, lastEntry).whenCompleteAsync(
                    (ledgerEntries, exception) -> {
                        if (exception != null) {
                            if (exception instanceof BKException
                                && ((BKException)exception).getCode() == BKException.Code.TooManyRequestsException) {
                                callback.readEntriesFailed(createManagedLedgerException(exception), ctx);
                            } else {
                                ml.invalidateLedgerHandle(lh, exception);
                                ManagedLedgerException mlException = createManagedLedgerException(exception);
                                callback.readEntriesFailed(mlException, ctx);
                            }
                            return;
                        }

                        checkNotNull(ml.getName());
                        checkNotNull(ml.getExecutor());

                        try {
                            // We got the entries, we need to transform them to a List<> type
                            long totalSize = 0;
                            final List<EntryImpl> entriesToReturn
                                = Lists.newArrayListWithExpectedSize(entriesToRead);
                            for (LedgerEntry e : ledgerEntries) {
                                EntryImpl entry = EntryImpl.create(e);

                                entriesToReturn.add(entry);
                                totalSize += entry.getLength();
                            }

                            manager.mlFactoryMBean.recordCacheMiss(entriesToReturn.size(), totalSize);
                            ml.getMBean().addReadEntriesSample(entriesToReturn.size(), totalSize);

                            callback.readEntriesComplete((List) entriesToReturn, ctx);
                        } finally {
                            ledgerEntries.close();
                        }
                    }, ml.getExecutor().chooseThread(ml.getName()));
        }
    }

    @Override
    public void clear() {
        long removedSize = entries.clear();
        manager.entriesRemoved(removedSize);
    }

    @Override
    public long getSize() {
        return entries.getSize();
    }

    @Override
    public int compareTo(EntryCache other) {
        return Longs.compare(getSize(), other.getSize());
    }

    @Override
    public Pair<Integer, Long> evictEntries(long sizeToFree) {
        checkArgument(sizeToFree > 0);
        Pair<Integer, Long> evicted = entries.evictLeastAccessedEntries(sizeToFree);
        int evictedEntries = evicted.getLeft();
        long evictedSize = evicted.getRight();
        if (log.isDebugEnabled()) {
            log.debug(
                    "[{}] Doing cache eviction of at least {} Mb -- Deleted {} entries - Total size deleted: {} Mb "
                            + " -- Current Size: {} Mb",
                    ml.getName(), sizeToFree / MB, evictedEntries, evictedSize / MB, entries.getSize() / MB);
        }
        manager.entriesRemoved(evictedSize);
        return evicted;
    }

    private static final Logger log = LoggerFactory.getLogger(EntryCacheImpl.class);
}

```

## Error
Handle unknown runtime exception while reading entries

## Error Description
### Motivation

Recently we have seen below runtime-exception while reading entries at broker and broker is not handling it correctly and not completing read callback so, dispatch get stuck for the subscription.

```
22:16:58.424 [bookkeeper-ml-workers-OrderedExecutor-0-0] ERROR org.apache.bookkeeper.common.util.SafeRunnable - Unexpected throwable caught 
java.lang.NullPointerException: null
        at org.apache.bookkeeper.mledger.impl.EntryImpl.create(EntryImpl.java:89) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.EntryCacheImpl.asyncReadEntry(EntryCacheImpl.java:225) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.internalReadFromLedger(ManagedLedgerImpl.java:1509) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.asyncReadEntries(ManagedLedgerImpl.java:1359) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedCursorImpl.notifyEntriesAvailable(ManagedCursorImpl.java:2221) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.lambda$notifyCursors$27(ManagedLedgerImpl.java:1580) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.util.SafeRun$1.safeRun(SafeRun.java:32) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.common.util.SafeRunnable.run(SafeRunnable.java:36) [bookkeeper-common-4.7.2.jar:4.7.2]
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142) [?:1.8.0_131]
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617) [?:1.8.0_131]
        at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30) [netty-all-4.1.22.Final.jar:4.1.22.Final]
        at java.lang.Thread.run(Thread.java:748) [?:1.8.0_131]
```

```
3:22:26.425 [bookkeeper-ml-workers-OrderedExecutor-10-0] ERROR org.apache.bookkeeper.common.util.SafeRunnable - Unexpected throwable caught 
java.lang.NullPointerException: null
        at org.apache.bookkeeper.mledger.impl.EntryImpl.create(EntryImpl.java:89) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.EntryCacheImpl.asyncReadEntry(EntryCacheImpl.java:225) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.internalReadFromLedger(ManagedLedgerImpl.java:1509) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.asyncReadEntries(ManagedLedgerImpl.java:1359) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.OpReadEntry.lambda$checkReadCompletion$76(OpReadEntry.java:136) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]


        06:58:57.334 [bookkeeper-ml-workers-OrderedExecutor-19-0] ERROR org.apache.bookkeeper.common.util.SafeRunnable - Unexpected throwable caught 
java.lang.NullPointerException: null
        at org.apache.bookkeeper.mledger.impl.EntryImpl.create(EntryImpl.java:89) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.EntryCacheImpl.asyncReadEntry(EntryCacheImpl.java:225) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.internalReadFromLedger(ManagedLedgerImpl.java:1509) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.asyncReadEntries(ManagedLedgerImpl.java:1359) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedCursorImpl.notifyEntriesAvailable(ManagedCursorImpl.java:2221) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.impl.ManagedLedgerImpl.lambda$notifyCursors$27(ManagedLedgerImpl.java:1580) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.mledger.util.SafeRun$1.safeRun(SafeRun.java:32) ~[managed-ledger-original-2.2.2-yahoo.jar:2.2.2-yahoo]
        at org.apache.bookkeeper.common.util.SafeRunnable.run(SafeRunnable.java:36) [bookkeeper-common-4.7.2.jar:4.7.2]
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142) [?:1.8.0_131]
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617) [?:1.8.0_131]
        at io.netty.util.concurrent.FastThreadLocalRunnable.run(FastThreadLocalRunnable.java:30) [pulsar-functions-metrics-2.2.2-yahoo.jar:?]
        at java.lang.Thread.run(Thread.java:748) [?:1.8.0_131]
```

### Modifications

Handle NPE and complete the callback with failure.

### Result

Dispatch will not be blocked if there is runtime exception while reading entries.

