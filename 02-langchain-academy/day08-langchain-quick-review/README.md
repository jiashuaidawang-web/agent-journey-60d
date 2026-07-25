# Day 8: LangChain 快速过

> **今日目标**: 快速了解 LangChain，并用它重写 Day 7 的 Mini Agent
> **核心问题**: LangChain 和 LangGraph 有什么区别？

---

## 🎯 今日目标

1. 了解 LangChain 核心概念：Runnable、LCEL、Chain
2. 了解 LangChain 的 Tool 和 Agent 抽象
3. 用 LangChain 重写 Day 7 的 Mini Agent
4. 对比手写 vs LangChain 的差异

---

## 📚 必学知识

### 1. LangChain 核心概念

**Runnable**：
- LangChain 的基本抽象，代表一个可执行单元
- 支持 `invoke()`（同步）、`ainvoke()`（异步）、`stream()`（流式）
- 所有 LangChain 组件都是 Runnable

**LCEL（LangChain Expression Language）**：
- 链式调用语法：`prompt | model | parser`
- 类似 Java Stream API：`list.stream().map().filter().collect()`
- 自动支持流式、批处理、并行

**Chain**：
- 多个 Runnable 的组合
- 例如：`prompt | model | output_parser`

### 2. LangChain vs LangGraph

| 维度 | LangChain | LangGraph |
|------|-----------|-----------|
| 抽象 | Chain（链式） | Graph（图） |
| 适用场景 | 线性流程 | 复杂分支、循环 |
| 状态管理 | 弱 | 强（State） |
| 多 Agent | 不支持原生支持 | 原生支持 |
| Human-in-the-loop | 复杂 | 原生支持 |
| 适用 | 简单任务 | 复杂 Agent |

### 3. 为什么学 LangGraph 而不是深入 LangChain？

- LangChain 适合**线性流程**（一次调用 → 输出）
- LangGraph 适合**复杂 Agent**（多步、分支、循环、多 Agent）
- 当前 Agent 系统的主流是 LangGraph
- LangChain 了解即可，LangGraph 必须深入

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangChain Python Docs | https://python.langchain.com/docs/ |
| LCEL | https://python.langchain.com/docs/concepts/lcel/ |
| LangChain Tools | https://python.langchain.com/docs/concepts/tools/ |
| LangChain Agents | https://python.langchain.com/docs/concepts/agents/ |
| LangGraph Docs | https://langchain-ai.github.io/langgraph/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Runnable 和 LCEL
- [ ] LangChain Tool 定义
- [ ] LangChain Agent 基本用法

### 只需理解（L2）
- [ ] LangChain 的 Memory 抽象
- [ ] LangChain 的 Retriever 抽象

---

## 💻 今日编码任务

### 文件结构

```
day08-langchain-quick-review/
├── README.md
├── LEARNING_FLOW.md           # 学习流程
├── 00_langchain_basics.py     # LangChain 基础演示
├── 01_langchain_agent.py      # 用 LangChain 写 Agent
├── 02_compare_agent.py        # 手写 vs LangChain 对比
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: langchain_basics.py（30min）

演示 LangChain 基础：
- Runnable 链式调用
- Prompt + Model + Parser
- Tool 定义

### Task 2: langchain_agent.py（45min）

用 LangChain 实现一个 Agent：
- 使用 `create_tool_calling_agent`
- 使用 `AgentExecutor`
- 支持工具调用

### Task 3: compare_agent.py（45min）

对比手写 vs LangChain：
- 代码量
- 抽象程度
- 扩展性
- 可维护性

---

## 🐉 今日 Boss

1. **LangChain 和 LangGraph 有什么区别？**
2. **LCEL 是什么？和 Java Stream 有什么相似？**
3. **为什么 Agent 系统更倾向于用 LangGraph？**

---

## 🎤 面试题

1. **请描述 LangChain 的 Runnable 抽象**
2. **LCEL 的链式调用有什么优势？**
3. **什么场景下用 LangChain，什么场景下用 LangGraph？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| langchain_basics.py | 25分 |
| langchain_agent.py | 30分 |
| compare_agent.py | 25分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 9: LangGraph State + Node + Edge**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 LangChain 的 Runnable 和 LCEL 核心概念
- 解释 LangChain Tool 定义和 Agent 用法
- 帮你调试代码报错
- 对比手写 Agent Runtime 和 LangChain Agent 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 经验，Python 的装饰器不太熟。请用 Java 的注解类比解释一下 @tool 装饰器，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 LangChain Agent。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day08-langchain-quick-review/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_langchain_basics.py     # LangChain 基础演示
    ├── 01_langchain_agent.py      # 用 LangChain 写 Agent
    ├── 02_compare_agent.py        # 手写 vs LangChain 对比
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 8 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Runnable | ... | ... |
| LCEL | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day08-langchain-quick-review/
git commit -m "feat(day08): LangChain 快速过 - Runnable/LCEL/Agent 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangChain Python Docs
- [ ] 读了 LCEL 文档
- [ ] 写了 00_langchain_basics.py
- [ ] 写了 01_langchain_agent.py
- [ ] 写了 02_compare_agent.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
