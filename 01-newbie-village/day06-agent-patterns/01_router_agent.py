"""
================================================================================
Day 6 - Router Agent | 01_router_agent.py
================================================================================

【学习目标】
实现 Router Agent：根据意图分发到不同的子 Agent

【前置知识】
- 00_react_agent.py（ReAct 模式）

【操作步骤】
1. 运行: python 01_router_agent.py
2. 观察输出：路由执行过程

【预期输出】
Router Agent 启动
============================================================
📝 用户输入: 今天北京天气怎么样

🔍 识别意图...
   意图: weather

🔀 路由到子 Agent...
   分发到: weather (处理天气查询)

⚙️ 子 Agent 处理中...
✅ 结果: 北京今天晴，气温25°C，湿度40%

【验证标准】
□ 能看到意图识别
□ 能看到路由分发
□ 能看到子 Agent 处理
□ 理解 Router 模式的核心思想

【代码要点】
- SubAgent: 子 Agent 基类
- RouterAgent: 路由器（意图识别 + 分发）
- can_handle(): 判断能否处理
- handle(): 处理请求

================================================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from registry import create_default_registry
from utils.Model_config import ModelConfig


class SubAgent:
    """子 Agent 基类。"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def can_handle(self, intent: str) -> bool:
        """是否能处理该意图。"""
        raise NotImplementedError

    def handle(self, user_input: str, client, config) -> str:
        """处理用户请求。"""
        raise NotImplementedError


class WeatherAgent(SubAgent):
    """天气子 Agent。"""

    def __init__(self):
        super().__init__("weather", "处理天气查询")
        self.registry = create_default_registry()

    def can_handle(self, intent: str) -> bool:
        return intent in ("weather", "天气")

    def handle(self, user_input: str, client, config) -> str:
        # 直接调用天气工具
        result = self.registry.execute("get_weather", {"city": self._extract_city(user_input)})
        return result

    def _extract_city(self, text: str) -> str:
        """简单提取城市名（实际应该用 LLM）。"""
        # 模拟：默认北京
        return "北京"


class StockAgent(SubAgent):
    """股票子 Agent。"""

    def __init__(self):
        super().__init__("stock", "处理股票查询")
        self.registry = create_default_registry()

    def can_handle(self, intent: str) -> bool:
        return intent in ("stock_analysis", "stock", "股票")

    def handle(self, user_input: str, client, config) -> str:
        result = self.registry.execute("get_stock_price", {"stock": "贵州茅台"})
        return result


class CalculatorAgent(SubAgent):
    """计算子 Agent。"""

    def __init__(self):
        super().__init__("calculator", "处理数学计算")
        self.registry = create_default_registry()

    def can_handle(self, intent: str) -> bool:
        return intent in ("calculation", "calculate", "计算")

    def handle(self, user_input: str, client, config) -> str:
        result = self.registry.execute("calculator", {"expression": "1 + 1"})
        return result


class RouterAgent:
    """路由器 Agent。

    流程：
    1. 识别用户意图
    2. 分发到对应的子 Agent
    3. 子 Agent 处理并返回结果
    """

    def __init__(self):
        self.sub_agents: list[SubAgent] = [
            WeatherAgent(),
            StockAgent(),
            CalculatorAgent(),
        ]

    def route(self, intent: str) -> SubAgent | None:
        """根据意图路由到子 Agent。"""
        for agent in self.sub_agents:
            if agent.can_handle(intent):
                return agent
        return None

    def detect_intent(self, user_input: str, client, config) -> str:
        """识别用户意图。"""
        system_prompt = """你是一个意图识别器。根据用户输入，识别其意图。

支持的意图：
- weather: 天气查询
- stock_analysis: 股票分析
- calculation: 数学计算
- unknown: 未知意图

只输出意图名称，不要解释。"""

        response = client.chat.completions.create(
            model=config.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.0,
            max_tokens=32,
        )

        intent = response.choices[0].message.content.strip().lower()
        return intent

    def run(self, user_input: str) -> str:
        """运行 Router Agent。"""
        try:
            from openai import OpenAI
        except ImportError:
            print("❌ 请先安装依赖: pip install openai")
            sys.exit(1)

        config = ModelConfig.from_env()
        client = OpenAI(**config.get_client_kwargs())

        print("=" * 60)
        print("Router Agent 启动")
        print("=" * 60)
        print(f"📝 用户输入: {user_input}\n")

        # 1. 识别意图
        print("🔍 识别意图...")
        intent = self.detect_intent(user_input, client, config)
        print(f"   意图: {intent}\n")

        # 2. 路由到子 Agent
        print("🔀 路由到子 Agent...")
        sub_agent = self.route(intent)

        if sub_agent is None:
            return f"❌ 没有找到能处理意图 '{intent}' 的 Agent"

        print(f"   分发到: {sub_agent.name} ({sub_agent.description})\n")

        # 3. 子 Agent 处理
        print("⚙️ 子 Agent 处理中...")
        result = sub_agent.handle(user_input, client, config)

        print(f"✅ 结果: {result}")
        return result


def main():
    router = RouterAgent()

    test_cases = [
        "今天北京天气怎么样",
        "帮我分析贵州茅台",
        "计算 123 * 456",
    ]

    for task in test_cases:
        result = router.run(task)
        print(f"\n{'=' * 60}\n")


if __name__ == "__main__":
    main()
