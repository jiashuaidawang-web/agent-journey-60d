"""
Day 32: Metrics Demo.

演示 Agent 系统的指标统计。

Usage:
    python metrics_demo.py
"""


class TokenCounter:
    """Token 计数器。"""

    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.call_count = 0

    def add(self, input_tokens: int, output_tokens: int):
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_tokens += input_tokens + output_tokens
        self.call_count += 1

    @property
    def average_tokens_per_call(self):
        return self.total_tokens / self.call_count if self.call_count > 0 else 0

    def to_dict(self):
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "call_count": self.call_count,
            "average_tokens_per_call": self.average_tokens_per_call,
        }


class CostCalculator:
    """成本计算器。"""

    # 每 1K Token 的价格（美元）
    PRICES = {
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
        "gpt-4o": {"input": 0.0025, "output": 0.01},
        "deepseek-chat": {"input": 0.00014, "output": 0.00028},
    }

    @classmethod
    def calculate(cls, model: str, input_tokens: int, output_tokens: int) -> float:
        prices = cls.PRICES.get(model, cls.PRICES["gpt-4o-mini"])
        cost = (input_tokens / 1000) * prices["input"] + (output_tokens / 1000) * prices["output"]
        return cost


class LatencyTracker:
    """延迟追踪。"""

    def __init__(self):
        self.latencies: list[float] = []

    def add(self, latency: float):
        self.latencies.append(latency)

    @property
    def average(self):
        return sum(self.latencies) / len(self.latencies) if self.latencies else 0

    @property
    def p95(self):
        if not self.latencies:
            return 0
        sorted_latencies = sorted(self.latencies)
        idx = int(len(sorted_latencies) * 0.95)
        return sorted_latencies[idx]

    @property
    def p99(self):
        if not self.latencies:
            return 0
        sorted_latencies = sorted(self.latencies)
        idx = int(len(sorted_latencies) * 0.99)
        return sorted_latencies[idx]

    def to_dict(self):
        return {
            "average": self.average,
            "p95": self.p95,
            "p99": self.p99,
            "count": len(self.latencies),
        }


def metrics_demo():
    """指标统计演示。"""
    print("=" * 60)
    print("Metrics Demo")
    print("=" * 60)

    # Token 统计
    print("\n📊 Token 统计:")
    counter = TokenCounter()

    # 模拟多次调用
    calls = [
        (100, 200),
        (150, 300),
        (80, 150),
        (200, 400),
    ]

    for input_t, output_t in calls:
        counter.add(input_t, output_t)

    token_data = counter.to_dict()
    print(f"   Input Tokens: {token_data['input_tokens']}")
    print(f"   Output Tokens: {token_data['output_tokens']}")
    print(f"   Total Tokens: {token_data['total_tokens']}")
    print(f"   调用次数: {token_data['call_count']}")
    print(f"   平均 Token/Call: {token_data['average_tokens_per_call']:.1f}")

    # 成本计算
    print("\n💰 成本计算:")
    for model in ["gpt-4o-mini", "gpt-4o", "deepseek-chat"]:
        cost = CostCalculator.calculate(model, counter.input_tokens, counter.output_tokens)
        print(f"   {model}: ${cost:.4f}")

    # 延迟统计
    print("\n⏱️ 延迟统计:")
    latency = LatencyTracker()

    import random
    for _ in range(100):
        latency.add(random.uniform(0.5, 3.0))

    latency_data = latency.to_dict()
    print(f"   平均延迟: {latency_data['average']:.2f}s")
    print(f"   P95 延迟: {latency_data['p95']:.2f}s")
    print(f"   P99 延迟: {latency_data['p99']:.2f}s")


if __name__ == "__main__":
    metrics_demo()
