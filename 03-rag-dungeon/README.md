# 03-rag-dungeon · Day 15-22 执行版 v3.0

> **定位**: RAG 全栈 —— 第一项目 Enterprise Agent Platform 的核心
> **目标**: 从 Embedding 到完整 RAG Pipeline 全链路打通

---

## 8天总览

```
Day 15  Embedding（嵌入模型）
Day 16  Vector DB（向量数据库）
Day 17  Chunking（文档分块）
Day 18  Dense Retrieval（稠密检索）
Day 19  BM25 + Hybrid（混合检索）
Day 20  Reranker（重排序）
Day 21  Query Rewrite / HyDE（查询重写）
Day 22  RAG Pipeline（完整流水线）
```

## RAG 全链路架构

```
用户问题
    ↓
[Query Rewrite] → 优化查询
    ↓
[Embedding] → 向量化
    ↓
[Vector Search] + [BM25] → 混合检索
    ↓
[Reranker] → 精排
    ↓
[Context Assembly] → 组装上下文
    ↓
[LLM] → 生成回答
    ↓
返回结果
```

## 核心技术栈

| 技术 | 用途 | 深度 |
|------|------|------|
| BGE-M3 | 嵌入模型 | L3 |
| Milvus / FAISS | 向量数据库 | L3 |
| BM25 | 稀疏检索 | L3 |
| bge-reranker | 重排序 | L3 |
| HyDE | 查询重写 | L2-L3 |
| RAGAS | RAG 评测 | L2 |

## Java 类比

| RAG 概念 | Java 类比 |
|----------|-----------|
| Embedding | 序列化（Object → byte[]） |
| Vector DB | 带索引的数据库 |
| Retrieval | SQL Query |
| Reranker | 二次排序 |
| RAG Pipeline | Spring Batch Pipeline |

---

**准备好了吗？从 Day 15 开始 RAG 全链路闯关。**
