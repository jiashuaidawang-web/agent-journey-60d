# Day 45 Boss 答案

## 1. 描述 GraphRAG 完整流程

```
1. 文档输入
   ↓
2. 实体抽取（Entity Extraction）
   - 从文本中抽取实体（人物、公司、地点等）
   ↓
3. 关系抽取（Relationship Extraction）
   - 抽取实体间的关系
   ↓
4. 知识图谱构建
   - 实体作为节点，关系作为边
   ↓
5. 混合索引
   - 向量索引（语义检索）
   - 图索引（关系检索）
   ↓
6. 查询处理
   - 向量检索 + 图检索
   ↓
7. 融合排序
   - RRF 融合
   ↓
8. LLM 生成
   ↓
9. 评测
   - Faithfulness、Answer Relevancy
   - Context Recall、Context Precision
```

## 2. 如何评测 GraphRAG？

**评测维度**：

| 维度 | 指标 |
|------|------|
| 检索质量 | 实体召回率、关系召回率 |
| 生成质量 | Faithfulness、Answer Relevancy |
| 端到端 | 任务完成率 |

## 3. GraphRAG 的适用场景？

- **多跳推理**：需要多步推理的问题
- **关系查询**：查询实体间的关系
- **全局视角**：需要全局理解的问题
- **知识密集型**：需要领域知识的问题

**不适用**：
- 简单问答（传统 RAG 即可）
- 实时性要求高的场景
