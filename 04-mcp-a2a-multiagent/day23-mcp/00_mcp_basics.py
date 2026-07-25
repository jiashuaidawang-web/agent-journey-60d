"""
Day 23: MCP Basics.

演示 MCP（Model Context Protocol）基础。

Usage:
    python mcp_basics.py
"""


def mcp_basics_demo():
    """MCP 基础演示。"""
    print("=" * 60)
    print("MCP Basics Demo")
    print("=" * 60)

    try:
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent
        import mcp
        print(f"✅ MCP SDK 版本: {mcp.__version__}")
    except ImportError:
        print("⚠️ MCP SDK 未安装，使用模拟演示")
        print("   安装: pip install mcp")
        return mcp_mock_demo()

    # 创建 MCP Server
    server = Server("demo-server")

    @server.list_tools()
    async def list_tools():
        """列出所有工具。"""
        return [
            Tool(
                name="get_weather",
                description="获取城市天气",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "城市名称"}
                    },
                    "required": ["city"],
                },
            ),
            Tool(
                name="calculator",
                description="数学计算",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "expression": {"type": "string", "description": "数学表达式"}
                    },
                    "required": ["expression"],
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        """调用工具。"""
        if name == "get_weather":
            city = arguments.get("city", "")
            result = f"{city}今天晴，25°C"
        elif name == "calculator":
            expression = arguments.get("expression", "")
            try:
                result = f"{expression} = {eval(expression)}"
            except Exception as e:
                result = f"计算错误: {e}"
        else:
            result = f"工具 '{name}' 不存在"

        return [TextContent(type="text", text=result)]

    print("\n✅ MCP Server 创建完成")
    print("   工具列表:")
    print("   - get_weather: 获取城市天气")
    print("   - calculator: 数学计算")

    return server


def mcp_mock_demo():
    """MCP 模拟演示。"""
    print("\n📦 MCP 概念演示...")

    # 模拟 MCP Server
    class MockMCPServer:
        def __init__(self, name):
            self.name = name
            self.tools = {}

        def register_tool(self, name, description, handler):
            self.tools[name] = {
                "description": description,
                "handler": handler,
            }

        def list_tools(self):
            return [
                {"name": name, "description": tool["description"]}
                for name, tool in self.tools.items()
            ]

        def call_tool(self, name, arguments):
            if name in self.tools:
                return self.tools[name]["handler"](**arguments)
            return f"工具 '{name}' 不存在"

    # 创建 Server
    server = MockMCPServer("demo-server")

    # 注册工具
    server.register_tool(
        "get_weather",
        "获取城市天气",
        lambda city: f"{city}今天晴，25°C"
    )
    server.register_tool(
        "calculator",
        "数学计算",
        lambda expression: f"{expression} = {eval(expression)}"
    )

    print(f"\n✅ MCP Server '{server.name}' 创建完成")
    print(f"   工具列表:")
    for tool in server.list_tools():
        print(f"   - {tool['name']}: {tool['description']}")

    # 调用工具
    print("\n🔧 调用工具:")
    result = server.call_tool("get_weather", {"city": "北京"})
    print(f"   get_weather('北京') → {result}")

    result = server.call_tool("calculator", {"expression": "123 * 456"})
    print(f"   calculator('123 * 456') → {result}")

    return server


if __name__ == "__main__":
    mcp_basics_demo()
