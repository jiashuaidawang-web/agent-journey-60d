# Day 25: MCP Client

> **今日目标**: 实现 MCP Client 调用 Server
> **核心问题**: Client 如何发现和调用 Server 的工具？

---

## 🎯 今日目标

1. 实现 MCP Client
2. 发现 Server 工具
3. 调用 Server 工具
4. 集成到 LangChain Agent

---

## 📚 必学知识

### 1. MCP Client 职责

- 连接 Server
- 发现工具（tools/list）
- 调用工具（tools/call）
- 读取资源（resources/read）

### 2. 集成到 LangChain

```python
from langchain_mcp_adapters import MultiServerMCPClient

client = MultiServerMCPClient({
    "research": {
        "url": "http://localhost:8000",
        "transport": "streamable_http",
    }
})

tools = await client.get_tools()
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| MCP Client SDK | https://modelcontextprotocol.io/docs/sdk/python |
| LangChain MCP Adapter | https://github.com/langchain-ai/langchain-mcp-adapters |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] MCP Client 实现
- [ ] 工具发现和调用
- [ ] LangChain 集成

---

## 💻 今日编码任务

### 文件结构

```
day25-mcp-client/
├── README.md
├── mcp_client.py            # MCP Client
├── langchain_integration.py # LangChain 集成
├── requirements.txt
└── boss-answer.md
```

### Task 1: mcp_client.py（60min）

实现 MCP Client

### Task 2: langchain_integration.py（45min）

集成到 LangChain

---

## 🐉 今日 Boss

1. **MCP Client 的职责？**
2. **Client 如何发现工具？**
3. **如何集成到 LangChain？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| mcp_client.py | 50分 |
| langchain_integration.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 26: Skill Architecture**
