"""
================================================================================
Day 7 - Mini Agent Runtime - 可观测性 | mini_agent_runtime/observability/__init__.py
================================================================================

【学习目标】
理解 TokenCounter：Token 统计

【前置知识】
- memory/__init__.py（记忆系统）

【代码结构】
- TokenCounter: Token 计数器

================================================================================
"""

from __future__ import annotations


class TokenCounter:
    """Token 计数器。"""

    def __init__(self):
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def add(self, input_tokens: int, output_tokens: int) -> None:
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_tokens += input_tokens + output_tokens

    def summary(self) -> dict:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
        }

    def __str__(self) -> str:
        return f"Tokens(input={self.input_tokens}, output={self.output_tokens}, total={self.total_tokens})"
