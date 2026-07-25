# Day 17: Chunking（文档分块）

> **今日目标**: 掌握文档分块策略
> **核心问题**: 为什么文档不能直接塞进向量库？

---

## 🎯 今日目标

1. 理解分块的必要性
2. 掌握 4 种分块策略
3. 实现分块对比实验
4. 理解 Chunk Size 的影响

---

## 📚 必学知识

### 1. 为什么要分块？

- Context Window 有限（如 4096 tokens）
- 长文档无法直接嵌入
- 小块更容易精确匹配
- 减少 Token 消耗

### 2. 分块策略

| 策略 | 说明 | 适用 |
|------|------|------|
| Fixed Size | 固定大小切分 | 通用 |
| Recursive | 按段落递归切长 | 结构化文档 |
| Semantic | 按语义切分 | 高质量需求 |
| Document | 按文档结构切分 | 有标题层级 |

### 3. 关键参数

- **Chunk Size**：每个块的大小（如 512 tokens）
- **Chunk Overlap**：块之间的重叠（如 50 tokens）
- 重叠可以防止信息在边界被切断

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain Text Splitters | https://python.langchain.com/docs/concepts/text_splitters/ |
| LlamaIndex Chunking | https://docs.llamaindex.ai/en/stable/optimizing/building_rag_best_practices/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 4 种分块策略
- [ ] Chunk Size 选择
- [ ] Overlap 的作用

---

## 💻 今日编码任务

### 文件结构

```
day17-chunking/
├── README.md
├── chunking_demo.py          # 分块演示
├── chunk_experiment.py       # 分块对比实验
├── requirements.txt
└── boss-answer.md
```

### Task 1: chunking_demo.py（45min）

实现 4 种分块策略：
- Fixed Size
- Recursive
- Semantic
- Document

### Task 2: chunk_experiment.py（45min）

对比不同 Chunk Size 的效果

---

## 🐉 今日 Boss

1. **为什么文档要分块？**
2. **Chunk Size 如何影响检索效果？**
3. **Overlap 的作用是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| chunking_demo.py | 45分 |
| chunk_experiment.py | 35分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 18: Dense Retrieval**
