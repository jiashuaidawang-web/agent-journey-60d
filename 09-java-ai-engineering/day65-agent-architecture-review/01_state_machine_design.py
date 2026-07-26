"""
Day 65: 状态机设计 - Agent 状态机 + 事件驱动架构

功能：
1. Agent 状态机定义
2. 状态转移逻辑
3. 事件驱动架构

示例：
    python 01_state_machine_design.py
    python 01_state_machine_design.py --demo

实际实现需要：
- transitions / spring-statemachine（Java）

作者：Agent Journey 60D
日期：Day 65
"""

import argparse
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional


class AgentState(Enum):
    """Agent 状态"""
    IDLE = "Idle"
    PLANNING = "Planning"
    EXECUTING = "Executing"
    TOOL_CALLING = "ToolCalling"
    REFLECTING = "Reflecting"
    WAITING_FOR_HUMAN = "WaitingForHuman"
    COMPLETED = "Completed"
    FAILED = "Failed"


class AgentEvent(Enum):
    """Agent 事件"""
    USER_INPUT = "UserInput"
    PLAN_COMPLETE = "PlanComplete"
    TOOL_CALL = "ToolCall"
    TOOL_RESULT = "ToolResult"
    TASK_COMPLETE = "TaskComplete"
    NEED_REFLECTION = "NeedReflection"
    REFLECTION_DONE = "ReflectionDone"
    NEED_HUMAN = "NeedHuman"
    HUMAN_APPROVED = "HumanApproved"
    HUMAN_REJECTED = "HumanRejected"
    ERROR = "Error"


@dataclass
class Transition:
    """状态转移"""
    from_state: AgentState
    event: AgentEvent
    to_state: AgentState
    action: Optional[str] = None


@dataclass
class Event:
    """事件"""
    type: AgentEvent
    data: dict[str, Any] = field(default_factory=dict)


class StateMachine:
    """状态机

    核心思想：
    - 定义状态、事件、转移
    - 根据当前状态和事件决定下一个状态
    - 执行对应的动作
    """

    def __init__(self, initial_state: AgentState = AgentState.IDLE):
        self.current_state = initial_state
        self.transitions: list[Transition] = []
        self.history: list[tuple[AgentState, AgentEvent, AgentState]] = []
        self.event_handlers: dict[AgentEvent, list[Callable]] = {}
        self._init_transitions()

    def _init_transitions(self) -> None:
        """初始化状态转移表"""
        self.transitions = [
            # 用户输入
            Transition(AgentState.IDLE, AgentEvent.USER_INPUT, AgentState.PLANNING, "开始规划"),
            # 规划完成
            Transition(AgentState.PLANNING, AgentEvent.PLAN_COMPLETE, AgentState.EXECUTING, "开始执行"),
            # 需要工具
            Transition(AgentState.EXECUTING, AgentEvent.TOOL_CALL, AgentState.TOOL_CALLING, "调用工具"),
            # 工具返回
            Transition(AgentState.TOOL_CALLING, AgentEvent.TOOL_RESULT, AgentState.EXECUTING, "继续执行"),
            # 任务完成
            Transition(AgentState.EXECUTING, AgentEvent.TASK_COMPLETE, AgentState.REFLECTING, "开始反思"),
            # 需要反思
            Transition(AgentState.EXECUTING, AgentEvent.NEED_REFLECTION, AgentState.REFLECTING, "开始反思"),
            # 反思完成
            Transition(AgentState.REFLECTING, AgentEvent.REFLECTION_DONE, AgentState.COMPLETED, "任务完成"),
            # 反思后需要修改
            Transition(AgentState.REFLECTING, AgentEvent.TASK_COMPLETE, AgentState.EXECUTING, "继续执行"),
            # 需要人类
            Transition(AgentState.EXECUTING, AgentEvent.NEED_HUMAN, AgentState.WAITING_FOR_HUMAN, "等待人类"),
            # 人类批准
            Transition(AgentState.WAITING_FOR_HUMAN, AgentEvent.HUMAN_APPROVED, AgentState.EXECUTING, "继续执行"),
            # 人类拒绝
            Transition(AgentState.WAITING_FOR_HUMAN, AgentEvent.HUMAN_REJECTED, AgentState.PLANNING, "重新规划"),
            # 错误
            Transition(AgentState.EXECUTING, AgentEvent.ERROR, AgentState.FAILED, "任务失败"),
            Transition(AgentState.TOOL_CALLING, AgentEvent.ERROR, AgentState.FAILED, "任务失败"),
        ]

    def handle_event(self, event: Event) -> Optional[Transition]:
        """处理事件

        Args:
            event: 事件

        Returns:
            状态转移（如果匹配）
        """
        # 查找匹配的转移
        for transition in self.transitions:
            if (transition.from_state == self.current_state and
                    transition.event == event.type):
                old_state = self.current_state
                self.current_state = transition.to_state
                self.history.append((old_state, event.type, self.current_state))

                # 执行动作
                if transition.action:
                    print(f"  🔄 {transition.action}")

                # 触发事件处理器
                self._trigger_handlers(event)

                return transition

        print(f"  ⚠️ 未匹配的转移：{self.current_state.value} + {event.type.value}")
        return None

    def register_handler(self, event_type: AgentEvent, handler: Callable) -> None:
        """注册事件处理器

        Args:
            event_type: 事件类型
            handler: 处理器
        """
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def _trigger_handlers(self, event: Event) -> None:
        """触发事件处理器

        Args:
            event: 事件
        """
        handlers = self.event_handlers.get(event.type, [])
        for handler in handlers:
            handler(event)

    def get_history(self) -> list[tuple[AgentState, AgentEvent, AgentState]]:
        """获取状态转移历史

        Returns:
            历史记录
        """
        return self.history


