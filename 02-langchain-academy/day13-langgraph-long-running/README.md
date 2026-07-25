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
├── LEARNING_FLOW.md           # 学习流程
├── 00_long_running_agent.py   # 长时间运行 Agent
├── 01_subgraph_demo.py        # 子图演示
├── requirements.txt
└── 99-boss-answer.md
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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Subgraph 的作用和优势
- 解释为什么要用 Subgraph 而不是一个大 Graph
- 帮你调试代码报错
- 解释长时间运行 Agent 如何保证可靠性

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "Subgraph 和父图的 State 怎么传递？请用 Java 的 Service 组合类比解释一下图嵌套。"

### 错误用法
> "帮我写一个完整的子图 Demo。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day13-langgraph-long-running/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_long_running_agent.py   # 长时间运行 Agent
    ├── 01_subgraph_demo.py        # 子图演示
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 13 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Subgraph | ... | ... |
| 长时间运行 Agent | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day13-langgraph-long-running/
git commit -m "feat(day13): LangGraph Long-running+Subgraph - 子图完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Subgraph 文档
- [ ] 读了 LangGraph Recursion 文档
- [ ] 写了 00_long_running_agent.py
- [ ] 写了 01_subgraph_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
