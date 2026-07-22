"""
Day 1: Synchronous LLM Chat Client.

Usage:
    python sync_chat.py "你好，请介绍一下你自己"
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


def sync_chat(prompt: str) -> str:
    """Synchronous chat completion call."""
    try:
        from openai import OpenAI
        from model_config import ModelConfig
    except ImportError:
        print("❌ 请先安装依赖: pip install openai pydantic")
        print("   并配置 .env 文件")
        sys.exit(1)

    # Load config from environment
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

    response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    result = response.choices[0].message.content
    print(f"\n✅ Response ({response.usage.total_tokens} tokens):")
    print(f"   {result}\n")
    return result


if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "你好，请介绍一下你自己"
    sync_chat(prompt)
