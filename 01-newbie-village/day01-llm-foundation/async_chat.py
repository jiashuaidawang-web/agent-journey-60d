import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.Model_config import ModelConfig
import asyncio

async def async_chat_single(
        prompt: str,
        system_prompt: str = "You are a helpful assistant."
) -> str:
    # 单次异步调用
    from openai import AsyncOpenAI

    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        sys.exit()

    client = AsyncOpenAI(**config.get_client_kwargs())

    messages = [
        {"role":"system","content":system_prompt},
        {"role":"user","content":prompt},
    ]

    response = await client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    return response.choices[0].message.content


async def async_chat_concurrent():
    prompts = [
        "用一句话介绍 Python",
        "用一句话介绍 Java",
        "用一句话介绍 AI Agent",
    ]

    tasks = [async_chat_single(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i in results:
        print(i)



if __name__ == "__main__":
    asyncio.run(async_chat_concurrent())