# Day 44: GraphRAG Hybrid - 学习流程

> **今日目标**: 实现 GraphRAG + 向量检索的混合索引
> **核心问题**: 如何结合图检索和向量检索的优势？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_hybrid_retrieval.py（15分钟）
    ↓ 理解：混合检索（向量检索 + 图检索 + RRF 融合）
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 15min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释混合索引的优势（向量检索 vs 图检索的互补）
- [ ] 描述混合检索的流程
- [ ] 解释三种融合策略（RRF / Weighted / Sequential）
- [ ] 能独立实现混合检索代码
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_hybrid_retrieval.py](00_hybrid_retrieval.py) | 混合检索（向量 + 图 + RRF 融合） | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
