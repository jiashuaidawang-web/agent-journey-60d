"""
Day 8: LangChain Basics.

快速了解 LangChain 核心概念：Runnable、LCEL、Tool。

Usage:
    python langchain_basics.py
"""

import os


def runnable_basics():
    """演示 Runnable 和 LCEL。"""
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI

    # 创建组件
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的{role}。"),
        ("human", "{question}"),
    ])
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    parser = StrOutputParser()

    # LCEL 链式调用：prompt | model | parser
    chain = prompt | model | parser

    # invoke 同步调用
    result = chain.invoke({
        "role": "Java架构师",
        "question": "请用一句话解释 Spring Boot 自动配置",
    })

    print("=" * 60)
    print("LCEL 链式调用")
    print("=" * 60)
    print(f"结果: {result}")

    return chain


def tool_basics():
    """演示 LangChain Tool 定义。"""
    from langchain_core.tools import tool

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

    print("\n" + "=" * 60)
    print("LangChain Tool")
    print("=" * 60)

    # 测试工具
    print(f"天气: {get_weather.invoke('北京')}")
    print(f"计算: {calculator.invoke('123 * 456')}")

    # 查看工具定义
    print(f"\n工具名: {get_weather.name}")
    print(f"工具描述: {get_weather.description}")

    return [get_weather, calculator]


def stream_basics():
    """演示流式调用。"""
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI

    prompt = ChatPromptTemplate.from_messages([
        ("human", "用一句话形容{topic}"),
    ])
    model = ChatOpenAI(model="gpt-4o-mini")

    chain = prompt | model

    print("\n" + "=" * 60)
    print("流式调用")
    print("=" * 60)

    for chunk in chain.stream({"topic": "编程"}):
        print(chunk.content, end="", flush=True)

    print()


if __name__ == "__main__":
    runnable_basics()
    tool_basics()
    stream_basics()
