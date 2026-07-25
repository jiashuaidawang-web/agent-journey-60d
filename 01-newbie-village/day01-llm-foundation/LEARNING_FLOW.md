# Day 1: LLM Foundation - 学习流程

> **今日目标**: 打通 LLM 调用的4种模式：同步、流式、异步、异步流式
> **核心问题**: 为什么 Agent 系统必须关心 Token 和 Context？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_model_config.py（10分钟）
    ↓ 理解：模型配置是怎么加载的
Step 4: 运行 01_sync_chat.py（15分钟）
    ↓ 理解：同步调用流程
Step 5: 运行 02_stream_chat.py（15分钟）
    ↓ 理解：流式调用 + TTFT/TPS
Step 6: 运行 03_async_chat.py（15分钟）
    ↓ 理解：异步并发调用
Step 7: 运行 04_async_stream.py（15分钟）
    ↓ 理解：异步流式调用
Step 8: 完成 99_boss_answer.md（30分钟）
    ↓
Step 9: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-7 | 5个代码文件 | 70min |
| 8 | Boss 问题 | 30min |
| 9 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Sync / Stream / Async / Async Stream 的区别
- [ ] 解释 Token 是什么，中英文 Token 化区别
- [ ] 解释 Context Window 是什么，为什么有限制
- [ ] 解释 TTFT 和 TPS 是什么
- [ ] 能独立写出4种调用模式的代码
- [ ] 能回答 Boss 7 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_model_config.py](Model_config.py) | 理解模型配置加载 | ⭐ |
| [01_sync_chat.py](01_sync_chat.py) | 同步调用 LLM | ⭐ |
| [02_stream_chat.py](02_stream_chat.py) | 流式调用 + TTFT/TPS | ⭐⭐ |
| [03_async_chat.py](03_async_chat.py) | 异步并发调用 | ⭐⭐ |
| [04_async_stream.py](04_async_stream.py) | 异步流式调用 | ⭐⭐⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐ |
