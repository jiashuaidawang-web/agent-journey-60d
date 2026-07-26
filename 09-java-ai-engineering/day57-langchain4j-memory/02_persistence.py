"""
================================================================================
Day 57 - Redis/MySQL 持久化 | 02_persistence.py
================================================================================

【学习目标】
实现 Redis / MySQL 持久化，理解持久化策略

【前置知识】
- 01_chatmemory_demo.py（记忆对话）

【操作步骤】
1. 阅读本文件，理解持久化方案
2. 实现 Redis 持久化
3. 实现 MySQL 持久化
4. 运行代码，观察输出

【预期输出】
💾 ChatMemory 持久化
├── Redis: ✅ 支持
└── MySQL: ✅ 支持

【验证标准】
□ 能实现 Redis 持久化
□ 能实现 MySQL 持久化
□ 理解两种方案优劣势

【代码要点】
- Redis: List 结构 + TTL
- MySQL: chat_message 表
- 混合方案: Redis 缓存 + MySQL 持久化

================================================================================
"""

import sys
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from collections import deque


@dataclass
class ChatMessage:
    """聊天消息。"""
    role: str
    content: str
    timestamp: float = field(default_factory=time.time)


class RedisChatMemory:
    """Redis ChatMemory 实现（模拟）。

    实际使用需要：
    - spring-data-redis 依赖
    - RedisTemplate<String, ChatMessage> 注入
    """

    def __init__(self, session_id: str, max_messages: int = 100):
        self.session_id = session_id
        self.max_messages = max_messages
        # 模拟 Redis List
        self.redis_store: Dict[str, List[ChatMessage]] = {}

    def add(self, message: ChatMessage):
        """添加消息到 Redis。

        Java 代码：
        ```java
        redisTemplate.opsForList().rightPush(sessionId, message);
        redisTemplate.expire(sessionId, Duration.ofHours(24));
        ```
        """
        if self.session_id not in self.redis_store:
            self.redis_store[self.session_id] = []
        self.redis_store[self.session_id].append(message)
        # 限制最大消息数
        if len(self.redis_store[self.session_id]) > self.max_messages:
            self.redis_store[self.session_id] = self.redis_store[self.session_id][-self.max_messages:]

    def get_messages(self) -> List[ChatMessage]:
        """获取所有消息。

        Java 代码：
        ```java
        return redisTemplate.opsForList().range(sessionId, 0, -1);
        ```
        """
        return self.redis_store.get(self.session_id, [])

    def clear(self):
        """清空记忆。"""
        self.redis_store.pop(self.session_id, None)


class MySQLChatMemory:
    """MySQL ChatMemory 实现（模拟）。

    实际使用需要：
    - spring-boot-starter-data-jpa 依赖
    - ChatMessageRepository 注入
    """

    def __init__(self, session_id: str):
        self.session_id = session_id
        # 模拟 MySQL 表
        self.mysql_store: Dict[str, List[ChatMessage]] = {}

    def add(self, message: ChatMessage):
        """添加消息到 MySQL。

        Java 代码：
        ```java
        ChatMessageEntity entity = new ChatMessageEntity();
        entity.setSessionId(sessionId);
        entity.setRole(message.getRole());
        entity.setContent(message.getContent());
        entity.setTimestamp(LocalDateTime.now());
        repository.save(entity);
        ```
        """
        if self.session_id not in self.mysql_store:
            self.mysql_store[self.session_id] = []
        self.mysql_store[self.session_id].append(message)

    def get_messages(self) -> List[ChatMessage]:
        """获取所有消息。

        Java 代码：
        ```java
        return repository.findBySessionIdOrderByTimestampAsc(sessionId);
        ```
        """
        return self.mysql_store.get(self.session_id, [])

    def clear(self):
        """清空记忆。"""
        self.mysql_store.pop(self.session_id, None)


def demo_redis_persistence():
    """演示 Redis 持久化。"""
    print("🔴 Redis 持久化：")
    print("-" * 40)

    memory = RedisChatMemory(session_id="user-123")

    # 添加消息
    memory.add(ChatMessage(role="user", content="你好"))
    memory.add(ChatMessage(role="assistant", content="你好！"))
    memory.add(ChatMessage(role="user", content="我叫张三"))

    # 获取消息
    print(f"   会话 ID: user-123")
    print(f"   消息数: {len(memory.get_messages())}")
    print(f"   消息列表：")
    for msg in memory.get_messages():
        print(f"     [{msg.role}] {msg.content}")

    print()
    print("   Redis 特点：")
    print("   ├── 读写性能极高（内存操作）")
    print("   ├── 天然支持 TTL（自动过期）")
    print("   └── 适合高性能、短期存储")
    print()


def demo_mysql_persistence():
    """演示 MySQL 持久化。"""
    print("🐬 MySQL 持久化：")
    print("-" * 40)

    memory = MySQLChatMemory(session_id="user-456")

    # 添加消息
    memory.add(ChatMessage(role="user", content="你好"))
    memory.add(ChatMessage(role="assistant", content="你好！"))
    memory.add(ChatMessage(role="user", content="我叫李四"))

    # 获取消息
    print(f"   会话 ID: user-456")
    print(f"   消息数: {len(memory.get_messages())}")
    print(f"   消息列表：")
    for msg in memory.get_messages():
        print(f"     [{msg.role}] {msg.content}")

    print()
    print("   MySQL 特点：")
    print("   ├── 磁盘存储，成本低")
    print("   ├── 支持复杂查询")
    print("   └── 适合长期存储、复杂查询")
    print()


def demo_hybrid_solution():
    """演示混合方案。"""
    print("🔀 混合方案（Redis + MySQL）：")
    print("-" * 40)
    print("""
   架构：
   ├── Redis: 缓存最近消息，提供高性能读写
   └── MySQL: 持久化所有消息，支持复杂查询

   流程：
   1. 写入：先写 Redis，异步写 MySQL
   2. 读取：先从 Redis 读，未命中从 MySQL 读
   3. 清理：Redis 设置 TTL，MySQL 定期归档

   优势：
   ├── 高性能（Redis 缓存）
   ├── 可靠持久（MySQL 备份）
   └── 成本低（热数据 Redis，冷数据 MySQL）
""")


def main():
    """主函数：展示 Redis/MySQL 持久化。"""
    print("=" * 60)
    print("💾 ChatMemory 持久化")
    print("=" * 60)
    print()

    demo_redis_persistence()
    demo_mysql_persistence()
    demo_hybrid_solution()

    print("=" * 60)
    print("✅ ChatMemory 持久化演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
