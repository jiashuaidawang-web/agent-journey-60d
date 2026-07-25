# Day 44: GraphRAG Hybrid（混合索引）

> **今日目标**: 实现 GraphRAG + 向量检索的混合索引
> **核心问题**: 如何结合图检索和向量检索的优势？

---

## 🎯 今日目标

1. 理解混合索引的优势
2. 实现 Graph + Vector 混合检索
3. 实现混合排序
4. 理解适用场景

---

## 📚 必学知识

### 1. 为什么需要混合索引？

| 检索方式 | 优势 | 局限 |
|----------|------|------|
| 向量检索 | 语义匹配 | 无法多跳推理 |
| 图检索 | 多跳推理 | 语义理解弱 |

**混合索引**：结合两者优势

### 2. 混合检索流程

```
查询
    ↓
[向量检索] → Top-K1 文档
    ↓
[图检索] → Top-K2 实体/关系
    ↓
[融合] → 混合排序
    ↓
Top-K 最终结果
```

### 3. 融合策略

| 策略 | 说明 |
|------|------|
| RRF | Reciprocal Rank Fusion |
| Weighted | 加权融合 |
| Sequential | 先图后向量 / 先向量后图 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Neo4j Hybrid | https://neo4j.com/docs/cypher-manual/current/indexes/ |

---

## 🧠 学习深度

### 必须掌握（L2-L3）
- [ ] 混合索引原理
- [ ] 混合检索流程

---

## 💻 今日编码任务

### 文件结构

```
day44-graphrag-hybrid/
├── README.md
├── hybrid_retrieval.py      # 混合检索
├── requirements.txt
└── boss-answer.md
```

### Task: hybrid_retrieval.py（90min）

实现混合检索

---

## 🐉 今日 Boss

1. **混合索引的优势？**
2. **混合检索的流程？**
3. **融合策略有哪些？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| hybrid_retrieval.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 45: Eval-GraphRAG Integration**
