# 04-mcp-a2a-multiagent · Day 23-31 执行版 v3.0

> **定位**: MCP + A2A + Multi-Agent —— 第二项目 Investment Research Platform 的核心
> **目标**: 从协议到多 Agent 编排全链路打通

---

## 9天总览

```
Day 23  MCP 协议详解
Day 24  MCP Server 实现
Day 25  MCP Client 实现
Day 26  Skill Architecture（技能架构）
Day 27  A2A 协议详解
Day 28  Multi-Agent: Supervisor
Day 29  Multi-Agent: Router
Day 30  Multi-Agent: Parallel Agent
Day 31  Multi-Agent: Hierarchical Agent
```

## 核心技术栈

| 技术 | 用途 | 深度 |
|------|------|------|
| MCP 3.0 | 工具标准化协议 | L3 |
| MCP Server | 工具服务化 | L3 |
| MCP Client | 工具调用 | L3 |
| Skill | Agent 能力封装 | L3 |
| A2A | Agent 间通信 | L2-L3 |
| Supervisor | 多 Agent 协调 | L4 |
| Router | 多 Agent 路由 | L4 |
| Parallel Agent | 并行执行 | L3 |
| Hierarchical Agent | 层级协作 | L3 |

## Java 类比

| 概念 | Java 类比 |
|------|-----------|
| MCP | SPI（Service Provider Interface） |
| MCP Server | Microservice |
| MCP Client | Feign Client |
| Skill | Service / UseCase |
| A2A | Message Queue / Event Bus |
| Supervisor | Orchestrator / Workflow Engine |

---

**准备好了吗？从 Day 23 开始 MCP + A2A + Multi-Agent 闯关。**
