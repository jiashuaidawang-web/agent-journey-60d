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
├── task_success_eval.py    # 任务完成率
├── tool_call_eval.py       # 工具调用评测
├── requirements.txt
└── boss-answer.md
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
