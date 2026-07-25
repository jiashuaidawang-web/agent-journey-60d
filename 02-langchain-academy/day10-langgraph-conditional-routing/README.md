# Day 10: LangGraph Conditional Routing

> **今日目标**: 掌握条件路由，实现复杂分支逻辑
> **核心问题**: 如何根据 State 动态决定执行路径？

---

## 🎯 今日目标

1. 理解条件边的路由函数
2. 实现多分支路由
3. 实现循环控制
4. 实现 Router Graph

---

## 📚 必学知识

### 1. 条件路由函数

```python
def route(state: State) -> str:
    """根据 State 返回下一个节点的名称。"""
    if state["intent"] == "weather":
        return "weather_agent"
    elif state["intent"] == "stock":
        return "stock_agent"
    else:
        return "fallback"
```

### 2. 路由映射

```python
graph.add_conditional_edges("router", route, {
    "weather_agent": "weather_agent",
    "stock_agent": "stock_agent",
    "fallback": "fallback",
})
```

---

## 💻 今日编码任务

### 文件结构

```
day10-langgraph-conditional-routing/
├── README.md
├── LEARNING_FLOW.md           # 学习流程
├── 00_router_graph.py         # Router Graph
├── 01_multi_branch_graph.py   # 多分支 Graph
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: router_graph.py（60min）

实现 Router Graph：
- 根据用户意图路由到不同 Agent
- 支持 weather / stock / calculator

### Task 2: multi_branch_graph.py（45min）

实现多分支 Graph：
- 根据条件走不同路径
- 支持循环

---

## 🐉 今日 Boss

1. **条件路由函数返回什么？**
2. **路由映射的作用是什么？**
3. **如何实现循环？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| router_graph.py | 50分 |
| multi_branch_graph.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 11: Persistence + Checkpoint**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释条件路由函数的作用和返回值
- 解释路由映射的作用
- 帮你调试代码报错
- 解释循环的实现和终止条件

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "条件路由函数返回的是节点名称还是 State 字段？请用 Java 的 Switch 语句类比解释一下路由映射。"

### 错误用法
> "帮我写一个完整的 Router Graph。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day10-langgraph-conditional-routing/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_router_graph.py         # Router Graph
    ├── 01_multi_branch_graph.py   # 多分支 Graph
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 10 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 条件路由 | ... | ... |
| 路由映射 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day10-langgraph-conditional-routing/
git commit -m "feat(day10): LangGraph Conditional Routing - Router Graph 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Edges 文档
- [ ] 写了 00_router_graph.py
- [ ] 写了 01_multi_branch_graph.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
