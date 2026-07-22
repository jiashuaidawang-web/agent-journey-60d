"""
Day 1: Streaming LLM Chat Client.

Usage:
    python stream_chat.py "写一篇关于AI Agent的短文"
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


def stream_chat(prompt: str) -> None:
    """Streaming chat completion call — outputs token by token."""
    try:
        from openai import OpenAI
        from model_config import ModelConfig
    except ImportError:
        print("❌ 请先安装依赖: pip install openai pydantic")
        print("   并配置 .env 文件")
        sys.exit(1)

    api_key = os.getenv("OPENAI_API_KEY", "your-key-here")
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model = os.getenv("MODEL_NAME", "gpt-4o")

    config = ModelConfig(
        api_key=api_key,
        base_url=base_url,
        model_name=model,
    )

    client = OpenAI(**config.get_client_kwargs())

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    print(f"\n📝 User: {prompt}\n")
    print("🤖 Assistant: ", end="", flush=True)

    total_tokens = 0
    stream = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
        if chunk.usage:
            total_tokens = chunk.usage.total_tokens

    print(f"\n\n✅ Done ({total_tokens} tokens)\n")


if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "写一篇关于AI Agent的短文"
    stream_chat(prompt)
