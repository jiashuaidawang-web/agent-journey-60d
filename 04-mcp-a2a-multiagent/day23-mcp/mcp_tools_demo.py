"""
Day 23: MCP Tools Demo.

演示 MCP Tools 的完整定义和调用。

Usage:
    python mcp_tools_demo.py
"""


def mcp_tools_demo():
    """MCP Tools 演示。"""
    print("=" * 60)
    print("MCP Tools Demo")
    print("=" * 60)

    # MCP Tool 定义（JSON Schema 格式）
    mcp_tools = [
        {
            "name": "get_weather",
            "description": "获取指定城市的实时天气信息，包括温度、天气状况、湿度",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如 '北京'、'上海'",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "温度单位",
                    },
                },
                "required": ["city"],
            },
        },
        {
            "name": "search_stock",
            "description": "搜索股票信息，获取实时行情",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词（股票名称或代码）",
                    },
                    "market": {
                        "type": "string",
                        "enum": ["SH", "SZ", "HK", "US"],
                        "description": "市场",
                    },
                },
                "required": ["query"],
            },
        },
        {
            "name": "calculate",
            "description": "执行数学计算，支持加减乘除和幂运算",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，如 '123 * 456'",
                    }
                },
                "required": ["expression"],
            },
        },
    ]

    print("\n📋 MCP Tools 定义:")
    for tool in mcp_tools:
        print(f"\n   🔧 {tool['name']}")
        print(f"      描述: {tool['description']}")
        print(f"      参数: {list(tool['inputSchema']['properties'].keys())}")

    # MCP Server 响应格式
    print(f"\n📤 MCP Server 响应格式示例:")
    response_example = {
        "jsonrpc": "2.0",
        "id": "req_001",
        "result": {
            "content": [
                {
                    "type": "text",
                    "text": "北京今天晴，25°C",
                }
            ],
        },
    }
    print(f"   {response_example}")

    # MCP 调用流程
    print(f"\n🔄 MCP 调用流程:")
    print("   1. Client 发送 tools/list 请求")
    print("   2. Server 返回工具列表")
    print("   3. LLM 决定调用某个工具")
    print("   4. Client 发送 tools/call 请求")
    print("   5. Server 执行工具并返回结果")

    return mcp_tools


if __name__ == "__main__":
    mcp_tools_demo()
