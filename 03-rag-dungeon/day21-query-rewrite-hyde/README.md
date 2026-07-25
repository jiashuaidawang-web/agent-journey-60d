# Day 21: Query Rewrite / HyDE（查询重写）

> **今日目标**: 掌握查询重写技术
> **核心问题**: 用户查询为什么需要重写？

---

## 🎯 今日目标

1. 理解查询重写的必要性
2. 掌握 HyDE（Hypothetical Document Embeddings）
3. 实现 Query Rewrite
4. 实现 HyDE

---

## 📚 必学知识

### 1. 为什么需要查询重写？

- 用户查询可能模糊、简短、不完整
- 查询和文档的表达方式可能不同
- 重写可以提升召回率

### 2. HyDE（Hypothetical Document Embeddings）

```
用户查询："白酒龙头股"
    ↓
[LLM 生成假设文档] → "贵州茅台是白酒行业龙头，市占率超过50%..."
    ↓
[嵌入假设文档] → 向量
    ↓
[向量搜索] → 匹配真实文档
```

**核心思想**：
- 用 LLM 生成一个"假设的"相关文档
- 用这个假设文档的向量去搜索
- 比直接用查询向量更准确

### 3. Query Rewrite 方法

| 方法 | 说明 |
|------|------|
| HyDE | 生成假设文档 |
| Query Expansion | 扩展查询词 |
| Multi-hop | 多跳查询分解 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| HyDE 论文 | https://arxiv.org/abs/2212.10496 |
| Query Rewrite | https://python.langchain.com/docs/tutorials/rag/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] HyDE 原理和实现
- [ ] Query Rewrite 实现

### 只需理解（L2）
- [ ] Multi-hop 查询分解

---

## 💻 今日编码任务

### 文件结构

```
day21-query-rewrite-hyde/
├── README.md
├── LEARNING_FLOW.md
├── 00_hyde_demo.py              # HyDE 演示
└── 99-boss-answer.md
```

### Task 1: query_rewrite.py（45min）

实现 Query Rewrite

### Task 2: hyde_demo.py（60min）

实现 HyDE

---

## 🐉 今日 Boss

1. **为什么需要查询重写？**
2. **HyDE 的原理是什么？**
3. **HyDE 比普通检索好在哪？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| query_rewrite.py | 40分 |
| hyde_demo.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 22: RAG Pipeline**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释查询重写的必要性
- 解释 HyDE 的原理和实现
- 帮你调试代码报错
- 对比不同查询重写方法的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解查询优化，但 HyDE 的假设文档生成不太熟，请解释一下为什么文档-文档相似度比查询-文档相似度更准确，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的查询重写系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day21-query-rewrite-hyde/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_hyde_demo.py      # HyDE 演示
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 21 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Query Rewrite | ... | ... |
| HyDE | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day21-query-rewrite-hyde/
git commit -m "feat(day21): Query Rewrite / HyDE - 查询重写技术完成"
```

---

## 📊 今日检查清单

- [ ] 读了 HyDE 论文或相关资料
- [ ] 写了 00_hyde_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
