# Day 20: Reranker（重排序）

> **今日目标**: 实现重排序，提升检索精度
> **核心问题**: 为什么检索后还需要重排序？

---

## 🎯 今日目标

1. 理解重排序的必要性
2. 掌握 bge-reranker 使用
3. 实现两阶段检索（召回 + 精排）
4. 理解 Cross-Encoder vs Bi-Encoder

---

## 📚 必学知识

### 1. 为什么需要重排序？

- 召回阶段：快速但粗糙（Top 20）
- 精排阶段：精确但慢（Top 5）
- 两阶段平衡效率和精度

### 2. 两阶段检索

```
查询
    ↓
[召回阶段] → Top 20（Bi-Encoder / 混合检索）
    ↓
[精排阶段] → Top 5（Reranker / Cross-Encoder）
    ↓
返回给 LLM
```

### 3. Cross-Encoder vs Bi-Encoder

| 维度 | Bi-Encoder | Cross-Encoder |
|------|------------|---------------|
| 原理 | 分别编码查询和文档 | 拼接查询+文档一起编码 |
| 速度 | 快 | 慢 |
| 精度 | 中等 | 高 |
| 阶段 | 召回 | 精排 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| bge-reranker | https://huggingface.co/BAAI/bge-reranker-v2-m3 |
| Reranker 论文 | https://arxiv.org/abs/2309.07568 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 两阶段检索
- [ ] Cross-Encoder 原理
- [ ] bge-reranker 使用

---

## 💻 今日编码任务

### 文件结构

```
day20-reranker/
├── README.md
├── reranker_demo.py         # Reranker 演示
├── two_stage_retrieval.py   # 两阶段检索
├── requirements.txt
└── boss-answer.md
```

### Task 1: reranker_demo.py（45min）

实现 Reranker 演示

### Task 2: two_stage_retrieval.py（60min）

实现两阶段检索（召回 + 精排）

---

## 🐉 今日 Boss

1. **为什么需要重排序？**
2. **Cross-Encoder 和 Bi-Encoder 的区别？**
3. **两阶段检索的优势？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| reranker_demo.py | 40分 |
| two_stage_retrieval.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 21: Query Rewrite / HyDE**
