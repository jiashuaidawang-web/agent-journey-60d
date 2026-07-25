# Day 19: BM25 + Hybrid（混合检索）- 学习流程

> **今日目标**: 实现混合检索，兼顾语义和关键词
> **核心问题**: 为什么单一检索不够？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_hybrid_retrieval.py（60分钟）
    ↓ 理解：BM25 + Dense 检索 + RRF 融合
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

- [ ] 解释 BM25 的原理（TF、IDF、文档长度）
- [ ] 理解为什么需要混合检索（单一检索的局限）
- [ ] 掌握 RRF 融合的计算方法
- [ ] 能独立实现混合检索 Pipeline
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_hybrid_retrieval.py](00_hybrid_retrieval.py) | 实现混合检索 + RRF 融合 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
