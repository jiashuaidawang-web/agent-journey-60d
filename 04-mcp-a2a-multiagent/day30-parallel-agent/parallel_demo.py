"""
Day 30: Parallel Agent Demo.

演示并行执行的多个 Agent。

Usage:
    python parallel_demo.py
"""


class Agent:
    """Agent。"""

    def __init__(self, name: str):
        self.name = name

    def execute(self, task: str) -> str:
        return f"[{self.name}] 完成: {task}"


class ParallelAgentManager:
    """并行 Agent 管理器。"""

    def __init__(self):
        self.agents: list[Agent] = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def execute_parallel(self, tasks: list[str]) -> list[str]:
        """并行执行多个任务。"""
        if len(tasks) > len(self.agents):
            tasks = tasks[:len(self.agents)]

        results = []
        for agent, task in zip(self.agents, tasks):
            result = agent.execute(task)
            results.append(result)

        return results

    def execute_with_aggregation(self, tasks: list[str]) -> dict:
        """并行执行 + 结果汇总。"""
        results = self.execute_parallel(tasks)

        return {
            "results": results,
            "summary": f"共完成 {len(results)} 个任务",
            "status": "success",
        }


def parallel_demo():
    """并行 Agent 演示。"""
    print("=" * 60)
    print("Parallel Agent Demo")
    print("=" * 60)

    # 创建管理器
    manager = ParallelAgentManager()

    # 添加 Agent
    manager.add_agent(Agent("researcher"))
    manager.add_agent(Agent("analyst"))
    manager.add_agent(Agent("reporter"))

    print(f"\n✅ 创建 {len(manager.agents)} 个 Agent")

    # 并行执行
    tasks = [
        "研究白酒行业",
        "分析财务数据",
        "生成投资报告",
    ]

    print(f"\n🔄 并行执行 {len(tasks)} 个任务:")
    results = manager.execute_parallel(tasks)
    for result in results:
        print(f"   {result}")

    # 带汇总
    print(f"\n📊 带汇总:")
    result = manager.execute_with_aggregation(tasks)
    print(f"   {result['summary']}")
    print(f"   状态: {result['status']}")


if __name__ == "__main__":
    parallel_demo()
