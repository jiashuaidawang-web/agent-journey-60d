"""
Day 27: A2A Demo.

演示 A2A（Agent-to-Agent）协议。

Usage:
    python a2a_demo.py
"""


class AgentCard:
    """Agent 能力描述。"""

    def __init__(self, name: str, description: str, capabilities: list[str]):
        self.name = name
        self.description = description
        self.capabilities = capabilities

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "capabilities": self.capabilities,
        }


class Task:
    """任务。"""

    def __init__(self, task_id: str, input_data: dict):
        self.task_id = task_id
        self.input_data = input_data
        self.output_data = None
        self.status = "pending"

    def complete(self, output_data):
        self.output_data = output_data
        self.status = "completed"


class A2AAgent:
    """A2A Agent。"""

    def __init__(self, name: str, description: str, capabilities: list[str]):
        self.card = AgentCard(name, description, capabilities)
        self.handlers = {}

    def register_handler(self, capability: str, handler):
        """注册能力处理器。"""
        self.handlers[capability] = handler

    def can_handle(self, capability: str) -> bool:
        return capability in self.capabilities

    def execute(self, task: Task):
        """执行任务。"""
        capability = task.input_data.get("capability")
        if capability not in self.handlers:
            task.status = "failed"
            return task

        result = self.handlers[capability](**task.input_data.get("args", {}))
        task.complete(result)
        return task


class A2ARegistry:
    """A2A 注册中心。"""

    def __init__(self):
        self.agents: dict[str, A2AAgent] = {}

    def register(self, agent: A2AAgent):
        self.agents[agent.card.name] = agent

    def find_agent(self, capability: str) -> A2AAgent | None:
        """根据能力查找 Agent。"""
        for agent in self.agents.values():
            if agent.can_handle(capability):
                return agent
        return None

    def list_agents(self):
        return [agent.card.to_dict() for agent in self.agents.values()]


def a2a_demo():
    """A2A 演示。"""
    print("=" * 60)
    print("A2A Demo")
    print("=" * 60)

    # 创建 Registry
    registry = A2ARegistry()

    # 创建 Agent 1：研究员
    researcher = A2AAgent(
        "researcher",
        "负责搜索和研究",
        ["search", "research"]
    )
    researcher.register_handler("search", lambda query: f"搜索结果: {query}")
    researcher.register_handler("research", lambda topic: f"研究报告: {topic}")

    # 创建 Agent 2：分析师
    analyst = A2AAgent(
        "analyst",
        "负责数据分析和报告",
        ["analyze", "report"]
    )
    analyst.register_handler("analyze", lambda data: f"分析结果: {data}")
    analyst.register_handler("report", lambda findings: f"报告: {findings}")

    # 注册到 Registry
    registry.register(researcher)
    registry.register(analyst)

    print(f"\n📋 注册 Agent:")
    for agent_info in registry.list_agents():
        print(f"   - {agent_info['name']}: {agent_info['description']}")
        print(f"     能力: {agent_info['capabilities']}")

    # 协作：研究员搜索 → 分析师分析
    print(f"\n🔄 Agent 协作:")

    # 研究员搜索
    task1 = Task("task_001", {"capability": "search", "args": {"query": "白酒龙头"}})
    agent = registry.find_agent("search")
    if agent:
        agent.execute(task1)
        print(f"   研究员搜索: {task1.output_data}")

    # 分析师分析
    task2 = Task("task_002", {"capability": "analyze", "args": {"data": task1.output_data}})
    agent = registry.find_agent("analyze")
    if agent:
        agent.execute(task2)
        print(f"   分析师分析: {task2.output_data}")

    print("\n✅ A2A 演示完成")


if __name__ == "__main__":
    a2a_demo()
