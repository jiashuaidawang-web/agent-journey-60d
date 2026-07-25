# Day 13: LangGraph Long-running Agent + Subgraph - 学习流程

> **今日目标**: 实现长时间运行的 Agent 和子图
> **核心问题**: 复杂 Agent 如何拆分和组合？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_long_running_agent.py（45分钟）
    ↓ 理解：多步骤任务 + 中断恢复
Step 4: 运行 01_subgraph_demo.py（60分钟）
    ↓ 理解：子图的使用 + 图嵌套
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 105min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 2.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Subgraph 的作用和优势
- [ ] 理解为什么要用 Subgraph 而不是一个大 Graph
- [ ] 理解长时间运行 Agent 如何保证可靠性
- [ ] 能独立实现子图嵌套
- [ ] 能独立实现长时间运行 Agent
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_long_running_agent.py](00_long_running_agent.py) | 多步骤 + 中断恢复 | ⭐⭐ |
| [01_subgraph_demo.py](01_subgraph_demo.py) | 子图 + 图嵌套 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
