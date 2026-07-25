# Day 6: Agent Patterns (ReAct / Router / Plan-Execute)

> **今日目标**: 掌握三种核心 Agent 模式
> **核心问题**: 不同场景该用哪种 Agent 模式？

---

## 🎯 今日目标

1. 理解 ReAct 模式：推理 + 行动交替
2. 理解 Router 模式：根据意图分发到不同 Agent
3. 理解 Plan-and-Execute 模式：先规划再执行
4. 实现 ReAct Agent 和 Router Agent

---

## 📚 必学知识

### 1. ReAct 模式（Reason + Act）

```
Thought: 我需要先查天气，再决定穿什么
Action: get_weather("北京")
Observation: 北京今天晴，25°C
Thought: 天气不错，可以穿短袖
Final Answer: 今天北京天气晴朗，建议穿短袖
```

**特点**：
- 推理和行动交替进行
- 每步都有 Thought → Action → Observation
- 适合：需要多步推理的任务

### 2. Router 模式

```
用户输入: "帮我分析贵州茅台"
    ↓
Router: 识别意图 → stock_analysis
    ↓
分发到: StockAnalysisAgent
    ↓
StockAnalysisAgent 处理
    ↓
返回结果
```

**特点**：
- 先分类，再分发
- 每个子 Agent 专注一类任务
- 适合：多领域、多任务场景

### 3. Plan-and-Execute 模式

```
用户输入: "帮我写一份行业研究报告"
    ↓
Planner: 制定计划
  1. 搜索行业数据
  2. 分析竞争格局
  3. 分析财务数据
  4. 撰写报告
    ↓
Executor: 逐步执行
  Step 1: 搜索行业数据 → 结果
  Step 2: 分析竞争格局 → 结果
  ...
    ↓
返回最终报告
```

**特点**：
- 先规划，后执行
- 计划可以动态调整
- 适合：复杂、多步骤任务

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| ReAct Paper | https://arxiv.org/abs/2210.03629 |
| LangChain Agent Types | https://python.langchain.com/docs/concepts/agents/ |
| LangGraph Multi-Agent | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] ReAct 模式实现
- [ ] Router 模式实现
- [ ] 三种模式的适用场景

### 只需理解（L2）
- [ ] Plan-and-Execute 实现
- [ ] Reflection / Self-Reflection

---

## 💻 今日编码任务

### 文件结构

```
day06-agent-patterns/
├── README.md
├── react_agent.py            # ReAct Agent
├── router_agent.py           # Router Agent
├── requirements.txt
└── boss-answer.md
```

### Task 1: react_agent.py（60min）

实现 ReAct Agent：
- Thought → Action → Observation 循环
- 支持多步推理
- 支持工具调用

### Task 2: router_agent.py（60min）

实现 Router Agent：
- 意图识别
- 分发到不同子 Agent
- 支持 WeatherAgent / StockAgent / CalculatorAgent

---

## 🐉 今日 Boss

1. **ReAct 和 Router 的适用场景有什么不同？**
2. **什么场景下用 Plan-and-Execute？**
3. **Router 模式如果路由错误怎么办？**

---

## 🎤 面试题

1. **Agent 有哪些常见模式？**
2. **ReAct 模式为什么有效？**
3. **如何设计一个多 Agent 路由系统？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| react_agent.py | 35分 |
| router_agent.py | 35分 |
| README 学习总结 | 15分 |
| Boss 答案 | 15分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] README 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 7: Mini Agent Runtime**
