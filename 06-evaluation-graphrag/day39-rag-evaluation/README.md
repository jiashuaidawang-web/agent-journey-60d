# Day 39: RAG Evaluation（RAG 评测）

> **今日目标**: 掌握 RAG 系统的评测方法
> **核心问题**: 如何评估 RAG 系统的效果？

---

## 🎯 今日目标

1. 理解 RAG 评测维度
2. 实现检索评测（Precision、Recall、MRR、NDCG）
3. 实现生成评测（Faithfulness、Answer Relevance）
4. 实现端到端评测

---

## 📚 必学知识

### 1. RAG 评测维度

| 维度 | 指标 | 说明 |
|------|------|------|
| 检索质量 | Precision@K | 检索结果中相关文档的比例 |
| 检索质量 | Recall@K | 相关文档被检索到的比例 |
| 检索质量 | MRR | 第一个相关文档的排名倒数 |
| 检索质量 | NDCG@K | 考虑排序的加权指标 |
| 生成质量 | Faithfulness | 回答是否基于上下文 |
| 生成质量 | Answer Relevance | 回答是否切题 |

### 2. 评测数据集

- 问题（Query）
- 标准答案（Ground Truth）
- 相关文档（Relevant Docs）

### 3. 评测流程

```
数据集 → RAG 系统 → 生成结果 → 评测指标 → 评分
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| RAGAS 文档 | https://docs.ragas.io/ |
| DeepEval | https://docs.confident-ai.io/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 检索评测指标
- [ ] 生成评测指标
- [ ] 评测数据集构建

---

## 💻 今日编码任务

### 文件结构

```
day39-rag-evaluation/
├── README.md
├── retrieval_eval.py        # 检索评测
├── generation_eval.py       # 生成评测
├── requirements.txt
└── boss-answer.md
```

### Task 1: retrieval_eval.py（60min）

实现检索评测：
- Precision@K、Recall@K
- MRR、NDCG@K

### Task 2: generation_eval.py（45min）

实现生成评测：
- Faithfulness
- Answer Relevance

---

## 🐉 今日 Boss

1. **RAG 评测的维度？**
2. **Precision@K 和 Recall@K 的区别？**
3. **如何评估生成质量？**

---

## 🎤 面试题

1. **如何评估 RAG 系统的效果？**
2. **检索评测和生成评测的区别？**
3. **MRR 和 NDCG 的区别？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| retrieval_eval.py | 50分 |
| generation_eval.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 40: Agent Evaluation**
