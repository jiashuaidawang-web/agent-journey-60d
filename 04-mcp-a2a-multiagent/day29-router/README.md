# Day 29: Multi-Agent Router

> **今日目标**: 实现 Router 模式的多 Agent 路由
> **核心问题**: Router 如何决定调用哪个 Agent？

---

## 🎯 今日目标

1. 理解 Router 模式
2. 实现意图路由
3. 实现多 Agent 路由
4. 理解 Router vs Supervisor 的区别

---

## 📚 必学知识

### 1. Router 模式

```
用户输入
    ↓
Router Agent（路由）
    ↓
├── 意图A → Agent A
├── 意图B → Agent B
└── 意图C → Agent C
```

### 2. Router vs Supervisor

| 维度 | Router | Supervisor |
|------|--------|------------|
| 决策 | 单次路由 | 持续协调 |
| 交互 | 一对一 | 一对多 |
| 适用 | 多领域任务 | 复杂协作任务 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Router | https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi-agent-collaboration/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Router 模式
- [ ] 意图路由

---

## 💻 今日编码任务

### 文件结构

```
day29-router/
├── README.md
├── router_demo.py           # Router 模式
├── requirements.txt
└── boss-answer.md
```

### Task: router_demo.py（90min）

实现 Router 模式：
- 意图识别
- 路由到不同 Agent
- 结果返回

---

## 🐉 今日 Boss

1. **Router 和 Supervisor 的区别？**
2. **Router 如何决定路由？**
3. **路由错误怎么办？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| router_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 30: Parallel Agent**
