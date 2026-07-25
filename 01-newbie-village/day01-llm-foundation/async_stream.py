"""
Day 1: Async Streaming LLM Chat Client.

异步流式调用：生产级 Agent 的基础。
多个请求同时流式输出，交错显示。

Usage:
    python async_stream.py
"""

import asyncio
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from model_config import ModelConfig


async def async_stream_single(
    request_id: int,
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
) -> str:
    """单次异步流式调用。"""
    from openai import AsyncOpenAI

    config = ModelConfig.from_env()
    client = AsyncOpenAI(**config.get_client_kwargs())

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    print(f"[请求{request_id}] 📤 发送: {prompt}")

    start_time = time.time()
    first_token_time = None
    token_count = 0
    full_response = []

    response_stream = await client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=256,  # 限制长度，方便演示
        stream=True,
    )

    async for chunk in response_stream:
        if chunk.choices and chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content

            if first_token_time is None:
                first_token_time = time.time() - start_time
                print(f"[请求{request_id}] ⚡ TTFT: {first_token_time:.3f}s")

            print(f"[请求{request_id}] {content}", end="", flush=True)
            full_response.append(content)
            token_count += 1

    total_time = time.time() - start_time
    tps = token_count / total_time if total_time > 0 else 0

    print(f"\n[请求{request_id}] ✅ 完成 | Tokens: {token_count} | TPS: {tps:.1f} | 耗时: {total_time:.2f}s")

    return "".join(full_response)


async def async_stream_concurrent():
    """并发多个异步流式请求。"""
    prompts = [
        (1, "用一句话形容春天"),
        (2, "用一句话形容编程"),
        (3, "用一句话形容 AI"),
    ]

    print(f"🚀 并发发送 {len(prompts)} 个流式请求...\n")

    start_time = time.time()

    tasks = [
        async_stream_single(req_id, prompt)
        for req_id, prompt in prompts
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    total_time = time.time() - start_time

    print(f"\n📊 全部完成 | 总耗时: {total_time:.2f}s")
    print(f"   如果是串行，预计需要: ~{total_time * 1.0:.2f}s")


if __name__ == "__main__":
    asyncio.run(async_stream_concurrent())
