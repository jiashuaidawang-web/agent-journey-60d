"""
Day 24: MCP Server.

实现一个完整的 MCP Server。

Usage:
    python mcp_server.py
"""

import asyncio


def create_mcp_server():
    """创建 MCP Server。"""
    try:
        from mcp.server.fastmcp import FastMCP
        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import Tool, TextContent, Resource
    except ImportError:
        print("⚠️ MCP SDK 未安装，使用模拟实现")
        return create_mock_server()

    # 使用 FastMCP 创建 Server
    mcp = FastMCP("research-server")

    @mcp.tool()
    def search_industry(industry: str) -> str:
        """搜索行业信息。"""
        return f"{industry}行业概况：市场规模持续增长，龙头企业市占率提升"

    @mcp.tool()
    def search_company(company: str) -> str:
        """搜索公司信息。"""
        return f"{company}：行业龙头，基本面稳健"

    @mcp.tool()
    def get_financial_data(company: str) -> str:
        """获取财务数据。"""
        return f"{company}财务数据：营收增长15%，净利润增长18%"

    @mcp.tool()
    def calculate(expression: str) -> str:
        """数学计算。"""
        try:
            result = eval(expression)
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"

    @mcp.resource("industry://{industry}")
    def industry_resource(industry: str) -> str:
        """行业资源。"""
        return f"{industry}行业详细报告..."

    print("✅ MCP Server 创建完成")
    print("   工具: search_industry, search_company, get_financial_data, calculate")
    print("   资源: industry://{industry}")

    return mcp


def create_mock_server():
    """创建模拟 MCP Server。"""
    class MockMCPServer:
        def __init__(self, name):
            self.name = name
            self.tools = {}
            self.resources = {}

        def register_tool(self, name, description, handler):
            self.tools[name] = {
                "description": description,
                "handler": handler,
            }

        def register_resource(self, uri, description, handler):
            self.resources[uri] = {
                "description": description,
                "handler": handler,
            }

        def list_tools(self):
            return [
                {"name": name, "description": tool["description"]}
                for name, tool in self.tools.items()
            ]

        def list_resources(self):
            return [
                {"uri": uri, "description": res["description"]}
                for uri, res in self.resources.items()
            ]

        def call_tool(self, name, arguments):
            if name in self.tools:
                return self.tools[name]["handler"](**arguments)
            return f"工具 '{name}' 不存在"

        def read_resource(self, uri):
            for pattern, res in self.resources.items():
                # 简单匹配
                if uri.startswith(pattern.split("{")[0]):
                    return res["handler"](uri)
            return f"资源 '{uri}' 不存在"

    server = MockMCPServer("research-server")

    # 注册工具
    server.register_tool(
        "search_industry",
        "搜索行业信息",
        lambda industry: f"{industry}行业概况：市场规模持续增长"
    )
    server.register_tool(
        "search_company",
        "搜索公司信息",
        lambda company: f"{company}：行业龙头"
    )
    server.register_tool(
        "get_financial_data",
        "获取财务数据",
        lambda company: f"{company}财务数据：营收增长15%"
    )
    server.register_tool(
        "calculate",
        "数学计算",
        lambda expression: f"{expression} = {eval(expression)}"
    )

    # 注册资源
    server.register_resource(
        "industry://",
        "行业报告",
        lambda uri: f"{uri} 的详细报告..."
    )

    print("✅ Mock MCP Server 创建完成")
    print("   工具:")
    for tool in server.list_tools():
        print(f"   - {tool['name']}: {tool['description']}")
    print("   资源:")
    for res in server.list_resources():
        print(f"   - {res['uri']}: {res['description']}")

    return server


if __name__ == "__main__":
    server = create_mcp_server()
