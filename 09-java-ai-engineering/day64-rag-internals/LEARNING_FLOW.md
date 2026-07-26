# Day 64: RAG 底层原理加深 - 学习流程

> **今日目标**: 打通 RAG 底层原理：向量检索数学 + 索引算法 + 向量数据库
> **核心问题**: 为什么 HNSW 比暴力检索快 1000 倍？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_hnsw_visualization.py（50分钟）
    ↓ 理解：HNSW 层级图结构 + 搜索过程
Step 4: 运行 01_ivf_pq_demo.py（50分钟）
    ↓ 理解：IVF 聚类 + PQ 量化
Step 5: 运行 02_vector_db_comparison.py（60分钟）
    ↓ 理解：向量数据库选型对比
Step 6: 运行 03_milvus_cluster.py（50分钟）
    ↓ 理解：Milvus 企业级部署
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4 个代码文件 | 210min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 4.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释三种距离度量的区别
- [ ] 解释 HNSW 算法原理和搜索过程
- [ ] 解释 IVF + PQ 组合原理
- [ ] 能根据场景选择合适的向量数据库
- [ ] 能部署 Milvus 集群
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_hnsw_visualization.py](00_hnsw_visualization.py) | HNSW 可视化 | ⭐⭐⭐ |
| [01_ivf_pq_demo.py](01_ivf_pq_demo.py) | IVF-PQ 演示 | ⭐⭐⭐ |
| [02_vector_db_comparison.py](02_vector_db_comparison.py) | 向量数据库对比 | ⭐⭐⭐ |
| [03_milvus_cluster.py](03_milvus_cluster.py) | Milvus 集群部署 | ⭐⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
