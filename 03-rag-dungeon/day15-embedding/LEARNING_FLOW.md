# Day 15: Embedding（嵌入模型）- 学习流程

> **今日目标**: 理解向量嵌入，掌握 BGE-M3 使用
> **核心问题**: 为什么 RAG 必须用 Embedding？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_embedding_demo.py（45分钟）
    ↓ 理解：文本如何转换为向量，BGE-M3 的使用方式
Step 4: 运行 01_similarity_demo.py（45分钟）
    ↓ 理解：Cosine Similarity 计算，语义相似 vs 字面相似
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 90min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 2.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Embedding 的本质：文本 → 向量
- [ ] 理解为什么 RAG 必须用 Embedding 而不是纯关键词匹配
- [ ] 掌握 Cosine Similarity 的计算方法和几何意义
- [ ] 能独立使用 BGE-M3 模型生成嵌入向量
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_embedding_demo.py](00_embedding_demo.py) | 理解文本如何转换为向量 | ⭐ |
| [01_similarity_demo.py](01_similarity_demo.py) | 掌握相似度计算与排序 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
