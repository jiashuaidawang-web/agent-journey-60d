"""
Day 3: Context Builder.

组装 Agent 的 Context：System + History + Memory + Retrieved + Tool Result。
支持 Token 限制和优先级裁剪。

Java 类比: 相当于一个 MessageAssembler，把多个来源的信息拼成最终请求。

Usage:
    python context_builder.py
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class Message:
    """单条消息。"""
    role: str  # system / user / assistant
    content: str
    priority: int = 0  # 优先级：越高越重要
    source: str = ""  # 来源标注：system / history / memory / retrieved / tool


@dataclass
class ContextBuilder:
    """Context 组装器。

    职责：收集所有信息源 → 按优先级排序 → 按 Token 限制裁剪 → 输出 messages。
    """

    max_tokens: int = 4000
    messages: list[Message] = field(default_factory=list)

    # Token 估算：中文约 1.5 token/字，英文约 0.75 token/词
    def _estimate_tokens(self, text: str) -> int:
        """估算 Token 数（粗略）。"""
        # 简单估算：中文字符数 * 1.5 + 英文单词数 * 0.75
        chinese_chars = sum(1 for c in text if '一' <= c <= '鿿')
        ascii_part = len(text) - chinese_chars
        return int(chinese_chars * 1.5 + ascii_part * 0.4)

    def set_system(self, content: str) -> "ContextBuilder":
        """设置 System Prompt（最高优先级）。"""
        self.messages.append(Message(
            role="system",
            content=content,
            priority=100,
            source="system",
        ))
        return self

    def add_history(self, role: str, content: str) -> "ContextBuilder":
        """添加历史消息。"""
        self.messages.append(Message(
            role=role,
            content=content,
            priority=50,
            source="history",
        ))
        return self

    def add_memory(self, content: str) -> "ContextBuilder":
        """添加长期记忆。"""
        self.messages.append(Message(
            role="system",
            content=f"[Memory] {content}",
            priority=80,
            source="memory",
        ))
        return self

    def add_retrieved(self, content: str) -> "ContextBuilder":
        """添加 RAG 检索结果。"""
        self.messages.append(Message(
            role="system",
            content=f"[Retrieved Context] {content}",
            priority=60,
            source="retrieved",
        ))
        return self

    def add_tool_result(self, tool_name: str, result: str) -> "ContextBuilder":
        """添加工具调用结果。"""
        self.messages.append(Message(
            role="system",
            content=f"[Tool: {tool_name}] {result}",
            priority=70,
            source="tool",
        ))
        return self

    def build(self) -> list[dict]:
        """组装最终 messages，按优先级排序并裁剪。

        Returns:
            最终的 messages 列表，可直接传给 OpenAI API。
        """
        # 按优先级降序排序
        sorted_messages = sorted(self.messages, key=lambda m: m.priority, reverse=True)

        result = []
        total_tokens = 0

        for msg in sorted_messages:
            tokens = self._estimate_tokens(msg.content)

            if total_tokens + tokens > self.max_tokens:
                # 超出限制，跳过低优先级消息
                print(f"⚠️ 裁剪: [{msg.source}] {msg.content[:30]}... ({tokens} tokens)")
                continue

            result.append({"role": msg.role, "content": msg.content})
            total_tokens += tokens

        print(f"✅ Context 组装完成: {len(result)} 条消息, 约 {total_tokens} tokens")
        return result

    def reset(self) -> "ContextBuilder":
        """清空所有消息。"""
        self.messages.clear()
        return self


def demo():
    """演示 ContextBuilder 的使用。"""
    print("=" * 60)
    print("ContextBuilder 演示")
    print("=" * 60)

    builder = ContextBuilder(max_tokens=2000)

    # 1. System Prompt
    builder.set_system("你是一个专业的股票分析师，回答要简洁专业。")

    # 2. Memory（长期记忆）
    builder.add_memory("用户偏好：关注科技股和消费股")
    builder.add_memory("用户风险偏好：稳健型")

    # 3. 历史对话
    builder.add_history("user", "我之前买过贵州茅台")
    builder.add_history("assistant", "贵州茅台是白酒龙头，基本面稳健。")

    # 4. RAG 检索结果
    builder.add_retrieved("贵州茅台2024年报：营收同比增长15%，净利润增长18%。")

    # 5. 工具调用结果
    builder.add_tool_result("stock_price", "当前价格：1680元，PE：30，PB：8.5")

    # 6. 当前用户输入
    builder.add_history("user", "帮我分析一下贵州茅台的投资价值")

    # 构建最终 Context
    messages = builder.build()

    print("\n📋 最终 Context:")
    for i, msg in enumerate(messages):
        content_preview = msg["content"][:60] + "..." if len(msg["content"]) > 60 else msg["content"]
        print(f"   [{i}] {msg['role']}: {content_preview}")

    return messages


if __name__ == "__main__":
    demo()
