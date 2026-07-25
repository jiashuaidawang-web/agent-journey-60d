"""
Day 29: Router Demo.

演示 Router 模式的多 Agent 路由。

Usage:
    python router_demo.py
"""


class Agent:
    """Agent。"""

    def __init__(self, name: str, domain: str):
        self.name = name
        self.domain = domain

    def handle(self, query: str) -> str:
        return f"[{self.name}] 处理: {query}"


class Router:
    """路由器。"""

    def __init__(self):
        self.agents: dict[str, Agent] = {}

    def register(self, domain: str, agent: Agent):
        self.agents[domain] = agent

    def detect_domain(self, query: str) -> str:
        """意图识别（简化版）。"""
        # 实际场景使用 LLM 识别
        if any(word in query for word in ["天气", "气温", "下雨"]):
            return "weather"
        elif any(word in query for word in ["股票", "股价", "行情"]):
            return "stock"
        elif any(word in query for word in ["计算", "数学", "+", "-", "*", "/"]):
            return "calculator"
        return "unknown"

    def route(self, query: str) -> str:
        """路由到合适的 Agent。"""
        domain = self.detect_domain(query)
        agent = self.agents.get(domain)
        if agent:
            return agent.handle(query)
        return f"没有找到能处理 '{domain}' 的 Agent"


def router_demo():
    """Router 演示。"""
    print("=" * 60)
    print("Router Demo")
    print("=" * 60)

    # 创建 Router
    router = Router()

    # 注册 Agent
    router.register("weather", Agent("weather_agent", "天气"))
    router.register("stock", Agent("stock_agent", "股票"))
    router.register("calculator", Agent("calculator_agent", "计算"))

    print(f"\n✅ Router 创建完成，{len(router.agents)} 个 Agent")

    # 路由测试
    queries = [
        "今天北京天气怎么样",
        "贵州茅台股价多少",
        "计算 123 * 456",
    ]

    print(f"\n🔄 路由测试:")
    for query in queries:
        result = router.route(query)
        print(f"   查询: '{query}'")
        print(f"   结果: {result}")


if __name__ == "__main__":
    router_demo()
