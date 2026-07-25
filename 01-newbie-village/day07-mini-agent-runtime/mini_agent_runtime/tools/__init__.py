"""
================================================================================
Day 7 - Mini Agent Runtime - 工具系统 | mini_agent_runtime/tools/__init__.py
================================================================================

【学习目标】
理解 Tool 系统：Tool 基类 + ToolRegistry

【前置知识】
- model/__init__.py（模型抽象）

【代码结构】
- Tool: 抽象基类
- CalculatorTool/WeatherTool/StockTool: 具体工具
- ToolRegistry: 注册表

================================================================================
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod


class Tool(ABC):
    """工具基类。"""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def description(self) -> str: ...

    @property
    @abstractmethod
    def parameters(self) -> dict: ...

    @abstractmethod
    def execute(self, **kwargs) -> str: ...

    def to_openai_format(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }


class CalculatorTool(Tool):
    """计算器。"""

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "执行数学计算（加减乘除）。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "数学表达式"}
            },
            "required": ["expression"],
        }

    def execute(self, **kwargs) -> str:
        expression = kwargs.get("expression", "")
        try:
            if not re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expression):
                return f"错误: 不支持的表达式"
            result = eval(expression)
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"


class WeatherTool(Tool):
    """天气查询（模拟）。"""

    MOCK = {
        "北京": "晴，25°C",
        "上海": "多云，28°C",
        "深圳": "雷阵雨，30°C",
    }

    @property
    def name(self) -> str:
        return "get_weather"

    @property
    def description(self) -> str:
        return "获取城市天气。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {"city": {"type": "string", "description": "城市名"}},
            "required": ["city"],
        }

    def execute(self, **kwargs) -> str:
        city = kwargs.get("city", "")
        if city in self.MOCK:
            return f"{city}今天{self.MOCK[city]}"
        return f"暂无{city}天气数据"


class StockTool(Tool):
    """股票查询（模拟）。"""

    MOCK = {
        "贵州茅台": "1680元，+1.5%",
        "宁德时代": "210元，-0.8%",
    }

    @property
    def name(self) -> str:
        return "get_stock_price"

    @property
    def description(self) -> str:
        return "获取股票价格。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {"stock": {"type": "string", "description": "股票名"}},
            "required": ["stock"],
        }

    def execute(self, **kwargs) -> str:
        stock = kwargs.get("stock", "")
        if stock in self.MOCK:
            return f"{stock} 当前{self.MOCK[stock]}"
        return f"暂无{stock}行情"


class ToolRegistry:
    """工具注册表。"""

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> "ToolRegistry":
        self._tools[tool.name] = tool
        return self

    def get(self, name: str) -> Tool | None:
        return self._tools.get(name)

    def list(self) -> list[Tool]:
        return list(self._tools.values())

    def execute(self, name: str, arguments: dict) -> str:
        tool = self.get(name)
        if tool is None:
            return f"错误: 工具 '{name}' 不存在"
        try:
            return tool.execute(**arguments)
        except Exception as e:
            return f"工具执行错误: {e}"

    def get_tools_definition(self) -> list[dict]:
        return [t.to_openai_format() for t in self.list()]

    def __len__(self) -> int:
        return len(self._tools)

    def __contains__(self, name: str) -> bool:
        return name in self._tools


def create_default_registry() -> ToolRegistry:
    """创建默认注册表。"""
    registry = ToolRegistry()
    registry.register(CalculatorTool())
    registry.register(WeatherTool())
    registry.register(StockTool())
    return registry
