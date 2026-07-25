# Day 24: MCP Server 实现

> **今日目标**: 实现一个完整的 MCP Server
> **核心问题**: MCP Server 如何暴露工具给外部调用？

---

## 🎯 今日目标

1. 实现完整的 MCP Server
2. 暴露 Tools、Resources、Prompts
3. 支持 stdio 和 HTTP 传输
4. 集成到 LangChain/LangGraph

---

## 📚 必学知识

### 1. MCP Server 实现方式

| 方式 | 说明 | 适用 |
|------|------|------|
| stdio | 标准输入输出 | 本地工具 |
| HTTP | HTTP 接口 | 远程服务 |
| SSE | Server-Sent Events | 流式传输 |

### 2. FastMCP

- MCP Python SDK 的高级封装
- 简化 Server 开发
- 支持装饰器定义工具

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| MCP Python SDK | https://github.com/modelcontextprotocol/python-sdk |
| FastMCP | https://github.com/jlowin/fastmcp |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] MCP Server 实现
- [ ] 工具注册
- [ ] 资源暴露

---

## 💻 今日编码任务

### 文件结构

```
day24-mcp-server/
├── README.md
├── mcp_server.py            # MCP Server 实现
├── mcp_resources.py         # MCP Resources
├── requirements.txt
└── boss-answer.md
```

### Task 1: mcp_server.py（90min）

实现 MCP Server：
- 定义 Tools
- 实现调用逻辑
- 支持 stdio

### Task 2: mcp_resources.py（45min）

实现 MCP Resources：
- 文件资源
- 数据库资源

---

## 🐉 今日 Boss

1. **MCP Server 的职责是什么？**
2. **如何注册一个 Tool？**
3. **MCP Server 如何被 Client 调用？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| mcp_server.py | 60分 |
| mcp_resources.py | 20分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 25: MCP Client**
