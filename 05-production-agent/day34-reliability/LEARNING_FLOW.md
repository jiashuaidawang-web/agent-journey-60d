# Day 34: Reliability - 学习流程

> **今日目标**: 实现 Agent 系统的可靠性保障
> **核心问题**: 如何保证 Agent 系统稳定运行？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_retry_demo.py（60分钟）
    ↓ 理解：Retry 机制 + Circuit Breaker
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 60min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Retry 机制的关键参数
- [ ] 理解 Circuit Breaker 的三种状态转换
- [ ] 实现指数退避的重试逻辑
- [ ] 理解幂等性的实现方式
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_retry_demo.py](00_retry_demo.py) | Retry + Circuit Breaker 实现 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
