import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.Model_config import ModelConfig


def sync_chat(prompt: str, system_prompt: str):
    """同步调用 LLM。

       Args:
           prompt: 用户输入
           system_prompt: 系统提示词

       Returns:
           模型回复文本
       """
    try:
        from openai import OpenAI
    except ImportError:
        raise ImportError("先导入大模型")
    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        sys.exit(1)

    # client = OpenAI(**config.get_client_kwargs())
    client = OpenAI(
        base_url=config.base_url,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=config.model_name,
        messages=message,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )
    result = response.choices[0].message.content
    print(result)
    return result

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "你好，请介绍一下你自己"
    sync_chat(prompt,'')