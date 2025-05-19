Here's the fixed code that replaces colons with dots in the crash report filename for Windows compatibility:

```java
File crashreportfile = new File(new File(coreMods.getParentFile(),"crash-reports"),String.format("fml-crash-%1$tY-%1$tm-%1$td_%1$tH.%1$tM.%1$tS.txt",Calendar.getInstance()));
```

The key change is replacing `%1$tT` (which formats time with colons) with `%1$tH.%1$tM.%1$tS` (which formats hours, minutes and seconds separately with dots between them). This matches the format used by vanilla Minecraft crash reports and works on Windows.

The rest of the code remains unchanged. This is the only modification needed to fix the Windows file naming issue while maintaining all the same functionality.