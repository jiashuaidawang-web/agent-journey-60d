# Day 44: GraphRAG Hybrid（混合索引）

> **今日目标**: 实现 GraphRAG + 向量检索的混合索引
> **核心问题**: 如何结合图检索和向量检索的优势？

---

## 🎯 今日目标

1. 理解混合索引的优势
2. 实现 Graph + Vector 混合检索
3. 实现混合排序
4. 理解适用场景

---

## 📚 必学知识

### 1. 为什么需要混合索引？

| 检索方式 | 优势 | 局限 |
|----------|------|------|
| 向量检索 | 语义匹配 | 无法多跳推理 |
| 图检索 | 多跳推理 | 语义理解弱 |

**混合索引**：结合两者优势

### 2. 混合检索流程

```
查询
    ↓
[向量检索] → Top-K1 文档
    ↓
[图检索] → Top-K2 实体/关系
    ↓
[融合] → 混合排序
    ↓
Top-K 最终结果
```

### 3. 融合策略

| 策略 | 说明 |
|------|------|
| RRF | Reciprocal Rank Fusion |
| Weighted | 加权融合 |
| Sequential | 先图后向量 / 先向量后图 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Neo4j Hybrid | https://neo4j.com/docs/cypher-manual/current/indexes/ |

---

## 🧠 学习深度

### 必须掌握（L2-L3）
- [ ] 混合索引原理
- [ ] 混合检索流程

---

## 💻 今日编码任务

### 文件结构

```
day44-graphrag-hybrid/
├── README.md
├── LEARNING_FLOW.md         # 学习流程
├── 00_hybrid_retrieval.py   # 混合检索
└── 99-boss-answer.md
```

### Task: hybrid_retrieval.py（90min）

实现混合检索

---

## 🐉 今日 Boss

1. **混合索引的优势？**
2. **混合检索的流程？**
3. **融合策略有哪些？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| hybrid_retrieval.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 45: Eval-GraphRAG Integration**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释混合索引的优势和融合策略（RRF / Weighted / Sequential）
- 解释向量检索和图检索的互补性
- 帮你调试混合检索代码报错
- 对比不同融合策略的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解向量检索和图检索各自的优势，但 RRF（Reciprocal Rank Fusion）具体怎么算？请用一个最小示例解释。"

### 错误用法
> "帮我写一个完整的混合检索系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
06-evaluation-graphrag/
└── day44-graphrag-hybrid/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_hybrid_retrieval.py  # 混合检索
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 44 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 混合索引 | ... | ... |
| RRF 融合 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 06-evaluation-graphrag/day44-graphrag-hybrid/
git commit -m "feat(day44): GraphRAG Hybrid - 混合检索完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Neo4j Hybrid 文档
- [ ] 写了 00_hybrid_retrieval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
