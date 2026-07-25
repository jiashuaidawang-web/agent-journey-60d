# Day 14: LangGraph Mini Project

> **今日目标**: 综合运用 Day 9-13 的知识，完成一个完整的 LangGraph 项目
> **核心要求**: 包含 State + Node + Edge + Conditional Routing + Checkpoint + Human-in-the-loop

---

## 🎯 今日目标

1. 综合运用 LangGraph 核心概念
2. 实现一个完整的 Research Agent
3. 包含：研究 → 分析 → 报告 → 审批 → 发布

---

## 📚 项目需求

### Research Agent

```
用户输入研究主题
    ↓
Research Agent 搜索信息
    ↓
Analysis Agent 分析信息
    ↓
Report Agent 生成报告
    ↓
人工审批
    ↓
通过 → 发布报告
拒绝 → 修改报告
```

### 技术要求

- [ ] StateGraph 定义
- [ ] 多个 Node（research / analysis / report / approval）
- [ ] 条件边（审批通过/拒绝）
- [ ] Checkpoint（支持断点续跑）
- [ ] interrupt（审批节点暂停）
- [ ] Subgraph（可选）

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Full Example | https://langchain-ai.github.io/langgraph/tutorials/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 综合运用所有 LangGraph 概念
- [ ] 独立完成一个完整项目

---

## 💻 今日编码任务

### 文件结构

```
day14-langgraph-mini-project/
├── README.md
├── research_agent.py        # 完整 Research Agent
├── requirements.txt
└── boss-answer.md
```

### Task: research_agent.py（3-4h）

实现完整 Research Agent：
- 研究节点：搜索信息
- 分析节点：分析信息
- 报告节点：生成报告
- 审批节点：人工审批
- 条件边：通过/拒绝
- Checkpoint：支持恢复

---

## 🐉 今日 Boss

1. **请描述你的 Research Agent 架构**
2. **如果让你扩展支持多 Agent 协作，你会怎么改？**
3. **如何保证长时间运行的可靠性？**

---

## 🎤 面试题

1. **LangGraph 的核心概念有哪些？**
2. **如何实现 Agent 的断点续跑？**
3. **Human-in-the-loop 的实现原理是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| 架构设计 | 20分 |
| 功能完整性 | 30分 |
| 代码质量 | 20分 |
| Boss 答案 | 15分 |
| 可扩展性 | 15分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，LangChain Academy 毕业！进入下一章：RAG Dungeon**

---

## 📊 今日检查清单

- [ ] StateGraph 定义正确
- [ ] 所有 Node 实现
- [ ] 条件边正确
- [ ] Checkpoint 配置
- [ ] interrupt 配置
- [ ] 代码能运行
- [ ] Boss 答案完成
- [ ] Git Commit
