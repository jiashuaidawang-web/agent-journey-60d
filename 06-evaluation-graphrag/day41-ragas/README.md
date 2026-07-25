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
├── LEARNING_FLOW.md         # 学习流程
├── 00_ragas_demo.py         # RAGAS 演示
└── 99-boss-answer.md
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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 RAGAS 四大指标（Faithfulness / Answer Relevancy / Context Recall / Context Precision）
- 解释 RAGAS 评测流程
- 帮你调试评测代码报错
- 对比 RAGAS 和其他评测框架的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解了 Faithfulness 是'回答基于上下文'，但 Context Recall 和 Context Precision 在 RAGAS 里具体怎么算？请用一个最小示例解释。"

### 错误用法
> "帮我写一个完整的 RAGAS 评测系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
06-evaluation-graphrag/
└── day41-ragas/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_ragas_demo.py    # RAGAS 演示
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 41 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Faithfulness | ... | ... |
| Context Recall | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 06-evaluation-graphrag/day41-ragas/
git commit -m "feat(day41): RAGAS - 四大评测指标完成"
```

---

## 📊 今日检查清单

- [ ] 读了 RAGAS 文档
- [ ] 读了 RAGAS 教程
- [ ] 写了 00_ragas_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
