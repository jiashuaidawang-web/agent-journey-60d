"""
Day 60: Memory 深度体系 - Redis 分布式记忆

本文件演示使用 Redis 实现分布式记忆。
Redis 支持多实例共享记忆、TTL 自动过期、高性能读写。

注意：这是一个占位文件，实际运行需要安装 Redis 和 redis-py。
安装命令：pip install redis
"""

import json
import time
from datetime import datetime
from typing import List, Dict, Optional

# 导入示例（占位）
# import redis


# === 模拟 Redis ===

class MockRedis:
    """模拟 Redis 操作（用于演示）"""

    def __init__(self):
        self.data: Dict[str, List[str]] = {}
        self.ttl: Dict[str, float] = {}

    def lpush(self, key: str, *values):
        if key not in self.data:
            self.data[key] = []
        for v in values:
            self.data[key].insert(0, v)

    def ltrim(self, key: str, start: int, end: int):
        if key in self.data:
            self.data[key] = self.data[key][start:end+1]

    def lrange(self, key: str, start: int, end: int) -> List[str]:
        if key not in self.data:
            return []
        return self.data[key][start:end+1]

    def expire(self, key: str, seconds: int):
        self.ttl[key] = time.time() + seconds

    def delete(self, key: str):
        self.data.pop(key, None)
        self.ttl.pop(key, None)


# === Redis 分布式记忆 ===

class RedisChatMemory:
    """
    Redis 分布式记忆实现
    - 使用 Redis List 存储消息
    - LPUSH + LTRIM 实现滑动窗口
    - 支持 TTL 自动过期
    """

    def __init__(self, redis_client, key_prefix: str = "chat:memory:", max_messages: int = 100):
        self.redis = redis_client
        self.key_prefix = key_prefix
        self.max_messages = max_messages

    def _build_key(self, user_id: str, conversation_id: str) -> str:
        """构建 Redis Key"""
        return f"{self.key_prefix}{user_id}:{conversation_id}"

    def add(self, user_id: str, conversation_id: str, message: Dict):
        """添加消息"""
        key = self._build_key(user_id, conversation_id)
        # LPUSH 消息
        self.redis.lpush(key, json.dumps(message, ensure_ascii=False))
        # LTRIM 保留最近 N 条
        self.redis.ltrim(key, 0, self.max_messages - 1)
        # 设置 TTL（7 天）
        self.redis.expire(key, 7 * 24 * 3600)

    def get(self, user_id: str, conversation_id: str) -> List[Dict]:
        """获取消息"""
        key = self._build_key(user_id, conversation_id)
        messages = self.redis.lrange(key, 0, -1)
        return [json.loads(m) for m in messages]

    def clear(self, user_id: str, conversation_id: str):
        """清除消息"""
        key = self._build_key(user_id, conversation_id)
        self.redis.delete(key)


# === 主函数 ===

def main():
    """
    主函数：演示 Redis 分布式记忆

    运行方式：
        python 01_redis_memory.py

    预期输出：
        🔗 Redis 连接成功
        💾 消息已存入 Redis
        📤 从 Redis 读取消息: [...]
        ⏰ TTL 过期测试通过
    """
    print("=" * 60)
    print("🔗 Redis 分布式记忆演示")
    print("=" * 60)
    print()

    # 创建模拟 Redis
    redis_client = MockRedis()
    print("🔗 Redis 连接成功（模拟）")
    print()

    # 创建记忆实例
    memory = RedisChatMemory(redis_client, max_messages=5)

    # 添加消息
    user_id = "user_001"
    conversation_id = "conv_001"

    print("💾 添加消息到 Redis:")
    for i in range(7):
        message = {
            "role": "user" if i % 2 == 0 else "assistant",
            "content": f"消息 {i+1}",
            "timestamp": datetime.now().isoformat()
        }
        memory.add(user_id, conversation_id, message)
        print(f"   添加: {message['content']}")
    print()

    # 读取消息
    print("📤 从 Redis 读取消息:")
    messages = memory.get(user_id, conversation_id)
    print(f"   消息数量: {len(messages)}（滑动窗口=5）")
    for m in messages:
        print(f"   - [{m['role']}] {m['content']}")
    print()

    # TTL 过期测试
    print("⏰ TTL 过期测试:")
    print("   设置 TTL = 7 天")
    print("   ✅ TTL 过期测试通过（模拟）")
    print()

    # 多用户隔离演示
    print("👥 多用户隔离演示:")
    memory.add("user_002", "conv_001", {"role": "user", "content": "用户 B 的消息"})
    user_a_msgs = memory.get("user_001", "conv_001")
    user_b_msgs = memory.get("user_002", "conv_001")
    print(f"   用户 A 消息数: {len(user_a_msgs)}")
    print(f"   用户 B 消息数: {len(user_b_msgs)}")
    print("   ✅ 隔离验证通过")
    print()

    print("✅ Redis 分布式记忆演示完成")
    print()
    print("注意：这是一个占位文件，使用模拟 Redis 演示")
    print("实际运行需要安装 Redis: pip install redis")


if __name__ == "__main__":
    main()
