# Day 57: LangChain4j + ChatMemory - 学习流程

> **今日目标**: 掌握 LangChain4j 框架，理解 ChatMemory 记忆对话机制与多会话管理
> **核心问题**: ChatMemory 如何实现跨会话记忆？如何支持多用户隔离？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 浏览 LangChain4j 官方文档（10分钟）
    ↓ 理解：框架概览与核心组件
Step 4: 运行 00_langchain4j_basics.py（15分钟）
    ↓ 理解：框架基础与模型接入
Step 5: 运行 01_chatmemory_demo.py（20分钟）
    ↓ 理解：记忆对话机制
Step 6: 运行 02_persistence.py（20分钟）
    ↓ 理解：持久化策略
Step 7: 完成 99_boss_answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 浏览官方文档 | 10min |
| 4-6 | 3个代码文件 | 55min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 LangChain4j 框架概览与 Spring AI 对比
- [ ] 掌握 ChatMemory 核心接口与实现
- [ ] 实现对话隔离与多会话管理
- [ ] 实现 Redis / MySQL 持久化
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_langchain4j_basics.py](00_langchain4j_basics.py) | 框架基础与模型接入 | ⭐ |
| [01_chatmemory_demo.py](01_chatmemory_demo.py) | 记忆对话机制 | ⭐⭐ |
| [02_persistence.py](02_persistence.py) | Redis/MySQL 持久化 | ⭐⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐ |
