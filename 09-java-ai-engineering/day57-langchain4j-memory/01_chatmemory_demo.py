"""
================================================================================
Day 57 - ChatMemory 记忆对话 | 01_chatmemory_demo.py
================================================================================

【学习目标】
实现 ChatMemory 记忆对话，理解多会话管理机制

【前置知识】
- 00_langchain4j_basics.py（框架基础）

【操作步骤】
1. 阅读本文件，理解 ChatMemory 核心接口
2. 实现多会话管理
3. 运行代码，观察输出

【预期输出】
🧠 ChatMemory 记忆对话
├── 第一轮: 你好，我是张三
├── 第二轮: 我叫什么名字？
└── 回复: 你叫张三 ✅

【验证标准】
□ 能实现记忆对话
□ 能实现多会话隔离
□ 理解滑动窗口机制

【代码要点】
- MessageWindowChatMemory: 滑动窗口
- ChatMemory: 核心接口
- 多会话管理: Map<String, ChatMemory>

================================================================================
"""

import sys
from dataclasses import dataclass, field
from typing import List, Dict
from collections import deque


@dataclass
class ChatMessage:
    """聊天消息。"""
    role: str       # user / assistant / system
    content: str


class MessageWindowChatMemory:
    """滑动窗口 ChatMemory 实现。"""

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.messages: deque[ChatMessage] = deque(maxlen=max_messages)

    def add(self, message: ChatMessage):
        """添加消息。"""
        self.messages.append(message)

    def get_messages(self) -> List[ChatMessage]:
        """获取所有消息。"""
        return list(self.messages)

    def clear(self):
        """清空记忆。"""
        self.messages.clear()


class ChatMemoryManager:
    """多会话 ChatMemory 管理器。"""

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.memory_map: Dict[str, MessageWindowChatMemory] = {}

    def get_memory(self, session_id: str) -> MessageWindowChatMemory:
        """获取或创建记忆。"""
        if session_id not in self.memory_map:
            self.memory_map[session_id] = MessageWindowChatMemory(self.max_messages)
        return self.memory_map[session_id]

    def clear_memory(self, session_id: str):
        """清空指定会话记忆。"""
        if session_id in self.memory_map:
            self.memory_map[session_id].clear()

    def get_session_ids(self) -> List[str]:
        """获取所有会话 ID。"""
        return list(self.memory_map.keys())


def demo_single_session():
    """演示单会话记忆对话。"""
    print("🧠 单会话记忆对话：")
    print("-" * 40)

    memory = MessageWindowChatMemory(max_messages=10)

    # 第一轮对话
    user_msg1 = ChatMessage(role="user", content="你好，我是张三")
    memory.add(user_msg1)
    print(f"📤 User: {user_msg1.content}")

    # 模拟 LLM 回复
    assistant_msg1 = ChatMessage(role="assistant", content="你好张三，有什么可以帮你的？")
    memory.add(assistant_msg1)
    print(f"🤖 Assistant: {assistant_msg1.content}")

    # 第二轮对话（带历史）
    user_msg2 = ChatMessage(role="user", content="我叫什么名字？")
    memory.add(user_msg2)
    print(f"📤 User: {user_msg2.content}")

    # 模拟 LLM 回复（基于历史）
    assistant_msg2 = ChatMessage(role="assistant", content="你叫张三")
    memory.add(assistant_msg2)
    print(f"🤖 Assistant: {assistant_msg2.content}")

    print()
    print("📜 当前记忆中的消息：")
    for i, msg in enumerate(memory.get_messages(), 1):
        print(f"   {i}. [{msg.role}] {msg.content}")
    print()


def demo_multi_session():
    """演示多会话隔离。"""
    print("👥 多会话隔离：")
    print("-" * 40)

    manager = ChatMemoryManager(max_messages=10)

    # 会话 A
    memory_a = manager.get_memory("session-a")
    memory_a.add(ChatMessage(role="user", content="我是张三"))
    memory_a.add(ChatMessage(role="assistant", content="你好张三"))

    # 会话 B
    memory_b = manager.get_memory("session-b")
    memory_b.add(ChatMessage(role="user", content="我是李四"))
    memory_b.add(ChatMessage(role="assistant", content="你好李四"))

    # 验证隔离
    print(f"📜 会话 A 的消息：")
    for msg in memory_a.get_messages():
        print(f"   [{msg.role}] {msg.content}")

    print(f"📜 会话 B 的消息：")
    for msg in memory_b.get_messages():
        print(f"   [{msg.role}] {msg.content}")

    print(f"📊 会话数量: {len(manager.get_session_ids())}")
    print()


def demo_sliding_window():
    """演示滑动窗口机制。"""
    print("🪟 滑动窗口机制：")
    print("-" * 40)

    memory = MessageWindowChatMemory(max_messages=3)

    # 添加 5 条消息，观察窗口滑动
    for i in range(1, 6):
        memory.add(ChatMessage(role="user", content=f"消息 {i}"))
        print(f"   添加: 消息 {i} → 当前: {[m.content for m in memory.get_messages()]}")

    print()
    print("   说明：窗口大小为 3，只保留最近 3 条消息")
    print()


def main():
    """主函数：展示 ChatMemory 记忆对话。"""
    print("=" * 60)
    print("🧠 ChatMemory 记忆对话")
    print("=" * 60)
    print()

    demo_single_session()
    demo_multi_session()
    demo_sliding_window()

    print("=" * 60)
    print("✅ ChatMemory 记忆对话演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
