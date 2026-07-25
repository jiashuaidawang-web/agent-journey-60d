# Day 18: Dense Retrieval（稠密检索）

> **今日目标**: 实现基于 Embedding 的语义检索
> **核心问题**: 稠密检索和稀疏检索有什么区别？

---

## 🎯 今日目标

1. 理解稠密检索原理
2. 实现 Query → Embedding → Vector Search
3. 理解召回率和精确率
4. 实现 Dense Retrieval Pipeline

---

## 📚 必学知识

### 1. 稠密检索流程

```
用户查询
    ↓
[Embedding Model] → 查询向量
    ↓
[Vector DB] → 相似度搜索
    ↓
Top-K 结果
```

### 2. 稠密 vs 稀疏检索

| 维度 | 稠密检索 | 稀疏检索（BM25） |
|------|----------|------------------|
| 原理 | 向量相似度 | 词频统计 |
| 理解语义 | ✅ | ❌ |
| 关键词精确 | ❌ | ✅ |
| 速度 | 快 | 很快 |
| 适用 | 语义查询 | 关键词查询 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Dense Retrieval | https://arxiv.org/abs/2112.10753 |
| Sentence Transformers | https://www.sbert.net/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 稠密检索流程
- [ ] Embedding + Vector Search
- [ ] Top-K 召回

---

## 💻 今日编码任务

### 文件结构

```
day18-dense-retrieval/
├── README.md
├── LEARNING_FLOW.md
├── 00_dense_retrieval.py        # 稠密检索实现
├── requirements.txt
└── 99-boss-answer.md
```

### Task: dense_retrieval.py（60min）

实现稠密检索：
- 文档嵌入
- 查询嵌入
- 相似度搜索
- Top-K 召回

---

## 🐉 今日 Boss

1. **稠密检索的流程是什么？**
2. **为什么需要 Embedding？**
3. **Top-K 的 K 如何选择？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| dense_retrieval.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 19: BM25 + Hybrid**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释稠密检索的核心流程
- 解释 Embedding + Vector Search 的实现
- 帮你调试代码报错
- 对比稠密检索和稀疏检索的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解数据库索引，但向量相似度搜索不太熟，请解释一下 Query → Embedding → Vector Search 的完整流程，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的语义检索系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day18-dense-retrieval/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_dense_retrieval.py # 稠密检索实现
    ├── 99-boss-answer.md   # Boss 答案
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 18 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Dense Retrieval | ... | ... |
| Top-K | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day18-dense-retrieval/
git commit -m "feat(day18): Dense Retrieval - 稠密检索流程完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Dense Retrieval 相关资料
- [ ] 写了 00_dense_retrieval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
