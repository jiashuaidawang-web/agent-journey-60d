# Day 17: Chunking（文档分块）- 学习流程

> **今日目标**: 掌握文档分块策略
> **核心问题**: 为什么文档不能直接塞进向量库？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_chunking_demo.py（45分钟）
    ↓ 理解：4 种分块策略的实现与对比
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 45min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释为什么文档必须分块（Context Window、嵌入模型限制、检索精度、成本）
- [ ] 掌握 4 种分块策略（Fixed Size、Recursive、Semantic、Document）
- [ ] 理解 Chunk Size 对检索效果的影响
- [ ] 理解 Overlap 的作用和推荐值
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_chunking_demo.py](00_chunking_demo.py) | 掌握 4 种分块策略 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
