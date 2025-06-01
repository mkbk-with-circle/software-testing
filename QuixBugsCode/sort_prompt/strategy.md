### 🎯 类别 1：模拟人类调试逻辑（Top-down）
```text
1. Failed test → Error → Test line → Error Code Block → Buggy code
```

### 🎯 类别 2：从 code 启发（Bottom-up）

```text
2. Buggy code → Error Code Block → Test line → Failed test → Error
```

### 🎯 类别 3：Test-first 策略

```text
3. Error Code Block → Test line → Failed test → Error → Buggy code
```

### 🎯 类别 4：Buggy-code 优先（模仿 CodeT5、Codex）

```text
4. Buggy code → Test line → Failed test → Error Code Block → Error
```

### 🎯 类别 5：先报错，后源码（反向推理）

```text
5. Error → Failed test → Test line → Error Code Block → Buggy code
```

### 🎯 类别 6：LLM 默认 style（常见文档风格）

```text
6. Buggy code → Failed test → Error → Error Code Block → Test line
```
