# Day 64: RAG 底层原理加深

> **今日目标**: 打通 RAG 底层原理：向量检索数学 + 索引算法 + 向量数据库
> **核心问题**: 为什么 HNSW 比暴力检索快 1000 倍？

---

## 🎯 今日目标

1. 理解向量检索数学原理（余弦相似度 / 内积 / L2 距离）
2. 掌握 HNSW 算法详解（层级图结构）
3. 掌握 IVF 倒排索引 + PQ 乘积量化
4. 向量数据库全对比（PGVector / Milvus / Qdrant / Weaviate / Chroma）
5. Milvus 企业级部署与运维
6. Document Loader 体系（Text / PDF / Markdown / Word / HTML / 代码文件）
7. 文档智能拆分策略（语义拆分 / 递归拆分 / 中文专属拆分）
8. 元数据与过滤器高级用法

---

## 📚 必学知识

### 1. 向量检索数学原理

**三种距离度量**：

| 度量 | 公式 | 取值范围 | 适用场景 |
|------|------|----------|----------|
| 余弦相似度 | cos(A,B) = A·B / (‖A‖·‖B‖) | [-1, 1] | 文本语义（最常用） |
| 内积（IP） | A·B = ΣAi·Bi | (-∞, +∞) | 推荐系统 |
| L2 距离（欧氏） | ‖A-B‖ = √Σ(Ai-Bi)² | [0, +∞) | 图像特征 |

**归一化后**：余弦相似度 = 内积，所以归一化向量用 IP 即可。

**为什么用余弦相似度**：
- 只关心方向，不关心长度
- 文本向量长度受文本长度影响，但语义由方向决定
- 值越大越相似（1 = 完全相同）

### 2. HNSW 算法详解

**HNSW（Hierarchical Navigable Small World）** 是近似最近邻检索的主流算法：

**核心思想**：
- 构建多层图结构（类似跳表）
- 高层图节点少，用于快速定位
- 底层图节点多，用于精确搜索

**层级结构**：
```
Layer 2:    A ——————————— D          （稀疏，快速定位）
            |           |
Layer 1:    A ——— B ——— D ——— E      （中等密度）
            |   |   |   |   |
Layer 0:    A — B — C — D — E — F    （密集，精确搜索）
```

**搜索过程**：
1. 从最高层开始，找到最近节点
2. 下降到下一层，继续搜索
3. 直到 Layer 0，返回 Top-K

**关键参数**：
- `M`：每个节点的最大连接数（默认 16）
- `efConstruction`：构建时的搜索宽度（默认 200）
- `efSearch`：搜索时的搜索宽度（默认 50）

**复杂度**：O(log N)，比暴力检索 O(N) 快 1000 倍。

### 3. IVF 倒排索引 + PQ 乘积量化

**IVF（Inverted File Index）**：
- 先对向量空间聚类（K-Means）
- 每个聚类有一个中心点（Centroid）
- 搜索时只查询最近的 nprobe 个聚类

**PQ（Product Quantization）**：
- 将向量分段，每段用聚类中心表示
- 大幅降低存储和计算量
- 例如 768 维向量分 8 段，每段 96 维，每段 256 个中心
- 存储从 768×4=3072 字节降到 8×1=8 字节

**IVF-PQ 组合**：
- IVF 减少搜索范围
- PQ 加速距离计算
- 是 Milvus / Faiss 的核心算法

### 4. 向量数据库全对比

| 数据库 | 类型 | 索引 | 过滤 | 部署 | 适用场景 |
|--------|------|------|------|------|----------|
| PGVector | PG 插件 | HNSW / IVF | SQL | PG 一体 | 中小规模 |
| Milvus | 专用 | HNSW / IVF-PQ / DiskANN | 表达式 | 分布式 | 大规模企业 |
| Qdrant | 专用 | HNSW | 过滤 | 单机 / 分布式 | Rust 高性能 |
| Weaviate | 专用 | HNSW | GraphQL | 分布式 | 多模态 |
| Chroma | 专用 | HNSW | 简单 | 单机 | 原型开发 |
| Faiss | 库 | 多种 | 无 | 嵌入应用 | 算法研究 |

