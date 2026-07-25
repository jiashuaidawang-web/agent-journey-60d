# Day 12: LangGraph Human-in-the-loop - 学习流程

> **今日目标**: 实现人工审批流程
> **核心问题**: Agent 如何在关键步骤暂停等待人工确认？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_approval_demo.py（60分钟）
    ↓ 理解：人工审批流程 + interrupt_after
Step 4: 运行 01_tool_approval.py（45分钟）
    ↓ 理解：工具调用前的人工审批
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

- [ ] 解释 interrupt 机制和 Checkpoint 的关系
- [ ] 理解 interrupt_after 和 interrupt_before 的区别
- [ ] 理解什么场景需要 Human-in-the-loop
- [ ] 能独立实现人工审批流程
- [ ] 能独立实现审批通过/拒绝的不同处理
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_approval_demo.py](00_approval_demo.py) | 人工审批流程演示 | ⭐⭐ |
| [01_tool_approval.py](01_tool_approval.py) | 工具调用审批演示 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
