"""
Day 28: Supervisor Demo.

演示 Supervisor 模式的多 Agent 协调。

Usage:
    python supervisor_demo.py
"""


class WorkerAgent:
    """工作 Agent。"""

    def __init__(self, name: str, capability: str):
        self.name = name
        self.capability = capability

    def execute(self, task: str) -> str:
        return f"[{self.name}] 完成: {task}"


class SupervisorAgent:
    """协调 Agent。"""

    def __init__(self):
        self.workers: list[WorkerAgent] = []

    def add_worker(self, worker: WorkerAgent):
        self.workers.append(worker)

    def assign_task(self, task: str, capability: str = None) -> str:
        """分配任务给合适的 Worker。"""
        if capability:
            for worker in self.workers:
                if worker.capability == capability:
                    return worker.execute(task)
        # 默认分配给第一个可用的 Worker
        if self.workers:
            return self.workers[0].execute(task)
        return "没有可用的 Worker"

    def execute_parallel(self, tasks: list[tuple[str, str]]) -> list[str]:
        """并行执行多个任务。"""
        results = []
        for task, capability in tasks:
            result = self.assign_task(task, capability)
            results.append(result)
        return results

    def execute_pipeline(self, task: str, pipeline: list[str]) -> str:
        """流水线执行：依次经过多个 Worker。"""
        result = task
        for capability in pipeline:
            result = self.assign_task(result, capability)
        return result


def supervisor_demo():
    """Supervisor 演示。"""
    print("=" * 60)
    print("Supervisor Demo")
    print("=" * 60)

    # 创建 Supervisor
    supervisor = SupervisorAgent()

    # 添加 Worker
    supervisor.add_worker(WorkerAgent("researcher", "research"))
    supervisor.add_worker(WorkerAgent("analyst", "analyze"))
    supervisor.add_worker(WorkerAgent("reporter", "report"))

    print(f"\n✅ Supervisor 创建完成，{len(supervisor.workers)} 个 Worker")

    # 单个任务
    print(f"\n📋 单个任务:")
    result = supervisor.assign_task("研究白酒行业", "research")
    print(f"   {result}")

    # 并行任务
    print(f"\n📋 并行任务:")
    tasks = [
        ("研究白酒行业", "research"),
        ("分析财务数据", "analyze"),
        ("生成报告", "report"),
    ]
    results = supervisor.execute_parallel(tasks)
    for result in results:
        print(f"   {result}")

    # 流水线
    print(f"\n📋 流水线:")
    pipeline = ["research", "analyze", "report"]
    result = supervisor.execute_pipeline("白酒行业研究", pipeline)
    print(f"   {result}")


if __name__ == "__main__":
    supervisor_demo()
