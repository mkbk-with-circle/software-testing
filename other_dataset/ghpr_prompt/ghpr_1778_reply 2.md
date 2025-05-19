Here's the fixed code that prevents the crash by properly handling the widget cleanup during shutdown:

```java
@Override
public void shutDown()
{
    spriteManager.removeSpriteOverrides(WikiSprite.values());
    clientThread.invokeLater(() ->
    {
        Widget minimapOrbs = client.getWidget(WidgetInfo.MINIMAP_ORBS);
        if (minimapOrbs == null)
        {
            return;
        }
        Widget[] children = minimapOrbs.getChildren();
        if (children == null || children.length < 1)
        {
            return;
        }
        // Properly clean up the widget
        if (icon != null)
        {
            icon.setHidden(true);
            icon.setOnTargetEnterListener(null);
            icon.setOnTargetLeaveListener(null);
            icon.setOnOpListener(null);
            icon = null;
        }
        children[0] = null;
    });
}
```

The fix involves:
1. Properly cleaning up the icon widget by setting it to hidden
2. Removing all event listeners from the widget
3. Setting the icon reference to null
4. Still maintaining the original behavior of clearing the children array

This prevents any potential NPEs that could occur when trying to interact with the widget after the plugin has been shut down.