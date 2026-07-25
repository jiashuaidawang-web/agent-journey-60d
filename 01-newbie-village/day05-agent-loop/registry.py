"""
Day 5: Tool Registry.

工具注册表：注册、查找、列出、执行工具。

Java 类比:
    ToolRegistry  ≈  Spring BeanFactory / ServiceLocator
    register()    ≈  @Bean / @Service 注册
    get()         ≈  ApplicationContext.getBean()
    execute()     ≈  反射调用方法
"""

from __future__ import annotations

from tool import Tool, ALL_TOOLS


class ToolRegistry:
    """工具注册表。

    管理所有可用工具，支持注册、查找、执行。
    """

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> "ToolRegistry":
        """注册一个工具。

        Args:
            tool: 工具实例

        Returns:
            self，支持链式调用
        """
        if tool.name in self._tools:
            print(f"⚠️ 工具 '{tool.name}' 已存在，将被覆盖")
        self._tools[tool.name] = tool
        return self

    def get(self, name: str) -> Tool | None:
        """根据名称查找工具。

        Args:
            name: 工具名称

        Returns:
            工具实例，不存在返回 None
        """
        return self._tools.get(name)

    def list(self) -> list[Tool]:
        """列出所有已注册工具。"""
        return list(self._tools.values())

    def list_names(self) -> list[str]:
        """列出所有工具名称。"""
        return list(self._tools.keys())

    def execute(self, name: str, arguments: dict) -> str:
        """执行指定工具。

        Args:
            name: 工具名称
            arguments: 工具参数

        Returns:
            执行结果

        Raises:
            ValueError: 工具不存在
        """
        tool = self.get(name)
        if tool is None:
            available = ", ".join(self.list_names())
            return f"错误: 工具 '{name}' 不存在。可用工具: [{available}]"

        try:
            return tool.execute(**arguments)
        except Exception as e:
            return f"工具 '{name}' 执行错误: {e}"

    def get_tools_definition(self) -> list[dict]:
        """获取所有工具的定义（OpenAI API 格式）。"""
        return [tool.to_openai_format() for tool in self.list()]

    def __len__(self) -> int:
        return len(self._tools)

    def __contains__(self, name: str) -> bool:
        return name in self._tools


def create_default_registry() -> ToolRegistry:
    """创建默认注册表，注册所有内置工具。"""
    registry = ToolRegistry()
    for tool in ALL_TOOLS:
        registry.register(tool)
    return registry


if __name__ == "__main__":
    # 测试
    registry = create_default_registry()

    print("=" * 60)
    print("Tool Registry 测试")
    print("=" * 60)

    print(f"\n已注册 {len(registry)} 个工具:")
    for name in registry.list_names():
        print(f"  🔧 {name}")

    # 测试执行
    print(f"\n{'─' * 40}")
    print("执行测试:")

    result = registry.execute("calculator", {"expression": "100 + 200 * 3"})
    print(f"  计算器: {result}")

    result = registry.execute("get_weather", {"city": "北京"})
    print(f"  天气: {result}")

    result = registry.execute("get_stock_price", {"stock": "贵州茅台"})
    print(f"  股票: {result}")

    # 测试不存在的工具
    result = registry.execute("nonexistent_tool", {})
    print(f"  不存在: {result}")
