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
├── graphrag_pipeline.py    # GraphRAG Pipeline
├── requirements.txt
└── boss-answer.md
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
