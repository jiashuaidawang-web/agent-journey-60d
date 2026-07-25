"""
================================================================================
Day 7 - Mini Agent Runtime - 记忆系统 | mini_agent_runtime/memory/__init__.py
================================================================================

【学习目标】
理解 Memory：简单的对话历史存储

【前置知识】
- tools/__init__.py（工具系统）

【代码结构】
- Memory: 记忆类（添加、检索、清空）

================================================================================
"""

from __future__ import annotations


class Memory:
    """简单记忆。

    存储对话历史，支持添加和检索。
    """

    def __init__(self, max_entries: int = 10):
        self.max_entries = max_entries
        self._entries: list[str] = []

    def add(self, entry: str) -> None:
        """添加一条记忆。"""
        self._entries.append(entry)
        # 超出限制时裁剪
        if len(self._entries) > self.max_entries:
            self._entries = self._entries[-self.max_entries:]

    def get_all(self) -> list[str]:
        """获取所有记忆。"""
        return self._entries.copy()

    def clear(self) -> None:
        """清空记忆。"""
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)
