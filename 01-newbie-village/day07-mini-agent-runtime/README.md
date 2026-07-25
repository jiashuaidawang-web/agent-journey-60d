# Day 7: Mini Agent Runtime (纯手写，禁用任何框架)

> **今日目标**: 把前6天全部串起来，实现一个完整的 Mini Agent Runtime
> **核心要求**: 禁止使用 LangChain / LangGraph，完全自己造轮子

---

## 🎯 今日目标

1. 整合前6天的所有抽象：Model + Tool + Registry + Context + Memory + State + Loop
2. 实现一个完整的、可运行的 Agent Runtime
3. 理解 Agent 系统的每一个组件为什么存在
4. 画出架构图并解释

---

## 📚 必学知识

### 回顾前6天的所有抽象

| 天数 | 抽象 | 职责 |
|------|------|------|
| Day 1 | ModelConfig | 模型配置 |
| Day 2 | Pydantic Models | 结构化输出 |
| Day 3 | ContextBuilder | Context 组装 |
| Day 4 | Tool | 工具定义与执行 |
| Day 5 | ToolRegistry + AgentExecutor | 工具注册 + 循环 |
| Day 6 | ReActAgent + RouterAgent | Agent 模式 |

### 今天要把它们整合成：

```
Mini Agent Runtime
├── core/
│   ├── Agent          # 对外统一接口
│   ├── AgentLoop      # 核心循环
│   ├── ContextManager # Context 组装
│   └── AgentState     # 状态管理
├── model/
│   └── Model          # 模型抽象
├── tools/
│   ├── Tool           # 工具基类
│   └── ToolRegistry   # 工具注册表
├── memory/
│   └── Memory         # 记忆
└── observability/
    └── TokenCounter   # Token 统计
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| ReAct Paper | https://arxiv.org/abs/2210.03629 |
| LangChain Agent | https://python.langchain.com/docs/concepts/agents/ |
| OpenAI Function Calling | https://platform.openai.com/docs/guides/function-calling |

---

## 🧠 学习深度

### 必须掌握（L4 架构级）
- [ ] 能画出完整架构图并解释每个模块
- [ ] 能手写 Agent Loop
- [ ] 能解释为什么需要 State / Memory / Context 分离
- [ ] 能解释 Agent Runtime 和 LangChain 的区别

---

## 💻 今日编码任务

### 文件结构

```
day07-mini-agent-runtime/
├── README.md
├── mini_agent_runtime/
│   ├── core/
│   │   └── __init__.py      # Agent + AgentLoop + ContextManager + AgentState
│   ├── model/
│   │   └── __init__.py      # Model 接口 + OpenAIModel
│   ├── tools/
│   │   └── __init__.py      # Tool 基类 + ToolRegistry + 内置工具
│   ├── memory/
│   │   └── __init__.py      # Memory
│   └── observability/
│       └── __init__.py      # TokenCounter
├── examples/
│   └── run_agent.py         # 使用示例
├── tests/
│   └── test_runtime.py      # 测试
├── requirements.txt
└── boss-answer.md
```

### Task: 实现完整 Runtime（3-4h）

按照上面的文件结构，实现所有模块。

**验收标准**：
```bash
python examples/run_agent.py
# 输出：
# 📝 用户: 今天北京天气怎么样
# 🤖 Agent: 北京今天晴，25°C
# ...
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释架构设计
- 帮你调试代码
- 解释模块间的关系

### 今天 AI 不能帮你
- 替你理解架构（你必须自己理解为什么这样设计）
- 替你回答 Boss（你必须自己回答）

---

## 📝 GitHub 提交规范

### 提交结构
```
day07-mini-agent-runtime/
├── README.md
├── mini_agent_runtime/       # 完整包
├── examples/                 # 示例
├── tests/                    # 测试
└── boss-answer.md
```

### README.md 必须包含
```markdown
# Day 7 学习总结

## 架构图
（Mermaid 或文字描述）

## 每个模块为什么存在
| 模块 | 职责 | 为什么需要 |

## 运行结果
（贴终端输出）

## 和 LangChain 的对比
| 维度 | 我们的 Runtime | LangChain |
```

---

## 🐉 今日 Boss

### Level 1: 基础概念
1. **LLM 和 Agent 有什么区别？**
2. **Agent 和 Workflow 有什么区别？**
3. **Tool Calling 到底是谁决定调用 Tool？**
4. **Agent Loop 为什么可能死循环？**

### Level 2: 深入理解
5. **Context 和 Memory 有什么区别？**
6. **为什么 Agent 需要 State？**
7. **为什么 Agent 不能无限保留历史消息？**
8. **Tool Schema 为什么重要？**

### Level 3: 架构设计
9. **如果 Tool 执行失败怎么办？**
10. **如果 LLM 连续调用 Tool 50 次怎么办？**
11. **Agent 如何支持多模型？**
12. **Agent 如何统计 Token？**
13. **Agent 如何恢复中断任务？**

### Level 4: 企业级设计
14. **如果让你设计一个企业级 Agent Runtime，你怎么设计？**

画出架构图并解释每个模块为什么存在：
```
             Agent Runtime
                  │
      ┌───────────┼───────────┐
      ↓           ↓           ↓
    Model        Tool        Memory
      │           │           │
      └───────────┼───────────┘
                  ↓
             Agent Loop
                  ↓
               State
                  ↓
             Observability
```

---

## 🎤 面试题

1. **请描述 Agent 的完整工作流程**
2. **Agent Runtime 包含哪些核心模块？**
3. **如何保证 Agent 不会无限循环？**
4. **Context、Memory、State 三者有什么区别？**
5. **如果要支持多模型，你会怎么设计？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| Model 抽象 | 10分 | 接口清晰 + OpenAI 实现 |
| Tool 系统 | 15分 | 基类 + Registry + 内置工具 |
| Agent Loop | 20分 | 完整循环 + 工具调用 + 终止条件 |
| Context + Memory + State | 15分 | 三者分离 + 职责清晰 |
| 示例能运行 | 15分 | run_agent.py 能跑通 |
| 架构图 + 解释 | 10分 | 清晰 + 每个模块为什么存在 |
| Boss 答案 | 15分 | 14题全部完成 |

---

## 🔓 解锁条件

- [ ] 所有模块实现完成
- [ ] 示例能运行
- [ ] Boss 14题完成
- [ ] 架构图完成
- [ ] 总分 ≥ 60分

**通关后，新手村毕业！进入第二章：LangChain Academy**

---

## 📊 今日检查清单

- [ ] 实现了 Model 接口 + OpenAIModel
- [ ] 实现了 Tool 基类 + ToolRegistry
- [ ] 实现了 AgentLoop
- [ ] 实现了 ContextManager
- [ ] 实现了 AgentState
- [ ] 实现了 Memory
- [ ] 实现了 TokenCounter
- [ ] 实现了 Agent（统一接口）
- [ ] 写了使用示例
- [ ] 示例能运行
- [ ] 写了架构图
- [ ] 写了 Boss 答案
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