**选型建议**：
- 原型开发：Chroma / Faiss
- 中小企业：PGVector / Qdrant
- 大规模企业：Milvus
- 多模态：Weaviate

### 5. Milvus 企业级部署

**架构**：
```
Client → Proxy → Coordinators → Workers → Storage
```

**组件**：
- **Proxy**：接入层，负载均衡
- **Coordinator**：元数据管理
- **Worker**：数据处理（DataNode / QueryNode / IndexNode）
- **Storage**：MinIO / S3

**部署模式**：
- **Standalone**：单节点，开发测试
- **Cluster**：分布式，生产环境
- **Cloud**：Zilliz Cloud（托管）

**运维要点**：
- 索引构建：离线批量构建
- 数据备份：定期快照
- 监控：Prometheus + Grafana
- 扩缩容：QueryNode 水平扩展

### 6. Document Loader 体系

| 文档类型 | Loader | 关键能力 |
|----------|--------|----------|
| Text | TextLoader | 编码处理 |
| PDF | PyPDFLoader / PDFPlumberLoader | 表格、版面 |
| Markdown | MarkdownLoader | 标题、代码块 |
| Word | DocxLoader | 段落、表格 |
| HTML | BeautifulSoupLoader | 标签过滤 |
| 代码 | LanguageLoader | 函数、类 |

### 7. 文档智能拆分策略

| 策略 | 原理 | 适用场景 |
|------|------|----------|
| 递归拆分 | 按分隔符递归切分 | 通用 |
| 语义拆分 | 基于 Embedding 相似度 | 长文档 |
| 中文专属 | 按句号/段落/标点 | 中文文档 |
| 固定长度 | 固定 chunk_size | 简单场景 |

**关键参数**：
- `chunk_size`：每块大小（500-1000 token）
- `chunk_overlap`：重叠大小（50-200 token）
- `separators`：分隔符（\n\n / \n / 。 / .）

### 8. 元数据与过滤器高级用法

**元数据**：
- 来源（source）
- 时间（date）
- 作者（author）
- 章节（section）
- 标签（tags）

**过滤器**：
- 精确匹配：`source == "财报.pdf"`
- 范围过滤：`date >= "2026-01-01"`
- 包含过滤：`tags in ["重要", "公告"]`
- 组合过滤：`AND / OR / NOT`

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| HNSW 论文 | https://arxiv.org/abs/1603.09320 |
| Milvus 文档 | https://milvus.io/docs |
| Qdrant 文档 | https://qdrant.tech/documentation/ |
| PGVector | https://github.com/pgvector/pgvector |
| Faiss | https://github.com/facebookresearch/faiss |
| LangChain Document Loaders | https://python.langchain.com/docs/modules/data_connection/document_loaders/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 三种距离度量（余弦 / 内积 / L2）
- [ ] HNSW 算法原理和搜索过程
- [ ] IVF + PQ 组合原理
- [ ] 向量数据库选型
- [ ] Document Loader 体系
- [ ] 文档拆分策略
- [ ] 元数据与过滤器

### 只需理解（L3）
- [ ] K-Means 聚类原理
- [ ] 乘积量化的数学推导
- [ ] DiskANN 算法
- [ ] BM25 算法

### 今天不深入（后面会讲）
- [ ] GPU 索引（FAISS-GPU）
- [ ] 混合检索（Dense + Sparse）
- [ ] 向量数据库内核实现

---

## 💻 今日编码任务

### 文件结构

