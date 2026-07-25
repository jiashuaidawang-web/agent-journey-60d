# Day 40: Agent Evaluation（Agent 评测）

> **今日目标**: 掌握 Agent 系统的评测方法
> **核心问题**: 如何评估 Agent 的任务完成能力？

---

## 🎯 今日目标

1. 理解 Agent 评测维度
2. 实现任务完成率评测
3. 实现工具调用评测
4. 实现端到端 Agent 评测

---

## 📚 必学知识

### 1. Agent 评测维度

| 维度 | 指标 | 说明 |
|------|------|------|
| 任务完成 | Task Success Rate | 任务成功完成的比例 |
| 工具调用 | Tool Call Accuracy | 工具调用正确的比例 |
| 效率 | Steps to Completion | 完成任务所需步数 |
| 成本 | Token Usage | Token 消耗 |
| 安全 | Safety Score | 安全性评分 |

### 2. 评测数据集

- 任务描述（Task）
- 期望结果（Expected Result）
- 可用工具（Available Tools）

### 3. 评测流程

```
数据集 → Agent 执行 → 生成结果 → 对比期望 → 评分
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| AgentBench | https://github.com/THUDM/AgentBench |
| LangSmith Eval | https://docs.smith.langchain.com/evaluation |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 任务完成率评测
- [ ] 工具调用评测
- [ ] 端到端评测

---

## 💻 今日编码任务

### 文件结构

```
day40-agent-evaluation/
├── README.md
├── LEARNING_FLOW.md         # 学习流程
├── 00_task_success_eval.py  # 任务完成率
└── 99-boss-answer.md
```

### Task 1: task_success_eval.py（60min）

实现任务完成率评测

### Task 2: tool_call_eval.py（45min）

实现工具调用评测

---

## 🐉 今日 Boss

1. **Agent 评测的维度？**
2. **如何评估任务完成率？**
3. **如何评估工具调用？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| task_success_eval.py | 50分 |
| tool_call_eval.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 41: RAGAS**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Agent 评测维度（任务完成率、工具调用准确率）的核心概念
- 解释如何评估工具调用的正确性
- 帮你调试评测代码报错
- 对比不同 Agent 评测方法的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我了解分类任务的准确率，但 Agent 的 Task Success Rate 怎么定义'成功'？请用一个最小示例解释完全成功、部分成功、失败的区分。"

### 错误用法
> "帮我写一个完整的 Agent 评测系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
06-evaluation-graphrag/
└── day40-agent-evaluation/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_task_success_eval.py  # 任务完成率
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 40 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Task Success Rate | ... | ... |
| Tool Call Accuracy | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 06-evaluation-graphrag/day40-agent-evaluation/
git commit -m "feat(day40): Agent Evaluation - 任务完成率与工具调用评测完成"
```

---

## 📊 今日检查清单

- [ ] 读了 AgentBench 文档
- [ ] 读了 LangSmith Eval 文档
- [ ] 写了 00_task_success_eval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
