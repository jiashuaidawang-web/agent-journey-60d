# Day 27: A2A 协议详解

> **今日目标**: 理解 A2A（Agent-to-Agent）协议
> **核心问题**: A2A 和 MCP 有什么区别？

---

## 🎯 今日目标

1. 理解 A2A 的本质：Agent 间通信协议
2. 理解 A2A 和 MCP 的区别
3. 实现最小 A2A Demo
4. 理解 Agent Card、Task、Message

---

## 📚 必学知识

### 1. 什么是 A2A？

**A2A（Agent-to-Agent）**：
- Google 提出的 Agent 间通信协议
- 标准化 Agent 之间的协作
- 类似 HTTP：Agent 之间的"语言"

### 2. A2A vs MCP

| 维度 | MCP | A2A |
|------|-----|-----|
| 定义 | LLM ↔ 工具/数据 | Agent ↔ Agent |
| 方向 | 上下级（Client-Server） | 对等（Peer-to-Peer） |
| 场景 | 调用工具 | Agent 协作 |
| 类比 | USB 接口 | HTTP 协议 |

### 3. A2A 核心概念

| 概念 | 说明 |
|------|------|
| Agent Card | Agent 的能力描述 |
| Task | 任务 |
| Message | 消息 |
| Part | 消息的一部分 |

### 4. A2A 架构

```
Agent A                    Agent B
   │                         │
   │  1. 获取 Agent Card     │
   │ ──────────────────────→ │
   │                         │
   │  2. 发送 Task           │
   │ ──────────────────────→ │
   │                         │
   │  3. 返回结果            │
   │ ←────────────────────── │
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| A2A 协议 | https://github.com/google/A2A |
| A2A 规范 | https://a2a-protocol.org/ |

---

## 🧠 学习深度

### 必须掌握（L2-L3）
- [ ] A2A 协议原理
- [ ] A2A vs MCP 区别
- [ ] Agent Card、Task、Message

---

## 💻 今日编码任务

### 文件结构

```
day27-a2a/
├── README.md
├── 00_a2a_demo.py            # A2A 最小 Demo
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: a2a_demo.py（60min）

实现 A2A 最小 Demo：
- Agent 注册
- Task 发送
- 结果返回

### Task 2: agent_card.py（45min）

实现 Agent Card：
- 能力描述
- 接口定义

---

## 🐉 今日 Boss

1. **A2A 和 MCP 有什么区别？**
2. **A2A 的核心概念有哪些？**
3. **什么场景需要 A2A？**

---

## 🎤 面试题

1. **MCP vs A2A 的区别和联系？**
2. **A2A 协议的价值是什么？**
3. **如何实现 Agent 间的协作？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| a2a_demo.py | 50分 |
| agent_card.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 28: Multi-Agent Supervisor**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 A2A（Agent-to-Agent）协议的核心概念
- 解释 A2A 和 MCP 的区别与联系
- 帮你调试 A2A Demo 代码报错
- 对比 A2A 与直接 RPC 调用的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解微服务之间的 HTTP 调用，A2A 的 Agent Card 服务发现机制我不太熟。请用 Consul/Nacos 的服务注册与发现类比解释 A2A Registry 的工作原理，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 A2A 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
04-mcp-a2a-multiagent/
└── day27-a2a/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_a2a_demo.py      # A2A 最小 Demo
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 27 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| A2A | ... | ... |
| Agent Card | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 04-mcp-a2a-multiagent/day27-a2a/
git commit -m "feat(day27): A2A 协议详解 - A2A Demo 和 Agent 协作完成"
```

---

## 📊 今日检查清单

- [ ] 读了 A2A 协议官方文档
- [ ] 读了 A2A 规范
- [ ] 写了 00_a2a_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
