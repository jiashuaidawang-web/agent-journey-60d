# Day 16: Vector DB（向量数据库）

> **今日目标**: 掌握向量数据库的使用
> **核心问题**: 向量数据库和普通数据库有什么区别？

---

## 🎯 今日目标

1. 理解向量数据库的原理
2. 掌握 Milvus 使用
3. 理解索引类型（IVF、HNSW）
4. 实现向量插入和搜索

---

## 📚 必学知识

### 1. 什么是向量数据库？

- 存储向量 + 元数据
- 支持向量相似度搜索
- 常见：Milvus、FAISS、Pinecone、Weaviate

### 2. Milvus 核心概念

| 概念 | 说明 |
|------|------|
| Collection | 类似表 |
| Entity | 类似行 |
| Field | 类似列 |
| Index | 向量索引 |

### 3. 索引类型

| 索引 | 特点 | 适用 |
|------|------|------|
| FLAT | 精确搜索，慢 | 小数据量 |
| IVF_FLAT | 聚类加速 | 中数据量 |
| HNSW | 图索引，快 | 大数据量 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Milvus 文档 | https://milvus.io/docs |
| FAISS 文档 | https://github.com/facebookresearch/faiss |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Milvus 基本操作
- [ ] 向量插入和搜索
- [ ] 索引类型选择

---

## 💻 今日编码任务

### 文件结构

```
day16-vector-db/
├── README.md
├── milvus_demo.py            # Milvus 演示
├── faiss_demo.py             # FAISS 演示
├── requirements.txt
└── boss-answer.md
```

### Task 1: milvus_demo.py（60min）

实现 Milvus 演示：
- 创建 Collection
- 插入向量
- 向量搜索

### Task 2: faiss_demo.py（45min）

实现 FAISS 演示：
- 创建索引
- 添加向量
- 搜索

---

## 🐉 今日 Boss

1. **向量数据库和普通数据库的区别？**
2. **HNSW 索引的原理是什么？**
3. **什么时候用 Milvus，什么时候用 FAISS？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| milvus_demo.py | 45分 |
| faiss_demo.py | 35分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 17: Chunking**
