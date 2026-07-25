# Day 45: Eval-GraphRAG Integration - 学习流程

> **今日目标**: 整合评测和 GraphRAG，完成本阶段综合项目
> **核心要求**: 包含：GraphRAG 构建 → 混合检索 → 评测 → 报告

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_graphrag_pipeline.py（20分钟）
    ↓ 理解：完整 GraphRAG Pipeline（知识图谱 → 检索 → 生成 → 评测）
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 20min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 描述 GraphRAG 的完整流程（实体抽取 → 关系抽取 → 图谱构建 → 混合索引 → 检索 → 生成 → 评测）
- [ ] 解释如何评测 GraphRAG（检索质量 / 生成质量 / 端到端）
- [ ] 理解 GraphRAG 的适用场景（多跳推理 / 关系查询 / 全局视角）
- [ ] 能独立实现完整的 GraphRAG Pipeline 代码
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_graphrag_pipeline.py](00_graphrag_pipeline.py) | 完整 GraphRAG Pipeline（构建 → 检索 → 评测） | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
