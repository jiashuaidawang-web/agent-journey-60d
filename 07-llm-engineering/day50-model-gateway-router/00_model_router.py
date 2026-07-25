"""
Day 50: Model Router Demo.

演示模型路由。

Usage:
    python model_router.py
"""


class ModelInfo:
    """模型信息。"""

    def __init__(self, name: str, cost_per_1k: float, latency_ms: int,
                 capability: str, max_tokens: int):
        self.name = name
        self.cost_per_1k = cost_per_1k
        self.latency_ms = latency_ms
        self.capability = capability  # high, medium, low
        self.max_tokens = max_tokens


class ModelRouter:
    """模型路由器。"""

    def __init__(self):
        self.models: dict[str, ModelInfo] = {}
        self.default_model = None

    def register_model(self, model: ModelInfo):
        """注册模型。"""
        self.models[model.name] = model
        if self.default_model is None:
            self.default_model = model.name

    def route(self, task_complexity: str = "medium",
              cost_sensitive: bool = False,
              latency_sensitive: bool = False) -> str:
        """路由到合适的模型。"""
        if not self.models:
            return self.default_model

        # 根据任务复杂度选择
        if task_complexity == "high":
            candidates = [m for m in self.models.values() if m.capability == "high"]
        elif task_complexity == "low":
            candidates = [m for m in self.models.values() if m.capability == "low"]
        else:
            candidates = list(self.models.values())

        if not candidates:
            candidates = list(self.models.values())

        # 根据成本/延迟敏感度排序
        if cost_sensitive:
            candidates.sort(key=lambda m: m.cost_per_1k)
        elif latency_sensitive:
            candidates.sort(key=lambda m: m.latency_ms)

        return candidates[0].name if candidates else self.default_model

    def list_models(self) -> list[ModelInfo]:
        """列出所有模型。"""
        return list(self.models.values())


class ModelGateway:
    """模型网关。"""

    def __init__(self):
        self.router = ModelRouter()
        self.stats = {}

    def register_model(self, model: ModelInfo):
        """注册模型。"""
        self.router.register_model(model)

    def execute(self, prompt: str, task_complexity: str = "medium",
                cost_sensitive: bool = False) -> dict:
        """执行请求。"""
        # 路由到合适的模型
        model_name = self.router.route(task_complexity, cost_sensitive)

        # 模拟执行
        model = self.router.models[model_name]
        tokens = len(prompt.split()) * 2  # 模拟 token 数
        cost = tokens / 1000 * model.cost_per_1k

        # 统计
        if model_name not in self.stats:
            self.stats[model_name] = {"calls": 0, "tokens": 0, "cost": 0}
        self.stats[model_name]["calls"] += 1
        self.stats[model_name]["tokens"] += tokens
        self.stats[model_name]["cost"] += cost

        return {
            "model": model_name,
            "tokens": tokens,
            "cost": cost,
            "latency_ms": model.latency_ms,
        }

    def get_stats(self) -> dict:
        """获取统计。"""
        return self.stats


def model_router_demo():
    """模型路由演示。"""
    print("=" * 60)
    print("Model Router Demo")
    print("=" * 60)

    gateway = ModelGateway()

    # 注册模型
    gateway.register_model(ModelInfo("gpt-4o", 0.01, 2000, "high", 128000))
    gateway.register_model(ModelInfo("gpt-4o-mini", 0.00015, 500, "medium", 128000))
    gateway.register_model(ModelInfo("deepseek-chat", 0.00014, 800, "medium", 32000))

    print("\n📦 注册模型:")
    for model in gateway.router.list_models():
        print(f"   - {model.name}: ${model.cost_per_1k}/1K, {model.latency_ms}ms, {model.capability}")

    # 路由测试
    print("\n🔄 路由测试:")
    test_cases = [
        {"complexity": "high", "cost_sensitive": False, "desc": "复杂任务"},
        {"complexity": "low", "cost_sensitive": True, "desc": "简单任务，成本敏感"},
        {"complexity": "medium", "cost_sensitive": False, "desc": "中等任务"},
    ]

    for case in test_cases:
        model = gateway.router.route(case["complexity"], case["cost_sensitive"])
        print(f"   {case['desc']}: 路由到 {model}")

    # 执行测试
    print("\n📤 执行测试:")
    for case in test_cases:
        result = gateway.execute("分析贵州茅台股票", case["complexity"], case["cost_sensitive"])
        print(f"   {case['desc']}: {result['model']}, ${result['cost']:.6f}")

    # 统计
    print("\n📊 统计:")
    stats = gateway.get_stats()
    for model, stat in stats.items():
        print(f"   {model}: {stat['calls']} 次, {stat['tokens']} tokens, ${stat['cost']:.6f}")


if __name__ == "__main__":
    model_router_demo()
