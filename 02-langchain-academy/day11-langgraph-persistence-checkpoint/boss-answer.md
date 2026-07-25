# Day 11 Boss 答案

## 1. Checkpoint 是什么？为什么需要？

**Checkpoint（检查点）**：
- LangGraph 在每个节点执行后自动保存 State 的快照
- 保存到 Checkpoint Saver（内存 / 数据库）
- 包含：当前 State、已执行的节点、待执行的节点

**为什么需要 Checkpoint？**

1. **断点续跑**：Agent 执行中断后，可以从断点恢复
2. **多会话管理**：不同用户/会话的 State 隔离
3. **历史回溯**：查看 Agent 的执行历史
4. **Human-in-the-loop**：在某个节点暂停，等待人工输入
5. **调试**：查看每一步的 State 变化

**Checkpoint 的结构**：
```python
{
    "id": "checkpoint_id",
    "ts": "2024-01-01T00:00:00",
    "channel_values": {"messages": [...], "step": 3},
    "channel_versions": {...},
    "versions_seen": {...},
}
```

## 2. Thread 的作用是什么？

**Thread（线程/会话）**：
- 每个会话有唯一的 `thread_id`
- 不同 thread_id 的 State 完全隔离
- 通过 `configurable.thread_id` 指定

**作用**：
1. **多用户隔离**：用户 A 和用户 B 的 Agent 状态互不干扰
2. **会话管理**：同一个用户的不同会话可以分开管理
3. **历史查询**：通过 thread_id 查询该会话的所有历史

**示例**：
```python
# 用户 A 的会话
config_a = {"configurable": {"thread_id": "user_a"}}
app.invoke(input_a, config_a)

# 用户 B 的会话
config_b = {"configurable": {"thread_id": "user_b"}}
app.invoke(input_b, config_b)

# 两个会话的 State 完全隔离
```

## 3. 如何实现断点续跑？

**断点续跑的核心**：
1. 使用 Checkpointer 保存 State
2. 通过 thread_id 标识会话
3. 从任意 Checkpoint 恢复

**实现方式**：

```python
# 1. 编译时加入 checkpointer
checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)

# 2. 执行时指定 thread_id
config = {"configurable": {"thread_id": "session_123"}}
app.invoke(input, config)

# 3. 查看历史
history = list(app.get_state_history(config))

# 4. 从某个 Checkpoint 恢复
app.update_state(config, new_values)

# 5. 继续执行
app.invoke(None, config)  # None 表示从当前 State 继续
```

**生产环境**：
- 使用 `SqliteSaver` 或 `PostgresSaver` 替代 MemorySaver
- State 持久化到数据库
- 支持跨进程恢复
