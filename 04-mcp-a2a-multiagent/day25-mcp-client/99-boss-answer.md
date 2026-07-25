# Day 25 Boss 答案

## 1. MCP Client 的职责？

1. **连接 Server**：建立通信（stdio / HTTP）
2. **发现工具**：调用 tools/list 获取工具列表
3. **调用工具**：调用 tools/call 执行工具
4. **读取资源**：调用 resources/read 获取数据
5. **处理响应**：解析 Server 返回的结果

## 2. Client 如何发现工具？

```python
# 1. 连接 Server
client = ClientSession(read, write)
await client.initialize()

# 2. 列出工具
tools = await client.list_tools()
# 返回: Tool(name="get_weather", description="...", inputSchema={...})

# 3. 调用工具
result = await client.call_tool("get_weather", {"city": "北京"})
# 返回: CallToolResult(content=[TextContent(text="晴，25°C")])
```

## 3. 如何集成到 LangChain？

```python
from langchain_mcp_adapters import MultiServerMCPClient

# 1. 创建 MCP Client
client = MultiServerMCPClient({
    "server": {"url": "http://localhost:8000", "transport": "streamable_http"}
})

# 2. 获取 LangChain Tools
tools = await client.get_tools()

# 3. 创建 Agent
agent = create_tool_calling_agent(llm, tools, prompt)
```
