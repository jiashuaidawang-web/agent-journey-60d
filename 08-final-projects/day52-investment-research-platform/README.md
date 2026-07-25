# Day 52: AI Investment Research Platform（AI 投研多 Agent 平台）

> **今日目标**: 完成项目二的核心开发
> **核心要求**: 多 Agent 协作、投研场景

---

## 🎯 今日目标

1. 实现 Supervisor 多 Agent 架构
2. 实现投研 Skills
3. 实现 MCP 工具调用
4. 实现完整投研流程

---

## 📚 项目架构

```
                    ┌──────────────┐
                    │  Supervisor  │
                    │   Agent      │
                    └──────┬───────┘
                           │
        ┌────────┬─────────┼─────────┬────────┐
        ▼        ▼         ▼        ▼        ▼
   ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
   │Industry││Company ││Financial││Market  ││  Risk  │
   │Research││Research││Analysis││Sentiment││Analysis│
   │ Agent  ││ Agent  ││ Agent  ││ Agent  ││ Agent  │
   └───┬────┘└───┬────┘└───┬────┘└───┬────┘└───┬────┘
       │         │         │         │         │
       └─────────┴────┬────┴─────────┴─────────┘
                      │
              ┌───────▼───────┐
              │  MCP + A2A    │
              │  Tool Layer   │
              └───────┬───────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐
   │  RAG    │  │ GraphRAG│  │ 外部数据  │
   │ 知识库  │  │ 图谱    │  │ 行情/财报 │
   └─────────┘  └─────────┘  └──────────┘
```

---

## 🔗 参考资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Multi-Agent | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Supervisor 多 Agent 架构
- [ ] 投研 Skills 实现

---

## 💻 今日编码任务

### 文件结构

```
day52-investment-research-platform/
├── README.md
├── LEARNING_FLOW.md
├── 00_investment_research_platform.py  # 主程序
├── architecture.md                      # 架构说明
└── 99-boss-answer.md
```

### Task 1: investment_research_platform.py（3-4h）

实现完整 Investment Research Platform：
- Supervisor Agent
- 多个专业 Agent
- Skills 封装
- MCP 工具调用

### Task 2: architecture.md

完成架构说明

---

## 🐉 今日 Boss

1. **请描述 Investment Research Platform 架构**
2. **Supervisor 如何协调多个 Agent？**
3. **投研 Skills 有哪些？**

---

## 🎤 面试题

1. **如何设计多 Agent 协作系统？**
2. **Supervisor 模式的优势？**
3. **投研场景的 Agent 设计？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| investment_research_platform.py | 50分 |
| architecture.md | 20分 |
| Boss 答案 | 30分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 53: Architecture Review**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Supervisor 多 Agent 架构的核心概念
- 解释 LangGraph Multi-Agent 的用法
- 帮你调试代码报错
- 对比不同 Agent 协作模式的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我不太理解 Supervisor 模式和 Swarm 模式的区别。请用一个投研场景的例子对比解释一下，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的投研多 Agent 平台。"

---

## 📝 GitHub 提交规范

### 提交结构
```
08-final-projects/
└── day52-investment-research-platform/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_investment_research_platform.py  # 主程序
    ├── architecture.md     # 架构说明
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 52 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Supervisor 模式 | ... | ... |
| Skills 层封装 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 08-final-projects/day52-investment-research-platform/
git commit -m "feat(day52): Investment Research Platform - 多 Agent 投研平台完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Multi-Agent 文档
- [ ] 写了 00_investment_research_platform.py
- [ ] 运行了代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
