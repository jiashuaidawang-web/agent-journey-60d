# Day 45: Eval-GraphRAG Integration（评测+GraphRAG 整合）

> **今日目标**: 整合评测和 GraphRAG，完成本阶段综合项目
> **核心要求**: 包含：GraphRAG 构建 → 混合检索 → 评测 → 报告

---

## 🎯 今日目标

1. 整合 GraphRAG 和评测
2. 实现完整的 GraphRAG Pipeline
3. 实现自动化评测
4. 完成本阶段综合项目

---

## 📚 综合项目架构

```
文档输入
    ↓
[实体抽取] → 实体列表
    ↓
[关系抽取] → 关系列表
    ↓
[知识图谱构建] → 图谱
    ↓
[混合索引] → 向量索引 + 图索引
    ↓
[查询处理]
    ├── [向量检索]
    └── [图检索]
    ↓
[融合排序]
    ↓
[LLM 生成]
    ↓
[评测] → 报告
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| GraphRAG Eval | https://docs.ragas.io/en/latest/howtos/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] GraphRAG Pipeline
- [ ] 自动化评测

---

## 💻 今日编码任务

### 文件结构

```
day45-eval-graphrag-integration/
├── README.md
├── LEARNING_FLOW.md         # 学习流程
├── 00_graphrag_pipeline.py  # GraphRAG Pipeline
└── 99-boss-answer.md
```

### Task: graphrag_pipeline.py（3-4h）

实现完整 GraphRAG Pipeline：
- 知识图谱构建
- 混合检索
- LLM 生成
- 自动评测

---

## 🐉 今日 Boss

1. **描述 GraphRAG 完整流程**
2. **如何评测 GraphRAG？**
3. **GraphRAG 的适用场景？**

---

## 🎤 面试题

1. **GraphRAG 和 RAG 的区别？**
2. **如何构建知识图谱？**
3. **如何评测 GraphRAG 效果？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| graphrag_pipeline.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，Evaluation + GraphRAG 毕业！进入下一章：LLM Engineering**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 GraphRAG 完整流程（实体抽取 → 关系抽取 → 图谱构建 → 混合索引 → 检索 → 生成 → 评测）
- 解释如何评测 GraphRAG
- 帮你调试 GraphRAG Pipeline 代码报错
- 对比 GraphRAG 和 RAG 的适用场景

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解了 GraphRAG 的完整流程，但如何评测 GraphRAG 的检索质量（实体召回率、关系召回率）？请用一个最小示例解释。"

### 错误用法
> "帮我写一个完整的 GraphRAG Pipeline 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
06-evaluation-graphrag/
└── day45-eval-graphrag-integration/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_graphrag_pipeline.py  # GraphRAG Pipeline
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 45 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| GraphRAG Pipeline | ... | ... |
| GraphRAG 评测 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 06-evaluation-graphrag/day45-eval-graphrag-integration/
git commit -m "feat(day45): Eval-GraphRAG Integration - 综合项目完成"
```

---

## 📊 今日检查清单

- [ ] 读了 GraphRAG Eval 文档
- [ ] 写了 00_graphrag_pipeline.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
