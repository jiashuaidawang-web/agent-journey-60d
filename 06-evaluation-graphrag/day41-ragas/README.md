# Day 41: RAGAS（RAG 评测框架）

> **今日目标**: 掌握 RAGAS 框架的使用
> **核心问题**: RAGAS 提供哪些评测指标？

---

## 🎯 今日目标

1. 理解 RAGAS 框架
2. 实现 RAGAS 评测
3. 理解各指标含义
4. 集成到评测流水线

---

## 📚 必学知识

### 1. RAGAS 指标

| 指标 | 说明 | 维度 |
|------|------|------|
| Faithfulness | 回答是否基于上下文 | 生成质量 |
| Answer Relevancy | 回答是否切题 | 生成质量 |
| Context Recall | 上下文是否覆盖答案 | 检索质量 |
| Context Precision | 上下文是否相关 | 检索质量 |

### 2. 使用流程

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

result = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| RAGAS 文档 | https://docs.ragas.io/ |
| RAGAS 教程 | https://docs.ragas.io/en/latest/getstarted/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] RAGAS 指标
- [ ] RAGAS 评测流程

---

## 💻 今日编码任务

### 文件结构

```
day41-ragas/
├── README.md
├── ragas_demo.py            # RAGAS 演示
├── requirements.txt
└── boss-answer.md
```

### Task: ragas_demo.py（90min）

实现 RAGAS 评测

---

## 🐉 今日 Boss

1. **RAGAS 提供哪些指标？**
2. **Faithfulness 和 Answer Relevancy 的区别？**
3. **Context Recall 和 Context Precision 的区别？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| ragas_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 42: Evaluation Pipeline**
