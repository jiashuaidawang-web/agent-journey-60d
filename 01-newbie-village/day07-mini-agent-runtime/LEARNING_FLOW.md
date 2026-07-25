# Day 7: Mini Agent Runtime - 学习流程

> **今日目标**: 把前6天全部串起来，实现一个完整的 Mini Agent Runtime
> **核心要求**: 禁止使用 LangChain / LangGraph，完全自己造轮子

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 浏览 mini_agent_runtime/ 目录结构（10分钟）
    ↓ 理解：模块划分
Step 4: 阅读 core/__init__.py（15分钟）
    ↓ 理解：Agent + AgentLoop + ContextManager
Step 5: 阅读 model/__init__.py（10分钟）
    ↓ 理解：Model 接口 + OpenAIModel
Step 6: 阅读 tools/__init__.py（10分钟）
    ↓ 理解：Tool + ToolRegistry
Step 7: 阅读 memory/__init__.py（5分钟）
    ↓ 理解：Memory
Step 8: 运行 examples/run_agent.py（10分钟）
    ↓ 验证：整体能跑通
Step 9: 运行 tests/test_runtime.py（5分钟）
    ↓ 验证：测试通过
Step 10: 完成 99_boss_answer.md（30分钟）
    ↓
Step 11: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-9 | 阅读和运行代码 | 65min |
| 10 | Boss 问题 | 30min |
| 11 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 画出完整架构图并解释每个模块
- [ ] 能手写 Agent Loop
- [ ] 能解释为什么需要 State / Memory / Context 分离
- [ ] 能回答 Boss 14 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [mini_agent_runtime/core/__init__.py](mini_agent_runtime/core/__init__.py) | Agent 核心 | ⭐⭐⭐ |
| [mini_agent_runtime/model/__init__.py](mini_agent_runtime/model/__init__.py) | 模型抽象 | ⭐⭐ |
| [mini_agent_runtime/tools/__init__.py](mini_agent_runtime/tools/__init__.py) | 工具系统 | ⭐⭐ |
| [mini_agent_runtime/memory/__init__.py](mini_agent_runtime/memory/__init__.py) | 记忆系统 | ⭐ |
| [examples/run_agent.py](examples/run_agent.py) | 运行示例 | ⭐⭐ |
| [tests/test_runtime.py](tests/test_runtime.py) | 测试 | ⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐⭐ |
