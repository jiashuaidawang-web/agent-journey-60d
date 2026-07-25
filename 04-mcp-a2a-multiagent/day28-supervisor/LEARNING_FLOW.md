# Day 28: Multi-Agent Supervisor - 学习流程

> **今日目标**: 实现 Supervisor 模式的多 Agent 协调
> **核心问题**: Supervisor 如何协调多个 Agent？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_supervisor_demo.py（30分钟）
    ↓ 理解：Supervisor 模式、任务分配、并行/流水线执行
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 30min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Supervisor 模式的流程
- [ ] 理解任务分配策略（能力匹配、负载均衡）
- [ ] 理解 Worker 失败的处理策略
- [ ] 理解 Supervisor 与 LangGraph 的集成方式
- [ ] 能独立实现 Supervisor + Worker 架构
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_supervisor_demo.py](00_supervisor_demo.py) | 实现 Supervisor 模式 + 任务分配 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
