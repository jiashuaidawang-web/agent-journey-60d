"""
Mini Agent Runtime - Core Module.

核心模块：Agent 类、Agent Loop、Context 管理、状态管理。

这是整个 Runtime 的心脏，把 Model + Tool + Memory + State 串起来。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field


@dataclass
class AgentState:
    """Agent 状态。"""
    messages: list[dict] = field(default_factory=list)
    tool_calls: list[dict] = field(default_factory=list)
    iteration: int = 0
    max_iterations: int = 10
    finished: bool = False
    final_response: str = ""
    error: str | None = None

    def to_dict(self) -> dict:
        return {
            "iteration": self.iteration,
            "tool_calls_count": len(self.tool_calls),
            "finished": self.finished,
            "error": self.error,
        }

    def increment_iteration(self) -> None:
        self.iteration += 1

    def is_max_iterations_reached(self) -> bool:
        return self.iteration >= self.max_iterations

    def mark_finished(self, response: str = "") -> None:
        self.finished = True
        self.final_response = response

    def mark_error(self, error: str) -> None:
        self.error = error
        self.finished = True


class ContextManager:
    """Context 管理器。"""

    def __init__(self, system_prompt: str, max_tokens: int = 4000):
        self.system_prompt = system_prompt
        self.max_tokens = max_tokens

    def build(self, history: list[dict], memory: list[str] | None = None) -> list[dict]:
        """构建最终消息列表。"""
        messages = [{"role": "system", "content": self.system_prompt}]

        if memory:
            for mem in memory:
                messages.append({"role": "system", "content": f"[Memory] {mem}"})

        messages.extend(history)
        return messages


class AgentLoop:
    """Agent 循环。"""

    def __init__(self, model, registry, max_iterations: int = 10):
        self.model = model
        self.registry = registry
        self.max_iterations = max_iterations

    def run(self, messages: list[dict], state: AgentState) -> AgentState:
        """执行 Agent Loop。"""
        tools = self.registry.get_tools_definition()

        while not state.finished and state.iteration < state.max_iterations:
            state.iteration += 1

            # 调用 Model（带工具）
            response = self.model.chat_with_tools(messages, tools)

            # 检查是否有工具调用
            if response.get("tool_calls"):
                messages.append({
                    "role": "assistant",
                    "content": response.get("content", ""),
                    "tool_calls": response["tool_calls"],
                })

                for tool_call in response["tool_calls"]:
                    tool_name = tool_call["function"]["name"]
                    tool_args = json.loads(tool_call["function"]["arguments"])

                    result = self.registry.execute(tool_name, tool_args)

                    state.tool_calls.append({
                        "tool": tool_name,
                        "args": tool_args,
                        "result": result,
                    })

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "content": result,
                    })
            else:
                state.final_response = response.get("content", "")
                state.finished = True

        if not state.finished:
            state.error = f"达到最大迭代次数 {state.max_iterations}"
            state.finished = True

        return state


class Agent:
    """Agent —— 对外统一接口。"""

    def __init__(self, model, registry, system_prompt: str = "你是一个有用的助手。",
                 memory=None, max_iterations: int = 10):
        self.model = model
        self.registry = registry
        self.memory = memory
        self.context_manager = ContextManager(system_prompt)
        self.loop = AgentLoop(model, registry, max_iterations)
        self.max_iterations = max_iterations

    def run(self, user_input: str) -> str:
        """运行 Agent。"""
        memory = self.memory.get_all() if self.memory else None
        messages = self.context_manager.build(
            history=[{"role": "user", "content": user_input}],
            memory=memory,
        )

        state = AgentState(max_iterations=self.max_iterations)
        state = self.loop.run(messages, state)

        if self.memory and state.final_response:
            self.memory.add(f"Q: {user_input}\nA: {state.final_response}")

        return state.final_response or state.error or "无响应"
