# Day 2: Structured Output - 学习流程

> **今日目标**: 让 LLM 输出结构化数据，为 Agent Router 做准备
> **核心问题**: 为什么 Agent 系统必须用 Structured Output？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_pydantic_models.py（10分钟）
    ↓ 理解：Pydantic 模型定义和校验
Step 4: 运行 01_intent_classifier.py（15分钟）
    ↓ 理解：意图分类器
Step 5: 完成 99_boss_answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 25min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释为什么 Agent 需要 Structured Output
- [ ] 解释 JSON Mode 和 Structured Output 的区别
- [ ] 理解 Pydantic BaseModel + Field 的用法
- [ ] 能独立实现意图分类器
- [ ] 能回答 Boss 4 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_pydantic_models.py](00_pydantic_models.py) | Pydantic 模型定义 | ⭐ |
| [01_intent_classifier.py](01_intent_classifier.py) | 意图分类器 | ⭐⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐ |
