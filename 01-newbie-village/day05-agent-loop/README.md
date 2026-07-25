# Day 5: Tool Registry / Agent Loop

> **今日目标**: 实现 Agent Loop —— Agent 的心脏
> **核心问题**: Agent Loop 为什么可能死循环？如何防止？

---

## 🎯 今日目标

1. 实现 ToolRegistry：工具的注册、查找、执行
2. 实现 AgentExecutor：while 循环 + 工具调用 + 终止条件
3. 理解 Max Iterations 为什么是必须的
4. 实现状态管理和 Token 统计

---

## 📚 必学知识

### 1. Agent Loop 核心流程

```
用户输入
    ↓
┌─────────────────────────────────┐
│  while not finished:            │
│      response = llm(messages)   │
│      if response.has_tool_call: │
│          result = execute(tool) │
│          messages.append(result) │
│      else:                      │
│          return response        │
│                                 │
│      if max_iterations reached: │
│          break                  │
└─────────────────────────────────┘
    ↓
返回结果
```

### 2. 为什么需要 Max Iterations？

- LLM 可能反复调用同一个工具（死循环）
- 每次调用都消耗 Token（成本）
- 必须设置上限（通常 5-10 次）

### 3. ToolRegistry 职责

- `register(tool)`：注册工具
- `get(name)`：查找工具
- `list()`：列出所有工具
- `execute(name, args)`：执行工具

### 4. Agent State

- 当前 messages 历史
- 已执行的工具调用
- Token 消耗统计
- 迭代次数
- 是否完成

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain Agent Loop | https://python.langchain.com/docs/concepts/agents/ |
| ReAct Paper | https://arxiv.org/abs/2210.03629 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Agent Loop 完整流程
- [ ] Max Iterations 必要性
- [ ] ToolRegistry 实现
- [ ] 状态管理

### 只需理解（L2）
- [ ] ReAct 模式
- [ ] Plan-and-Execute 模式

---

## 💻 今日编码任务

### 文件结构

```
day05-agent-loop/
├── README.md
├── registry.py             # ToolRegistry
├── state.py                # AgentState
├── agent_executor.py       # AgentExecutor
├── requirements.txt
└── boss-answer.md
```

### Task 1: registry.py（30min）

实现 ToolRegistry：
- register / get / list / execute
- 支持工具查找和执行

### Task 2: state.py（20min）

实现 AgentState：
- messages 历史
- token 统计
- 迭代次数
- 完成状态

### Task 3: agent_executor.py（60min）

实现 AgentExecutor：
- while 循环
- 工具调用
- max_iterations 限制
- 错误处理
- Token 统计

---

## 🐉 今日 Boss

1. **Agent Loop 为什么可能死循环？**
2. **如何检测并终止无效循环？**
3. **Tool 执行失败时 Agent 应该怎么处理？**
4. **Max Iterations 设多少合适？**

---

## 🎤 面试题

1. **Agent Loop 的核心是什么？**
2. **如何防止 Agent 无限循环？**
3. **Agent 的状态应该包含哪些信息？**
4. **Token 消耗如何统计和优化？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| registry.py | 20分 |
| state.py | 15分 |
| agent_executor.py | 40分 |
| README 学习总结 | 10分 |
| Boss 答案 | 15分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 4题完成
- [ ] README 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 6: Agent Patterns**
