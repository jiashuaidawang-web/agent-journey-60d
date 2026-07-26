# Day 60: Memory 深度体系 - 学习流程

> **今日目标**: 掌握 Agent Memory 的完整体系：短期/长期/工作/情景记忆
> **核心问题**: 为什么 Agent 需要记忆？记忆体系是如何分层的？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_memory_hierarchy.py（15分钟）
    ↓ 理解：Memory 分层体系的工作流程
Step 4: 运行 01_redis_memory.py（15分钟）
    ↓ 理解：Redis 分布式记忆的实现
Step 5: 运行 02_multi_user_isolation.py（15分钟）
    ↓ 理解：多用户会话隔离机制
Step 6: 运行 03_pii_desensitization.py（15分钟）
    ↓ 理解：PII 脱敏的实现
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4个代码文件 | 60min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Agent 为什么需要记忆
- [ ] 解释四种记忆类型（Short-term/Long-term/Working/Episodic）
- [ ] 解释 TokenWindow 滑动窗口的工作原理
- [ ] 解释 SummaryMemory 摘要记忆的工作原理
- [ ] 解释 Redis 分布式记忆的实现
- [ ] 解释多用户会话隔离的实现
- [ ] 解释 PII 脱敏的策略和实现
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_memory_hierarchy.py](00_memory_hierarchy.py) | 理解 Memory 分层体系 | ⭐⭐ |
| [01_redis_memory.py](01_redis_memory.py) | 理解 Redis 分布式记忆 | ⭐⭐ |
| [02_multi_user_isolation.py](02_multi_user_isolation.py) | 理解多用户会话隔离 | ⭐⭐ |
| [03_pii_desensitization.py](03_pii_desensitization.py) | 理解 PII 脱敏 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
