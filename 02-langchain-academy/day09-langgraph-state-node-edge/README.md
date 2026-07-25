# Day 9: LangGraph State + Node + Edge

> **今日目标**: 理解 LangGraph 的三个核心概念
> **核心问题**: State 为什么是一等公民？

---

## 🎯 今日目标

1. 理解 State：图的状态，所有节点共享
2. 理解 Node：执行单元，接收 State 返回更新
3. 理解 Edge：连接节点，决定执行顺序
4. 实现第一个 LangGraph

---

## 📚 必学知识

### 1. State（状态）

```python
from typing import TypedDict

class AgentState(TypedDict):
    messages: list      # 消息历史
    next_step: str      # 下一步
    result: str         # 最终结果
```

- State 是**所有节点共享**的数据
- 每个节点可以**读取** State，**返回**要更新的字段
- LangGraph 自动**合并**更新（Reducer）

### 2. Node（节点）

```python
def call_model(state: AgentState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}  # 返回要更新的字段
```

- Node 是一个**函数**
- 接收 State 作为参数
- 返回要**更新**的字段（不是整个 State）

### 3. Edge（边）

```python
graph.add_edge("agent", "tools")      # 普通边：固定连接
graph.add_conditional_edges("agent", route, {...})  # 条件边
```

- Edge 决定**节点之间的执行顺序**
- 普通边：固定连接
- 条件边：根据 State 动态决定

### 4. 完整流程

```python
# 1. 定义 State
class State(TypedDict):
    messages: list

# 2. 创建 Graph
graph = StateGraph(State)

# 3. 添加 Node
graph.add_node("agent", call_model)
graph.add_node("tools", tool_node)

# 4. 添加 Edge
graph.add_edge("tools", "agent")
graph.add_conditional_edges("agent", should_continue, {...})

# 5. 编译
app = graph.compile()

# 6. 运行
app.invoke({"messages": [("user", "你好")]})
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph StateGraph | https://langchain-ai.github.io/langgraph/concepts/low_level/#stategraph |
| LangGraph Nodes | https://langchain-ai.github.io/langgraph/concepts/low_level/#nodes |
| LangGraph Edges | https://langchain-ai.github.io/langgraph/concepts/low_level/#edges |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] State 定义和 Reducer
- [ ] Node 编写
- [ ] Edge（普通边 + 条件边）
- [ ] StateGraph 编译和运行

---

## 💻 今日编码任务

### 文件结构

```
day09-langgraph-state-node-edge/
├── README.md
├── simple_graph.py          # 最简单的 Graph
├── agent_graph.py           # Agent + Tool Graph
├── requirements.txt
└── boss-answer.md
```

### Task 1: simple_graph.py（30min）

实现最简单的 LangGraph：
- 一个节点 + 一个结束
- 理解 State 流转

### Task 2: agent_graph.py（60min）

实现 Agent Graph：
- agent 节点：调用 LLM
- tools 节点：执行工具
- 条件边：根据是否有 tool_calls 决定走向

---

## 🐉 今日 Boss

1. **State 为什么是一等公民？**
2. **Node 和 Edge 的职责分别是什么？**
3. **条件边和普通边有什么区别？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| simple_graph.py | 30分 |
| agent_graph.py | 50分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 10: Conditional Routing**
