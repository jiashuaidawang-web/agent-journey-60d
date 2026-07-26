"""
================================================================================
Day 1 - 异步并发诊断 | debug_async.py
================================================================================

【用途】
测试 asyncio 是否真的并发，排除 API/Ollama 的影响

【运行】
python debug_async.py
================================================================================
"""

import asyncio
import time


async def mock_request(name: str, delay: float = 2.0) -> str:
    """模拟一个耗时任务（不需要 API）"""
    print(f"🚀 开始 {name}")
    await asyncio.sleep(delay)  # 模拟 I/O 等待
    print(f"✅ 完成 {name}")
    return f"{name} 结果"


async def test_concurrency():
    """测试并发效果"""
    print("=" * 50)
    print("测试 1：并发执行（asyncio.gather）")
    print("=" * 50)

    start = time.time()

    # 并发执行 3 个任务
    tasks = [
        mock_request("任务A", 2.0),
        mock_request("任务B", 2.0),
        mock_request("任务C", 2.0),
    ]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start
    print(f"\n⏱️  并发总耗时: {elapsed:.2f}s")
    print(f"   预期: ~2.0s（如果真正并发）")
    print(f"   如果 >5s 说明并发没生效")

    print("\n" + "=" * 50)
    print("测试 2：串行执行（for 循环）")
    print("=" * 50)

    start = time.time()

    # 串行执行
    results = []
    for name in ["任务X", "任务Y", "任务Z"]:
        result = await mock_request(name, 2.0)
        results.append(result)

    elapsed = time.time() - start
    print(f"\n⏱️  串行总耗时: {elapsed:.2f}s")
    print(f"   预期: ~6.0s")


if __name__ == "__main__":
    asyncio.run(test_concurrency())
