"""
================================================================================
Day 7 - Mini Agent Runtime - 运行示例 | examples/run_agent.py
================================================================================

【学习目标】
使用自己写的 Runtime 创建一个 Agent 并运行

【前置知识】
- mini_agent_runtime/core/__init__.py（核心模块）
- mini_agent_runtime/model/__init__.py（模型抽象）
- mini_agent_runtime/tools/__init__.py（工具系统）
- mini_agent_runtime/memory/__init__.py（记忆系统）

【操作步骤】
1. 运行: python examples/run_agent.py
2. 观察输出：Agent 执行过程

【预期输出】
Mini Agent Runtime 示例
============================================================

📝 用户: 今天北京天气怎么样
🤖 Agent: 北京今天晴，气温25°C
----------------------------------------

📝 用户: 计算 123 * 456
🤖 Agent: 123 * 456 = 56088
----------------------------------------

📝 用户: 贵州茅台当前价格是多少
🤖 Agent: 贵州茅台 当前1680元，+1.5%
----------------------------------------

【验证标准】
□ 能看到 Agent 执行 3 个任务
□ 能看到工具调用结果
□ 理解 Runtime 的使用方式

================================================================================
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from mini_agent_runtime.core import Agent
from mini_agent_runtime.model import OpenAIModel
from mini_agent_runtime.tools import create_default_registry
from mini_agent_runtime.memory import Memory


def main():
    """运行示例 Agent。"""
    # 1. 创建 Model
    model = OpenAIModel(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    )

    # 2. 创建 Tool Registry
    registry = create_default_registry()

    # 3. 创建 Memory
    memory = Memory(max_entries=5)

    # 4. 创建 Agent
    agent = Agent(
        model=model,
        registry=registry,
        system_prompt="你是一个有用的助手，可以使用工具来帮助用户。",
        memory=memory,
        max_iterations=5,
    )

    # 5. 运行
    print("=" * 60)
    print("Mini Agent Runtime 示例")
    print("=" * 60)

    test_cases = [
        "今天北京天气怎么样",
        "计算 123 * 456",
        "贵州茅台当前价格是多少",
    ]

    for user_input in test_cases:
        print(f"\n📝 用户: {user_input}")
        response = agent.run(user_input)
        print(f"🤖 Agent: {response}")
        print("-" * 40)


if __name__ == "__main__":
    main()
