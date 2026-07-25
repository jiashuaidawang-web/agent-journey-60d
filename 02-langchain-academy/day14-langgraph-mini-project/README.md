# Day 14: LangGraph Mini Project

> **今日目标**: 综合运用 Day 9-13 的知识，完成一个完整的 LangGraph 项目
> **核心要求**: 包含 State + Node + Edge + Conditional Routing + Checkpoint + Human-in-the-loop

---

## 🎯 今日目标

1. 综合运用 LangGraph 核心概念
2. 实现一个完整的 Research Agent
3. 包含：研究 → 分析 → 报告 → 审批 → 发布

---

## 📚 项目需求

### Research Agent

```
用户输入研究主题
    ↓
Research Agent 搜索信息
    ↓
Analysis Agent 分析信息
    ↓
Report Agent 生成报告
    ↓
人工审批
    ↓
通过 → 发布报告
拒绝 → 修改报告
```

### 技术要求

- [ ] StateGraph 定义
- [ ] 多个 Node（research / analysis / report / approval）
- [ ] 条件边（审批通过/拒绝）
- [ ] Checkpoint（支持断点续跑）
- [ ] interrupt（审批节点暂停）
- [ ] Subgraph（可选）

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Full Example | https://langchain-ai.github.io/langgraph/tutorials/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 综合运用所有 LangGraph 概念
- [ ] 独立完成一个完整项目

---

## 💻 今日编码任务

### 文件结构

```
day14-langgraph-mini-project/
├── README.md
├── LEARNING_FLOW.md           # 学习流程
├── 00_research_agent.py       # 完整 Research Agent
├── requirements.txt
└── 99-boss-answer.md
```

### Task: research_agent.py（3-4h）

实现完整 Research Agent：
- 研究节点：搜索信息
- 分析节点：分析信息
- 报告节点：生成报告
- 审批节点：人工审批
- 条件边：通过/拒绝
- Checkpoint：支持恢复

---

## 🐉 今日 Boss

1. **请描述你的 Research Agent 架构**
2. **如果让你扩展支持多 Agent 协作，你会怎么改？**
3. **如何保证长时间运行的可靠性？**

---

## 🎤 面试题

1. **LangGraph 的核心概念有哪些？**
2. **如何实现 Agent 的断点续跑？**
3. **Human-in-the-loop 的实现原理是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| 架构设计 | 20分 |
| 功能完整性 | 30分 |
| 代码质量 | 20分 |
| Boss 答案 | 15分 |
| 可扩展性 | 15分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，LangChain Academy 毕业！进入下一章：RAG Dungeon**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 LangGraph 核心概念的综合运用
- 解释 State + Node + Edge + Conditional Routing + Checkpoint + Human-in-the-loop
- 帮你调试代码报错
- 解释多 Agent 协作的扩展方案

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我想扩展 Research Agent 支持多 Agent 协作，请用 Supervisor 模式给我一个架构设计思路，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Research Agent。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day14-langgraph-mini-project/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_research_agent.py       # 完整 Research Agent
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 14 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| LangGraph 综合运用 | ... | ... |
| Research Agent 架构 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day14-langgraph-mini-project/
git commit -m "feat(day14): LangGraph Mini Project - Research Agent 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Full Example 文档
- [ ] 写了 00_research_agent.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
