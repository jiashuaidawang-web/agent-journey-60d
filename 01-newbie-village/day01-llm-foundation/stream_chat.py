import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.Model_config import ModelConfig


def stream_chat(prompt: str, sys_prompt: str):
    """
        通过Model_Config 封装好的env，组装 userPrompt 跟 sysPrompt 请求OpenAiChat
    """

    # 代码健壮性
    try:
        from openai import OpenAI
    except ImportError:
        print("importError")
        raise ImportError("Please install OpenAI to use stream_chat")
        sys.exit("Please install OpenAI")

    config = ModelConfig.from_env()

    # 判断ModelConfig为空判断
    if not config.api_key or config.api_key == "":
        sys.exit("Please install OpenAI to use stream_chat")

    # 初始化OpenAI客户端
    client = OpenAI(**config.get_client_kwargs())

    # 组装参数
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
        stream=True
    )
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content)



if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "写一首关于编程的诗"
    stream_chat(prompt,"")