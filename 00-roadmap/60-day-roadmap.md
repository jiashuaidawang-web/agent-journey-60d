---
name: 60-day-roadmap
description: 完整的60天Agent架构闯关式学习路线，8章30关，从新手村到Production
metadata:
  type: reference
---

# Agent Journey 60d — 60天Agent架构转型计划

> 10年Java架构师 → Agentic AI Engineer / AI应用架构师 的冲刺路径
> 闯关式学习 · 项目驱动 · Boss Challenge · 每周验收

## 路线总览

| 章节 | 阶段 | 天数 | 等级 | 主题 |
|------|------|------|------|------|
| 第一章 | 新手村 | Day 1-7 | 🟢 Apprentice | LLM → Tool Calling → Agent Loop → 手写Mini Agent Runtime |
| 第二章 | LangChain学院 | Day 8-14 | 🟡 Developer | LangChain组件化：Model/Prompt/Tool/Retriever/Agent |
| 第三章 | RAG副本 | Day 15-21 | 🟠 Engineer | 企业知识库：Hybrid Search + Rerank + Query Rewrite |
| 第四章 | LangGraph深渊 | Day 22-30 | 🔵 Architect | State/Node/Edge/Checkpoint/Human-in-the-loop |
| 第五章 | MCP城 | Day 31-37 | 🔴 Production Eng | MCP Server/Client + Multi-Agent + A2A + Security |
| 第六章 | Multi-Agent竞技场 | Day 38-44 | ⭐ Senior | Supervisor/Hierarchical/Multi-Agent Research System |
| 第七章 | Production地狱 | Day 45-52 | 🏭 Production | Gateway/Auth/MQ/并发/模型路由/可观测性 |
| 第八章 | 最终Boss | Day 53-60 | 🎓 Architect | 两个企业级项目交付 |

## 技术栈优先级

```
★★★★★ LangGraph / RAG / Tool Calling / MCP
★★★★☆ LangChain / Agent Architecture / Memory / Context Engineering
★★★☆☆ Multi-Agent / A2A / Evaluation / Observability / Security
```

## 核心能力地图

```
                         Agent Engineer
                               │
              ┌────────────────┼────────────────┐
              │                │                │
           LLM基础          Agent基础         工程能力
              │                │                │
      Prompt / Context / Token  │        API / Async / MQ
              │                │                │
             LLM         Tool Calling         Backend
              │                │                │
              └────────────────┼────────────────┘
                               │
                        LangChain / LangGraph
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                RAG          Memory       Planning
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                              MCP
                               │
                        Multi-Agent / A2A
                               │
                    Eval / Trace / Security
                               │
                       Production Agent
```

## 两个最终项目

### 项目一：Enterprise Knowledge Agent Platform
企业级AI知识与业务Agent平台
- Python / FastAPI / LangChain / LangGraph
- RAG / Hybrid Search / Rerank / Memory / MCP
- PostgreSQL / Vector DB / Redis
- Observability / Human Approval / Evaluation

### 项目二：AI Investment Research Multi-Agent Platform
A股AI投研多Agent平台（与你现有项目融合）
- Supervisor → Industry/Company/Data/Risk/Review/Report Agents
- MCP连接真实数据源
- LangGraph编排复杂工作流
- 输出完整投资研究报告

## 闯关积分系统

| 活动 | 分数 |
|------|------|
| 理论理解 (+10) | |
| 编码实践 (+20) | |
| 测试通过 (+10) | |
| Boss挑战 (+30) | |
| 面试表达 (+10) | |
| **每日满分** | **80** |

### 等级评定
- 0-300: Agent Apprentice
- 300-700: Agent Developer
- 700-1200: Agent Engineer
- 1200-1800: Agent Architect
- 1800+: Production Agent Architect

## 学习方式

- 20% 理论（官方文档 > GitHub源码 > AI辅助理解）
- 60% 编码（每天必须敲代码）
- 20% 总结（README + Boss答案 + 架构图）

> **铁律**：不直接看答案，先自己推导。框架是工具，原理才是护城河。
