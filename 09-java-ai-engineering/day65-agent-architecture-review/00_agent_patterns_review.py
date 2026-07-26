"""
Day 65: Agent 模式复习 - 9 种 Agent 模式的代码骨架

功能：
1. 9 种 Agent 模式的代码骨架
2. 每种模式的核心组件
3. 模式对比表

示例：
    python 00_agent_patterns_review.py
    python 00_agent_patterns_review.py --pattern react

实际实现需要：
- langchain / langgraph
- openai

作者：Agent Journey 60D
日期：Day 65
"""

import argparse
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional


class AgentPattern(Enum):
    """Agent 模式枚举"""
    REACT = "react"
    ROUTER = "router"
    PLAN_EXECUTE = "plan_execute"
    REFLECTION = "reflection"
    EVALUATOR_OPTIMIZER = "evaluator_optimizer"
    SUPERVISOR = "supervisor"
    HIERARCHICAL = "hierarchical"
    HUMAN_IN_LOOP = "human_in_loop"
    LONG_RUNNING = "long_running"


@dataclass
class AgentState:
    """Agent 状态"""
    messages: list[dict] = field(default_factory=list)
    current_step: str = ""
    result: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


class BaseAgent(ABC):
    """Agent 基类"""

    def __init__(self, name: str, pattern: AgentPattern):
        self.name = name
        self.pattern = pattern
        self.state = AgentState()

    @abstractmethod
    def run(self, user_input: str) -> str:
        """运行 Agent

        Args:
            user_input: 用户输入

        Returns:
            Agent 回复
        """
        pass

    def reset(self) -> None:
        """重置状态"""
        self.state = AgentState()


class ReActAgent(BaseAgent):
    """ReAct Agent - 推理 + 行动交替

    核心思想：Thought → Action → Observation 循环
    """

    def __init__(self):
        super().__init__("ReAct", AgentPattern.REACT)
        self.max_iterations = 10

    def run(self, user_input: str) -> str:
        # TODO: 实现 ReAct 循环
        # for i in range(self.max_iterations):
        #     thought = self._think(user_input)
        #     action = self._act(thought)
        #     observation = self._observe(action)
        #     if self._is_done(observation):
        #         return observation
        pass

    def _think(self, user_input: str) -> str:
        """思考"""
        pass

    def _act(self, thought: str) -> str:
        """行动"""
        pass

    def _observe(self, action: str) -> str:
        """观察"""
        pass

    def _is_done(self, observation: str) -> bool:
        """是否完成"""
        pass


class RouterAgent(BaseAgent):
    """Router Agent - 路由到不同 Agent

    核心思想：根据输入类型路由到不同的 Agent
    """

    def __init__(self):
        super().__init__("Router", AgentPattern.ROUTER)
        self.routes: dict[str, BaseAgent] = {}

    def add_route(self, name: str, agent: BaseAgent) -> None:
        """添加路由

        Args:
            name: 路由名称
            agent: 目标 Agent
        """
        self.routes[name] = agent

    def run(self, user_input: str) -> str:
        # TODO: 实现路由逻辑
        # route = self._route(user_input)
        # agent = self.routes[route]
        # return agent.run(user_input)
        pass

    def _route(self, user_input: str) -> str:
        """路由决策"""
        pass


class PlanExecuteAgent(BaseAgent):
    """Plan-Execute Agent - 先规划再执行

    核心思想：Planner 制定计划，Executor 执行计划，Replanner 调整计划
    """

    def __init__(self):
        super().__init__("Plan-Execute", AgentPattern.PLAN_EXECUTE)

    def run(self, user_input: str) -> str:
        # TODO: 实现 Plan-Execute 逻辑
        # plan = self._plan(user_input)
        # for step in plan:
        #     result = self._execute(step)
        #     if self._need_replan(result):
        #         plan = self._replan(plan, result)
        pass

    def _plan(self, user_input: str) -> list[str]:
        """规划"""
        pass

    def _execute(self, step: str) -> str:
        """执行"""
        pass

    def _need_replan(self, result: str) -> bool:
        """是否需要重新规划"""
        pass

    def _replan(self, plan: list[str], result: str) -> list[str]:
        """重新规划"""
        pass


class ReflectionAgent(BaseAgent):
    """Reflection Agent - 自我反思改进

    核心思想：Generator 生成结果，Critic 批评改进
    """

    def __init__(self):
        super().__init__("Reflection", AgentPattern.REFLECTION)

    def run(self, user_input: str) -> str:
        # TODO: 实现 Reflection 逻辑
        # draft = self._generate(user_input)
        # for i in range(3):
        #     critique = self._critique(draft)
        #     if self._is_satisfied(critique):
        #         break
        #     draft = self._improve(draft, critique)
        # return draft
        pass

    def _generate(self, user_input: str) -> str:
        """生成"""
        pass

    def _critique(self, draft: str) -> str:
        """批评"""
        pass

    def _is_satisfied(self, critique: str) -> bool:
        """是否满意"""
        pass

    def _improve(self, draft: str, critique: str) -> str:
        """改进"""
        pass


def print_pattern_comparison() -> None:
    """打印模式对比表"""
    print("📚 Agent 模式对比表")
    print("=" * 80)
    print(f"{'模式':<20} {'核心思想':<20} {'适用场景':<20} {'关键组件'}")
    print("-" * 80)
    patterns = [
        ("ReAct", "推理+行动交替", "通用 Agent", "Thought/Action/Observation"),
        ("Router", "路由到不同 Agent", "多任务分发", "Router/Handoff"),
        ("Plan-Execute", "先规划再执行", "复杂任务", "Planner/Executor"),
        ("Reflection", "自我反思改进", "代码生成", "Generator/Critic"),
        ("Evaluator-Optimizer", "评估+优化", "内容创作", "Generator/Evaluator"),
        ("Supervisor", "主管协调", "多 Agent 协作", "Supervisor/Workers"),
        ("Hierarchical", "层级管理", "大型组织", "CEO/Manager/Worker"),
        ("Human-in-loop", "人类审批", "高风险决策", "Approval Node"),
        ("Long-running", "长时间运行", "批处理任务", "Checkpoint/Resume"),
    ]
    for name, core, scene, components in patterns:
        print(f"{name:<20} {core:<20} {scene:<20} {components}")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Agent 模式复习")
    parser.add_argument("--pattern", type=str, help="指定模式")
    args = parser.parse_args()

    print_pattern_comparison()

    if args.pattern:
        print(f"\n🔍 演示模式：{args.pattern}")
        # TODO: 演示指定模式


if __name__ == "__main__":
    main()
