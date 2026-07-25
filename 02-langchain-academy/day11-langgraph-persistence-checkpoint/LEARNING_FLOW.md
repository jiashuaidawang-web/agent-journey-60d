# Day 11: LangGraph Persistence + Checkpoint - 学习流程

> **今日目标**: 实现 Agent 的断点续跑
> **核心问题**: Agent 如何从中断中恢复？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_checkpoint_demo.py（45分钟）
    ↓ 理解：Checkpoint 机制 + MemorySaver + 多会话
Step 4: 运行 01_resume_demo.py（60分钟）
    ↓ 理解：断点续跑 + update_state
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

- [ ] 解释 Checkpoint 机制及其作用
- [ ] 理解 Thread 和多会话隔离
- [ ] 理解如何实现断点续跑
- [ ] 能独立使用 MemorySaver 保存状态
- [ ] 能独立实现状态更新和历史查询
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_checkpoint_demo.py](00_checkpoint_demo.py) | Checkpoint + 多会话演示 | ⭐⭐ |
| [01_resume_demo.py](01_resume_demo.py) | 断点续跑演示 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
