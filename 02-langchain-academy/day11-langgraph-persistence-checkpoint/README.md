# Day 11: LangGraph Persistence + Checkpoint

> **今日目标**: 实现 Agent 的断点续跑
> **核心问题**: Agent 如何从中断中恢复？

---

## 🎯 今日目标

1. 理解 Checkpoint 机制
2. 实现状态持久化
3. 实现断点续跑
4. 理解 Thread 和多会话

---

## 📚 必学知识

### 1. Checkpoint（检查点）

- LangGraph 在每个节点执行后自动保存 State
- 保存到 Checkpoint Saver（内存 / 数据库）
- 支持从任意 Checkpoint 恢复

### 2. MemorySaver

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)
```

### 3. Thread（线程/会话）

```python
# 每个会话有唯一的 thread_id
config = {"configurable": {"thread_id": "user_123"}}
app.invoke(input, config)
```

### 4. 获取历史

```python
# 获取某个会话的所有 State
history = list(app.get_state_history(config))
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Persistence | https://langchain-ai.github.io/langgraph/concepts/persistence/ |
| LangGraph Checkpoint | https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints |
| MemorySaver | https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Checkpoint 机制
- [ ] MemorySaver 使用
- [ ] Thread 和多会话
- [ ] 断点续跑
- [ ] 历史查询

---

## 💻 今日编码任务

### 文件结构

```
day11-langgraph-persistence-checkpoint/
├── README.md
├── checkpoint_demo.py       # Checkpoint 演示
├── resume_demo.py           # 断点续跑
├── requirements.txt
└── boss-answer.md
```

### Task 1: checkpoint_demo.py（45min）

演示 Checkpoint：
- 使用 MemorySaver
- 保存多个会话
- 查询历史

### Task 2: resume_demo.py（60min）

演示断点续跑：
- 中断执行
- 从 Checkpoint 恢复
- 继续执行

---

## 🐉 今日 Boss

1. **Checkpoint 是什么？为什么需要？**
2. **Thread 的作用是什么？**
3. **如何实现断点续跑？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| checkpoint_demo.py | 40分 |
| resume_demo.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 12: Human-in-the-loop**
