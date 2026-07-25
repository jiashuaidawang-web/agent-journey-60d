"""
Day 1: Streaming LLM Chat Client.

流式调用：逐 token 返回，提升用户体验。
核心指标：TTFT（首Token时间）+ TPS（每秒Token数）

Usage:
    python stream_chat.py "写一首关于编程的诗"
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from model_config import ModelConfig


def stream_chat(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    """流式调用 LLM。

    逐字打印输出，统计 TTFT 和 TPS。

    Args:
        prompt: 用户输入
        system_prompt: 系统提示词

    Returns:
        完整回复文本
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ 请先安装依赖: pip install openai")
        sys.exit(1)

    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        sys.exit(1)

    client = OpenAI(**config.get_client_kwargs())

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    print(f"📤 发送流式请求到 {config.model_name}...")
    print(f"   User: {prompt}")
    print(f"\n📡 等待首Token...\n")

    start_time = time.time()
    first_token_time = None
    token_count = 0
    full_response = []

    response_stream = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        stream=True,  # 关键：开启流式
    )

    for chunk in response_stream:
        if chunk.choices and chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content

            # 记录首Token时间
            if first_token_time is None:
                first_token_time = time.time() - start_time
                print(f"⚡ TTFT: {first_token_time:.3f}s\n")

            print(content, end="", flush=True)
            full_response.append(content)
            token_count += 1

    total_time = time.time() - start_time
    tps = token_count / total_time if total_time > 0 else 0

    result = "".join(full_response)

    print(f"\n\n📊 统计:")
    if first_token_time:
        print(f"   TTFT (首Token时间): {first_token_time:.3f}s")
    print(f"   Tokens:              {token_count}")
    print(f"   TPS (每秒Token数):   {tps:.1f}")
    print(f"   总耗时:              {total_time:.2f}s")

    return result


if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "写一首关于编程的诗"
    stream_chat(prompt)
