# DEVLoRe

#### 核心：

* 通过整合多种软件工件——**问题内容**、**调试信息**和**错误堆栈**，利用大LLM进行故障定位和程序修复
* 依靠两个轻量级工具：**MethodRecorder**（用于捕捉运行时执行过的方法签名）和 **DebugRecorder**（用于提取方法内部的调试信息）

#### 实验：

* 数据集：在 Defects4J 数据集上进行评估（v1.2和v2.0）
  * 缺陷引入版本
  * 缺陷修复版本
  * 测试套件
* 任务：覆盖单一方法和跨方法故障
* 对比实验：通过分别提供**问题内容**、**调试信息**和**错误堆栈**以及三者的组合来评估对故障定位和补丁生成的影响；（重点考察不同软件工件对 LLM 表现的补充效应）

#### 结论：

1. 问题内容在方法级故障定位上效果最佳（单一方法故障：43.6%，跨方法故障：40.6%）
2. 错误堆栈在单一方法故障修复上效果最佳（修复准确率：27.0%）
3. 不同类型的软件信息可以互补，在故障定位和修复上提升整体表现，特别是对跨方法故障的修复

#### 流程：

1. 故障定位阶段

   + 定位错误方法
     + 使用 **MethodRecorder** 记录运行失败测试时调用的所有方法签名；
     + 将**方法签名**、**问题内容**以及测试产生的**错误堆栈**一起输入给 LLM，定位出有问题的方法
     + 对比实验：**方法签名 + [问题内容] + [错误堆栈]**
   + 定位错误行
     + 使用 **DebugRecorder** 获取定位方法内的详细**调试信息**
     + 将**问题内容**、**错误堆栈**以及**调试信息**一起输入给 LLM，定位出有问题的行
     + 对比实验：**[问题内容] + [错误堆栈] + [调试信息]**
2. 补丁生成

   + 提供所有相关信息，以最大化 LLM 生成准确修复方案的能力
   + 生成多个 .diff 格式的候选补丁
   + 对比实验：**[问题内容] + [错误堆栈] + [调试信息]**
3. 补丁验证
   (ymy:我觉得验证的话我们只需要初步测试就行嘿嘿，如果学有余力那可以试试回归测试)

   + 初步测试：通过最初失败的测试
   + 回归测试：通过所有测试
   + Defects4J 框架测试

#### 其他

1. LLM prompt：
   固定化模版：General Task Prompt + Input Prompt + Expected Output Prompt

+ General Task Prompt: You are a Software Engineer......Try to fix the bug.
+ Input Prompt: {related_methods} {error_stack} {issue_content} {debugging_info}
+ Expected Output Prompt: Please localize/generate......

2. 使用**openai_api_key**：
   **DebugRecorder** 记录的调试信息可能极长，超出大多数 LLM 的 token 限制，采用了 GPT-4o-mini（支持 128k token 的上下文窗口）

# SWE-BENCH

#### 任务定义

+ 输入：包含GitHub问题描述和完整代码库快照
+ 输出：生成一个补丁文件，使得代码在应用补丁后，相关测试由失败转为通过

#### 数据采集与筛选流程

+ 数据来源：收集自12个流行Python仓库的合并Pull Request
