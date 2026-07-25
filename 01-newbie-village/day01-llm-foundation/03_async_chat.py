"""
================================================================================
Day 1 - 异步调用 | 03_async_chat.py
================================================================================

【学习目标】
理解 LLM 异步调用：使用 asyncio 并发多个请求，对比同步 vs 异步耗时

【前置知识】
- Model_config.py（模型配置）
- 01_sync_chat.py（同步调用）

【操作步骤】
1. 运行: python 03_async_chat.py
2. 观察输出：并发发送 3 个请求，总耗时 < 串行耗时

【预期输出】
🚀 并发发送 3 个请求...

✅ 请求1: 用一句话介绍 Python
   → Python 是一种...

✅ 请求2: 用一句话介绍 Java
   → Java 是一种...

✅ 请求3: 用一句话介绍 AI Agent
   → AI Agent 是...

📊 并发总耗时: 1.5s
   如果是串行执行，预计: ~4.2s

【验证标准】
□ 能看到 3 个请求并发执行
□ 并发总耗时 < 串行耗时
□ 理解 async def / await / asyncio.gather

【代码要点】
- AsyncOpenAI: 异步客户端
- async def: 异步函数
- asyncio.gather(): 并发执行多个协程

================================================================================
"""

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Model_config import ModelConfig


async def async_chat_single(
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
) -> str:
    """单次异步 LLM 调用。"""
    from openai import AsyncOpenAI

    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        raise ValueError("Missing API key")

    client = AsyncOpenAI(**config.get_client_kwargs())

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    response = await client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return response.choices[0].message.content


async def async_chat_concurrent():
    """并发多个异步请求，对比同步耗时。"""
    prompts = [
        "用一句话介绍 Python",
        "用一句话介绍 Java",
        "用一句话介绍 AI Agent",
    ]

    print(f"🚀 并发发送 {len(prompts)} 个请求...\n")

    start_time = time.time()

    # asyncio.gather 并发执行
    tasks = [async_chat_single(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    total_time = time.time() - start_time

    # 打印结果
    for i, (prompt, result) in enumerate(zip(prompts, results)):
        if isinstance(result, Exception):
            print(f"❌ 请求{i+1}失败: {result}")
        else:
            # 截断显示
            short_result = result[:50] + "..." if len(result) > 50 else result
            print(f"✅ 请求{i+1}: {prompt}")
            print(f"   → {short_result}")
        print()

    print(f"📊 并发总耗时: {total_time:.2f}s")
    print(f"   如果是串行执行，预计: ~{total_time * 1.0:.2f}s（单次约 {total_time / len(prompts):.2f}s）")


if __name__ == "__main__":
    asyncio.run(async_chat_concurrent())
