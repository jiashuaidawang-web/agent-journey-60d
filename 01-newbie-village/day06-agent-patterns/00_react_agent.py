"""
================================================================================
Day 6 - ReAct Agent | 00_react_agent.py
================================================================================

【学习目标】
实现 ReAct Agent：Thought → Action → Observation 循环

【前置知识】
- Day 4 Tool Calling
- Day 5 Agent Loop

【操作步骤】
1. 运行: python 00_react_agent.py
2. 观察输出：ReAct 执行过程

【预期输出】
ReAct Agent 启动
============================================================
📝 任务: 计算 123 * 456 的结果

─── 迭代 1/5 ───
🤖 LLM 输出:
Thought: 我需要计算 123 * 456，可以使用 calculator 工具
Action: calculator
Action Input: {"expression": "123 * 456"}

🔧 执行工具: calculator({'expression': '123 * 456'})
   结果: 123 * 456 = 56088

─── 迭代 2/5 ───
🤖 LLM 输出:
Thought: 我已经得到了计算结果
Final Answer: 123 * 456 的结果是 56088

✅ 最终答案: 123 * 456 的结果是 56088

【验证标准】
□ 能看到 Thought → Action → Observation 循环
□ 能看到工具执行
□ 能看到最终答案
□ 理解 ReAct 模式的核心思想

【代码要点】
- SYSTEM_PROMPT: 定义 ReAct 格式
- Thought/Action/Observation: 三步循环
- Final Answer: 结束条件

================================================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from registry import create_default_registry
from utils.Model_config import ModelConfig


class ReActAgent:
    """ReAct Agent。

    核心循环：
    1. Thought: LLM 思考下一步该做什么
    2. Action: LLM 决定调用工具
    3. Observation: 获取工具执行结果
    4. 重复 1-3 直到得出结论
    """

    SYSTEM_PROMPT = """你是一个使用 ReAct（Reason + Act）模式的助手。

每次回复必须遵循以下格式：
Thought: [你的推理思考]
Action: [工具名称]
Action Input: [工具参数，JSON格式]

或者，当你有最终答案时：
Thought: [你的推理思考]
Final Answer: [最终回答]

可用工具：
- calculator: 执行数学计算
- get_weather: 获取城市天气
- get_stock_price: 获取股票价格

请严格遵循格式，每次只输出一个 Thought + Action 或 Final Answer。
"""

    def __init__(self, max_iterations: int = 5):
        self.registry = create_default_registry()
        self.max_iterations = max_iterations

    def run(self, user_input: str) -> str:
        """运行 ReAct Agent。"""
        try:
            from openai import OpenAI
        except ImportError:
            print("❌ 请先安装依赖: pip install openai")
            sys.exit(1)

        config = ModelConfig.from_env()
        client = OpenAI(**config.get_client_kwargs())

        # 初始化消息
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ]

        print("=" * 60)
        print("ReAct Agent 启动")
        print("=" * 60)
        print(f"📝 任务: {user_input}\n")

        for iteration in range(1, self.max_iterations + 1):
            print(f"─── 迭代 {iteration}/{self.max_iterations} ───")

            # 发送消息给 LLM
            response = client.chat.completions.create(
                model=config.model_name,
                messages=messages,
                temperature=0.0,
                max_tokens=512,
            )

            llm_output = response.choices[0].message.content.strip()
            print(f"🤖 LLM 输出:\n{llm_output}\n")

            # 解析输出
            if "Final Answer:" in llm_output:
                # 提取最终答案
                final_answer = llm_output.split("Final Answer:")[-1].strip()
                print(f"✅ 最终答案: {final_answer}")
                return final_answer

            # 解析 Action
            if "Action:" in llm_output and "Action Input:" in llm_output:
                action_lines = llm_output.split("\n")
                action_name = ""
                action_input = ""

                for line in action_lines:
                    if line.startswith("Action:"):
                        action_name = line.replace("Action:", "").strip()
                    elif line.startswith("Action Input:"):
                        action_input = line.replace("Action Input:", "").strip()

                # 执行工具
                try:
                    args = json.loads(action_input) if action_input else {}
                except json.JSONDecodeError:
                    args = {"expression": action_input}

                print(f"🔧 执行工具: {action_name}({args})")
                result = self.registry.execute(action_name, args)
                print(f"   结果: {result}\n")

                # 把 Thought + Action + Observation 加入消息
                messages.append({"role": "assistant", "content": llm_output})
                messages.append({
                    "role": "user",
                    "content": f"Observation: {result}\n\n请继续。如果你已经有最终答案，请输出 Final Answer:",
                })
            else:
                # 格式不对，提示 LLM 重新输出
                messages.append({"role": "assistant", "content": llm_output})
                messages.append({
                    "role": "user",
                    "content": "输出格式不正确。请严格按照格式输出：\nThought: ...\nAction: ...\nAction Input: ...\n或者\nThought: ...\nFinal Answer: ...",
                })

        return "达到最大迭代次数，未能完成任务"


def main():
    agent = ReActAgent(max_iterations=5)

    # 测试用例
    test_cases = [
        "计算 123 * 456 的结果",
        "今天北京天气怎么样",
    ]

    for task in test_cases:
        result = agent.run(task)
        print(f"\n{'=' * 60}\n")


if __name__ == "__main__":
    main()
