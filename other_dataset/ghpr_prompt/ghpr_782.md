## Buggy code
```java
/*
 * Copyright 2015 Ben Manes. All Rights Reserved.
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
package com.github.benmanes.caffeine.jcache.event;

import static java.util.Objects.requireNonNull;

import java.util.logging.Level;
import java.util.logging.Logger;

import javax.annotation.Nonnull;
import javax.cache.event.CacheEntryCreatedListener;
import javax.cache.event.CacheEntryEvent;
import javax.cache.event.CacheEntryExpiredListener;
import javax.cache.event.CacheEntryListener;
import javax.cache.event.CacheEntryRemovedListener;
import javax.cache.event.CacheEntryUpdatedListener;
import javax.cache.event.EventType;

/**
 * A decorator that dispatches the event iff the listener supports that action.
 *
 * @author ben.manes@gmail.com (Ben Manes)
 */
final class EventTypeAwareListener<K, V> implements CacheEntryCreatedListener<K, V>,
    CacheEntryUpdatedListener<K, V>, CacheEntryRemovedListener<K, V>,
    CacheEntryExpiredListener<K, V> {
  static final Logger logger = Logger.getLogger(EventTypeAwareListener.class.getName());

  final CacheEntryListener<? super K, ? super V> listener;

  public EventTypeAwareListener(CacheEntryListener<? super K, ? super V> listener) {
    this.listener = requireNonNull(listener);
  }

  /** Returns if the backing listener consumes this type of event. */
  public boolean isCompatible(@Nonnull EventType eventType) {
    switch (eventType) {
      case CREATED:
        return (listener instanceof CacheEntryCreatedListener<?, ?>);
      case UPDATED:
        return (listener instanceof CacheEntryUpdatedListener<?, ?>);
      case REMOVED:
        return (listener instanceof CacheEntryRemovedListener<?, ?>);
      case EXPIRED:
        return (listener instanceof CacheEntryExpiredListener<?, ?>);
    }
    throw new IllegalStateException("Unknown event type: " + eventType);
  }

  /** Processes the event and logs if an exception is thrown. */
  public void dispatch(@Nonnull JCacheEntryEvent<K, V> event) {
    try {
      switch (event.getEventType()) {
        case CREATED:
          onCreated(event);
          break;
        case UPDATED:
          onUpdated(event);
          break;
        case REMOVED:
          onRemoved(event);
          break;
        case EXPIRED:
          onExpired(event);
          break;
      }
      throw new IllegalStateException("Unknown event type: " + event.getEventType());
    } catch (Exception e) {
      logger.log(Level.WARNING, null, e);
    } catch (Throwable t) {
      logger.log(Level.SEVERE, null, t);
    }
  }

  @Override
  @SuppressWarnings("unchecked")
  public void onCreated(Iterable<CacheEntryEvent<? extends K, ? extends V>> events) {
    if (listener instanceof CacheEntryCreatedListener<?, ?>) {
      ((CacheEntryCreatedListener<K, V>) listener).onCreated(events);
    }
  }

  @Override
  @SuppressWarnings("unchecked")
  public void onUpdated(Iterable<CacheEntryEvent<? extends K, ? extends V>> events) {
    if (listener instanceof CacheEntryUpdatedListener<?, ?>) {
      ((CacheEntryUpdatedListener<K, V>) listener).onUpdated(events);
    }
  }

  @Override
  @SuppressWarnings("unchecked")
  public void onRemoved(Iterable<CacheEntryEvent<? extends K, ? extends V>> events) {
    if (listener instanceof CacheEntryRemovedListener<?, ?>) {
      ((CacheEntryRemovedListener<K, V>) listener).onRemoved(events);
    }
  }

  @Override
  @SuppressWarnings("unchecked")
  public void onExpired(Iterable<CacheEntryEvent<? extends K, ? extends V>> events) {
    if (listener instanceof CacheEntryExpiredListener<?, ?>) {
      ((CacheEntryExpiredListener<K, V>) listener).onExpired(events);
    }
  }
}

```

## Error
Fix IllegalStateException being thrown for all event types.

## Error Description
I ran into a problem where an IllegalStateException was being thrown every time my event listeners were invoked.

```
Jul 02, 2017 9:30:20 PM com.github.benmanes.caffeine.jcache.event.EventTypeAwareListener dispatch
WARNING: null
java.lang.IllegalStateException: Unknown event type: REMOVED
	at com.github.benmanes.caffeine.jcache.event.EventTypeAwareListener.dispatch(EventTypeAwareListener.java:80)
	at com.github.benmanes.caffeine.jcache.event.EventDispatcher.lambda$publish$2(EventDispatcher.java:215)
	at java.util.concurrent.CompletableFuture.uniRun(CompletableFuture.java:705)
	at java.util.concurrent.CompletableFuture$UniRun.tryFire(CompletableFuture.java:687)
	at java.util.concurrent.CompletableFuture$Completion.exec(CompletableFuture.java:443)
	at java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:289)
	at java.util.concurrent.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:1056)
	at java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1692)
	at java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:157)
```

I traced it down to what appears to be a missing default case in the EventType switch statement. This patch resolves the issue for me and passes the relevant tests.
