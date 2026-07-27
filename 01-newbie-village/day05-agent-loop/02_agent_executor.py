"""
================================================================================
Day 5 - Agent 执行器 | 02_agent_executor.py
================================================================================

【学习目标】
实现 AgentExecutor：while 循环 + 工具调用 + 终止条件

【前置知识】
- 00_state.py（状态管理）
- 01_registry.py（工具注册表）

【操作步骤】
1. 运行: python 02_agent_executor.py
2. 观察输出：Agent 执行过程

【预期输出】
Agent Executor 启动
============================================================
📝 用户输入: 今天北京天气怎么样
🔧 可用工具: calculator, get_weather, get_stock_price
🔄 最大迭代: 5

─── 迭代 1/5 ───
  🔧 调用工具: get_weather({'city': '北京'})
     结果: 北京今天晴，气温25°C，湿度40%
─── 迭代 2/5 ───
  ✅ LLM 直接回复

============================================================
Agent 执行完成
============================================================
📊 迭代次数: 2
🔧 工具调用: 1 次
📊 Token 消耗: input=xxx, output=xxx, total=xxx
✅ 最终回复:
北京今天天气晴朗，气温25°C...

【验证标准】
□ 能看到 Agent 执行过程
□ 能看到工具调用
□ 能看到迭代次数统计
□ 理解 while 循环 + 终止条件

【代码要点】
- while not state.finished: 核心循环
- tool_calls: 检查是否有工具调用
- is_max_iterations_reached(): 防止死循环

================================================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from registry import create_default_registry
from state import AgentState
from utils.Model_config import ModelConfig


class AgentExecutor:
    """Agent 执行器。

    核心循环：
    1. 发送消息给 LLM
    2. 如果 LLM 决定调用工具 → 执行工具 → 结果加入消息 → 继续循环
    3. 如果 LLM 直接回复 → 结束
    4. 如果达到最大迭代次数 → 强制结束
    """

    def __init__(
        self,
        registry=None,
        max_iterations: int = 10,
        system_prompt: str = "你是一个有用的助手，可以使用工具来帮助用户。",
    ):
        self.registry = registry or create_default_registry()
        self.max_iterations = max_iterations
        self.system_prompt = system_prompt

    def run(self, user_input: str) -> AgentState:
        """运行 Agent。

        Args:
            user_input: 用户输入

        Returns:
            AgentState: 最终状态
        """
        try:
            from openai import OpenAI
        except ImportError:
            print("❌ 请先安装依赖: pip install openai")
            sys.exit(1)

        config = ModelConfig.from_env()
        client = OpenAI(**config.get_client_kwargs())

        # 初始化状态
        state = AgentState(max_iterations=self.max_iterations)
        state.add_message({"role": "system", "content": self.system_prompt})
        state.add_message({"role": "user", "content": user_input})

        print("=" * 60)
        print("Agent Executor 启动")
        print("=" * 60)
        print(f"📝 用户输入: {user_input}")
        print(f"🔧 可用工具: {', '.join(self.registry.list_names())}")
        print(f"🔄 最大迭代: {self.max_iterations}\n")

        # ====== 核心循环 ======
        while not state.finished:
            state.increment_iteration()
            print(f"─── 迭代 {state.iteration}/{self.max_iterations} ───")

            # 1. 发送消息给 LLM
            response = client.chat.completions.create(
                model=config.model_name,
                messages=state.messages,
                tools=self.registry.get_tools_definition(),
                tool_choice="auto",
            )

            assistant_message = response.choices[0].message

            # 更新 Token 统计
            if response.usage:
                state.update_tokens(response.usage.prompt_tokens, response.usage.completion_tokens)

            # 2. 检查是否有工具调用
            if assistant_message.tool_calls:
                # 把 assistant 消息加入历史
                state.add_message({
                    "role": "assistant",
                    "content": assistant_message.content,
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {"name": tc.function.name, "arguments": tc.function.arguments},
                        }
                        for tc in assistant_message.tool_calls
                    ],
                })

                # 逐个执行工具
                for tool_call in assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)

                    print(f"  🔧 调用工具: {tool_name}({tool_args})")

                    # 执行工具
                    result = self.registry.execute(tool_name, tool_args)
                    success = not result.startswith("错误:")

                    print(f"     结果: {result[:100]}{'...' if len(result) > 100 else ''}")

                    # 记录工具调用
                    state.add_tool_call(tool_name, tool_args, result, success)

                    # 把工具结果加入消息历史
                    state.add_message({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    })

            else:
                # 3. LLM 直接回复，结束循环
                state.mark_finished(assistant_message.content or "")
                print(f"  ✅ LLM 直接回复")

            # 4. 检查是否达到最大迭代次数
            if not state.finished and state.is_max_iterations_reached():
                state.mark_error(f"达到最大迭代次数 {self.max_iterations}")
                print(f"  ⚠️ 达到最大迭代次数，强制结束")

        # 打印总结
        print(f"\n{'=' * 60}")
        print("Agent 执行完成")
        print(f"{'=' * 60}")
        print(f"📊 迭代次数: {state.iteration}")
        print(f"🔧 工具调用: {len(state.tool_calls)} 次")
        print(f"📊 Token 消耗: input={state.input_tokens}, output={state.output_tokens}, total={state.total_tokens}")

        if state.error:
            print(f"❌ 错误: {state.error}")
        else:
            print(f"✅ 最终回复:\n{state.final_response}")

        return state


def main():
    """命令行入口。"""
    executor = AgentExecutor(max_iterations=5)

    # 测试场景
    test_cases = [
        "今天北京天气怎么样",
        "贵州茅台当前价格是多少",
        "计算 123 * 456 + 789",
    ]

    for user_input in test_cases:
        state = executor.run(user_input)
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
