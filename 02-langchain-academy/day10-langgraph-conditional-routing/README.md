# Day 10: LangGraph Conditional Routing

> **今日目标**: 掌握条件路由，实现复杂分支逻辑
> **核心问题**: 如何根据 State 动态决定执行路径？

---

## 🎯 今日目标

1. 理解条件边的路由函数
2. 实现多分支路由
3. 实现循环控制
4. 实现 Router Graph

---

## 📚 必学知识

### 1. 条件路由函数

```python
def route(state: State) -> str:
    """根据 State 返回下一个节点的名称。"""
    if state["intent"] == "weather":
        return "weather_agent"
    elif state["intent"] == "stock":
        return "stock_agent"
    else:
        return "fallback"
```

### 2. 路由映射

```python
graph.add_conditional_edges("router", route, {
    "weather_agent": "weather_agent",
    "stock_agent": "stock_agent",
    "fallback": "fallback",
})
```

---

## 💻 今日编码任务

### 文件结构

```
day10-langgraph-conditional-routing/
├── README.md
├── router_graph.py          # Router Graph
├── multi_branch_graph.py    # 多分支 Graph
├── requirements.txt
└── boss-answer.md
```

### Task 1: router_graph.py（60min）

实现 Router Graph：
- 根据用户意图路由到不同 Agent
- 支持 weather / stock / calculator

### Task 2: multi_branch_graph.py（45min）

实现多分支 Graph：
- 根据条件走不同路径
- 支持循环

---

## 🐉 今日 Boss

1. **条件路由函数返回什么？**
2. **路由映射的作用是什么？**
3. **如何实现循环？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| router_graph.py | 50分 |
| multi_branch_graph.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 11: Persistence + Checkpoint**
