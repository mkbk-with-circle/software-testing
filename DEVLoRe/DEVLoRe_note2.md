## MethodRecorder

1. MethodRecorder 是由三个 Kotlin 文件构成的一个基于 Java Agent 的方法调用监控系统
2. 通过在目标方法开头插入调用监控函数的指令，每当这些方法被调用时，就会触发对 MethodRecorder.record 方法的调用，从而记录该方法的唯一标识（完整类名::方法名）
3. 在测试运行过程中，可以通过日志信息了解到哪些方法被调用
4. [MethodRecorder](https://github.com/XYZboom/MethodRecorder) 可单独使用

## DebugRecorder

1. DebugRecorder 结构与 MethodRecorder 类似
2. 通过在方法的每个执行行前插入调用监控函数的指令，在目标方法内每到一个行号时，就会读取局部变量表，从而构造并记录变量集合
3. 在每个行号处重复上述过程，能够动态捕捉方法内各个时刻局部变量的状态变化
4. 对变量信息进行格式化输出，同样记录到日志中
5. [DebugRecorder](https://github.com/XYZboom/DebugRecorder) 可单独使用
   
## 使用方法

1. 在 JVM（java虚拟机）启动时通过 -javaagent 参数加载 Recorder
2. 运行后，通过日志即可查看记录情况

## Defects4J 

1. 调用 Defects4J 的 pids 命令，可以返回所有项目的 ID 列表
2. 传入项目 ID，调用 Defects4J 的 bids 命令，可以返回该项目中所有 Bug 的 ID
3. 调用 Defects4J 的 checkout 命令，可以检出指定项目 (pid) 和 Bug (bid) 的代码
