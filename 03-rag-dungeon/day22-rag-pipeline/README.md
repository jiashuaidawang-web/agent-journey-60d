# Day 22: RAG Pipeline（完整流水线）

> **今日目标**: 整合 Day 15-21，实现完整 RAG Pipeline
> **核心要求**: 包含：Query Rewrite → Hybrid Search → Reranker → LLM

---

## 🎯 今日目标

1. 整合所有 RAG 组件
2. 实现完整 RAG Pipeline
3. 实现 RAG 评测
4. 理解 RAG 全链路

---

## 📚 RAG 全链路架构

```
用户查询
    ↓
[Query Rewrite] → 优化查询
    ↓
[Embedding] → 向量化
    ↓
[Hybrid Search] → Dense + BM25 混合检索
    ↓
[Reranker] → 精排
    ↓
[Context Assembly] → 组装上下文
    ↓
[LLM] → 生成回答
    ↓
返回结果
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain RAG | https://python.langchain.com/docs/tutorials/rag/ |
| LlamaIndex RAG | https://docs.llamaindex.ai/en/stable/getting_started/starter_example/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 完整 RAG Pipeline
- [ ] 各组件集成
- [ ] RAG 评测

---

## 💻 今日编码任务

### 文件结构

```
day22-rag-pipeline/
├── README.md
├── LEARNING_FLOW.md
├── 00_rag_evaluation.py         # RAG 评测
├── 01_rag_pipeline.py           # 完整 RAG Pipeline
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: rag_pipeline.py（3-4h）

实现完整 RAG Pipeline：
- Query Rewrite
- Hybrid Search（Dense + BM25）
- Reranker
- Context Assembly
- LLM 生成

### Task 2: rag_evaluation.py（45min）

实现 RAG 评测：
- 召回率
- 准确率
- 端到端评测

---

## 🐉 今日 Boss

1. **描述 RAG 完整流程**
2. **如何评估 RAG 效果？**
3. **RAG 的常见问题和解决方案？**

---

## 🎤 面试题

1. **RAG 系统的核心组件有哪些？**
2. **如何提升 RAG 的召回率？**
3. **如何评估 RAG 的效果？**
4. **RAG 和微调的区别和选择？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| rag_pipeline.py | 60分 |
| rag_evaluation.py | 20分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，RAG Dungeon 毕业！进入下一章：MCP + A2A + Multi-Agent**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 RAG 完整流程的各阶段作用
- 解释 RAG 评测指标（Precision@K、Recall@K、MRR、NDCG）
- 帮你调试代码报错
- 对比不同 RAG 架构的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解 Spring Batch Pipeline，但 RAG 的上下文组装不太熟，请解释一下 Chunk 结果如何组装成 LLM 的输入，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 RAG Pipeline 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
03-rag-dungeon/
└── day22-rag-pipeline/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_rag_evaluation.py # RAG 评测
    ├── 01_rag_pipeline.py   # 完整 RAG Pipeline
    ├── 99-boss-answer.md   # Boss 答案
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 22 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| RAG Pipeline | ... | ... |
| RAG Evaluation | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 03-rag-dungeon/day22-rag-pipeline/
git commit -m "feat(day22): RAG Pipeline - 完整 RAG 流水线完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangChain RAG 或 LlamaIndex RAG 文档
- [ ] 写了 00_rag_evaluation.py
- [ ] 写了 01_rag_pipeline.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
