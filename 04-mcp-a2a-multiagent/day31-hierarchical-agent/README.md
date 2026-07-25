# Day 31: Hierarchical Agent

> **今日目标**: 实现层级结构的多 Agent 协作
> **核心问题**: 复杂任务如何分层协调？

---

## 🎯 今日目标

1. 理解层级 Agent 模式
2. 实现 Manager → Worker 层级
3. 实现多层协调
4. 完成本阶段综合项目

---

## 📚 必学知识

### 1. 层级 Agent

```
Top Manager（顶层协调）
    ├── Manager A（中层协调）
    │   ├── Worker A1
    │   └── Worker A2
    ├── Manager B（中层协调）
    │   ├── Worker B1
    │   └── Worker B2
    └── Manager C（中层协调）
        └── Worker C1
```

### 2. 适用场景

- 复杂任务（需要多层分解）
- 大规模协作（多个团队）
- 需要分层管理

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Hierarchical | https://langchain-ai.github.io/langgraph/concepts/multi_agent/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 层级 Agent 模式
- [ ] 多层协调

---

## 💻 今日编码任务

### 文件结构

```
day31-hierarchical-agent/
├── README.md
├── 00_hierarchical_demo.py   # 层级 Agent
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_hierarchical_demo.py（90min）

实现层级 Agent：
- 顶层 Manager
- 中层 Manager
- 底层 Worker

---

## 🐉 今日 Boss

1. **层级 Agent 的流程？**
2. **什么时候用层级结构？**
3. **层级过多有什么问题？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| hierarchical_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，MCP/A2A/Multi-Agent 毕业！进入下一章：Production Agent**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释层级 Agent 模式的核心概念
- 解释 LangGraph Hierarchical 的用法
- 帮你调试层级 Agent 代码报错
- 对比层级与扁平 Agent 架构的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解公司组织架构（CEO → 总监 → 经理 → 员工），层级 Agent 的多层协调我不太熟。请用公司管理层级类比解释 TopManager → Manager → Worker 的任务分解与汇总流程，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的层级 Agent 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
04-mcp-a2a-multiagent/
└── day31-hierarchical-agent/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_hierarchical_demo.py # 层级 Agent
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 31 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 层级 Agent | ... | ... |
| 多层协调 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 04-mcp-a2a-multiagent/day31-hierarchical-agent/
git commit -m "feat(day31): Hierarchical Agent - 层级 Agent 和综合项目完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Hierarchical 文档
- [ ] 写了 00_hierarchical_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
