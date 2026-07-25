# Day 13: LangGraph Long-running Agent + Subgraph

> **今日目标**: 实现长时间运行的 Agent 和子图
> **核心问题**: 复杂 Agent 如何拆分和组合？

---

## 🎯 今日目标

1. 理解 Subgraph（子图）
2. 实现图嵌套
3. 实现长时间运行的 Agent
4. 理解递归和组合

---

## 📚 必学知识

### 1. Subgraph（子图）

- 一个 Graph 可以作为另一个 Graph 的节点
- 实现模块化和复用
- 子图有自己的 State，可以和父图 State 重叠

### 2. 添加子图节点

```python
# 子图编译后作为节点
subgraph = sub_graph.compile()
graph.add_node("sub_task", subgraph)
```

### 3. 长时间运行

- 通过 Checkpoint 支持中断恢复
- 通过 interrupt 支持人工介入
- 通过 Subgraph 拆分复杂任务

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Subgraph | https://langchain-ai.github.io/langgraph/concepts/low_level/#subgraphs |
| LangGraph Recursion | https://langchain-ai.github.io/langgraph/concepts/low_level/#recursion |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Subgraph 概念
- [ ] 图嵌套
- [ ] 复杂 Agent 拆分

---

## 💻 今日编码任务

### 文件结构

```
day13-langgraph-long-running/
├── README.md
├── subgraph_demo.py         # 子图演示
├── long_running_agent.py    # 长时间运行 Agent
├── requirements.txt
└── boss-answer.md
```

### Task 1: subgraph_demo.py（60min）

实现子图：
- 创建子图
- 作为节点加入父图
- 理解 State 传递

### Task 2: long_running_agent.py（45min）

实现长时间运行 Agent：
- 多步骤任务
- 支持中断恢复

---

## 🐉 今日 Boss

1. **Subgraph 的作用是什么？**
2. **为什么要用 Subgraph 而不是一个大 Graph？**
3. **长时间运行 Agent 如何保证可靠性？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| subgraph_demo.py | 50分 |
| long_running_agent.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 14: LangGraph Mini Project**
