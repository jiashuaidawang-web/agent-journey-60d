"""
Day 35: Async + MQ Demo.

演示 Agent 系统的异步处理。

Usage:
    python async_agent.py
"""


import asyncio
import uuid
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task:
    """任务。"""

    def __init__(self, input_data: dict):
        self.task_id = str(uuid.uuid4())
        self.input_data = input_data
        self.output_data = None
        self.status = TaskStatus.PENDING
        self.error = None
        self.created_at = asyncio.get_event_loop().time()

    def complete(self, output_data):
        self.output_data = output_data
        self.status = TaskStatus.COMPLETED

    def fail(self, error: str):
        self.error = error
        self.status = TaskStatus.FAILED


class TaskStore:
    """任务存储。"""

    def __init__(self):
        self.tasks: dict[str, Task] = {}

    def save(self, task: Task):
        self.tasks[task.task_id] = task

    def get(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)


class AsyncAgent:
    """异步 Agent。"""

    def __init__(self):
        self.task_store = TaskStore()

    async def submit(self, input_data: dict) -> str:
        """提交任务。"""
        task = Task(input_data)
        task.status = TaskStatus.PENDING
        self.task_store.save(task)

        # 异步执行
        asyncio.create_task(self._execute(task))

        return task.task_id

    async def _execute(self, task: Task):
        """执行任务。"""
        task.status = TaskStatus.RUNNING

        try:
            # 模拟长时间执行
            await asyncio.sleep(2)

            # 模拟结果
            result = f"处理完成: {task.input_data}"
            task.complete(result)
        except Exception as e:
            task.fail(str(e))

    async def get_result(self, task_id: str) -> Task | None:
        """获取结果。"""
        return self.task_store.get(task_id)


async def async_agent_demo():
    """异步 Agent 演示。"""
    print("=" * 60)
    print("Async Agent Demo")
    print("=" * 60)

    agent = AsyncAgent()

    # 提交任务
    print("\n📤 提交任务:")
    task_id = await agent.submit({"query": "分析贵州茅台"})
    print(f"   任务 ID: {task_id}")
    print(f"   状态: 已提交")

    # 轮询结果
    print("\n🔄 轮询结果:")
    for i in range(5):
        await asyncio.sleep(0.5)
        task = await agent.get_result(task_id)
        print(f"   第 {i+1} 次轮询: {task.status.value}")

        if task.status in (TaskStatus.COMPLETED, TaskStatus.FAILED):
            if task.status == TaskStatus.COMPLETED:
                print(f"   结果: {task.output_data}")
            break


if __name__ == "__main__":
    asyncio.run(async_agent_demo())
