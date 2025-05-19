Here's the fixed code with checks for negative keycodes:

```java
@Override
public boolean onKey (View v, int keyCode, android.view.KeyEvent e) {
    for (int i = 0, n = keyListeners.size(); i < n; i++)
        if (keyListeners.get(i).onKey(v, keyCode, e)) return true;

    synchronized (this) {
        KeyEvent event = null;

        if (e.getKeyCode() == android.view.KeyEvent.KEYCODE_UNKNOWN && e.getAction() == android.view.KeyEvent.ACTION_MULTIPLE) {
            String chars = e.getCharacters();
            for (int i = 0; i < chars.length(); i++) {
                event = usedKeyEvents.obtain();
                event.timeStamp = System.nanoTime();
                event.keyCode = 0;
                event.keyChar = chars.charAt(i);
                event.type = KeyEvent.KEY_TYPED;
                keyEvents.add(event);
            }
            return false;
        }

        char character = (char)e.getUnicodeChar();
        // Android doesn't report a unicode char for back space. hrm...
        if (keyCode == 67) character = '\b';
        if (e.getKeyCode() < 0 || e.getKeyCode() >= SUPPORTED_KEYS) return false;
        
        switch (e.getAction()) {
        case android.view.KeyEvent.ACTION_DOWN:
            event = usedKeyEvents.obtain();
            event.timeStamp = System.nanoTime();
            event.keyChar = 0;
            event.keyCode = e.getKeyCode();
            event.type = KeyEvent.KEY_DOWN;

            // Xperia hack for circle key. gah...
            if (keyCode == android.view.KeyEvent.KEYCODE_BACK && e.isAltPressed()) {
                keyCode = Keys.BUTTON_CIRCLE;
                event.keyCode = keyCode;
            }

            keyEvents.add(event);
            if (event.keyCode >= 0 && event.keyCode < keys.length && !keys[event.keyCode]) {
                keyCount++;
                keys[event.keyCode] = true;
            }
            break;
        case android.view.KeyEvent.ACTION_UP:
            long timeStamp = System.nanoTime();
            event = usedKeyEvents.obtain();
            event.timeStamp = timeStamp;
            event.keyChar = 0;
            event.keyCode = e.getKeyCode();
            event.type = KeyEvent.KEY_UP;
            // Xperia hack for circle key. gah...
            if (keyCode == android.view.KeyEvent.KEYCODE_BACK && e.isAltPressed()) {
                keyCode = Keys.BUTTON_CIRCLE;
                event.keyCode = keyCode;
            }
            keyEvents.add(event);

            event = usedKeyEvents.obtain();
            event.timeStamp = timeStamp;
            event.keyChar = character;
            event.keyCode = 0;
            event.type = KeyEvent.KEY_TYPED;
            keyEvents.add(event);

            if (keyCode == Keys.BUTTON_CIRCLE) {
                if (Keys.BUTTON_CIRCLE >= 0 && Keys.BUTTON_CIRCLE < keys.length && keys[Keys.BUTTON_CIRCLE]) {
                    keyCount--;
                    keys[Keys.BUTTON_CIRCLE] = false;
                }
            } else {
                if (e.getKeyCode() >= 0 && e.getKeyCode() < keys.length && keys[e.getKeyCode()]) {
                    keyCount--;
                    keys[e.getKeyCode()] = false;
                }
            }
        }
        app.getGraphics().requestRendering();
    }

    // circle button on Xperia Play shouldn't need catchBack == true
    if (keyCode == Keys.BUTTON_CIRCLE) return true;
    if (catchBack && keyCode == android.view.KeyEvent.KEYCODE_BACK) return true;
    if (catchMenu && keyCode == android.view.KeyEvent.KEYCODE_MENU) return true;
    return false;
}
```

The main changes are:
1. Added check for negative keycodes in the initial validation: `if (e.getKeyCode() < 0 || e.getKeyCode() >= SUPPORTED_KEYS) return false;`
2. Added bounds checking when accessing the keys array: `if (event.keyCode >= 0 && event.keyCode < keys.length && !keys[event.keyCode])`
3. Added bounds checking when clearing key states in the ACTION_UP case

These changes prevent ArrayIndexOutOfBoundsException when negative keycodes are received from certain devices.