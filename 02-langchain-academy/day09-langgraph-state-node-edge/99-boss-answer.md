# Day 9 Boss 答案

## 1. State 为什么是一等公民？

**State 是 LangGraph 的核心设计**：

1. **所有节点共享**：每个节点都能读取 State，返回更新
2. **自动合并**：节点返回的字段会自动合并到 State（通过 Reducer）
3. **类型安全**：State 用 TypedDict 定义，有类型检查
4. **可序列化**：State 可以保存到 Checkpoint，支持恢复

**为什么这样设计？**
- Agent 系统需要**记住历史**（消息、工具调用、中间结果）
- 不同节点需要**协作**（一个节点的输出是另一个节点的输入）
- State 是**唯一真相源**（Single Source of Truth）

**类比**：
- State ≈ Java 的 ApplicationContext / RequestContext
- Node ≈ Service 方法（接收 Context，修改 Context）
- Edge ≈ 流程控制（if/else/switch）

## 2. Node 和 Edge 的职责分别是什么？

**Node（节点）**：
- 职责：**执行逻辑**
- 输入：State
- 输出：要更新的字段（不是整个 State）
- 例如：调用 LLM、执行工具、查询数据库

**Edge（边）**：
- 职责：**控制流程**
- 决定：执行完当前节点后，下一个执行谁
- 类型：
  - 普通边：固定连接（A → B）
  - 条件边：根据 State 动态决定（A → B 或 A → C）

**协作关系**：
```
Node A 执行完毕
    ↓
Edge 决定下一步
    ↓
Node B 或 Node C 执行
```

## 3. 条件边和普通边有什么区别？

**普通边**：
```python
graph.add_edge("agent", "tools")  # agent 执行完一定去 tools
```
- 固定连接
- 无条件判断
- 适用于线性流程

**条件边**：
```python
graph.add_conditional_edges("agent", should_continue, {
    "tools": "tools",   # 返回 "tools" → 去 tools 节点
    END: END,           # 返回 END → 结束
})
```
- 动态连接
- 根据 State 决定走向
- 适用于分支、循环

**条件边是 LangGraph 的核心优势**：
- 实现 Agent 的循环（agent → tools → agent → tools → ...）
- 实现复杂的分支逻辑
- 实现动态路由
