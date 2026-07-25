# Day 12: LangGraph Human-in-the-loop

> **今日目标**: 实现人工审批流程
> **核心问题**: Agent 如何在关键步骤暂停等待人工确认？

---

## 🎯 今日目标

1. 理解 interrupt 机制
2. 实现人工审批节点
3. 实现 interrupt_after / interrupt_before
4. 实现动态人工介入

---

## 📚 必学知识

### 1. interrupt 机制

- LangGraph 可以在指定节点**前/后**暂停
- 等待人工输入后继续执行
- 通过 `checkpointer` 保存暂停时的 State

### 2. interrupt_after

```python
# 在 "agent" 节点执行后暂停
app = graph.compile(checkpointer=checkpointer, interrupt_after=["agent"])
```

### 3. interrupt_before

```python
# 在 "tools" 节点执行前暂停
app = graph.compile(checkpointer=checkpointer, interrupt_before=["tools"])
```

### 4. 恢复执行

```python
# 人工审批后，传入 None 继续
app.invoke(None, config)
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Human-in-the-loop | https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/ |
| interrupts | https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] interrupt 机制
- [ ] 人工审批流程
- [ ] 恢复执行

---

## 💻 今日编码任务

### 文件结构

```
day12-langgraph-human-in-loop/
├── README.md
├── approval_demo.py         # 人工审批演示
├── tool_approval.py         # 工具调用审批
├── requirements.txt
└── boss-answer.md
```

### Task 1: approval_demo.py（60min）

实现人工审批：
- Agent 生成方案
- 暂停等待审批
- 审批通过/拒绝
- 继续执行

### Task 2: tool_approval.py（45min）

实现工具调用审批：
- 工具执行前暂停
- 人工确认后执行

---

## 🐉 今日 Boss

1. **interrupt 和 Checkpoint 的关系？**
2. **什么场景需要 Human-in-the-loop？**
3. **如何实现审批通过/拒绝的不同处理？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| approval_demo.py | 50分 |
| tool_approval.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 13: Long-running Agent**
