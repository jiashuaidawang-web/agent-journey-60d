"""
================================================================================
Day 58 - Advisor 责任链基础 | 00_advisor_chain.py
================================================================================

【学习目标】
理解 Advisor 责任链基础，掌握核心接口和执行顺序

【前置知识】
- Day 55 Spring AI 总览

【操作步骤】
1. 阅读本文件，理解 Advisor 核心接口
2. 实现自定义 Advisor
3. 运行代码，观察输出

【预期输出】
🔗 Advisor 责任链基础
├── before → Advisor1 → Advisor2 → Advisor3 → LLM
└── after  → Advisor3 → Advisor2 → Advisor1 → 返回

【验证标准】
□ 能解释 Advisor 责任链
□ 能实现自定义 Advisor
□ 能控制执行顺序

【代码要点】
- Advisor 接口: before / after
- Ordered 接口: getOrder()
- AdvisorChain: nextBefore / nextAfter

================================================================================
"""

import sys
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


@dataclass
class AdvisorRequest:
    """Advisor 请求。"""
    user_text: str
    system_text: str = ""
    advise_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AdvisorResponse:
    """Advisor 响应。"""
    user_text: str
    system_text: str = ""
    advise_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChatClientResponse:
    """ChatClient 响应。"""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class Advisor:
    """Advisor 接口。"""

    def before(self, request: AdvisorRequest, chain: 'AdvisorChain') -> AdvisorResponse:
        """前置处理。"""
        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: 'AdvisorChain') -> ChatClientResponse:
        """后置处理。"""
        return chain.next_after(response)

    def get_order(self) -> int:
        """执行顺序（越小越先执行）。"""
        return 0


class AdvisorChain:
    """Advisor 责任链。"""

    def __init__(self, advisors: List[Advisor]):
        self.advisors = sorted(advisors, key=lambda a: a.get_order())
        self.before_index = 0
        self.after_index = len(self.advisors) - 1

    def next_before(self, request: AdvisorRequest) -> AdvisorResponse:
        """执行下一个 before。"""
        if self.before_index < len(self.advisors):
            advisor = self.advisors[self.before_index]
            self.before_index += 1
            print(f"   📤 before: {advisor.__class__.__name__}")
            return advisor.before(request, self)
        # 所有 before 执行完毕，调用 LLM（模拟）
        print("   🤖 LLM.call()")
        return AdvisorResponse(
            user_text=request.user_text,
            system_text=request.system_text,
            advise_context=request.advise_context
        )

    def next_after(self, response: ChatClientResponse) -> ChatClientResponse:
        """执行下一个 after。"""
        if self.after_index >= 0:
            advisor = self.advisors[self.after_index]
            self.after_index -= 1
            print(f"   📥 after: {advisor.__class__.__name__}")
            return advisor.after(response, self)
        return response


class LoggingAdvisor(Advisor):
    """日志 Advisor。"""

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        print(f"      📝 记录请求: {request.user_text[:20]}...")
        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: AdvisorChain) -> ChatClientResponse:
        print(f"      📝 记录回复: {response.content[:20]}...")
        return chain.next_after(response)

    def get_order(self) -> int:
        return 0


class SecurityAdvisor(Advisor):
    """安全 Advisor。"""

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        print(f"      🔒 安全检查: {request.user_text[:20]}...")
        return chain.next_before(request)

    def get_order(self) -> int:
        return 10


def demo_advisor_chain():
    """演示 Advisor 责任链。"""
    print("🔗 Advisor 责任链演示：")
    print("-" * 40)

    # 创建 Advisor 链
    advisors = [
        LoggingAdvisor(),
        SecurityAdvisor(),
    ]
    chain = AdvisorChain(advisors)

    # 创建请求
    request = AdvisorRequest(user_text="你好，请介绍一下你自己")

    print(f"📤 用户输入: {request.user_text}")
    print()
    print("⏩ 执行 before 链：")
    response = chain.next_before(request)

    # 模拟 LLM 返回
    llm_response = ChatClientResponse(content="你好！我是一个AI助手。")

    print()
    print("⏪ 执行 after 链：")
    final_response = chain.next_after(llm_response)

    print()
    print(f"✅ 最终回复: {final_response.content}")
    print()


def demo_execution_order():
    """演示执行顺序。"""
    print("📊 执行顺序说明：")
    print("-" * 40)
    print("""
before 执行顺序（正序）：
    LoggingAdvisor (order=0) → SecurityAdvisor (order=10) → LLM

after 执行顺序（逆序）：
    LLM → SecurityAdvisor (order=10) → LoggingAdvisor (order=0)

特点：
    - before 正序执行（order 小的先执行）
    - after 逆序执行（order 大的先执行）
    - 类似栈结构：先进后出
""")


def main():
    """主函数：展示 Advisor 责任链基础。"""
    print("=" * 60)
    print("🔗 Advisor 责任链基础")
    print("=" * 60)
    print()

    demo_advisor_chain()
    demo_execution_order()

    print("=" * 60)
    print("✅ Advisor 责任链基础演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
