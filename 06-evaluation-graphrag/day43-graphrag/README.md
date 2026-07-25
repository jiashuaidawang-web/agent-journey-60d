# Day 43: GraphRAG（图检索增强生成）

> **今日目标**: 理解 GraphRAG 原理和实现
> **核心问题**: 为什么需要 GraphRAG？

---

## 🎯 今日目标

1. 理解 GraphRAG 原理
2. 实现知识图谱构建
3. 实现图检索
4. 理解 GraphRAG vs RAG

---

## 📚 必学知识

### 1. 为什么需要 GraphRAG？

**传统 RAG 的局限**：
- 基于块检索，无法捕捉全局关系
- 难以回答需要多跳推理的问题
- 例如："贵州茅台的竞争对手的总部在哪里？"（需要两跳）

**GraphRAG 的优势**：
- 实体关系建模
- 多跳推理能力
- 全局视角

### 2. GraphRAG 流程

```
文档 → 实体抽取 → 关系抽取 → 知识图谱 → 图检索 → LLM 生成
```

### 3. 核心概念

| 概念 | 说明 |
|------|------|
| Entity | 实体（节点） |
| Relationship | 关系（边） |
| Community | 社区（聚类） |
| Knowledge Graph | 知识图谱 |

### 4. GraphRAG vs RAG

| 维度 | RAG | GraphRAG |
|------|-----|----------|
| 检索方式 | 向量相似度 | 图遍历 |
| 推理能力 | 单跳 | 多跳 |
| 全局视角 | 弱 | 强 |
| 适用 | 简单问答 | 复杂推理 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| GraphRAG 论文 | https://arxiv.org/abs/2404.16130 |
| Neo4j GraphRAG | https://neo4j.com/docs/neo4j-graphrag/ |
| LangChain GraphRAG | https://python.langchain.com/docs/use_cases/graph/ |

---

## 🧠 学习深度

### 必须掌握（L2-L3）
- [ ] GraphRAG 原理
- [ ] 知识图谱构建
- [ ] 图检索

---

## 💻 今日编码任务

### 文件结构

```
day43-graphrag/
├── README.md
├── knowledge_graph.py       # 知识图谱构建
├── graph_retrieval.py       # 图检索
├── requirements.txt
└── boss-answer.md
```

### Task 1: knowledge_graph.py（60min）

实现知识图谱构建

### Task 2: graph_retrieval.py（60min）

实现图检索

---

## 🐉 今日 Boss

1. **为什么需要 GraphRAG？**
2. **GraphRAG 的流程？**
3. **GraphRAG 和 RAG 的区别？**

---

## 🎤 面试题

1. **GraphRAG 的原理是什么？**
2. **如何构建知识图谱？**
3. **GraphRAG 的适用场景？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| knowledge_graph.py | 50分 |
| graph_retrieval.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 44: GraphRAG Hybrid**
