Here's the fixed code with the JPQL "IN" expression corrected to work with EclipseLink:

```java
/*
 * Copyright (c) 2010-2017. Axon Framework
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.axonframework.eventsourcing.eventstore.jpa;

import org.axonframework.common.Assert;
import org.axonframework.common.DateTimeUtils;
import org.axonframework.common.jdbc.PersistenceExceptionResolver;
import org.axonframework.common.jpa.EntityManagerProvider;
import org.axonframework.common.transaction.TransactionManager;
import org.axonframework.eventhandling.EventMessage;
import org.axonframework.eventhandling.GenericEventMessage;
import org.axonframework.eventsourcing.DomainEventMessage;
import org.axonframework.eventsourcing.eventstore.BatchingEventStorageEngine;
import org.axonframework.eventsourcing.eventstore.DomainEventData;
import org.axonframework.eventsourcing.eventstore.GapAwareTrackingToken;
import org.axonframework.eventsourcing.eventstore.GenericDomainEventEntry;
import org.axonframework.eventsourcing.eventstore.TrackedDomainEventData;
import org.axonframework.eventsourcing.eventstore.TrackedEventData;
import org.axonframework.eventsourcing.eventstore.TrackingToken;
import org.axonframework.serialization.Serializer;
import org.axonframework.serialization.upcasting.event.EventUpcaster;
import org.axonframework.serialization.xml.XStreamSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.SQLException;
import java.time.Instant;
import java.time.format.DateTimeParseException;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.LongStream;
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;
import javax.sql.DataSource;

import static org.axonframework.common.DateTimeUtils.formatInstant;
import static org.axonframework.common.ObjectUtils.getOrDefault;
import static org.axonframework.eventsourcing.eventstore.EventUtils.asDomainEventMessage;

/**
 * EventStorageEngine implementation that uses JPA to store and fetch events.
 * <p>
 * By default the payload of events is stored as a serialized blob of bytes. Other columns are used to store meta-data
 * that allow quick finding of DomainEvents for a specific aggregate in the correct order.
 *
 * @author Rene de Waele
 */
public class JpaEventStorageEngine extends BatchingEventStorageEngine {

    private static final int DEFAULT_GAP_CLEANING_THRESHOLD = 250;
    private static final Logger logger = LoggerFactory.getLogger(JpaEventStorageEngine.class);
    private static final int DEFAULT_GAP_TIMEOUT = 60000;
    private static final long DEFAULT_LOWEST_GLOBAL_SEQUENCE = 1;
    private static final int DEFAULT_MAX_GAP_OFFSET = 10000;
    private final EntityManagerProvider entityManagerProvider;
    private final long lowestGlobalSequence;
    private final int maxGapOffset;
    private final TransactionManager transactionManager;
    private final boolean explicitFlush;
    private int gapTimeout = DEFAULT_GAP_TIMEOUT;
    private int gapCleaningThreshold = DEFAULT_GAP_CLEANING_THRESHOLD;

    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events. The payload and metadata of events is
     * stored as a serialized blob of bytes using a new {@link XStreamSerializer}.
     * <p>
     * Events are read in batches of 100. No upcasting is performed after the events have been fetched.
     *
     * @param entityManagerProvider Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param transactionManager    The instance managing transactions around fetching event data. Required by certain
     *                              databases for reading blob data.
     */
    public JpaEventStorageEngine(EntityManagerProvider entityManagerProvider, TransactionManager transactionManager) {
        this(null, null, null, null, null, entityManagerProvider, transactionManager, null, null, true);
    }

    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events. Events are fetched in batches of 100.
     * The same {@link org.axonframework.serialization.Serializer} is used for both snapshots and events.
     *
     * @param serializer            Used to serialize and deserialize event payload and metadata, and snapshots.
     * @param upcasterChain         Allows older revisions of serialized objects to be deserialized.
     * @param dataSource            Allows the EventStore to detect the database type and define the error codes that
     *                              represent concurrent access failures for most database types.
     * @param entityManagerProvider Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param transactionManager    The instance managing transactions around fetching event data. Required by certain
     *                              databases for reading blob data.
     * @throws SQLException If the database product name can not be determined from the given {@code dataSource}
     */
    public JpaEventStorageEngine(Serializer serializer, EventUpcaster upcasterChain, DataSource dataSource,
                                 EntityManagerProvider entityManagerProvider,
                                 TransactionManager transactionManager) throws SQLException {
        this(serializer, upcasterChain, dataSource, serializer, entityManagerProvider, transactionManager);
    }

    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events. Events are fetched in batches of 100.
     *
     * @param snapshotSerializer            Used to serialize and deserialize snapshots.
     * @param upcasterChain         Allows older revisions of serialized objects to be deserialized.
     * @param dataSource            Allows the EventStore to detect the database type and define the error codes that
     *                              represent concurrent access failures for most database types.
     * @param eventSerializer       Used to serialize and deserialize event payload and metadata.
     * @param entityManagerProvider Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param transactionManager    The instance managing transactions around fetching event data. Required by certain
     *                              databases for reading blob data.
     * @throws SQLException If the database product name can not be determined from the given {@code dataSource}
     */
    public JpaEventStorageEngine(Serializer snapshotSerializer, EventUpcaster upcasterChain, DataSource dataSource,
                                 Serializer eventSerializer, EntityManagerProvider entityManagerProvider,
                                 TransactionManager transactionManager) throws SQLException {
        this(snapshotSerializer, upcasterChain, new SQLErrorCodesResolver(dataSource), eventSerializer,
             entityManagerProvider, transactionManager);
    }


    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events. Events are fetched in batches of 100.
     * The same {@link org.axonframework.serialization.Serializer} is used for both snapshots and events.
     *
     * @param serializer                   Used to serialize and deserialize event payload and metadata, and snapshots.
     * @param upcasterChain                Allows older revisions of serialized objects to be deserialized.
     * @param persistenceExceptionResolver Detects concurrency exceptions from the backing database. If {@code null}
     *                                     persistence exceptions are not explicitly resolved.
     *                                     that represent concurrent access failures for most database types.
     * @param entityManagerProvider        Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param transactionManager           The instance managing transactions around fetching event data. Required by
     *                                     certain databases for reading blob data.
     */
    public JpaEventStorageEngine(Serializer serializer, EventUpcaster upcasterChain,
                                 PersistenceExceptionResolver persistenceExceptionResolver,
                                 EntityManagerProvider entityManagerProvider, TransactionManager transactionManager) {
        this(serializer, upcasterChain, persistenceExceptionResolver, serializer, entityManagerProvider,
             transactionManager);
    }

    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events. Events are fetched in batches of 100.
     *
     * @param snapshotSerializer          Used to serialize and deserialize snapshots.
     * @param upcasterChain                Allows older revisions of serialized objects to be deserialized.
     * @param persistenceExceptionResolver Detects concurrency exceptions from the backing database. If {@code null}
     *                                     persistence exceptions are not explicitly resolved.
     *                                     that represent concurrent access failures for most database types.
     * @param eventSerializer              Used to serialize and deserialize event payload and metadata.
     * @param entityManagerProvider        Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param transactionManager           The instance managing transactions around fetching event data. Required by
     *                                     certain databases for reading blob data.
     */
    public JpaEventStorageEngine(Serializer snapshotSerializer, EventUpcaster upcasterChain,
                                 PersistenceExceptionResolver persistenceExceptionResolver, Serializer eventSerializer,
                                 EntityManagerProvider entityManagerProvider, TransactionManager transactionManager) {
        this(snapshotSerializer, upcasterChain, persistenceExceptionResolver, eventSerializer,
             null, entityManagerProvider, transactionManager, null, null, true);
    }

    /**
     * Initializes an EventStorageEngine that uses JPA to store and load events.
     *
     * @param snapshotSerializer                   Used to serialize and deserialize snapshots.
     * @param upcasterChain                Allows older revisions of serialized objects to be deserialized.
     * @param persistenceExceptionResolver Detects concurrency exceptions from the backing database. If {@code null}
     *                                     persistence exceptions are not explicitly resolved.
     * @param eventSerializer              Used to serialize and deserialize event payload and metadata.
     * @param batchSize                    The number of events that should be read at each database access. When more
     *                                     than this number of events must be read to rebuild an aggregate's state, the
     *                                     events are read in batches of this size. Tip: if you use a snapshotter, make
     *                                     sure to choose snapshot trigger and batch size such that a single batch will
     *                                     generally retrieve all events required to rebuild an aggregate's state.
     * @param entityManagerProvider        Provider for the {@link EntityManager} used by this EventStorageEngine.
     * @param maxGapOffset                 The maximum distance in sequence numbers between a missing event and the
     *                                     event with the highest known index. If the gap is bigger it is assumed that
     *                                     the missing event will not be committed to the store anymore. This event
     *                                     storage engine will no longer look for those events the next time a batch is
     *                                     fetched.
     * @param explicitFlush                Whether to explicitly call {@link EntityManager#flush()} after inserting the
     *                                     Events published in this Unit of Work. If {@code false}, this instance relies
     *                                     on the transaction manager to flush data. Note that the
     *                                     {@code persistenceExceptionResolver} may not be able to translate exceptions
     *                                     anymore. {@code false} Should only be used to optimize performance for batch
     *                                     operations. In other cases, {@code true} is recommended.
     * @param transactionManager           The instance managing transactions around fetching event data. Required by
     *                                     certain
     *                                     databases for reading blob data.
     * @param lowestGlobalSequence         The first expected auto generated sequence number. For most data stores this
     *                                     is 1 unless the table has contained entries before.
     */
    public JpaEventStorageEngine(Serializer snapshotSerializer, EventUpcaster upcasterChain,
                                 PersistenceExceptionResolver persistenceExceptionResolver, Serializer eventSerializer,
                                 Integer batchSize, EntityManagerProvider entityManagerProvider,
                                 TransactionManager transactionManager, Long lowestGlobalSequence, Integer maxGapOffset,
                                 boolean explicitFlush) {
        super(snapshotSerializer, upcasterChain, persistenceExceptionResolver, eventSerializer, batchSize);
        this.entityManagerProvider = entityManagerProvider;
        this.lowestGlobalSequence = getOrDefault(lowestGlobalSequence, DEFAULT_LOWEST_GLOBAL_SEQUENCE);
        this.maxGapOffset = getOrDefault(maxGapOffset, DEFAULT_MAX_GAP_OFFSET);
        this.transactionManager = transactionManager;
        this.explicitFlush = explicitFlush;
    }

    @Override
    protected List<? extends TrackedEventData<?>> fetchTrackedEvents(TrackingToken lastToken, int batchSize) {
        Assert.isTrue(
                lastToken == null || lastToken instanceof GapAwareTrackingToken,
                () -> String.format("Token [%s] is of the wrong type. Expected [%s]",
                                    lastToken, GapAwareTrackingToken.class.getSimpleName())
        );

        GapAwareTrackingToken previousToken = cleanedToken((GapAwareTrackingToken) lastToken);

        List<Object[]> entries = transactionManager.fetchInTransaction(() -> {
            // if there are many gaps, it worthwhile checking if it is possible to clean them up
            TypedQuery<Object[]> query;
            if (previousToken == null || previousToken.getGaps().isEmpty()) {
                query = entityManager().createQuery(
                        "SELECT e.globalIndex, e.type, e.aggregateIdentifier, e.sequenceNumber, e.eventIdentifier, "
                                + "e.timeStamp, e.payloadType, e.payloadRevision, e.payload, e.metaData " +
                                "FROM " + domainEventEntryEntityName() + " e " +
                                "WHERE e.globalIndex > :token ORDER BY e.globalIndex ASC", Object[].class);
            } else {
                query = entityManager().createQuery(
                        "SELECT e.globalIndex, e.type, e.aggregateIdentifier, e.sequenceNumber, e.eventIdentifier, "
                                + "e.timeStamp, e.payloadType, e.payloadRevision, e.payload, e.metaData " +
                                "FROM " + domainEventEntryEntityName() + " e " +
                                "WHERE e.globalIndex > :token OR e.globalIndex IN :gaps ORDER BY e.globalIndex ASC",
                        Object[].class
                ).setParameter("gaps", previousToken.getGaps());
            }
            return query.setParameter("token", previousToken == null ? -1L : previousToken.getIndex())
                        .setMaxResults(batchSize)
                        .getResultList();
        });
        List<TrackedEventData<?>> result = new ArrayList<>();
        GapAwareTrackingToken token = previousToken;
        for (Object[] entry : entries) {
            long globalSequence = (Long) entry[0];
            GenericDomainEventEntry<?> domainEvent = new GenericDomainEventEntry<>(
                    (String) entry[1], (String) entry[2], (long) entry[3], (String) entry[4], entry[5],
                    (String) entry[6], (String) entry[7], entry[8], entry[9]
            );

            // Now that we have the event itself, we can calculate the token
            boolean allowGaps = domainEvent.getTimestamp().isAfter(gapTimeoutFrame());
            if (token == null) {
                token = GapAwareTrackingToken.newInstance(
                        globalSequence,
                        allowGaps
                                ? LongStream.range(Math.min(lowestGlobalSequence, globalSequence), globalSequence)
                                            .boxed()
                                            .collect(Collectors.toCollection(TreeSet::new))
                                : Collections.emptySortedSet()
                );
            } else {
                token = token.advanceTo(globalSequence, maxGapOffset, allowGaps);
            }
            result.add(new TrackedDomainEventData<>(token, domainEvent));
        }
        return result;
    }

    private GapAwareTrackingToken cleanedToken(GapAwareTrackingToken lastToken) {
        GapAwareTrackingToken previousToken = lastToken;
        if (lastToken != null && lastToken.getGaps().size() > gapCleaningThreshold) {
            List<Object[]> results = transactionManager.fetchInTransaction(() -> entityManager()
                    .createQuery(
                            "SELECT e.globalIndex, e.timeStamp FROM " + domainEventEntryEntityName() + " e "
                                    + "WHERE e.globalIndex >= :firstGapOffset "
                                    + "AND e.globalIndex <= :maxGlobalIndex",
                            Object[].class
                    )
                    .setParameter("firstGapOffset", lastToken.getGaps().first())
                    .setParameter("maxGlobalIndex", lastToken.getGaps().last() + 1L)
                    .getResultList());
            for (Object[] result : results) {
                try {
                    Instant timestamp = DateTimeUtils.parseInstant(result[1].toString());
                    long sequenceNumber = (long) result[0];
                    if (previousToken.getGaps().contains(sequenceNumber) || timestamp.isAfter(gapTimeoutFrame())) {
                        // filled a gap, should not continue cleaning up
                        break;
                    }
                    if (previousToken.getGaps().contains(sequenceNumber - 1)) {
                        previousToken = previousToken.advanceTo(sequenceNumber - 1, maxGapOffset, false);
                    }
                } catch (DateTimeParseException e) {
                    logger.info("Unable to parse timestamp to clean old gaps", e);
                    break;
                }
            }
        }
        return previousToken;
    }

    private Instant gapTimeoutFrame() {
        return GenericEventMessage.clock.instant().minus(gapTimeout, ChronoUnit.MILLIS);
    }

    @Override
    @SuppressWarnings("unchecked")
    protected List<? extends DomainEventData<?>> fetchDomainEvents(String aggregateIdentifier, long firstSequenceNumber,
                                                                   int batchSize) {
        return transactionManager.fetchInTransaction(
                () -> entityManager()
                        .createQuery(
                                "SELECT new org.axonframework.eventsourcing.eventstore.GenericDomainEventEntry(" +
                                        "e.type, e.aggregateIdentifier, e.sequenceNumber, e.eventIdentifier, e.timeStamp, "
                                        + "e.payloadType, e.payloadRevision, e.payload, e.metaData) FROM "
                                        + domainEventEntryEntityName() + " e WHERE e.aggregateIdentifier = :id "
                                        + "AND e.sequenceNumber >= :seq ORDER BY e.sequenceNumber ASC"
                        )
                        .setParameter("id", aggregateIdentifier)
                        .setParameter("seq", firstSequenceNumber)
                        .setMaxResults(batchSize)
                        .getResultList());
    }

    @Override
    @SuppressWarnings("unchecked")
    protected Optional<? extends DomainEventData<?>> readSnapshotData(String aggregateIdentifier) {
        return transactionManager.fetchInTransaction(
                () -> entityManager()
                        .