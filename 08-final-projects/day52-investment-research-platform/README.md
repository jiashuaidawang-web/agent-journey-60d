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
├── investment_research_platform.py  # 主程序
├── architecture.md                   # 架构说明
├── requirements.txt
└── boss-answer.md
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
