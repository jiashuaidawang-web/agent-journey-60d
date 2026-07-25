# Day 31: Hierarchical Agent

> **今日目标**: 实现层级结构的多 Agent 协作
> **核心问题**: 复杂任务如何分层协调？

---

## 🎯 今日目标

1. 理解层级 Agent 模式
2. 实现 Manager → Worker 层级
3. 实现多层协调
4. 完成本阶段综合项目

---

## 📚 必学知识

### 1. 层级 Agent

```
Top Manager（顶层协调）
    ├── Manager A（中层协调）
    │   ├── Worker A1
    │   └── Worker A2
    ├── Manager B（中层协调）
    │   ├── Worker B1
    │   └── Worker B2
    └── Manager C（中层协调）
        └── Worker C1
```

### 2. 适用场景

- 复杂任务（需要多层分解）
- 大规模协作（多个团队）
- 需要分层管理

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Hierarchical | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 层级 Agent 模式
- [ ] 多层协调

---

## 💻 今日编码任务

### 文件结构

```
day31-hierarchical-agent/
├── README.md
├── hierarchical_demo.py     # 层级 Agent
├── requirements.txt
└── boss-answer.md
```

### Task: hierarchical_demo.py（90min）

实现层级 Agent：
- 顶层 Manager
- 中层 Manager
- 底层 Worker

---

## 🐉 今日 Boss

1. **层级 Agent 的流程？**
2. **什么时候用层级结构？**
3. **层级过多有什么问题？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| hierarchical_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，MCP/A2A/Multi-Agent 毕业！进入下一章：Production Agent**
