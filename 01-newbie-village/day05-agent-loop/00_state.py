"""
================================================================================
Day 5 - Agent 状态管理 | 00_state.py
================================================================================

【学习目标】
实现 AgentState：消息历史、工具调用记录、Token 统计、迭代次数

【前置知识】
- Day 1 LLM Foundation
- Day 4 Tool Calling

【操作步骤】
1. 运行: python 00_state.py
2. 观察输出：状态摘要

【预期输出】
AgentState(iter=1/5, tools=1, tokens=150, finished=False)
Summary: {'iterations': 1, 'tool_calls_count': 1, 'tool_names': ['get_weather'], 'input_tokens': 100, 'output_tokens': 50, 'total_tokens': 150, 'finished': False, 'error': None}

【验证标准】
□ 能看到状态摘要
□ 理解 AgentState 的职责（记录运行状态）

【代码要点】
- AgentState: 状态数据类
- ToolCallRecord: 工具调用记录
- is_max_iterations_reached(): 检查是否达到最大迭代
- summary(): 返回状态摘要

================================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ToolCallRecord:
    """单次工具调用记录。"""
    tool_name: str
    arguments: dict
    result: str
    success: bool = True


@dataclass
class AgentState:
    """Agent 状态。

    记录 Agent 运行过程中的所有信息。
    """

    # 消息历史
    messages: list[dict] = field(default_factory=list)

    # 工具调用历史
    tool_calls: list[ToolCallRecord] = field(default_factory=list)

    # Token 统计
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    # 迭代控制
    iteration: int = 0
    max_iterations: int = 10

    # 完成状态
    finished: bool = False
    final_response: str = ""

    # 错误信息
    error: str | None = None

    def add_message(self, message: dict) -> None:
        """添加一条消息。"""
        self.messages.append(message)

    def add_tool_call(self, tool_name: str, arguments: dict, result: str, success: bool = True) -> None:
        """记录一次工具调用。"""
        self.tool_calls.append(ToolCallRecord(
            tool_name=tool_name,
            arguments=arguments,
            result=result,
            success=success,
        ))

    def update_tokens(self, input_tokens: int, output_tokens: int) -> None:
        """更新 Token 统计。"""
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_tokens += input_tokens + output_tokens

    def increment_iteration(self) -> None:
        """增加迭代次数。"""
        self.iteration += 1

    def is_max_iterations_reached(self) -> bool:
        """是否达到最大迭代次数。"""
        return self.iteration >= self.max_iterations

    def mark_finished(self, response: str = "") -> None:
        """标记完成。"""
        self.finished = True
        self.final_response = response

    def mark_error(self, error: str) -> None:
        """标记错误。"""
        self.error = error
        self.finished = True

    def summary(self) -> dict:
        """返回状态摘要。"""
        return {
            "iterations": self.iteration,
            "tool_calls_count": len(self.tool_calls),
            "tool_names": [tc.tool_name for tc in self.tool_calls],
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "finished": self.finished,
            "error": self.error,
        }

    def __str__(self) -> str:
        return (
            f"AgentState(iter={self.iteration}/{self.max_iterations}, "
            f"tools={len(self.tool_calls)}, tokens={self.total_tokens}, "
            f"finished={self.finished})"
        )


if __name__ == "__main__":
    # 测试
    state = AgentState(max_iterations=5)

    state.add_message({"role": "user", "content": "你好"})
    state.add_tool_call("get_weather", {"city": "北京"}, "北京晴，25°C")
    state.update_tokens(100, 50)
    state.increment_iteration()

    print(state)
    print(f"Summary: {state.summary()}")
