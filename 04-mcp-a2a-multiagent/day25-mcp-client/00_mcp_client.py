"""
Day 25: MCP Client.

实现 MCP Client 调用 Server。

Usage:
    python mcp_client.py
"""


def mcp_client_demo():
    """MCP Client 演示。"""
    print("=" * 60)
    print("MCP Client Demo")
    print("=" * 60)

    # 模拟 MCP Client
    class MockMCPClient:
        def __init__(self, server):
            self.server = server

        def list_tools(self):
            """发现工具。"""
            return self.server.list_tools()

        def call_tool(self, name, arguments):
            """调用工具。"""
            return self.server.call_tool(name, arguments)

        def list_resources(self):
            """列出资源。"""
            return self.server.list_resources()

        def read_resource(self, uri):
            """读取资源。"""
            return self.server.read_resource(uri)

    # 创建 Server（复用 Day 24）
    from mcp_server import create_mock_server
    server = create_mock_server()

    # 创建 Client
    client = MockMCPClient(server)

    print("\n📋 发现工具:")
    tools = client.list_tools()
    for tool in tools:
        print(f"   - {tool['name']}: {tool['description']}")

    print("\n🔧 调用工具:")
    result = client.call_tool("search_industry", {"industry": "白酒"})
    print(f"   search_industry('白酒') → {result}")

    result = client.call_tool("calculate", {"expression": "123 * 456"})
    print(f"   calculate('123 * 456') → {result}")

    print("\n📂 列出资源:")
    resources = client.list_resources()
    for res in resources:
        print(f"   - {res['uri']}: {res['description']}")

    return client


def langchain_integration_demo():
    """LangChain 集成演示。"""
    print("\n" + "=" * 60)
    print("LangChain Integration Demo")
    print("=" * 60)

    print("\n📦 MCP Tools → LangChain Tools 转换:")
    print("   1. 从 MCP Server 获取工具列表")
    print("   2. 转换为 LangChain Tool 格式")
    print("   3. 绑定到 LangChain Agent")

    # 模拟转换
    mcp_tools = [
        {"name": "search_industry", "description": "搜索行业信息"},
        {"name": "search_company", "description": "搜索公司信息"},
        {"name": "calculate", "description": "数学计算"},
    ]

    langchain_tools = []
    for tool in mcp_tools:
        # 转换为 LangChain Tool 格式
        lc_tool = {
            "name": tool["name"],
            "description": tool["description"],
            "func": lambda **kwargs: f"调用 {tool['name']}({kwargs})",
        }
        langchain_tools.append(lc_tool)

    print(f"\n✅ 转换完成: {len(langchain_tools)} 个工具")
    for tool in langchain_tools:
        print(f"   - {tool['name']}: {tool['description']}")

    print("\n🔄 使用流程:")
    print("   1. MCP Client 连接 Server")
    print("   2. 获取工具列表")
    print("   3. 转换为 LangChain Tools")
    print("   4. 创建 Agent，绑定工具")
    print("   5. Agent 自动调用 MCP 工具")


if __name__ == "__main__":
    mcp_client_demo()
    langchain_integration_demo()
