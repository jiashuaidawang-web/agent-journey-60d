# Day 18: Dense Retrieval（稠密检索）

> **今日目标**: 实现基于 Embedding 的语义检索
> **核心问题**: 稠密检索和稀疏检索有什么区别？

---

## 🎯 今日目标

1. 理解稠密检索原理
2. 实现 Query → Embedding → Vector Search
3. 理解召回率和精确率
4. 实现 Dense Retrieval Pipeline

---

## 📚 必学知识

### 1. 稠密检索流程

```
用户查询
    ↓
[Embedding Model] → 查询向量
    ↓
[Vector DB] → 相似度搜索
    ↓
Top-K 结果
```

### 2. 稠密 vs 稀疏检索

| 维度 | 稠密检索 | 稀疏检索（BM25） |
|------|----------|------------------|
| 原理 | 向量相似度 | 词频统计 |
| 理解语义 | ✅ | ❌ |
| 关键词精确 | ❌ | ✅ |
| 速度 | 快 | 很快 |
| 适用 | 语义查询 | 关键词查询 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Dense Retrieval | https://arxiv.org/abs/2112.10753 |
| Sentence Transformers | https://www.sbert.net/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 稠密检索流程
- [ ] Embedding + Vector Search
- [ ] Top-K 召回

---

## 💻 今日编码任务

### 文件结构

```
day18-dense-retrieval/
├── README.md
├── dense_retrieval.py        # 稠密检索实现
├── requirements.txt
└── boss-answer.md
```

### Task: dense_retrieval.py（60min）

实现稠密检索：
- 文档嵌入
- 查询嵌入
- 相似度搜索
- Top-K 召回

---

## 🐉 今日 Boss

1. **稠密检索的流程是什么？**
2. **为什么需要 Embedding？**
3. **Top-K 的 K 如何选择？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| dense_retrieval.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 19: BM25 + Hybrid**
