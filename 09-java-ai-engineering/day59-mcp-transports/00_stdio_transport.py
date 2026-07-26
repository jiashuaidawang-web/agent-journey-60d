"""
Day 59: MCP 三种传输方式 - STDIO 传输演示

本文件演示 MCP 的 STDIO（Standard Input/Output）传输方式。
STDIO 是最简单的传输方式，通过进程的标准输入/输出传递 JSON-RPC 消息。

适用场景：
- 本地 CLI 工具
- IDE 插件（Claude Code、Cursor）
- 单机开发调试

核心概念：
- Client 启动 MCP Server 作为子进程
- 双方通过 stdin/stdout 读写消息
- 每行一条 JSON-RPC 消息（换行符分隔）
"""

# 注意：这是一个占位文件，用于演示 STDIO 传输的实现思路
# 实际运行时需要安装 MCP SDK: pip install mcp

# 导入示例（占位）
# from mcp.server import Server
# from mcp.server.stdio import stdio_server
# from mcp.types import Tool, TextContent
# import asyncio


# === Server 端 ===

# 创建 MCP Server 实例
# server = Server("demo-server")


# @server.list_tools()
# async def list_tools():
#     """注册工具列表"""
#     return [
#         Tool(
#             name="get_weather",
#             description="获取指定城市的天气",
#             inputSchema={
#                 "type": "object",
#                 "properties": {
#                     "city": {"type": "string", "description": "城市名称"}
#                 },
#                 "required": ["city"]
#             }
#         )
#     ]


# @server.call_tool()
# async def call_tool(name: str, arguments: dict):
#     """处理工具调用"""
#     if name == "get_weather":
#         city = arguments["city"]
#         # 模拟天气查询
#         return [TextContent(type="text", text=f"{{city: {city}, temp: 25°C}}")]
#     raise ValueError(f"Unknown tool: {name}")


# async def run_server():
#     """启动 STDIO Server"""
#     async with stdio_server() as (read_stream, write_stream):
#         await server.run(read_stream, write_stream, server.create_initialization_options())


# === Client 端 ===

# from mcp.client.stdio import stdio_client
# from mcp import ClientSession
#
#
# async def run_client():
#     """启动 STDIO Client"""
#     # 启动 Server 子进程
#     async with stdio_client(ServerParameters(command="python", args=["server.py"])) as (
#         read,
#         write,
#     ):
#         async with ClientSession(read, write) as session:
#             # 初始化连接
#             await session.initialize()
#
#             # 列出所有工具
#             tools = await session.list_tools()
#             print(f"可用工具: {[t.name for t in tools.tools]}")
#
#             # 调用工具
#             result = await session.call_tool("get_weather", {"city": "北京"})
#             print(f"调用结果: {result.content}")


# === 主函数 ===

def main():
    """
    主函数：演示 STDIO 传输的完整流程

    运行方式：
        python 00_stdio_transport.py

    预期输出：
        🔌 STDIO 传输启动
        📡 Server 已启动（子进程模式）
        🔧 工具注册：get_weather
        ✅ 调用结果：{city: "北京", temp: "25°C"}
    """
    print("🔌 STDIO 传输启动")
    print("📡 Server 已启动（子进程模式）")
    print("🔧 工具注册：get_weather")
    print("✅ 调用结果：{city: 北京, temp: 25°C}")
    print()
    print("注意：这是一个占位文件，实际运行需要安装 MCP SDK")
    print("安装命令：pip install mcp")


if __name__ == "__main__":
    main()
