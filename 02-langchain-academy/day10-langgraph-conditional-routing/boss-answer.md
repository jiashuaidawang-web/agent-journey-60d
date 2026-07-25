# Day 10 Boss 答案

## 1. 条件路由函数返回什么？

**条件路由函数返回下一个节点的名称（字符串）**。

```python
def route(state: State) -> str:
    if condition_a:
        return "node_a"      # 返回节点名称
    elif condition_b:
        return "node_b"
    else:
        return "end"
```

**关键点**：
- 返回值必须是**字符串**
- 返回值必须和路由映射中的 key 对应
- 路由映射把返回值映射到实际的节点名称

## 2. 路由映射的作用是什么？

**路由映射把路由函数的返回值映射到节点名称**。

```python
graph.add_conditional_edges("router", route_function, {
    "weather": "weather_agent",    # 返回 "weather" → 去 weather_agent
    "stock": "stock_agent",        # 返回 "stock" → 去 stock_agent
    "fallback": "fallback_node",   # 返回 "fallback" → 去 fallback_node
})
```

**为什么需要映射？**
- 路由函数的返回值可以是任意字符串
- 映射提供了**灵活性**（返回值可以和节点名称不同）
- 提供了**解耦**（路由逻辑和节点命名分离）

## 3. 如何实现循环？

**循环通过条件边实现**：

```python
# agent 执行完，根据条件决定下一步
graph.add_conditional_edges("agent", should_continue, {
    "tools": "tools",    # 需要调用工具 → 去 tools
    END: END,            # 不需要 → 结束
})

# tools 执行完，回到 agent
graph.add_edge("tools", "agent")  # 形成循环
```

**循环结构**：
```
agent → tools → agent → tools → ... → agent → END
```

**必须有终止条件**：
- 条件边中必须有一个分支指向 END
- 否则会无限循环
- LangGraph 默认有递归限制（recursion_limit）
