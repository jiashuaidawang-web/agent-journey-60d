# Day 15: Embedding（嵌入模型）

> **今日目标**: 理解向量嵌入，掌握 BGE-M3 使用
> **核心问题**: 为什么 RAG 必须用 Embedding？

---

## 🎯 今日目标

1. 理解 Embedding 的本质：文本 → 向量
2. 理解相似度计算：Cosine Similarity
3. 掌握 BGE-M3 嵌入模型使用
4. 实现 Embedding Demo

---

## 📚 必学知识

### 1. 什么是 Embedding？

```
"苹果" → [0.12, 0.34, -0.56, ..., 0.78]  (1024维向量)
"香蕉" → [0.15, 0.31, -0.52, ..., 0.80]  (相似的水果，向量接近)
"汽车" → [-0.45, 0.22, 0.67, ..., -0.12] (不相关，向量远离)
```

**本质**：
- 将文本转换为高维向量
- 语义相似的文本，向量也相似
- 通过向量相似度衡量语义相似度

### 2. 为什么 RAG 必须用 Embedding？

- 传统检索：关键词匹配（BM25）→ 无法理解语义
- 向量检索：语义匹配 → "苹果" 能匹配 "水果"
- Embedding 是语义检索的基础

### 3. 常用嵌入模型

| 模型 | 维度 | 语言 | 特点 |
|------|------|------|------|
| BGE-M3 | 1024 | 多语言 | 当前最强开源 |
| text-embedding-3-large | 3072 | 多语言 | OpenAI 商用 |
| m3e-base | 768 | 中文 | 中文专用 |

### 4. 相似度计算

```python
# Cosine Similarity
similarity = dot(A, B) / (norm(A) * norm(B))
# 值域：[-1, 1]，越接近 1 越相似
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| BGE-M3 论文 | https://arxiv.org/abs/2402.03216 |
| Hugging Face Embeddings | https://huggingface.co/docs/hub/embeddings |
| Sentence Transformers | https://www.sbert.net/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Embedding 原理
- [ ] Cosine Similarity
- [ ] BGE-M3 使用
- [ ] 相似度计算

### 只需理解（L2）
- [ ] 不同嵌入模型的差异
- [ ] 嵌入维度的影响

---

## 💻 今日编码任务

### 文件结构

```
day15-embedding/
├── README.md
├── embedding_demo.py         # 嵌入演示
├── similarity_demo.py        # 相似度计算
├── requirements.txt
└── boss-answer.md
```

### Task 1: embedding_demo.py（45min）

实现嵌入演示：
- 加载 BGE-M3 模型
- 将文本转换为向量
- 展示向量维度

### Task 2: similarity_demo.py（45min）

实现相似度计算：
- 计算文本相似度
- 排序最相似的文本
- 理解语义相似 vs 字面相似

---

## 🐉 今日 Boss

1. **Embedding 的本质是什么？**
2. **为什么 RAG 不能只用关键词匹配？**
3. **Cosine Similarity 怎么计算？**

---

## 🎤 面试题

1. **RAG 系统中 Embedding 的作用是什么？**
2. **如何选择嵌入模型？**
3. **嵌入维度越高越好吗？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| embedding_demo.py | 40分 |
| similarity_demo.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 16: Vector DB**
