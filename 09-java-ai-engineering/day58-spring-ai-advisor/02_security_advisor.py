"""
================================================================================
Day 58 - 安全 Advisor | 02_security_advisor.py
================================================================================

【学习目标】
实现安全 Advisor，理解敏感词过滤和限流机制

【前置知识】
- 00_advisor_chain.py（责任链基础）
- 01_logging_advisor.py（日志 Advisor）

【操作步骤】
1. 阅读本文件，理解安全 Advisor 实现
2. 扩展敏感词库
3. 运行代码，观察输出

【预期输出】
🔒 安全 Advisor
├── 敏感词过滤: ✅
└── 限流: ✅

【验证标准】
□ 能实现敏感词过滤
□ 能实现限流
□ 能处理异常情况

【代码要点】
- 敏感词库: Set<String>
- 限流: RateLimiter (Guava)
- 异常处理: 抛出异常中断请求

================================================================================
"""

import sys
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set


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


class SensitiveWordAdvisor(Advisor):
    """敏感词过滤 Advisor。

    检查输入和输出中的敏感词，进行过滤或拒绝。
    """

    def __init__(self, sensitive_words: Optional[Set[str]] = None):
        self.sensitive_words = sensitive_words or {
            "密码", "密钥", "token", "api-key", "secret",
            "身份证", "银行卡", "信用卡"
        }

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        """前置处理：检查输入敏感词。"""
        print(f"   🔒 [SensitiveWord] 检查输入敏感词...")

        for word in self.sensitive_words:
            if word in request.user_text:
                print(f"      ❌ 发现敏感词: {word}")
                raise ValueError(f"输入包含敏感词: {word}")

        print(f"      ✅ 输入检查通过")
        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: AdvisorChain) -> ChatClientResponse:
        """后置处理：过滤输出敏感词。"""
        print(f"   🔒 [SensitiveWord] 过滤输出敏感词...")

        filtered_content = response.content
        for word in self.sensitive_words:
            if word in filtered_content:
                filtered_content = filtered_content.replace(word, "***")
                print(f"      🔄 过滤敏感词: {word}")

        response.content = filtered_content
        return chain.next_after(response)

    def get_order(self) -> int:
        return 10


class RateLimitAdvisor(Advisor):
    """限流 Advisor。

    基于令牌桶算法限制请求频率。
    """

    def __init__(self, max_qps: int = 10):
        self.max_qps = max_qps
        self.tokens = max_qps
        self.last_refill = time.time()

    def _refill_tokens(self):
        """补充令牌。"""
        now = time.time()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.max_qps
        self.tokens = min(self.max_qps, self.tokens + new_tokens)
        self.last_refill = now

    def _try_acquire(self) -> bool:
        """尝试获取令牌。"""
        self._refill_tokens()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        """前置处理：限流检查。"""
        print(f"   ⏱️ [RateLimit] 限流检查 (QPS={self.max_qps})...")

        if not self._try_acquire():
            print(f"      ❌ 请求过于频繁，请稍后再试")
            raise RuntimeError("请求过于频繁，请稍后再试")

        print(f"      ✅ 限流检查通过 (剩余令牌: {self.tokens:.1f})")
        return chain.next_before(request)

    def get_order(self) -> int:
        return 5  # 限流在安全检查之前


def demo_sensitive_word_filter():
    """演示敏感词过滤。"""
    print("🔒 敏感词过滤演示：")
    print("-" * 40)

    advisor = SensitiveWordAdvisor()

    # 正常输入
    print("📤 测试1: 正常输入")
    request1 = AdvisorRequest(user_text="你好，请介绍一下你自己")
    try:
        chain1 = AdvisorChain([advisor])
        chain1.next_before(request1)
        print(f"   ✅ 通过")
    except ValueError as e:
        print(f"   ❌ 拒绝: {e}")

    print()

    # 包含敏感词的输入
    print("📤 测试2: 包含敏感词")
    request2 = AdvisorRequest(user_text="我的密码是123456")
    try:
        chain2 = AdvisorChain([advisor])
        chain2.next_before(request2)
        print(f"   ✅ 通过")
    except ValueError as e:
        print(f"   ❌ 拒绝: {e}")

    print()


def demo_rate_limit():
    """演示限流。"""
    print("⏱️ 限流演示：")
    print("-" * 40)

    advisor = RateLimitAdvisor(max_qps=3)

    for i in range(5):
        print(f"📤 请求 {i+1}:")
        request = AdvisorRequest(user_text=f"请求 {i+1}")
        try:
            chain = AdvisorChain([advisor])
            chain.next_before(request)
            print(f"   ✅ 通过")
        except RuntimeError as e:
            print(f"   ❌ 拒绝: {e}")
        time.sleep(0.1)

    print()


def show_java_code():
    """展示 Java 实现。"""
    print("💻 Java 实现：")
    print("-" * 40)
    print("""
// 敏感词 Advisor
public class SensitiveWordAdvisor implements Advisor {

    private final Set<String> sensitiveWords = Set.of("密码", "密钥", "token");

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        for (String word : sensitiveWords) {
            if (request.userText().contains(word)) {
                throw new SensitiveWordException("输入包含敏感词: " + word);
            }
        }
        return chain.nextBefore(request);
    }
}

// 限流 Advisor
public class RateLimitAdvisor implements Advisor {

    private final RateLimiter rateLimiter = RateLimiter.create(10); // 10 QPS

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        if (!rateLimiter.tryAcquire()) {
            throw new RateLimitExceededException("请求过于频繁");
        }
        return chain.nextBefore(request);
    }
}
""")


def main():
    """主函数：展示安全 Advisor。"""
    print("=" * 60)
    print("🔒 安全 Advisor")
    print("=" * 60)
    print()

    demo_sensitive_word_filter()
    demo_rate_limit()
    show_java_code()

    print("=" * 60)
    print("✅ 安全 Advisor 演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
