修复后的代码主要添加了对`mEndCallback`是否为null的检查，防止空指针异常。以下是修复后的代码：

```java
package com.koushikdutta.async;

import com.koushikdutta.async.callback.CompletedCallback;
import com.koushikdutta.async.callback.DataCallback;

public class BufferedDataEmitter implements DataEmitter, DataCallback {
    DataEmitter mEmitter;
    public BufferedDataEmitter(DataEmitter emitter) {
        mEmitter = emitter;
        mEmitter.setDataCallback(this);
        
        mEmitter.setEndCallback(new CompletedCallback() {
            @Override
            public void onCompleted(Exception ex) {
                mEnded = true;
                mEndException = ex;
                if (mBuffers.remaining() == 0 && mEndCallback != null)
                    mEndCallback.onCompleted(ex);
            }
        });
    }

    @Override
    public void close() {
        mEmitter.close();
    }

    boolean mEnded = false;
    Exception mEndException;
    
    public void onDataAvailable() {
        if (mDataCallback != null && !mPaused && mBuffers.remaining() > 0)
            mDataCallback.onDataAvailable(this, mBuffers);
        
        if (mEnded && mBuffers.remaining() == 0 && mEndCallback != null)
            mEndCallback.onCompleted(mEndException);
    }
    
    ByteBufferList mBuffers = new ByteBufferList();

    DataCallback mDataCallback;
    @Override
    public void setDataCallback(DataCallback callback) {
        mDataCallback = callback;
    }

    @Override
    public DataCallback getDataCallback() {
        return mDataCallback;
    }

    @Override
    public boolean isChunked() {
        return false;
    }

    @Override
    public void onDataAvailable(DataEmitter emitter, ByteBufferList bb) {
        bb.get(mBuffers);

        onDataAvailable();        
    }

    private boolean mPaused;
    @Override
    public void pause() {
        mPaused = true;
    }

    @Override
    public void resume() {
        if (!mPaused)
            return;
        mPaused = false;
        onDataAvailable();
    }

    @Override
    public boolean isPaused() {
        return mPaused;
    }


    CompletedCallback mEndCallback;
    @Override
    public void setEndCallback(CompletedCallback callback) {
        mEndCallback = callback;
    }

    @Override
    public CompletedCallback getEndCallback() {
        return mEndCallback;
    }

    @Override
    public AsyncServer getServer() {
        return mEmitter.getServer();
    }

    @Override
    public String charset() {
        return mEmitter.charset();
    }
}
```

主要修改是在`onDataAvailable()`方法中，在调用`mEndCallback.onCompleted()`之前添加了对`mEndCallback`是否为null的检查。这样可以避免当`mEndCallback`未设置时出现空指针异常。