# Day 32: Observability（可观测性）

> **今日目标**: 实现 Agent 系统的可观测性
> **核心问题**: 如何监控 Agent 的运行状态？

---

## 🎯 今日目标

1. 理解 Agent 可观测性的重要性
2. 实现 Trace（追踪）
3. 实现 Token / Cost / Latency 统计
4. 集成 LangSmith / Phoenix

---

## 📚 必学知识

### 1. 为什么 Agent 需要可观测性？

- Agent 是多步骤流程，需要追踪每一步
- Token 消耗需要统计和优化
- 问题排查需要完整链路
- 成本需要核算

### 2. Agent 可观测性指标

| 指标 | 说明 |
|------|------|
| Trace | 完整执行链路 |
| Token | Token 消耗 |
| Latency | 延迟 |
| Cost | 成本 |
| Tool Call | 工具调用次数和结果 |
| Agent Step | Agent 步骤 |

### 3. LangSmith

- LangChain 官方可观测性平台
- 自动追踪 LangChain / LangGraph 调用
- 支持 Trace、Token、Latency 统计

### 4. Phoenix (Arize)

- 开源 LLM 可观测性平台
- 支持 Trace、Span、Token
- 支持 Prompt 分析

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangSmith | https://docs.smith.langchain.com/ |
| Phoenix | https://docs.arize.com/phoenix |
| OpenTelemetry | https://opentelemetry.io/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Agent 可观测性指标
- [ ] Trace 实现
- [ ] Token/Cost/Latency 统计

---

## 💻 今日编码任务

### 文件结构

```
day32-observability/
├── README.md
├── 00_metrics_demo.py          # 指标统计
├── 01_trace_demo.py            # Trace 实现
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: trace_demo.py（60min）

实现 Trace：
- 记录 Agent 执行链路
- 记录每个步骤的输入输出

### Task 2: metrics_demo.py（45min）

实现指标统计：
- Token 消耗
- 延迟
- 成本

---

## 🐉 今日 Boss

1. **Agent 可观测性需要哪些指标？**
2. **Trace 的作用是什么？**
3. **如何统计 Token 消耗？**

---

## 🎤 面试题

1. **如何监控 Agent 系统的运行状态？**
2. **Agent 的 Token 消耗如何优化？**
3. **如何排查 Agent 的问题？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| trace_demo.py | 50分 |
| metrics_demo.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 33: Security**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Agent 可观测性的核心概念
- 解释 LangSmith / Phoenix 的用法
- 帮你调试代码报错
- 对比不同实现方案的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 经验，Python 的装饰器和上下文管理器我不太熟。请用 Java 的 AOP 类比解释一下可观测性中的 Span 机制，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Agent 监控系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
05-production-agent/
└── day32-observability/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_metrics_demo.py   # 指标统计
    ├── 01_trace_demo.py     # Trace 实现
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 32 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Trace | ... | ... |
| Token 统计 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 05-production-agent/day32-observability/
git commit -m "feat(day32): Observability - Trace 和 Metrics 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangSmith / Phoenix 官方文档
- [ ] 写了 00_metrics_demo.py
- [ ] 写了 01_trace_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
