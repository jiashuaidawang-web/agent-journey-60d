"""
================================================================================
Day 58 - 日志 Advisor | 01_logging_advisor.py
================================================================================

【学习目标】
实现日志 Advisor，理解前置后置处理和日志记录

【前置知识】
- 00_advisor_chain.py（责任链基础）

【操作步骤】
1. 阅读本文件，理解日志 Advisor 实现
2. 扩展日志内容（耗时、Token 等）
3. 运行代码，观察输出

【预期输出】
📝 日志 Advisor
├── before: 📤 请求: 你好
└── after: 📥 回复: 你好！我是...

【验证标准】
□ 能实现日志 Advisor
□ 能记录请求和响应
□ 能统计耗时

【代码要点】
- before: 记录请求信息
- after: 记录响应信息
- 耗时统计: time.time()

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
        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: 'AdvisorChain') -> ChatClientResponse:
        return chain.next_after(response)

    def get_order(self) -> int:
        return 0


class AdvisorChain:
    """Advisor 责任链。"""

    def __init__(self, advisors: List[Advisor]):
        self.advisors = sorted(advisors, key=lambda a: a.get_order())
        self.before_index = 0
        self.after_index = len(self.advisors) - 1

    def next_before(self, request: AdvisorRequest) -> AdvisorResponse:
        if self.before_index < len(self.advisors):
            advisor = self.advisors[self.before_index]
            self.before_index += 1
            return advisor.before(request, self)
        return AdvisorResponse(
            user_text=request.user_text,
            system_text=request.system_text,
            advise_context=request.advise_context
        )

    def next_after(self, response: ChatClientResponse) -> ChatClientResponse:
        if self.after_index >= 0:
            advisor = self.advisors[self.after_index]
            self.after_index -= 1
            return advisor.after(response, self)
        return response


class LoggingAdvisor(Advisor):
    """日志 Advisor。

    记录每次 AI 调用的请求、响应、耗时等信息。
    """

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        """前置处理：记录请求信息。"""
        print(f"   📝 [Logging] 请求信息：")
        print(f"      User: {request.user_text}")
        print(f"      System: {request.system_text[:50] if request.system_text else '(无)'}")
        print(f"      Context: {request.advise_context}")
        print(f"      Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        # 记录开始时间
        request.advise_context['__start_time'] = time.time()

        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: AdvisorChain) -> ChatClientResponse:
        """后置处理：记录响应信息。"""
        # 计算耗时
        start_time = response.metadata.get('__start_time', time.time())
        elapsed = time.time() - start_time

        print(f"   📝 [Logging] 响应信息：")
        print(f"      Content: {response.content[:50]}...")
        print(f"      Elapsed: {elapsed:.3f}s")
        print(f"      Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")

        return chain.next_after(response)

    def get_order(self) -> int:
        return 0


def demo_logging_advisor():
    """演示日志 Advisor。"""
    print("📝 日志 Advisor 演示：")
    print("-" * 40)

    # 创建 Advisor 链
    chain = AdvisorChain([LoggingAdvisor()])

    # 创建请求
    request = AdvisorRequest(
        user_text="你好，请介绍一下你自己",
        system_text="你是一个AI助手",
        advise_context={"userId": "user-123"}
    )

    print(f"📤 用户输入: {request.user_text}")
    print()

    # 执行 before
    print("⏩ before 处理：")
    response = chain.next_before(request)

    # 模拟 LLM 返回
    llm_response = ChatClientResponse(
        content="你好！我是一个AI助手，可以回答你的问题。",
        metadata={'__start_time': time.time()}
    )

    print()

    # 执行 after
    print("⏪ after 处理：")
    final_response = chain.next_after(llm_response)

    print()
    print(f"✅ 最终回复: {final_response.content}")
    print()


def show_java_code():
    """展示 Java 实现。"""
    print("💻 Java 实现：")
    print("-" * 40)
    print("""
public class LoggingAdvisor implements Advisor {

    private static final Logger log = LoggerFactory.getLogger(LoggingAdvisor.class);

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        log.info("📤 请求: userText={}, userId={}",
            request.userText(),
            request.adviseContext().get("userId"));

        // 记录开始时间
        request.adviseContext().put("__start_time", System.currentTimeMillis());

        return chain.nextBefore(request);
    }

    @Override
    public ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
        long startTime = (Long) response.adviseContext().get("__start_time");
        long elapsed = System.currentTimeMillis() - startTime;

        log.info("📥 回复: content={}, elapsed={}ms",
            response.getResult().getOutput().getContent(),
            elapsed);

        return chain.nextAfter(response);
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
""")


def main():
    """主函数：展示日志 Advisor。"""
    print("=" * 60)
    print("📝 日志 Advisor")
    print("=" * 60)
    print()

    demo_logging_advisor()
    show_java_code()

    print("=" * 60)
    print("✅ 日志 Advisor 演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
