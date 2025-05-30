## Buggy code
```java
package com.ning.http.client.providers.netty;

import com.ning.http.client.Body;
import com.ning.http.client.BodyGenerator;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.nio.ByteBuffer;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * {@link com.ning.http.client.BodyGenerator} which may return just part of the payload at the time handler is requesting it.
 * If it happens, PartialBodyGenerator becomes responsible for finishing payload transferring asynchronously.
 */
public class FeedableBodyGenerator implements BodyGenerator {
    private static final String US_ASCII = "US-ASCII";
    private final static byte[] END_PADDING = getBytes("\r\n");
    private final static byte[] ZERO = getBytes("0");
    private final Queue<BodyPart> queue = new ConcurrentLinkedQueue<BodyPart>();
    private final AtomicInteger queueSize = new AtomicInteger();
    private FeedListener listener;

    @Override
    public Body createBody() throws IOException {
        return new PushBody();
    }

    public void feed(final ByteBuffer buffer, final boolean isLast) throws IOException {
        queue.offer(new BodyPart(buffer, isLast));
        queueSize.incrementAndGet();
        if (listener != null) {
            listener.onContentAdded();
        }
    }

    public static interface FeedListener {
        void onContentAdded();
    }

    public void setListener(FeedListener listener) {
        this.listener = listener;
    }

    private final class PushBody implements Body {
        private final int ONGOING = 0;
        private final int CLOSING = 1;
        private final int FINISHED = 2;

        private int finishState = 0;

        @Override
        public long getContentLength() {
            return -1;
        }

        @Override
        public long read(final ByteBuffer buffer) throws IOException {
            BodyPart nextPart = queue.peek();
            if (nextPart == null) {
                // Nothing in the queue
                switch (finishState) {
                    case ONGOING:
                        return 0;
                    case CLOSING:
                        buffer.put(ZERO);
                        buffer.put(END_PADDING);
                        finishState = FINISHED;
                        return buffer.position();
                    case FINISHED:
                        buffer.put(END_PADDING);
                        return -1;
                }
            }
            int capacity = buffer.remaining() - 10; // be safe (we'll have to add size, ending, etc.)
            int size = Math.min(nextPart.buffer.remaining(), capacity);
            buffer.put(getBytes(Integer.toHexString(size)));
            buffer.put(END_PADDING);
            for (int i = 0; i < size; i++) {
                buffer.put(nextPart.buffer.get());
            }
            buffer.put(END_PADDING);
            if (!nextPart.buffer.hasRemaining()) {
                if (nextPart.isLast) {
                    finishState = CLOSING;
                }
                queue.remove();
            }
            return size;
        }

        @Override
        public void close() throws IOException {
        }

    }

    private final static class BodyPart {
        private final boolean isLast;
        private final ByteBuffer buffer;

        public BodyPart(final ByteBuffer buffer, final boolean isLast) {
            this.buffer = buffer;
            this.isLast = isLast;
        }
    }

    private static byte[] getBytes(String s) {
        // for compatibility with java5, we cannot use s.getBytes(Charset)
        try {
            return s.getBytes(US_ASCII);
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }
    }
}
```

## Error
avoid writing 2 new lines without content

## Error Description
Fix the following error happening on the server side:
java.lang.NullPointerException: null
    at org.jboss.netty.handler.codec.http.HttpClientCodec$Decoder.isContentAlwaysEmpty(HttpClientCodec.java:179) ~[netty-3.9.2.Final.jar:na]

