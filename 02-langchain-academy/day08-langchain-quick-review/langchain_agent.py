"""
Day 8: LangChain Agent.

用 LangChain 实现一个 Tool Calling Agent。

Usage:
    python langchain_agent.py
"""


def run_langchain_agent():
    """用 LangChain 创建 Agent。"""
    from langchain_core.messages import HumanMessage, SystemMessage
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_tool_calling_agent
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

    # 1. 定义工具
    @tool
    def get_weather(city: str) -> str:
        """获取指定城市的天气。"""
        weather_data = {
            "北京": "晴，25°C",
            "上海": "多云，28°C",
            "深圳": "雷阵雨，30°C",
        }
        return weather_data.get(city, f"暂无{city}天气数据")

    @tool
    def calculator(expression: str) -> str:
        """执行数学计算。"""
        try:
            result = eval(expression)
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算错误: {e}"

    tools = [get_weather, calculator]

    # 2. 创建 Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个有用的助手，可以使用工具来帮助用户。"),
        MessagesPlaceholder(variable_name="messages"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    # 3. 创建 Model（绑定工具）
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    model_with_tools = model.bind_tools(tools)

    # 4. 创建 Agent
    agent = create_tool_calling_agent(model_with_tools, tools, prompt)

    # 5. 创建 AgentExecutor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,  # 打印详细执行过程
    )

    # 6. 运行
    print("=" * 60)
    print("LangChain Agent")
    print("=" * 60)

    result = agent_executor.invoke({
        "input": "今天北京天气怎么样，另外计算 123 * 456"
    })

    print(f"\n✅ 最终结果: {result['output']}")
    return result


if __name__ == "__main__":
    run_langchain_agent()
