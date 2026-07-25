# Day 23: MCP 协议详解

> **今日目标**: 理解 MCP（Model Context Protocol）协议
> **核心问题**: MCP 和 Function Calling 有什么区别？

---

## 🎯 今日目标

1. 理解 MCP 的本质：工具标准化协议
2. 理解 MCP 的核心概念：Tools、Resources、Prompts
3. 理解 MCP Server / Client 架构
4. 了解 MCP 3.0 新特性

---

## 📚 必学知识

### 1. 什么是 MCP？

**MCP（Model Context Protocol）**：
- Anthropic 提出的开放协议
- 标准化 LLM 应用与外部数据源的连接
- 类似 USB-C 接口：统一、通用、即插即用

### 2. MCP 和 Function Calling 的区别

| 维度 | Function Calling | MCP |
|------|------------------|-----|
| 定义 | LLM 输出工具调用 | 工具标准化协议 |
| 范围 | LLM → 工具 | LLM ↔ 工具 ↔ 数据源 |
| 标准化 | 各家不同 | 统一协议 |
| 复用性 | 低 | 高（一次开发，多处使用） |
| 生态 | 封闭 | 开放 |

### 3. MCP 核心概念

| 概念 | 说明 |
|------|------|
| Tools | 工具（LLM 可以调用） |
| Resources | 资源（数据源） |
| Prompts | 提示词模板 |
| Server | 提供工具/资源的服务 |
| Client | 调用工具/资源的客户端 |

### 4. MCP 架构

```
LLM Application (Client)
        ↓
    [MCP Protocol]
        ↓
MCP Server (Tools + Resources)
        ↓
External Systems (DB, API, Files)
```

### 5. MCP 3.0 新特性

- **Streamable HTTP**：支持流式传输
- **OAuth 2.1**：标准化认证
- **Tasks**：异步任务支持

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| MCP 官方文档 | https://modelcontextprotocol.io/ |
| MCP Python SDK | https://github.com/modelcontextprotocol/python-sdk |
| MCP 3.0 规范 | https://modelcontextprotocol.io/specification/2025-03-26/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] MCP 协议原理
- [ ] Tools / Resources / Prompts
- [ ] Server / Client 架构

### 只需理解（L2）
- [ ] MCP 3.0 新特性
- [ ] OAuth 认证

---

## 💻 今日编码任务

### 文件结构

```
day23-mcp/
├── README.md
├── mcp_basics.py            # MCP 基础演示
├── mcp_tools_demo.py        # MCP Tools 演示
├── requirements.txt
└── boss-answer.md
```

### Task 1: mcp_basics.py（45min）

演示 MCP 基础：
- 创建 MCP Server
- 定义 Tools
- 启动 Server

### Task 2: mcp_tools_demo.py（45min）

演示 MCP Tools：
- 定义多个工具
- 工具注册
- 工具调用

---

## 🐉 今日 Boss

1. **MCP 和 Function Calling 有什么区别？**
2. **MCP 的核心概念有哪些？**
3. **MCP 的架构是什么？**

---

## 🎤 面试题

1. **为什么需要 MCP？**
2. **MCP 的 Tools 和 Function Calling 的工具有什么不同？**
3. **MCP 的生态价值是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| mcp_basics.py | 45分 |
| mcp_tools_demo.py | 35分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 24: MCP Server**
