"""
================================================================================
Day 4 - 工具定义与实现 | 00_tool.py
================================================================================

【学习目标】
实现 3 个工具：CalculatorTool / WeatherTool / StockTool

【前置知识】
- Day 1 LLM Foundation
- Day 2 Structured Output

【操作步骤】
1. 运行: python 00_tool.py
2. 观察输出：工具列表 + 工具测试

【预期输出】
工具列表
============================================================
🔧 calculator
   描述: 执行数学计算。支持加减乘除（+ - * /）和幂运算（**）。
   参数: {"type": "object", "properties": {"expression": {"type": "string", ...}}}

🔧 get_weather
   描述: 获取指定城市的天气信息...
   参数: {"type": "object", "properties": {"city": {"type": "string", ...}}}

🔧 get_stock_price
   描述: 获取指定股票的当前价格...
   参数: {"type": "object", "properties": {"stock": {"type": "string", ...}}}

工具测试
============================================================
计算器: 123 * 456 = 56088
天气: 北京今天晴，气温25°C，湿度40%
股票: 贵州茅台 当前价格: 1680元，涨跌幅: +1.5%，PE: 30

【验证标准】
□ 能看到工具列表
□ 能看到工具测试结果
□ 理解 Tool 基类的抽象（name/description/parameters/execute）

【代码要点】
- Tool: 抽象基类（定义接口）
- CalculatorTool/WeatherTool/StockTool: 具体实现
- to_openai_format(): 转换为 OpenAI API 格式

================================================================================
"""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod


class Tool(ABC):
    """工具基类。

    所有工具必须实现 name / description / parameters / execute。
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """工具名称（唯一标识）。"""
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        """工具描述（LLM 根据这个决定什么时候调用）。"""
        ...

    @property
    @abstractmethod
    def parameters(self) -> dict:
        """参数 Schema（JSON Schema 格式）。"""
        ...

    @abstractmethod
    def execute(self, **kwargs) -> str:
        """执行工具。

        Args:
            **kwargs: 工具参数

        Returns:
            执行结果（字符串）
        """
        ...

    def to_openai_format(self) -> dict:
        """转换为 OpenAI API 的 tools 格式。"""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }


class CalculatorTool(Tool):
    """计算器工具。

    支持加减乘除和幂运算。
    """

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "执行数学计算。支持加减乘除（+ - * /）和幂运算（**）。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式，如 '123 * 456' 或 '100 + 200 / 2'",
                }
            },
            "required": ["expression"],
        }

    def execute(self, **kwargs) -> str:
        expression = kwargs.get("expression", "")
        try:
            # 安全计算：只允许数字和运算符
            if not re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expression):
                return f"错误: 不支持的表达式 '{expression}'"

            result = eval(expression)
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"


class WeatherTool(Tool):
    """天气查询工具（模拟）。"""

    MOCK_WEATHER = {
        "北京": {"temp": 25, "weather": "晴", "humidity": 40},
        "上海": {"temp": 28, "weather": "多云", "humidity": 65},
        "深圳": {"temp": 30, "weather": "雷阵雨", "humidity": 80},
        "杭州": {"temp": 26, "weather": "阴", "humidity": 55},
    }

    @property
    def name(self) -> str:
        return "get_weather"

    @property
    def description(self) -> str:
        return "获取指定城市的天气信息，包括温度、天气状况、湿度。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称，如 '北京'、'上海'",
                }
            },
            "required": ["city"],
        }

    def execute(self, **kwargs) -> str:
        city = kwargs.get("city", "")

        if city in self.MOCK_WEATHER:
            data = self.MOCK_WEATHER[city]
            return f"{city}今天{data['weather']}，气温{data['temp']}°C，湿度{data['humidity']}%"
        else:
            return f"暂无{city}的天气数据。支持的城市：{', '.join(self.MOCK_WEATHER.keys())}"


class StockTool(Tool):
    """股票查询工具（模拟）。"""

    MOCK_STOCKS = {
        "贵州茅台": {"price": 1680, "change": "+1.5%", "pe": 30},
        "宁德时代": {"price": 210, "change": "-0.8%", "pe": 25},
        "比亚迪": {"price": 280, "change": "+2.1%", "pe": 20},
        "腾讯控股": {"price": 380, "change": "+0.5%", "pe": 18},
    }

    @property
    def name(self) -> str:
        return "get_stock_price"

    @property
    def description(self) -> str:
        return "获取指定股票的当前价格、涨跌幅和市盈率（PE）。"

    @property
    def parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "stock": {
                    "type": "string",
                    "description": "股票名称，如 '贵州茅台'、'宁德时代'",
                }
            },
            "required": ["stock"],
        }

    def execute(self, **kwargs) -> str:
        stock = kwargs.get("stock", "")

        if stock in self.MOCK_STOCKS:
            data = self.MOCK_STOCKS[stock]
            return (
                f"{stock} 当前价格: {data['price']}元，"
                f"涨跌幅: {data['change']}，PE: {data['pe']}"
            )
        else:
            return f"暂无{stock}的行情数据。支持的股票：{', '.join(self.MOCK_STOCKS.keys())}"


# 工具注册表（简单版）
ALL_TOOLS = [
    CalculatorTool(),
    WeatherTool(),
    StockTool(),
]


if __name__ == "__main__":
    print("=" * 60)
    print("工具列表")
    print("=" * 60)

    for tool in ALL_TOOLS:
        print(f"\n🔧 {tool.name}")
        print(f"   描述: {tool.description}")
        print(f"   参数: {json.dumps(tool.parameters, ensure_ascii=False, indent=4)}")

    # 测试执行
    print(f"\n{'=' * 60}")
    print("工具测试")
    print(f"{'=' * 60}")

    calc = CalculatorTool()
    print(f"\n计算器: {calc.execute(expression='123 * 456')}")

    weather = WeatherTool()
    print(f"天气: {weather.execute(city='北京')}")

    stock = StockTool()
    print(f"股票: {stock.execute(stock='贵州茅台')}")
