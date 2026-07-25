"""
Day 36: Cost Tracker.

演示成本核算（Java 控制平面核心功能）。

Usage:
    python cost_tracker.py
"""


from datetime import datetime


class UsageRecord:
    """使用记录。"""

    def __init__(self, tenant_id: str, model: str, input_tokens: int,
                 output_tokens: int, latency_ms: int):
        self.tenant_id = tenant_id
        self.model = model
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.latency_ms = latency_ms
        self.cost = self._calculate_cost()
        self.timestamp = datetime.now()

    def _calculate_cost(self) -> float:
        """计算成本。"""
        # 每 1K Token 价格（美元）
        prices = {
            "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
            "gpt-4o": {"input": 0.0025, "output": 0.01},
            "deepseek-chat": {"input": 0.00014, "output": 0.00028},
        }
        price = prices.get(self.model, prices["gpt-4o-mini"])
        cost = (self.input_tokens / 1000) * price["input"] + \
               (self.output_tokens / 1000) * price["output"]
        return cost


class CostTracker:
    """成本追踪器。"""

    def __init__(self):
        self.records: list[UsageRecord] = []

    def record(self, tenant_id: str, model: str, input_tokens: int,
               output_tokens: int, latency_ms: int):
        """记录使用。"""
        record = UsageRecord(tenant_id, model, input_tokens, output_tokens, latency_ms)
        self.records.append(record)
        return record

    def get_tenant_cost(self, tenant_id: str) -> dict:
        """获取租户成本。"""
        tenant_records = [r for r in self.records if r.tenant_id == tenant_id]

        return {
            "tenant_id": tenant_id,
            "total_cost": sum(r.cost for r in tenant_records),
            "total_tokens": sum(r.input_tokens + r.output_tokens for r in tenant_records),
            "total_calls": len(tenant_records),
            "avg_latency_ms": (
                sum(r.latency_ms for r in tenant_records) / len(tenant_records)
                if tenant_records else 0
            ),
        }

    def get_model_cost(self) -> dict:
        """按模型统计成本。"""
        model_costs = {}
        for record in self.records:
            if record.model not in model_costs:
                model_costs[record.model] = {"cost": 0, "calls": 0}
            model_costs[record.model]["cost"] += record.cost
            model_costs[record.model]["calls"] += 1
        return model_costs

    def get_daily_cost(self) -> dict:
        """按天统计成本。"""
        daily = {}
        for record in self.records:
            day = record.timestamp.strftime("%Y-%m-%d")
            if day not in daily:
                daily[day] = 0
            daily[day] += record.cost
        return daily


def cost_tracker_demo():
    """成本核算演示。"""
    print("=" * 60)
    print("Cost Tracker Demo")
    print("=" * 60)

    tracker = CostTracker()

    # 模拟使用记录
    print("\n📊 记录使用:")
    usages = [
        ("tenant_001", "gpt-4o-mini", 1000, 500, 1200),
        ("tenant_001", "gpt-4o", 2000, 1000, 2500),
        ("tenant_002", "deepseek-chat", 1500, 800, 1800),
        ("tenant_002", "gpt-4o-mini", 800, 400, 1000),
        ("tenant_003", "gpt-4o", 5000, 2000, 3500),
    ]

    for tenant_id, model, input_t, output_t, latency in usages:
        record = tracker.record(tenant_id, model, input_t, output_t, latency)
        print(f"   {tenant_id} | {model} | ${record.cost:.4f} | {latency}ms")

    # 租户成本
    print("\n💰 租户成本:")
    for tenant_id in ["tenant_001", "tenant_002", "tenant_003"]:
        cost_info = tracker.get_tenant_cost(tenant_id)
        print(f"   {tenant_id}:")
        print(f"     总成本: ${cost_info['total_cost']:.4f}")
        print(f"     总Token: {cost_info['total_tokens']:,}")
        print(f"     调用次数: {cost_info['total_calls']}")
        print(f"     平均延迟: {cost_info['avg_latency_ms']:.0f}ms")

    # 模型成本
    print("\n🤖 模型成本:")
    model_costs = tracker.get_model_cost()
    for model, info in model_costs.items():
        print(f"   {model}: ${info['cost']:.4f} ({info['calls']} 次调用)")


if __name__ == "__main__":
    cost_tracker_demo()
