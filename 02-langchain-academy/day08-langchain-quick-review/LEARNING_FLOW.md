# Day 8: LangChain 快速过 - 学习流程

> **今日目标**: 快速了解 LangChain，并用它重写 Day 7 的 Mini Agent
> **核心问题**: LangChain 和 LangGraph 有什么区别？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_langchain_basics.py（30分钟）
    ↓ 理解：Runnable、LCEL 链式调用、Tool 定义
Step 4: 运行 01_langchain_agent.py（45分钟）
    ↓ 理解：用 LangChain 创建 Tool Calling Agent
Step 5: 运行 02_compare_agent.py（45分钟）
    ↓ 理解：手写 vs LangChain 的差异
Step 6: 完成 99-boss-answer.md（30分钟）
    ↓
Step 7: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-5 | 3个代码文件 | 120min |
| 6 | Boss 问题 | 30min |
| 7 | 学习总结 | 15min |
| **总计** | | **约 3h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Runnable 和 LCEL 的核心概念
- [ ] 理解 LangChain Tool 定义和 Agent 用法
- [ ] 对比手写 Agent Runtime 和 LangChain Agent 的优劣
- [ ] 理解为什么 Agent 系统更倾向于用 LangGraph
- [ ] 能独立写出 LangChain Tool Calling Agent
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_langchain_basics.py](00_langchain_basics.py) | 理解 Runnable、LCEL、Tool | ⭐ |
| [01_langchain_agent.py](01_langchain_agent.py) | 用 LangChain 写 Agent | ⭐⭐ |
| [02_compare_agent.py](02_compare_agent.py) | 手写 vs LangChain 对比 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
