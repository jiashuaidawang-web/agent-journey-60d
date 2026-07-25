# Day 16 Boss 答案

## 1. 向量数据库和普通数据库的区别？

| 维度 | 普通数据库（MySQL） | 向量数据库（Milvus） |
|------|---------------------|----------------------|
| 存储 | 结构化数据 | 向量 + 元数据 |
| 查询 | 精确匹配 | 相似度搜索 |
| 索引 | B+Tree、Hash | IVF、HNSW |
| 操作 | CRUD | Insert、Search |
| 适用 | 结构化查询 | 语义搜索 |

**核心区别**：
- 普通数据库：`SELECT * FROM users WHERE id = 1`（精确匹配）
- 向量数据库：`SELECT * ORDER BY distance(query, embedding) LIMIT 10`（相似度搜索）

## 2. HNSW 索引的原理是什么？

**HNSW（Hierarchical Navigable Small World）**：
- 基于图的索引
- 多层结构（类似跳表）
- 上层稀疏，下层稠密
- 搜索时从上层快速定位，再逐层细化

**优势**：
- 搜索速度快（对数级别）
- 召回率高
- 适合高维向量

**劣势**：
- 构建索引慢
- 内存占用大

## 3. 什么时候用 Milvus，什么时候用 FAISS？

| 场景 | 选择 |
|------|------|
| 单机、小数据量 | FAISS |
| 分布式、大数据量 | Milvus |
| 需要元数据过滤 | Milvus |
| 纯向量搜索 | FAISS |
| 生产环境 | Milvus |
| 研究/原型 | FAISS |

**类比**：
- FAISS ≈ SQLite（嵌入式，轻量）
- Milvus ≈ MySQL（服务端，功能全）
