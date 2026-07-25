# 02-langchain-academy · Day 8-14 执行版 v3.0

> **定位**: LangGraph 深一周 + LangChain 快速过
> **目标**: 掌握 Agent 编排的核心框架

---

## 7天总览

```
Day 8   LangChain 快速过 + 用 LangChain 重写 Mini Agent
Day 9   LangGraph State + Node + Edge
Day 10  LangGraph Conditional Routing
Day 11  LangGraph Persistence + Checkpoint
Day 12  LangGraph Human-in-the-loop
Day 13  LangGraph Long-running Agent + Subgraph
Day 14  LangGraph Mini Project
```

## 核心重点

**Day 8 是快速过**：LangChain 了解即可，重点是用它重写 Day 7 的 Mini Agent

**Day 9-14 是重点**：LangGraph 是 Agent 编排的核心框架，必须深入掌握

## 学习资料

| 框架 | 文档地址 |
|------|----------|
| LangChain Python | https://python.langchain.com/docs/ |
| LangGraph Python | https://langchain-ai.github.io/langgraph/ |
| LangGraph Studio | https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/ |

## Java → LangChain/LangGraph 对照

| 概念 | Java | LangChain/LangGraph |
|------|------|---------------------|
| 链式调用 | Stream API | LCEL (Runnable) |
| 模板方法 | AbstractClass | Runnable |
| 状态机 | StateMachine | StateGraph |
| 事件驱动 | ApplicationEvent | Node + Edge |
| 持久化 | JPA Repository | Checkpoint |

---

**准备好了吗？从 Day 8 开始。**
