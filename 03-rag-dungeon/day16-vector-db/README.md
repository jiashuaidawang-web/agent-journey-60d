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
├── LEARNING_FLOW.md
├── 00_faiss_demo.py             # FAISS 演示
├── 01_milvus_demo.py            # Milvus 演示
├── requirements.txt
└── 99-boss-answer.md
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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释向量数据库的核心概念（Collection、Entity、Index）
- 解释 Milvus / FAISS 的用法
- 帮你调试代码报错
- 对比不同索引类型（FLAT、IVF、HNSW）的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解 B+Tree 索引，但 HNSW 图索引不太熟，请用跳表的类比解释一下 HNSW 的多层搜索原理，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的向量检索系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day16-vector-db/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_faiss_demo.py     # FAISS 演示
    ├── 01_milvus_demo.py    # Milvus 演示
    ├── 99-boss-answer.md   # Boss 答案
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 16 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Vector DB | ... | ... |
| HNSW | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day16-vector-db/
git commit -m "feat(day16): Vector DB - FAISS 与 Milvus 向量检索完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Milvus 文档或 FAISS 文档
- [ ] 写了 00_faiss_demo.py
- [ ] 写了 01_milvus_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
