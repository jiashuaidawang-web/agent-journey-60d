# Day 22: RAG Pipeline（完整流水线）

> **今日目标**: 整合 Day 15-21，实现完整 RAG Pipeline
> **核心要求**: 包含：Query Rewrite → Hybrid Search → Reranker → LLM

---

## 🎯 今日目标

1. 整合所有 RAG 组件
2. 实现完整 RAG Pipeline
3. 实现 RAG 评测
4. 理解 RAG 全链路

---

## 📚 RAG 全链路架构

```
用户查询
    ↓
[Query Rewrite] → 优化查询
    ↓
[Embedding] → 向量化
    ↓
[Hybrid Search] → Dense + BM25 混合检索
    ↓
[Reranker] → 精排
    ↓
[Context Assembly] → 组装上下文
    ↓
[LLM] → 生成回答
    ↓
返回结果
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain RAG | https://python.langchain.com/docs/tutorials/rag/ |
| LlamaIndex RAG | https://docs.llamaindex.ai/en/stable/getting_started/starter_example/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 完整 RAG Pipeline
- [ ] 各组件集成
- [ ] RAG 评测

---

## 💻 今日编码任务

### 文件结构

```
day22-rag-pipeline/
├── README.md
├── rag_pipeline.py           # 完整 RAG Pipeline
├── rag_evaluation.py         # RAG 评测
├── requirements.txt
└── boss-answer.md
```

### Task 1: rag_pipeline.py（3-4h）

实现完整 RAG Pipeline：
- Query Rewrite
- Hybrid Search（Dense + BM25）
- Reranker
- Context Assembly
- LLM 生成

### Task 2: rag_evaluation.py（45min）

实现 RAG 评测：
- 召回率
- 准确率
- 端到端评测

---

## 🐉 今日 Boss

1. **描述 RAG 完整流程**
2. **如何评估 RAG 效果？**
3. **RAG 的常见问题和解决方案？**

---

## 🎤 面试题

1. **RAG 系统的核心组件有哪些？**
2. **如何提升 RAG 的召回率？**
3. **如何评估 RAG 的效果？**
4. **RAG 和微调的区别和选择？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| rag_pipeline.py | 60分 |
| rag_evaluation.py | 20分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，RAG Dungeon 毕业！进入下一章：MCP + A2A + Multi-Agent**
