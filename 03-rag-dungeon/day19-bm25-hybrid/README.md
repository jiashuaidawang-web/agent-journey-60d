# Day 19: BM25 + Hybrid（混合检索）

> **今日目标**: 实现混合检索，兼顾语义和关键词
> **核心问题**: 为什么单一检索不够？

---

## 🎯 今日目标

1. 理解 BM25 原理
2. 实现 BM25 检索
3. 实现混合检索（Dense + Sparse）
4. 理解 RRF 融合策略

---

## 📚 必学知识

### 1. BM25（Best Matching 25）

- 基于词频的检索算法
- 经典的信息检索方法
- 考虑：词频（TF）、逆文档频率（IDF）、文档长度

### 2. 混合检索

```
查询
    ↓
[Dense Retrieval] → Top-K1
    ↓
[Sparse Retrieval (BM25)] → Top-K2
    ↓
[Fusion (RRF)] → 融合排序
    ↓
Top-K 最终结果
```

### 3. RRF（Reciprocal Rank Fusion）

```python
score(doc) = Σ 1 / (k + rank_i(doc))
# k 是平滑参数（通常 60）
# rank_i 是文档在第 i 个列表中的排名
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| BM25 原理 | https://en.wikipedia.org/wiki/Okapi_BM25 |
| Elastic BM25 | https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html |
| RRF | https://plg.uwaterloo.ca/~gvcormac/cormacksigir2009-rrf.pdf |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] BM25 原理
- [ ] 混合检索流程
- [ ] RRF 融合

---

## 💻 今日编码任务

### 文件结构

```
day19-bm25-hybrid/
├── README.md
├── bm25_demo.py             # BM25 演示
├── hybrid_retrieval.py      # 混合检索
├── requirements.txt
└── boss-answer.md
```

### Task 1: bm25_demo.py（45min）

实现 BM25 检索

### Task 2: hybrid_retrieval.py（60min）

实现混合检索 + RRF 融合

---

## 🐉 今日 Boss

1. **BM25 的原理是什么？**
2. **为什么需要混合检索？**
3. **RRF 融合怎么计算？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| bm25_demo.py | 35分 |
| hybrid_retrieval.py | 45分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 20: Reranker**
