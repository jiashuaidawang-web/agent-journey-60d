"""
Day 60: Memory 深度体系 - Memory 分层体系演示

本文件演示 Agent Memory 的四种记忆类型：
- Short-term Memory（短期记忆）
- Long-term Memory（长期记忆）
- Working Memory（工作记忆）
- Episodic Memory（情景记忆）

以及滑动窗口（TokenWindow）和摘要记忆（SummaryMemory）的实现。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json


# === 数据模型 ===

@dataclass
class Message:
    """消息"""
    role: str           # user / assistant / system
    content: str        # 消息内容
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class UserProfile:
    """用户画像（长期记忆）"""
    user_id: str
    preferences: Dict[str, str] = field(default_factory=dict)  # 偏好
    tags: List[str] = field(default_factory=list)              # 标签
    summary: str = ""                                           # 用户摘要


# === 四种记忆类型 ===

class WorkingMemory:
    """
    工作记忆：任务执行的中间状态
    - 生命周期：单次任务
    - 特点：临时、高频读写
    """

    def __init__(self):
        self.task_state: Dict[str, any] = {}    # 任务状态
        self.tool_results: List[any] = []       # 工具调用结果
        self.temp_vars: Dict[str, any] = {}     # 临时变量

    def set_state(self, key: str, value: any):
        self.task_state[key] = value

    def get_state(self, key: str) -> any:
        return self.task_state.get(key)

    def add_tool_result(self, result: any):
        self.tool_results.append(result)

    def clear(self):
        self.task_state.clear()
        self.tool_results.clear()
        self.temp_vars.clear()


class ShortTermMemory:
    """
    短期记忆：当前会话的对话内容
    - 生命周期：单次会话
    - 特点：滑动窗口控制容量
    """

    def __init__(self, max_messages: int = 10):
        self.messages: List[Message] = []
        self.max_messages = max_messages

    def add(self, message: Message):
        """添加消息（滑动窗口）"""
        self.messages.append(message)
        # 超出窗口，删除最早的消息
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self) -> List[Message]:
        return self.messages

    def clear(self):
        self.messages.clear()


class SummaryMemory:
    """
    摘要记忆：历史对话的摘要
    - 生命周期：跨会话
    - 特点：压缩存储，节省 token
    """

    def __init__(self):
        self.summaries: List[str] = []  # 摘要列表

    def add_summary(self, summary: str):
        """添加摘要"""
        self.summaries.append(summary)

    def get_context(self) -> str:
        """获取摘要上下文"""
        return "\n".join(self.summaries)

    def clear(self):
        self.summaries.clear()


class LongTermMemory:
    """
    长期记忆：跨会话持久化的信息
    - 生命周期：永久
    - 特点：用户画像、偏好、历史摘要
    """

    def __init__(self):
        self.user_profiles: Dict[str, UserProfile] = {}

    def get_or_create_profile(self, user_id: str) -> UserProfile:
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = UserProfile(user_id=user_id)
        return self.user_profiles[user_id]

    def update_preference(self, user_id: str, key: str, value: str):
        profile = self.get_or_create_profile(user_id)
        profile.preferences[key] = value

    def get_profile(self, user_id: str) -> Optional[UserProfile]:
        return self.user_profiles.get(user_id)


class EpisodicMemory:
    """
    情景记忆：用户历史事件记录
    - 生命周期：长期
    - 特点：按事件组织，支持时间线查询
    """

    def __init__(self):
        self.events: List[Dict] = []

    def add_event(self, user_id: str, event_type: str, content: str):
        """添加事件"""
        self.events.append({
            "user_id": user_id,
            "event_type": event_type,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })

    def get_events(self, user_id: str) -> List[Dict]:
        """获取用户事件"""
        return [e for e in self.events if e["user_id"] == user_id]


# === 主函数 ===

def main():
    """
    主函数：演示 Memory 分层体系

    运行方式：
        python 00_memory_hierarchy.py

    预期输出：
        🧠 Memory 分层体系演示
        📝 Working Memory: [当前轮次消息]
        📝 Short-term Memory: [最近 5 轮]
        📝 Summary Memory: [历史摘要]
        📝 Long-term Memory: [用户画像]
    """
    print("=" * 60)
    print("🧠 Memory 分层体系演示")
    print("=" * 60)
    print()

    # Working Memory
    working = WorkingMemory()
    working.set_state("current_task", "查询订单")
    working.add_tool_result({"order_id": "12345", "status": "已发货"})
    print("📝 Working Memory:")
    print(f"   当前任务: {working.get_state('current_task')}")
    print(f"   工具结果: {working.tool_results}")
    print()

    # Short-term Memory
    short_term = ShortTermMemory(max_messages=5)
    for i in range(7):
        short_term.add(Message(role="user", content=f"消息 {i+1}"))
    print("📝 Short-term Memory（滑动窗口=5）:")
    print(f"   消息数量: {len(short_term.get_messages())}")
    print(f"   最新消息: {short_term.get_messages()[-1].content}")
    print()

    # Summary Memory
    summary = SummaryMemory()
    summary.add_summary("用户偏好简洁回答")
    summary.add_summary("用户经常查询订单")
    print("📝 Summary Memory:")
    print(f"   摘要: {summary.get_context()}")
    print()

    # Long-term Memory
    long_term = LongTermMemory()
    long_term.update_preference("user_001", "language", "中文")
    long_term.update_preference("user_001", "style", "简洁")
    profile = long_term.get_profile("user_001")
    print("📝 Long-term Memory:")
    print(f"   用户偏好: {profile.preferences}")
    print()

    # Episodic Memory
    episodic = EpisodicMemory()
    episodic.add_event("user_001", "order", "下单购买商品 A")
    episodic.add_event("user_001", "support", "咨询订单状态")
    print("📝 Episodic Memory:")
    print(f"   事件数量: {len(episodic.get_events('user_001'))}")
    print()

    print("✅ Memory 分层体系演示完成")


if __name__ == "__main__":
    main()
