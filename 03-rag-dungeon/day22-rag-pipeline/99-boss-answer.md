# Day 22 Boss 答案

## 1. 描述 RAG 完整流程

**RAG 完整流程**：

```
1. 用户查询
       ↓
2. 查询重写（Query Rewrite / HyDE）
       ↓
3. 文档嵌入（离线已完成）
       ↓
4. 混合检索（Dense + BM25）
       ↓
5. 重排序（Reranker）
       ↓
6. 上下文组装
       ↓
7. LLM 生成
       ↓
8. 返回结果
```

**各阶段作用**：

| 阶段 | 作用 | 关键技术 |
|------|------|----------|
| 查询重写 | 优化查询 | HyDE、Query Expansion |
| 混合检索 | 召回相关文档 | Dense + BM25 |
| 重排序 | 精排 Top-K | Cross-Encoder |
| 上下文组装 | 构建 LLM 输入 | Token 控制 |
| LLM 生成 | 最终回答 | Prompt Engineering |

## 2. 如何评估 RAG 效果？

**评测维度**：

| 维度 | 指标 | 说明 |
|------|------|------|
| 检索质量 | Precision@K | 检索结果中相关文档的比例 |
| 检索质量 | Recall@K | 相关文档被检索到的比例 |
| 检索质量 | MRR | 第一个相关文档的排名倒数 |
| 检索质量 | NDCG@K | 考虑排序的加权指标 |
| 生成质量 | Faithfulness | 回答是否基于上下文 |
| 生成质量 | Answer Relevance | 回答是否切题 |
| 端到端 | RAGAS | 综合评测框架 |

## 3. RAG 的常见问题和解决方案？

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 召回率低 | 查询和文档不匹配 | 查询重写、HyDE |
| 噪声多 | 检索结果不相关 | Reranker、调整 Top-K |
| 上下文不足 | Chunk Size 太小 | 增大 Chunk Size |
| 信息切断 | 边界切分 | 增加 Overlap |
| 幻觉 | LLM 编造 | 增加 Faithfulness 约束 |
| 成本过高 | Token 消耗大 | 优化 Prompt、减少上下文 |
