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
├── 00_router_demo.py         # Router 模式
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_router_demo.py（90min）

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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Router 模式的核心概念
- 解释 LangGraph Router 的用法
- 帮你调试 Router Demo 代码报错
- 对比 Router 与 Supervisor 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解 Nginx 请求路由的机制，Router Agent 的意图路由我不太熟。请用 Nginx 的 location 匹配类比解释 Router 如何根据意图分发到不同 Agent，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Router 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
04-mcp-a2a-multiagent/
└── day29-router/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_router_demo.py   # Router 模式
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 29 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Router | ... | ... |
| 意图路由 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 04-mcp-a2a-multiagent/day29-router/
git commit -m "feat(day29): Multi-Agent Router - Router 模式和意图路由完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Router 文档
- [ ] 写了 00_router_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