```
day64-rag-internals/
├── README.md
├── LEARNING_FLOW.md
├── 00_hnsw_visualization.py      # HNSW 可视化
├── 01_ivf_pq_demo.py             # IVF-PQ 演示
├── 02_vector_db_comparison.py    # 向量数据库对比
├── 03_milvus_cluster.py          # Milvus 集群部署
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_hnsw_visualization.py（50min）

实现 HNSW 可视化：
- 生成随机向量
- 构建 HNSW 图
- 可视化层级结构
- 展示搜索过程

**验收标准**：
```bash
python 00_hnsw_visualization.py
# 输出：
# 📊 HNSW 图构建完成
# Layer 2: 5 nodes
# Layer 1: 20 nodes
# Layer 0: 100 nodes
# 搜索路径：Layer 2 → Layer 1 → Layer 0
```

### Task 2: 01_ivf_pq_demo.py（50min）

实现 IVF-PQ 演示：
- 生成随机向量
- IVF 聚类
- PQ 量化
- 对比暴力检索

**验收标准**：
```bash
python 01_ivf_pq_demo.py
# 输出：
# 暴力检索：10ms（精确）
# IVF-PQ：0.5ms（近似，召回率 95%）
```

### Task 3: 02_vector_db_comparison.py（60min）

实现向量数据库对比：
- 对比 PGVector / Milvus / Qdrant / Chroma
- 测试插入 / 查询 / 过滤性能
- 输出对比报告

**验收标准**：
```bash
python 02_vector_db_comparison.py
# 输出：
# 数据库 | 插入/s | 查询/s | 过滤
# PGVector | 1000 | 500 | ✅
# Milvus | 5000 | 3000 | ✅
# Qdrant | 3000 | 2000 | ✅
# Chroma | 500 | 300 | ⚠️
```

### Task 4: 03_milvus_cluster.py（50min）

实现 Milvus 集群部署：
- Docker Compose 部署
- 创建 Collection
- 插入 / 查询 / 删除

**验收标准**：
```bash
python 03_milvus_cluster.py
# 输出：
# ✅ Milvus 集群启动
# ✅ Collection 创建
# ✅ 插入 10000 条向量
# ✅ 查询耗时 5ms
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 HNSW 算法原理
- 解释 IVF + PQ 组合
- 帮你调试向量数据库代码
- 解释向量数据库选型

### 今天 AI 不能帮你
- 替你理解索引算法（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "HNSW 的层级图结构我不太理解。请用 Java 的 ConcurrentHashMap  Segment 分层锁类比解释一下。"

### 错误用法
> "帮我写一个完整的向量检索系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day64-rag-internals/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_hnsw_visualization.py
    ├── 01_ivf_pq_demo.py
    ├── 02_vector_db_comparison.py
    ├── 03_milvus_cluster.py
    ├── requirements.txt
    └── 99-boss-answer.md
```

### README.md 必须包含
```markdown
# Day 64 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| HNSW | ... | ... |
| IVF-PQ | ... | ... |
| 向量数据库 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day64-rag-internals/
git commit -m "feat(day64): RAG Internals - 向量检索底层原理打通"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **余弦相似度、内积、L2 距离三种度量有什么区别？各自适用场景？**
2. **HNSW 算法的核心思想是什么？搜索过程是怎样的？**
3. **IVF + PQ 组合是如何加速检索的？**
4. **向量数据库如何选型？各自适用场景是什么？**
5. **文档拆分有哪些策略？中文文档拆分有什么特殊之处？**

### 验收标准
- 每个答案 **不少于 80 字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **HNSW 和暴力检索的复杂度分别是多少？**
2. **IVF-PQ 的召回率如何提升？**
3. **Milvus 的架构是怎样的？**
4. **Document Loader 如何处理 PDF 表格？**
5. **元数据过滤的实现原理是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_hnsw_visualization.py | 20分 | 能可视化 HNSW 层级 |
| 01_ivf_pq_demo.py | 20分 | 能演示 IVF-PQ |
| 02_vector_db_comparison.py | 20分 | 能对比 4 种数据库 |
| 03_milvus_cluster.py | 15分 | 能部署 Milvus |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5 题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4 个代码文件全部能运行
- [ ] Boss 5 题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 65: Agent 架构综合复习**

---

## 📊 今日检查清单

- [ ] 读了 HNSW 论文
- [ ] 读了 Milvus 文档
- [ ] 读了 Qdrant 文档
- [ ] 写了 00_hnsw_visualization.py
- [ ] 写了 01_ivf_pq_demo.py
- [ ] 写了 02_vector_db_comparison.py
- [ ] 写了 03_milvus_cluster.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
