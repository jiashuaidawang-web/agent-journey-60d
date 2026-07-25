# Day 32: Observability（可观测性）

> **今日目标**: 实现 Agent 系统的可观测性
> **核心问题**: 如何监控 Agent 的运行状态？

---

## 🎯 今日目标

1. 理解 Agent 可观测性的重要性
2. 实现 Trace（追踪）
3. 实现 Token / Cost / Latency 统计
4. 集成 LangSmith / Phoenix

---

## 📚 必学知识

### 1. 为什么 Agent 需要可观测性？

- Agent 是多步骤流程，需要追踪每一步
- Token 消耗需要统计和优化
- 问题排查需要完整链路
- 成本需要核算

### 2. Agent 可观测性指标

| 指标 | 说明 |
|------|------|
| Trace | 完整执行链路 |
| Token | Token 消耗 |
| Latency | 延迟 |
| Cost | 成本 |
| Tool Call | 工具调用次数和结果 |
| Agent Step | Agent 步骤 |

### 3. LangSmith

- LangChain 官方可观测性平台
- 自动追踪 LangChain / LangGraph 调用
- 支持 Trace、Token、Latency 统计

### 4. Phoenix (Arize)

- 开源 LLM 可观测性平台
- 支持 Trace、Span、Token
- 支持 Prompt 分析

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangSmith | https://docs.smith.langchain.com/ |
| Phoenix | https://docs.arize.com/phoenix |
| OpenTelemetry | https://opentelemetry.io/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Agent 可观测性指标
- [ ] Trace 实现
- [ ] Token/Cost/Latency 统计

---

## 💻 今日编码任务

### 文件结构

```
day32-observability/
├── README.md
├── trace_demo.py            # Trace 实现
├── metrics_demo.py          # 指标统计
├── requirements.txt
└── boss-answer.md
```

### Task 1: trace_demo.py（60min）

实现 Trace：
- 记录 Agent 执行链路
- 记录每个步骤的输入输出

### Task 2: metrics_demo.py（45min）

实现指标统计：
- Token 消耗
- 延迟
- 成本

---

## 🐉 今日 Boss

1. **Agent 可观测性需要哪些指标？**
2. **Trace 的作用是什么？**
3. **如何统计 Token 消耗？**

---

## 🎤 面试题

1. **如何监控 Agent 系统的运行状态？**
2. **Agent 的 Token 消耗如何优化？**
3. **如何排查 Agent 的问题？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| trace_demo.py | 50分 |
| metrics_demo.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 33: Security**
