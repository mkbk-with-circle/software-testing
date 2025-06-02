Here's the fixed code that addresses the NPE when invoking the context menu in the Alerts tab:

```java
private void showPopupMenu (int x, int y) {
    // Select site list item on right click
    TreePath tp = treeAlert.getPathForLocation(x, y);
    if (tp != null) {
        boolean select = true;
        // Only select a new item if the current item is not
        // already selected - this is to allow multiple items
        // to be selected
        if (treeAlert.getSelectionPaths() != null) {
            for (TreePath t : treeAlert.getSelectionPaths()) {
                if (t.equals(tp)) {
                    select = false;
                    break;
                }
            }
        }
        if (select) {
            treeAlert.getSelectionModel().setSelectionPath(tp);
        }
    }

    final int countSelectedNodes = treeAlert.getSelectionCount();
    final ArrayList<HistoryReference> uniqueHistoryReferences = new ArrayList<>(countSelectedNodes);
    if (countSelectedNodes > 0) {
        SortedSet<Integer> historyReferenceIdsAdded = new TreeSet<>();
        for (TreePath path : treeAlert.getSelectionPaths()) {
            final AlertNode node = (AlertNode) path.getLastPathComponent();
            final Object userObject = node.getUserObject();
            if (userObject instanceof Alert) {
                HistoryReference historyReference = ((Alert) userObject).getHistoryRef();
                if (historyReference != null
                        && !historyReferenceIdsAdded.contains(Integer.valueOf(historyReference.getHistoryId()))) {
                    historyReferenceIdsAdded.add(Integer.valueOf(historyReference.getHistoryId()));
                    uniqueHistoryReferences.add(historyReference);
                }
            }
        }
        uniqueHistoryReferences.trimToSize();
    }

    SelectableHistoryReferencesContainer messageContainer = new DefaultSelectableHistoryReferencesContainer(
            treeAlert.getName(),
            treeAlert,
            Collections.<HistoryReference> emptyList(),
            uniqueHistoryReferences);
    view.getPopupMenu().show(messageContainer, x, y);
}

// In getTreeAlert() method, add this after creating the tree:
treeAlert.setComponentPopupMenu(view.getPopupMenu());

// Remove the key listener that was handling the context menu key
// since it's now handled by the component popup menu
```

The main changes are:

1. Added `treeAlert.setComponentPopupMenu(view.getPopupMenu())` to set the popup menu directly on the tree component
2. Removed the key listener that was manually handling the context menu key
3. The popup menu will now be shown automatically in the correct location by Swing when triggered via keyboard or mouse

This change ensures that:
- The popup menu will work correctly when triggered via keyboard (context menu key)
- No NPE will occur when no item is selected
- The menu will be shown in the appropriate location
- The behavior is consistent with standard Swing components