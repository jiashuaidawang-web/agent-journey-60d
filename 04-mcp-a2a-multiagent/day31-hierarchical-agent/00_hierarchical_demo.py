"""
Day 31: Hierarchical Agent Demo.

演示层级结构的多 Agent 协作。

Usage:
    python hierarchical_demo.py
"""


class Worker:
    """底层工作者。"""

    def __init__(self, name: str):
        self.name = name

    def work(self, task: str) -> str:
        return f"  [{self.name}] 完成: {task}"


class Manager:
    """中层管理者。"""

    def __init__(self, name: str):
        self.name = name
        self.workers: list[Worker] = []

    def add_worker(self, worker: Worker):
        self.workers.append(worker)

    def handle(self, task: str) -> list[str]:
        print(f"[{self.name}] 分配任务: {task}")
        results = []
        for worker in self.workers:
            result = worker.work(f"{task} (由{self.name}分配)")
            results.append(result)
        return results


class TopManager:
    """顶层管理者。"""

    def __init__(self):
        self.managers: list[Manager] = []

    def add_manager(self, manager: Manager):
        self.managers.append(manager)

    def execute(self, task: str) -> dict:
        """执行复杂任务。"""
        print(f"[TopManager] 接收任务: {task}")
        print(f"[TopManager] 分配给 {len(self.managers)} 个 Manager\n")

        all_results = {}
        for manager in self.managers:
            results = manager.handle(task)
            all_results[manager.name] = results

        return all_results


def hierarchical_demo():
    """层级 Agent 演示。"""
    print("=" * 60)
    print("Hierarchical Agent Demo")
    print("=" * 60)

    # 创建顶层 Manager
    top = TopManager()

    # 创建中层 Manager
    research_manager = Manager("研究经理")
    research_manager.add_worker(Worker("研究员A"))
    research_manager.add_worker(Worker("研究员B"))

    analysis_manager = Manager("分析经理")
    analysis_manager.add_worker(Worker("分析师A"))
    analysis_manager.add_worker(Worker("分析师B"))

    report_manager = Manager("报告经理")
    report_manager.add_worker(Worker("报告员"))

    # 添加到顶层
    top.add_manager(research_manager)
    top.add_manager(analysis_manager)
    top.add_manager(report_manager)

    # 执行任务
    task = "完成白酒行业研究报告"
    results = top.execute(task)

    print("\n📊 执行结果:")
    for manager_name, manager_results in results.items():
        print(f"\n   {manager_name}:")
        for result in manager_results:
            print(f"   {result}")


if __name__ == "__main__":
    hierarchical_demo()
