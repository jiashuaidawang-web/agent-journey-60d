# Day 39: RAG Evaluation - 学习流程

> **今日目标**: 掌握 RAG 系统的评测方法（检索评测 + 生成评测）
> **核心问题**: 如何评估 RAG 系统的效果？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_generation_eval.py（15分钟）
    ↓ 理解：生成质量评测（Faithfulness + Answer Relevance）
Step 4: 运行 01_retrieval_eval.py（15分钟）
    ↓ 理解：检索质量评测（Precision@K / Recall@K / MRR / NDCG@K）
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 30min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 RAG 评测的两个维度（检索质量 vs 生成质量）
- [ ] 解释 Precision@K 和 Recall@K 的区别
- [ ] 理解 MRR 和 NDCG@K 的含义
- [ ] 理解 Faithfulness 和 Answer Relevance 的区别
- [ ] 能独立实现检索评测和生成评测的代码
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_generation_eval.py](00_generation_eval.py) | 生成质量评测（Faithfulness / Relevance） | ⭐⭐ |
| [01_retrieval_eval.py](01_retrieval_eval.py) | 检索质量评测（P@K / R@K / MRR / NDCG） | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
