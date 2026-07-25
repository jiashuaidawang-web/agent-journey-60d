# Day 24 Boss 答案

## 1. MCP Server 的职责是什么？

**MCP Server 的核心职责**：

1. **暴露工具（Tools）**：提供 LLM 可以调用的函数
2. **暴露资源（Resources）**：提供数据源（文件、数据库等）
3. **暴露提示词（Prompts）**：提供预定义的提示词模板
4. **处理请求**：接收 Client 的请求，执行并返回结果

**类比**：
- MCP Server = RESTful API Server
- Tools = API Endpoints
- Resources = Database / File Storage

## 2. 如何注册一个 Tool？

**使用 FastMCP 注册**：
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def get_weather(city: str) -> str:
    """获取城市天气。"""
    return f"{city}今天晴，25°C"
```

**使用底层 SDK 注册**：
```python
from mcp.server import Server

server = Server("my-server")

@server.list_tools()
async def list_tools():
    return [Tool(name="get_weather", ...)]

@server.call_tool()
async def call_tool(name, arguments):
    if name == "get_weather":
        return [TextContent(text="晴，25°C")]
```

## 3. MCP Server 如何被 Client 调用？

**调用流程**：
```
1. Client 连接 Server（stdio / HTTP）
2. Client 发送 tools/list 请求
3. Server 返回工具列表
4. LLM 看到工具列表，决定调用
5. Client 发送 tools/call 请求
6. Server 执行工具
7. Server 返回结果
8. Client 把结果反馈给 LLM
```

**代码示例**：
```python
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async with streamablehttp_client("http://localhost:8000") as (read, write, _):
    async with ClientSession(read, write) as session:
        await session.initialize()
        
        # 列出工具
        tools = await session.list_tools()
        
        # 调用工具
        result = await session.call_tool("get_weather", {"city": "北京"})
```
