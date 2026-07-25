"""
================================================================================
Day 4 - Function Calling 演示 | 01_function_calling_demo.py
================================================================================

【学习目标】
完整的 Tool Calling 流程：定义工具 → 发送请求 → 执行工具 → 反馈结果

【前置知识】
- 00_tool.py（工具定义）

【操作步骤】
1. 运行: python 01_function_calling_demo.py
2. 观察输出：完整 Function Calling 流程

【预期输出】
Function Calling Demo
============================================================
📝 用户输入: 今天北京天气怎么样，另外帮我计算 123 * 456

📤 发送请求（带工具定义）...
🔧 LLM 决定调用 2 个工具:

  [1] 🔧 调用工具: get_weather
      参数: {"city": "北京"}
      结果: 北京今天晴，气温25°C，湿度40%

  [2] 🔧 调用工具: calculator
      参数: {"expression": "123 * 456"}
      结果: 123 * 456 = 56088

📤 把工具结果反馈给 LLM...
✅ 最终回复:
北京今天天气晴朗，气温25°C，湿度40%，适合出行。
另外，123 乘以 456 的结果是 56088。

【验证标准】
□ 能看到 LLM 决定调用哪些工具
□ 能看到工具执行结果
□ 能看到 LLM 基于工具结果生成最终回复
□ 理解"LLM 只选择不执行"的设计

【代码要点】
- tools=get_tools_definition(): 发送工具定义
- tool_choice="auto": 自动决定是否调用工具
- tool_calls: LLM 返回的工具调用请求
- execute_tool_call(): 程序执行工具（不是 LLM）

================================================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tool import ALL_TOOLS, CalculatorTool, WeatherTool, StockTool
from model_config import ModelConfig


def get_tools_definition() -> list[dict]:
    """获取所有工具的定义（OpenAI API 格式）。"""
    return [tool.to_openai_format() for tool in ALL_TOOLS]


def execute_tool_call(tool_name: str, arguments: dict) -> str:
    """根据工具名称和参数执行工具。

    这是 Tool Calling 的关键步骤：LLM 只决定调用什么，程序负责执行。
    """
    # 查找工具
    tool_map = {tool.name: tool for tool in ALL_TOOLS}

    if tool_name not in tool_map:
        return f"错误: 工具 '{tool_name}' 不存在"

    tool = tool_map[tool_name]

    try:
        result = tool.execute(**arguments)
        return result
    except Exception as e:
        return f"工具执行错误: {e}"


def function_calling_demo():
    """Function Calling 完整流程演示。"""
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ 请先安装依赖: pip install openai")
        sys.exit(1)

    config = ModelConfig.from_env()
    client = OpenAI(**config.get_client_kwargs())

    # 用户输入
    user_input = "今天北京天气怎么样，另外帮我计算 123 * 456"

    print("=" * 60)
    print("Function Calling Demo")
    print("=" * 60)
    print(f"📝 用户输入: {user_input}\n")

    # 1. 构建消息
    messages = [
        {"role": "system", "content": "你是一个有用的助手，可以使用工具来帮助用户。"},
        {"role": "user", "content": user_input},
    ]

    # 2. 发送带工具的请求
    print("📤 发送请求（带工具定义）...")

    response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        tools=get_tools_definition(),
        tool_choice="auto",  # auto / none / specific
    )

    # 3. 检查是否有工具调用
    assistant_message = response.choices[0].message
    tool_calls = assistant_message.tool_calls

    if not tool_calls:
        print(f"✅ 无需调用工具，直接回复: {assistant_message.content}")
        return

    # 4. 有工具调用
    print(f"🔧 LLM 决定调用 {len(tool_calls)} 个工具:\n")

    # 把 assistant 消息加入历史
    messages.append(assistant_message)

    # 5. 逐个执行工具
    for i, tool_call in enumerate(tool_calls):
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)

        print(f"  [{i+1}] 🔧 调用工具: {tool_name}")
        print(f"      参数: {tool_args}")

        # 执行工具（关键：程序执行，不是LLM执行）
        result = execute_tool_call(tool_name, tool_args)
        print(f"      结果: {result}\n")

        # 把工具结果加入消息历史
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })

    # 6. 把工具结果反馈给 LLM，获取最终回复
    print("📤 把工具结果反馈给 LLM...")

    final_response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        tools=get_tools_definition(),
    )

    final_message = final_response.choices[0].message.content

    print(f"✅ 最终回复:\n{final_message}")


if __name__ == "__main__":
    function_calling_demo()
