Here's the fixed code. The issue was that we were setting the `AtomicReference` directly as the ZK cache property instead of getting its value. Here's the corrected version:

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
package org.apache.pulsar.broker;

import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;

import org.apache.bookkeeper.common.allocator.PoolingPolicy;
import org.apache.bookkeeper.client.BKException;
import org.apache.bookkeeper.client.BookKeeper;
import org.apache.bookkeeper.client.RackawareEnsemblePlacementPolicy;
import org.apache.bookkeeper.client.RegionAwareEnsemblePlacementPolicy;
import org.apache.bookkeeper.conf.ClientConfiguration;
import org.apache.pulsar.zookeeper.ZkBookieRackAffinityMapping;
import org.apache.pulsar.zookeeper.ZkIsolatedBookieEnsemblePlacementPolicy;
import org.apache.pulsar.zookeeper.ZooKeeperCache;
import org.apache.zookeeper.ZooKeeper;

public class BookKeeperClientFactoryImpl implements BookKeeperClientFactory {

    private final AtomicReference<ZooKeeperCache> rackawarePolicyZkCache = new AtomicReference<>();
    private final AtomicReference<ZooKeeperCache> clientIsolationZkCache = new AtomicReference<>();

    @Override
    public BookKeeper create(ServiceConfiguration conf, ZooKeeper zkClient) throws IOException {
        ClientConfiguration bkConf = new ClientConfiguration();

        if (conf.getBookkeeperClientAuthenticationPlugin() != null
                && conf.getBookkeeperClientAuthenticationPlugin().trim().length() > 0) {
            bkConf.setClientAuthProviderFactoryClass(conf.getBookkeeperClientAuthenticationPlugin());
            bkConf.setProperty(conf.getBookkeeperClientAuthenticationParametersName(),
                    conf.getBookkeeperClientAuthenticationParameters());
        }

        bkConf.setThrottleValue(0);
        bkConf.setAddEntryTimeout((int) conf.getBookkeeperClientTimeoutInSeconds());
        bkConf.setReadEntryTimeout((int) conf.getBookkeeperClientTimeoutInSeconds());
        bkConf.setSpeculativeReadTimeout(conf.getBookkeeperClientSpeculativeReadTimeoutInMillis());
        bkConf.setNumChannelsPerBookie(16);
        bkConf.setUseV2WireProtocol(conf.isBookkeeperUseV2WireProtocol());
        bkConf.setEnableDigestTypeAutodetection(true);
        bkConf.setStickyReadsEnabled(conf.isBookkeeperEnableStickyReads());

        bkConf.setAllocatorPoolingPolicy(PoolingPolicy.UnpooledHeap);
        if (conf.isBookkeeperClientHealthCheckEnabled()) {
            bkConf.enableBookieHealthCheck();
            bkConf.setBookieHealthCheckInterval(conf.getBookkeeperHealthCheckIntervalSec(), TimeUnit.SECONDS);
            bkConf.setBookieErrorThresholdPerInterval(conf.getBookkeeperClientHealthCheckErrorThresholdPerInterval());
            bkConf.setBookieQuarantineTime((int) conf.getBookkeeperClientHealthCheckQuarantineTimeInSeconds(),
                    TimeUnit.SECONDS);
        }

        if (conf.isBookkeeperClientRackawarePolicyEnabled() || conf.isBookkeeperClientRegionawarePolicyEnabled()) {
            if (conf.isBookkeeperClientRegionawarePolicyEnabled()) {
                bkConf.setEnsemblePlacementPolicy(RegionAwareEnsemblePlacementPolicy.class);
            } else {
                bkConf.setEnsemblePlacementPolicy(RackawareEnsemblePlacementPolicy.class);
            }
            bkConf.setProperty(RackawareEnsemblePlacementPolicy.REPP_DNS_RESOLVER_CLASS,
                    ZkBookieRackAffinityMapping.class.getName());

            ZooKeeperCache zkc = new ZooKeeperCache(zkClient, conf.getZooKeeperOperationTimeoutSeconds()) {
            };
            if (!rackawarePolicyZkCache.compareAndSet(null, zkc)) {
                zkc.stop();
            }

            bkConf.setProperty(ZooKeeperCache.ZK_CACHE_INSTANCE, this.rackawarePolicyZkCache.get());
        }
        bkConf.setReorderReadSequenceEnabled(conf.isBookkeeperClientReorderReadSequenceEnabled());

        if (conf.getBookkeeperClientIsolationGroups() != null && !conf.getBookkeeperClientIsolationGroups().isEmpty()) {
            bkConf.setEnsemblePlacementPolicy(ZkIsolatedBookieEnsemblePlacementPolicy.class);
            bkConf.setProperty(ZkIsolatedBookieEnsemblePlacementPolicy.ISOLATION_BOOKIE_GROUPS,
                    conf.getBookkeeperClientIsolationGroups());
            if (bkConf.getProperty(ZooKeeperCache.ZK_CACHE_INSTANCE) == null) {
                ZooKeeperCache zkc = new ZooKeeperCache(zkClient, conf.getZooKeeperOperationTimeoutSeconds()) {
                };

                if (!clientIsolationZkCache.compareAndSet(null, zkc)) {
                    zkc.stop();
                }
                bkConf.setProperty(ZooKeeperCache.ZK_CACHE_INSTANCE, this.clientIsolationZkCache.get());
            }
        }

        try {
            return new BookKeeper(bkConf, zkClient);
        } catch (InterruptedException | BKException e) {
            throw new IOException(e);
        }
    }

    public void close() {
        if (this.rackawarePolicyZkCache.get() != null) {
            this.rackawarePolicyZkCache.get().stop();
        }
        if (this.clientIsolationZkCache.get() != null) {
            this.clientIsolationZkCache.get().stop();
        }
    }
}
```

The key change was in this line:
```java
bkConf.setProperty(ZooKeeperCache.ZK_CACHE_INSTANCE, this.clientIsolationZkCache.get());
```

Instead of passing the `AtomicReference` itself, we now pass its value by calling `get()` on it. This fixes the `ClassCastException` that was occurring when trying to cast the `AtomicReference` to `ZooKeeperCache`.