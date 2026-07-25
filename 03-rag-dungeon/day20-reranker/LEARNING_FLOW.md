# Day 20: Reranker（重排序）- 学习流程

> **今日目标**: 实现重排序，提升检索精度
> **核心问题**: 为什么检索后还需要重排序？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_two_stage_retrieval.py（60分钟）
    ↓ 理解：召回 + 精排两阶段检索实现
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

- [ ] 解释为什么需要重排序（召回阶段的局限）
- [ ] 区分 Cross-Encoder 和 Bi-Encoder
- [ ] 理解两阶段检索的优势
- [ ] 掌握 bge-reranker 的使用
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_two_stage_retrieval.py](00_two_stage_retrieval.py) | 实现两阶段检索（召回 + 精排） | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
