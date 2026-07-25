# Day 30: Parallel Agent

> **今日目标**: 实现并行执行的多个 Agent
> **核心问题**: 什么任务可以并行执行？

---

## 🎯 今日目标

1. 理解并行 Agent 模式
2. 实现并行执行
3. 实现结果汇总
4. 理解并行 vs 串行

---

## 📚 必学知识

### 1. 并行 Agent

```
任务
    ↓
┌─────────┬─────────┬─────────┐
│ Agent A │ Agent B │ Agent C │  ← 并行执行
└────┬────┴────┬────┴────┬────┘
     └─────────┼─────────┘
               ↓
         汇总结果
```

### 2. 适用场景

- 任务之间无依赖
- 多个独立子任务
- 需要多角度分析

### 3. LangGraph 实现

- 使用 Fan-out / Fan-in 模式
- 多个 Node 并行执行
- 汇总 Node 收集结果

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Parallel | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 并行 Agent 模式
- [ ] 并行执行和汇总

---

## 💻 今日编码任务

### 文件结构

```
day30-parallel-agent/
├── README.md
├── parallel_demo.py         # 并行 Agent
├── requirements.txt
└── boss-answer.md
```

### Task: parallel_demo.py（90min）

实现并行 Agent：
- 并行执行多个 Agent
- 结果汇总

---

## 🐉 今日 Boss

1. **什么任务适合并行？**
2. **并行和串行的区别？**
3. **如何汇总并行结果？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| parallel_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 31: Hierarchical Agent**
