# Day 27 Boss 答案

## 1. A2A 和 MCP 有什么区别？

| 维度 | MCP | A2A |
|------|-----|-----|
| 定义 | LLM ↔ 工具/数据 | Agent ↔ Agent |
| 方向 | 上下级（Client-Server） | 对等（Peer-to-Peer） |
| 场景 | 调用工具 | Agent 协作 |
| 角色 | Client、Server | 都是 Agent |
| 类比 | USB 接口 | HTTP 协议 |

**核心区别**：
- MCP 解决的是 LLM 如何调用工具
- A2A 解决的是 Agent 如何协作

## 2. A2A 的核心概念有哪些？

| 概念 | 说明 |
|------|------|
| Agent Card | Agent 的能力描述（类似 API 文档） |
| Task | 任务（Agent 执行的工作单元） |
| Message | Agent 间的消息 |
| Part | 消息的一部分（文本、文件等） |

## 3. 什么场景需要 A2A？

**典型场景**：
1. **多 Agent 协作**：研究员 Agent → 分析师 Agent → 报告 Agent
2. **跨系统协作**：不同系统的 Agent 互相调用
3. **动态组队**：根据任务动态组合 Agent
4. **能力复用**：一个 Agent 的能力被多个 Agent 使用
