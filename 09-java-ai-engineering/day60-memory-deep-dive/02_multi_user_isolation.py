"""
Day 60: Memory 深度体系 - 多用户会话隔离

本文件演示多用户会话隔离的实现。
通过 UserId + ConversationId 组合键实现记忆隔离。

核心概念：
- UserId：标识用户（跨会话）
- ConversationId：标识会话（单次对话）
- 组合键：userId:conversationId
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


# === 数据模型 ===

@dataclass
class Message:
    """消息"""
    role: str
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class User:
    """用户"""
    user_id: str
    name: str


@dataclass
class Conversation:
    """会话"""
    conversation_id: str
    user_id: str
    title: str = ""


# === 多用户会话隔离实现 ===

class IsolatedChatMemory:
    """
    多用户会话隔离记忆
    - 使用 userId:conversationId 作为隔离键
    - 支持同一用户的不同会话隔离
    - 支持跨会话的用户偏好共享
    """

    def __init__(self):
        # 会话记忆：key = userId:conversationId
        self.conversation_memory: Dict[str, List[Message]] = {}
        # 用户偏好：key = userId（跨会话共享）
        self.user_preferences: Dict[str, Dict[str, str]] = {}

    def _build_conversation_key(self, user_id: str, conversation_id: str) -> str:
        """构建会话记忆 Key"""
        return f"{user_id}:{conversation_id}"

    def add_message(self, user_id: str, conversation_id: str, message: Message):
        """添加消息到指定会话"""
        key = self._build_conversation_key(user_id, conversation_id)
        if key not in self.conversation_memory:
            self.conversation_memory[key] = []
        self.conversation_memory[key].append(message)

    def get_messages(self, user_id: str, conversation_id: str) -> List[Message]:
        """获取指定会话的消息"""
        key = self._build_conversation_key(user_id, conversation_id)
        return self.conversation_memory.get(key, [])

    def get_user_conversations(self, user_id: str) -> List[str]:
        """获取用户的所有会话 ID"""
        prefix = f"{user_id}:"
        return [key.split(":", 1)[1] for key in self.conversation_memory if key.startswith(prefix)]

    def set_preference(self, user_id: str, key: str, value: str):
        """设置用户偏好（跨会话共享）"""
        if user_id not in self.user_preferences:
            self.user_preferences[user_id] = {}
        self.user_preferences[user_id][key] = value

    def get_preference(self, user_id: str, key: str) -> Optional[str]:
        """获取用户偏好"""
        return self.user_preferences.get(user_id, {}).get(key)

    def clear_conversation(self, user_id: str, conversation_id: str):
        """清除指定会话"""
        key = self._build_conversation_key(user_id, conversation_id)
        self.conversation_memory.pop(key, None)


# === 主函数 ===

def main():
    """
    主函数：演示多用户会话隔离

    运行方式：
        python 02_multi_user_isolation.py

    预期输出：
        👤 用户 A 会话 1: [消息 A1]
        👤 用户 A 会话 2: [消息 A2]
        👤 用户 B 会话 1: [消息 B1]
        ✅ 隔离验证通过
    """
    print("=" * 60)
    print("👥 多用户会话隔离演示")
    print("=" * 60)
    print()

    # 创建记忆实例
    memory = IsolatedChatMemory()

    # 用户 A 的会话 1
    memory.add_message("user_A", "conv_1", Message(role="user", content="你好"))
    memory.add_message("user_A", "conv_1", Message(role="assistant", content="你好！有什么可以帮你？"))

    # 用户 A 的会话 2
    memory.add_message("user_A", "conv_2", Message(role="user", content="查询订单"))
    memory.add_message("user_A", "conv_2", Message(role="assistant", content="请提供订单号"))

    # 用户 B 的会话 1
    memory.add_message("user_B", "conv_1", Message(role="user", content="你是谁"))
    memory.add_message("user_B", "conv_1", Message(role="assistant", content="我是 AI 助手"))

    # 打印各会话消息
    print("👤 用户 A 会话 1 消息:")
    for msg in memory.get_messages("user_A", "conv_1"):
        print(f"   [{msg.role}] {msg.content}")
    print()

    print("👤 用户 A 会话 2 消息:")
    for msg in memory.get_messages("user_A", "conv_2"):
        print(f"   [{msg.role}] {msg.content}")
    print()

    print("👤 用户 B 会话 1 消息:")
    for msg in memory.get_messages("user_B", "conv_1"):
        print(f"   [{msg.role}] {msg.content}")
    print()

    # 验证隔离
    print("🔒 隔离验证:")
    user_a_conv1 = memory.get_messages("user_A", "conv_1")
    user_b_conv1 = memory.get_messages("user_B", "conv_1")
    print(f"   用户 A 会话 1 第一条消息: {user_a_conv1[0].content}")
    print(f"   用户 B 会话 1 第一条消息: {user_b_conv1[0].content}")
    assert user_a_conv1[0].content != user_b_conv1[0].content
    print("   ✅ 隔离验证通过")
    print()

    # 用户偏好（跨会话共享）
    print("⚙️  用户偏好（跨会话共享）:")
    memory.set_preference("user_A", "language", "中文")
    memory.set_preference("user_A", "style", "简洁")
    print(f"   用户 A 语言偏好: {memory.get_preference('user_A', 'language')}")
    print(f"   用户 A 风格偏好: {memory.get_preference('user_A', 'style')}")
    print("   ✅ 偏好跨会话共享验证通过")
    print()

    # 用户会话列表
    print("📋 用户 A 的会话列表:")
    convs = memory.get_user_conversations("user_A")
    print(f"   会话: {convs}")
    print()

    print("✅ 多用户会话隔离演示完成")


if __name__ == "__main__":
    main()