class EventBus:
    """事件总线

    核心思想：
    - 事件的发布和订阅
    - 解耦事件生产者和消费者
    """

    def __init__(self):
        self.subscribers: dict[AgentEvent, list[Callable]] = {}
        self.event_log: list[Event] = []

    def subscribe(self, event_type: AgentEvent, handler: Callable) -> None:
        """订阅事件

        Args:
            event_type: 事件类型
            handler: 处理器
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event: Event) -> None:
        """发布事件

        Args:
            event: 事件
        """
        self.event_log.append(event)
        handlers = self.subscribers.get(event.type, [])
        for handler in handlers:
            handler(event)

    def get_event_log(self) -> list[Event]:
        """获取事件日志

        Returns:
            事件日志
        """
        return self.event_log


def demo_state_machine() -> None:
    """演示状态机"""
    print("🔄 Agent 状态机演示")
    print("=" * 50)

    sm = StateMachine(AgentState.IDLE)
    print(f"初始状态：{sm.current_state.value}")

    # 模拟事件序列
    events = [
        Event(AgentEvent.USER_INPUT, {"text": "分析贵州茅台财报"}),
        Event(AgentEvent.PLAN_COMPLETE, {"plan": ["读取财报", "提取指标", "生成分析"]}),
        Event(AgentEvent.TOOL_CALL, {"tool": "read_pdf"}),
        Event(AgentEvent.TOOL_RESULT, {"result": "财报内容..."}),
        Event(AgentEvent.TASK_COMPLETE),
        Event(AgentEvent.REFLECTION_DONE),
    ]

    for event in events:
        print(f"\n📨 事件：{event.type.value}")
        sm.handle_event(event)
        print(f"  📍 当前状态：{sm.current_state.value}")

    print("\n📜 状态转移历史：")
    for from_state, event, to_state in sm.get_history():
        print(f"  {from_state.value} --{event.value}--> {to_state.value}")


def demo_event_bus() -> None:
    """演示事件总线"""
    print("\n📡 事件总线演示")
    print("=" * 50)

    bus = EventBus()

    # 订阅事件
    def on_user_input(event: Event):
        print(f"  [AgentHandler] 收到用户输入：{event.data.get('text')}")

    def on_tool_call(event: Event):
        print(f"  [ToolHandler] 调用工具：{event.data.get('tool')}")

    def on_tool_result(event: Event):
        print(f"  [AgentHandler] 收到工具结果")

    bus.subscribe(AgentEvent.USER_INPUT, on_user_input)
    bus.subscribe(AgentEvent.TOOL_CALL, on_tool_call)
    bus.subscribe(AgentEvent.TOOL_RESULT, on_tool_result)

    # 发布事件
    bus.publish(Event(AgentEvent.USER_INPUT, {"text": "分析财报"}))
    bus.publish(Event(AgentEvent.TOOL_CALL, {"tool": "read_pdf"}))
    bus.publish(Event(AgentEvent.TOOL_RESULT, {"result": "..."}))


def main():
    parser = argparse.ArgumentParser(description="状态机设计")
    parser.add_argument("--demo", action="store_true", help="运行演示")
    args = parser.parse_args()

    if args.demo:
        demo_state_machine()
        demo_event_bus()
    else:
        demo_state_machine()


if __name__ == "__main__":
    main()
