"""
================================================================================
Day 1 - 同步调用 | 01_sync_chat.py
================================================================================

【学习目标】
理解 LLM 同步调用的完整流程：用户输入 → LLM → 完整返回

【前置知识】
- Model_config.py（模型配置）

【操作步骤】
1. 确保 .env 文件中已配置 OPENAI_API_KEY
2. 运行: python 01_sync_chat.py "你好，请介绍一下你自己"
3. 观察输出：回复内容 + Token 统计 + 耗时

【预期输出】
📤 发送请求到 gpt-4o-mini...
   System: You are a helpful assistant.
   User: 你好，请介绍一下你自己

✅ Response:
   你好！我是一个AI助手，可以回答你的问题...

📊 统计:
   Input Tokens:  15
   Output Tokens: 45
   Total Tokens:  60
   耗时:          1.2s

【验证标准】
□ 能看到完整回复
□ 能看到 Token 统计（Input/Output/Total）
□ 能看到耗时
□ 尝试修改 temperature 参数，观察输出变化

【代码要点】
- client.chat.completions.create(): 同步调用
- response.choices[0].message.content: 获取回复
- response.usage: 获取 Token 统计

================================================================================
"""

import sys
import time
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Model_config import ModelConfig



def sync_chat(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
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
        print("❌ 请先安装依赖: pip install openai")
        sys.exit(1)

    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        print("   或在 .env 文件中配置")
        sys.exit(1)

    client = OpenAI(**config.get_client_kwargs())

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    print(f"📤 发送请求到 {config.model_name}...")
    print(f"   System: {system_prompt}")
    print(f"   User: {prompt}")
    print()

    start_time = time.time()

    response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=config.temperature,
        max_tokens=config.max_tokens,
    )

    elapsed = time.time() - start_time
    result = response.choices[0].message.content

    # 打印结果
    print(f"✅ Response:")
    print(f"   {result}")
    print()

    # 打印统计
    usage = response.usage
    print(f"📊 统计:")
    print(f"   Input Tokens:  {usage.prompt_tokens}")
    print(f"   Output Tokens: {usage.completion_tokens}")
    print(f"   Total Tokens:  {usage.total_tokens}")
    print(f"   耗时:          {elapsed:.2f}s")

    return result


if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "你好，请介绍一下你自己"
    sync_chat(prompt)
