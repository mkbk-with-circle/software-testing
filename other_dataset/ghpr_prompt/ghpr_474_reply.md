I'll help fix the initialization order issue in the ConsumerImpl class. The problem is that the `acknowledgmentsGroupingTracker` is initialized before the `connectionHandler`, which can lead to a race condition. Here's the fixed code:

```java
public ConsumerImpl(PulsarClientImpl client, String topic, ConsumerConfigurationData<T> conf,
                 ExecutorService listenerExecutor, int partitionIndex, CompletableFuture<Consumer<T>> subscribeFuture,
                 SubscriptionMode subscriptionMode, MessageId startMessageId, Schema<T> schema) {
    super(client, topic, conf, conf.getReceiverQueueSize(), listenerExecutor, subscribeFuture, schema);
    this.consumerId = client.newConsumerId();
    this.subscriptionMode = subscriptionMode;
    this.startMessageId = startMessageId != null ? new BatchMessageIdImpl((MessageIdImpl) startMessageId) : null;
    AVAILABLE_PERMITS_UPDATER.set(this, 0);
    this.subscribeTimeout = System.currentTimeMillis() + client.getConfiguration().getOperationTimeoutMs();
    this.partitionIndex = partitionIndex;
    this.receiverQueueRefillThreshold = conf.getReceiverQueueSize() / 2;
    this.priorityLevel = conf.getPriorityLevel();
    this.readCompacted = conf.isReadCompacted();
    this.subscriptionInitialPosition = conf.getSubscriptionInitialPosition();

    // Initialize connectionHandler first
    this.connectionHandler = new ConnectionHandler(this,
        new Backoff(100, TimeUnit.MILLISECONDS, 60, TimeUnit.SECONDS, 0, TimeUnit.MILLISECONDS),
        this);

    // Then initialize acknowledgmentsGroupingTracker
    TopicName topicName = TopicName.get(topic);
    if (topicName.isPersistent()) {
        this.acknowledgmentsGroupingTracker =
            new PersistentAcknowledgmentsGroupingTracker(this, conf, client.eventLoopGroup());
    } else {
        this.acknowledgmentsGroupingTracker =
            NonPersistentAcknowledgmentGroupingTracker.of();
    }

    if (client.getConfiguration().getStatsIntervalSeconds() > 0) {
        stats = new ConsumerStatsRecorderImpl(client, conf, this);
    } else {
        stats = ConsumerStatsDisabled.INSTANCE;
    }

    if (conf.getReceiverQueueSize() <= 1) {
        zeroQueueLock = new ReentrantReadWriteLock();
    } else {
        zeroQueueLock = null;
    }

    if (conf.getAckTimeoutMillis() != 0) {
        this.unAckedMessageTracker = new UnAckedMessageTracker(client, this, conf.getAckTimeoutMillis());
    } else {
        this.unAckedMessageTracker = UnAckedMessageTracker.UNACKED_MESSAGE_TRACKER_DISABLED;
    }

    // Create msgCrypto if not created already
    if (conf.getCryptoKeyReader() != null) {
        String logCtx = "[" + topic + "] [" + subscription + "]";
        this.msgCrypto = new MessageCrypto(logCtx, false);
    }

    if (conf.getProperties().isEmpty()) {
        metadata = Collections.emptyMap();
    } else {
        metadata = Collections.unmodifiableMap(new HashMap<>(conf.getProperties()));
    }

    grabCnx();
}
```

The key change is moving the `connectionHandler` initialization before the `acknowledgmentsGroupingTracker` initialization. This ensures that when the `PersistentAcknowledgmentsGroupingTracker` is created and potentially schedules its first flush task, the `connectionHandler` field is already initialized and available.

This prevents the race condition where the flush task could try to access `connectionHandler` through `getClientCnx()` before it was initialized, which was causing the NPE.