Based on the error stack trace, the NPE occurs in Android 2.x (Froyo) when calling `selectNow()` on the Selector. This appears to be a platform bug in older Android versions. The fix is to wrap the `selectNow()` call in a try-catch block to handle this case gracefully.

Here's the fixed code for the `runLoop` method:

```java
private static void runLoop(final AsyncServer server, final SelectorWrapper selector, final PriorityQueue<Scheduled> queue) throws AsyncSelectorException {
//        Log.i(LOGTAG, "Keys: " + selector.keys().size());
    boolean needsSelect = true;

    // run the queue to populate the selector with keys
    long wait = lockAndRunQueue(server, queue);
    try {
        synchronized (server) {
            // select now to see if anything is ready immediately. this
            // also clears the canceled key queue.
            int readyNow;
            try {
                readyNow = selector.selectNow();
            }
            catch (NullPointerException e) {
                // Android 2.x bug, treat as if nothing was ready
                readyNow = 0;
            }
            if (readyNow == 0) {
                // if there is nothing to select now, make sure we don't have an empty key set
                // which means it would be time to turn this thread off.
                if (selector.keys().size() == 0 && wait == QUEUE_EMPTY) {
//                    Log.i(LOGTAG, "Shutting down. keys: " + selector.keys().size() + " keepRunning: " + keepRunning);
                    return;
                }
            }
            else {
                needsSelect = false;
            }
        }

        if (needsSelect) {
            if (wait == QUEUE_EMPTY) {
                // wait until woken up
                selector.select();
            }
            else {
                // nothing to select immediately but there's something pending so let's block that duration and wait.
                selector.select(wait);
            }
        }
    }
    catch (IOException e) {
        throw new AsyncSelectorException(e);
    }

    // process whatever keys are ready
    Set<SelectionKey> readyKeys = selector.selectedKeys();
    for (SelectionKey key: readyKeys) {
        try {
            if (key.isAcceptable()) {
                ServerSocketChannel nextReady = (ServerSocketChannel) key.channel();
                SocketChannel sc = null;
                SelectionKey ckey = null;
                try {
                    sc = nextReady.accept();
                    if (sc == null)
                        continue;
                    sc.configureBlocking(false);
                    ckey = sc.register(selector.getSelector(), SelectionKey.OP_READ);
                    ListenCallback serverHandler = (ListenCallback) key.attachment();
                    AsyncNetworkSocket handler = new AsyncNetworkSocket();
                    handler.attach(sc, (InetSocketAddress)sc.socket().getRemoteSocketAddress());
                    handler.setup(server, ckey);
                    ckey.attach(handler);
                    serverHandler.onAccepted(handler);
                }
                catch (IOException e) {
                    StreamUtility.closeQuietly(sc);
                    if (ckey != null)
                        ckey.cancel();
                }
            }
            else if (key.isReadable()) {
                AsyncNetworkSocket handler = (AsyncNetworkSocket) key.attachment();
                int transmitted = handler.onReadable();
                server.onDataReceived(transmitted);
            }
            else if (key.isWritable()) {
                AsyncNetworkSocket handler = (AsyncNetworkSocket) key.attachment();
                handler.onDataWritable();
            }
            else if (key.isConnectable()) {
                ConnectFuture cancel = (ConnectFuture) key.attachment();
                SocketChannel sc = (SocketChannel) key.channel();
                key.interestOps(SelectionKey.OP_READ);
                AsyncNetworkSocket newHandler;
                try {
                    sc.finishConnect();
                    newHandler = new AsyncNetworkSocket();
                    newHandler.setup(server, key);
                    newHandler.attach(sc, (InetSocketAddress)sc.socket().getRemoteSocketAddress());
                    key.attach(newHandler);
                }
                catch (IOException ex) {
                    key.cancel();
                    StreamUtility.closeQuietly(sc);
                    if (cancel.setComplete(ex))
                        cancel.callback.onConnectCompleted(ex, null);
                    continue;
                }
                try {
                    if (cancel.setComplete(newHandler))
                        cancel.callback.onConnectCompleted(null, newHandler);
                }
                catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
            else {
                Log.i(LOGTAG, "wtf");
                throw new RuntimeException("Unknown key state.");
            }
        }
        catch (CancelledKeyException ex) {
        }
    }
    readyKeys.clear();
}
```

The key change is wrapping the `selector.selectNow()` call in a try-catch block to handle the NullPointerException that can occur on Android 2.x devices. When this happens, we treat it as if no keys were ready (readyNow = 0) and continue with normal processing.

This change maintains the same behavior while preventing the rare crash on older Android versions. The rest of the method remains unchanged.