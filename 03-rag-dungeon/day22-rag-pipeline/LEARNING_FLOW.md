# Day 22: RAG Pipeline（完整流水线）- 学习流程

> **今日目标**: 整合 Day 15-21，实现完整 RAG Pipeline
> **核心要求**: 包含：Query Rewrite → Hybrid Search → Reranker → LLM

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_rag_evaluation.py（45分钟）
    ↓ 理解：RAG 评测指标（Precision@K、Recall@K、MRR、NDCG）
Step 4: 运行 01_rag_pipeline.py（3-4小时）
    ↓ 理解：完整 RAG 全链路集成
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 285min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 5.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 描述 RAG 完整流程（8 个阶段）
- [ ] 理解如何评估 RAG 效果（检索质量 + 生成质量）
- [ ] 掌握 RAG 常见问题和解决方案
- [ ] 能独立实现完整 RAG Pipeline
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_rag_evaluation.py](00_rag_evaluation.py) | 实现 RAG 评测指标 | ⭐⭐ |
| [01_rag_pipeline.py](01_rag_pipeline.py) | 实现完整 RAG 全链路 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
