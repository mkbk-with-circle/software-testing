Here's the fixed code with the main method modified to handle the SecurityException from Oozie:

```java
    public static void main(String[] args) {
        int res;
        try {
            res = ToolRunner.run(new Configuration(), new HadoopStoreJobRunner(), args);
            System.exit(res);
        } catch(SecurityException e) {
            // Ignore SecurityException from Oozie's launcher
            return;
        } catch(Exception e) {
            e.printStackTrace();
            System.err.print("\nTry '--help' for more information.");
            System.exit(1);
        }
    }
```

The change adds a specific catch block for SecurityException before the general Exception catch. When running under Oozie, the SecurityException from the launcher will be caught and ignored, allowing successful jobs to complete normally. Other exceptions will still be handled as before.