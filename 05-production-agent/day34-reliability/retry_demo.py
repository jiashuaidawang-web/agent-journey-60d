"""
Day 34: Reliability Demo.

演示 Retry 和 Circuit Breaker。

Usage:
    python retry_demo.py
"""


import time
import random


class RetryConfig:
    """Retry 配置。"""

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0,
                 max_delay: float = 60.0, exponential_backoff: bool = True):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_backoff = exponential_backoff


def with_retry(func, config: RetryConfig = None):
    """Retry 装饰器。"""
    if config is None:
        config = RetryConfig()

    def wrapper(*args, **kwargs):
        last_exception = None

        for attempt in range(config.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e

                if attempt < config.max_retries:
                    if config.exponential_backoff:
                        delay = min(config.base_delay * (2 ** attempt), config.max_delay)
                    else:
                        delay = config.base_delay

                    print(f"   重试 {attempt + 1}/{config.max_retries}, 等待 {delay:.1f}s...")
                    time.sleep(delay)

        raise last_exception

    return wrapper


class CircuitBreaker:
    """Circuit Breaker。"""

    CLOSED = "closed"       # 正常
    OPEN = "open"           # 断开
    HALF_OPEN = "half_open" # 半开

    def __init__(self, failure_threshold: int = 5, recovery_timeout: float = 30.0):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.state = self.CLOSED
        self.failure_count = 0
        self.last_failure_time = 0

    def call(self, func, *args, **kwargs):
        """调用函数。"""
        if self.state == self.OPEN:
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = self.HALF_OPEN
            else:
                raise Exception("Circuit Breaker is OPEN")

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise e

    def _on_success(self):
        self.failure_count = 0
        self.state = self.CLOSED

    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.failure_count >= self.failure_threshold:
            self.state = self.OPEN


def retry_demo():
    """Retry 演示。"""
    print("=" * 60)
    print("Retry Demo")
    print("=" * 60)

    # 模拟不稳定的 API
    call_count = 0

    @with_retry(RetryConfig(max_retries=3, base_delay=0.5))
    def unstable_api():
        nonlocal call_count
        call_count += 1

        if call_count < 3:
            raise Exception(f"API 调用失败 (第 {call_count} 次)")

        return f"API 调用成功 (第 {call_count} 次)"

    print("\n🔄 Retry 测试:")
    result = unstable_api()
    print(f"   结果: {result}")


def circuit_breaker_demo():
    """Circuit Breaker 演示。"""
    print("\n" + "=" * 60)
    print("Circuit Breaker Demo")
    print("=" * 60)

    cb = CircuitBreaker(failure_threshold=3, recovery_timeout=2.0)

    # 模拟总是失败的 API
    def failing_api():
        raise Exception("API 调用失败")

    print("\n🔌 Circuit Breaker 测试:")

    # 前 3 次调用
    for i in range(3):
        try:
            cb.call(failing_api)
        except Exception as e:
            print(f"   调用 {i+1}: {e}")

    # 第 4 次（Circuit Breaker 应该断开）
    try:
        cb.call(failing_api)
    except Exception as e:
        print(f"   调用 4: {e}")

    print(f"   状态: {cb.state}")


if __name__ == "__main__":
    retry_demo()
    circuit_breaker_demo()
