# Day 19: BM25 + Hybrid（混合检索）

> **今日目标**: 实现混合检索，兼顾语义和关键词
> **核心问题**: 为什么单一检索不够？

---

## 🎯 今日目标

1. 理解 BM25 原理
2. 实现 BM25 检索
3. 实现混合检索（Dense + Sparse）
4. 理解 RRF 融合策略

---

## 📚 必学知识

### 1. BM25（Best Matching 25）

- 基于词频的检索算法
- 经典的信息检索方法
- 考虑：词频（TF）、逆文档频率（IDF）、文档长度

### 2. 混合检索

```
查询
    ↓
[Dense Retrieval] → Top-K1
    ↓
[Sparse Retrieval (BM25)] → Top-K2
    ↓
[Fusion (RRF)] → 融合排序
    ↓
Top-K 最终结果
```

### 3. RRF（Reciprocal Rank Fusion）

```python
score(doc) = Σ 1 / (k + rank_i(doc))
# k 是平滑参数（通常 60）
# rank_i 是文档在第 i 个列表中的排名
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| BM25 原理 | https://en.wikipedia.org/wiki/Okapi_BM25 |
| Elastic BM25 | https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-similarity.html |
| RRF | https://plg.uwaterloo.ca/~gvcormac/cormacksigir2009-rrf.pdf |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] BM25 原理
- [ ] 混合检索流程
- [ ] RRF 融合

---

## 💻 今日编码任务

### 文件结构

```
day19-bm25-hybrid/
├── README.md
├── LEARNING_FLOW.md
├── 00_hybrid_retrieval.py       # 混合检索
└── 99-boss-answer.md
```

### Task 1: bm25_demo.py（45min）

实现 BM25 检索

### Task 2: hybrid_retrieval.py（60min）

实现混合检索 + RRF 融合

---

## 🐉 今日 Boss

1. **BM25 的原理是什么？**
2. **为什么需要混合检索？**
3. **RRF 融合怎么计算？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| bm25_demo.py | 35分 |
| hybrid_retrieval.py | 45分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 20: Reranker**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 BM25 的原理（TF、IDF、文档长度）
- 解释 RRF 融合的计算方法
- 帮你调试代码报错
- 对比不同融合策略的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解数据库的全文检索，但 BM25 的公式不太熟，请解释一下 TF 和 IDF 是怎么影响最终分数的，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的混合检索系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day19-bm25-hybrid/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_hybrid_retrieval.py # 混合检索
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 19 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| BM25 | ... | ... |
| RRF | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day19-bm25-hybrid/
git commit -m "feat(day19): BM25 + Hybrid - 混合检索与 RRF 融合完成"
```

---

## 📊 今日检查清单

- [ ] 读了 BM25 原理相关资料
- [ ] 读了 RRF 融合相关资料
- [ ] 写了 00_hybrid_retrieval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
