# Day 42: Evaluation Pipeline（评测流水线）

> **今日目标**: 实现完整的评测流水线
> **核心问题**: 如何自动化 RAG 评测？

---

## 🎯 今日目标

1. 实现评测流水线
2. 实现自动化评测
3. 实现评测报告生成
4. 理解 CI/CD 集成

---

## 📚 必学知识

### 1. 评测流水线流程

```
数据集加载 → RAG 执行 → 指标计算 → 报告生成 → 结果存储
```

### 2. 自动化评测

- 定期运行
- 对比历史结果
- 告警退化

### 3. CI/CD 集成

- 每次代码变更后自动评测
- 评测不通过则阻止上线
- 持续监控

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangSmith Eval | https://docs.smith.langchain.com/evaluation |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 评测流水线
- [ ] 自动化评测

---

## 💻 今日编码任务

### 文件结构

```
day42-evaluation-pipeline/
├── README.md
├── LEARNING_FLOW.md         # 学习流程
├── 00_eval_pipeline.py      # 评测流水线
└── 99-boss-answer.md
```

### Task: eval_pipeline.py（90min）

实现评测流水线

---

## 🐉 今日 Boss

1. **评测流水线的流程？**
2. **如何自动化评测？**
3. **如何发现 RAG 退化？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| eval_pipeline.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 43: GraphRAG**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释评测流水线的完整流程
- 解释如何发现 RAG 退化
- 帮你调试评测代码报错
- 对比不同自动化评测方案的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解了评测流水线的流程，但如何在 CI/CD 里集成自动评测并设置退化告警？请用一个最小示例解释。"

### 错误用法
> "帮我写一个完整的自动化评测流水线。"

---

## 📝 GitHub 提交规范

### 提交结构
```
06-evaluation-graphrag/
└── day42-evaluation-pipeline/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_eval_pipeline.py # 评测流水线
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 42 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 评测流水线 | ... | ... |
| RAG 退化 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 06-evaluation-graphrag/day42-evaluation-pipeline/
git commit -m "feat(day42): Evaluation Pipeline - 自动化评测流水线完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangSmith Eval 文档
- [ ] 写了 00_eval_pipeline.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
