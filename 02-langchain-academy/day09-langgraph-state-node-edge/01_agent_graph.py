"""
Day 9: Agent Graph.

用 LangGraph 实现 Agent + Tool Calling。

Usage:
    python agent_graph.py
"""


def agent_graph():
    """Agent Graph：agent 节点 + tools 节点 + 条件边。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langchain_core.messages import HumanMessage, AIMessage
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI

    # 1. 定义工具
    @tool
    def get_weather(city: str) -> str:
        """获取城市天气。"""
        data = {"北京": "晴，25°C", "上海": "多云，28°C"}
        return data.get(city, f"暂无{city}天气")

    @tool
    def calculator(expression: str) -> str:
        """数学计算。"""
        try:
            return f"{expression} = {eval(expression)}"
        except Exception as e:
            return f"错误: {e}"

    tools = [get_weather, calculator]
    tools_by_name = {t.name: t for t in tools}

    # 2. 定义 State
    class State(TypedDict):
        messages: Annotated[list, add_messages]

    # 3. 定义 Node
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)

    def agent_node(state: State):
        """Agent 节点：调用 LLM。"""
        messages = state["messages"]
        response = model.invoke(messages)
        return {"messages": [response]}

    def tools_node(state: State):
        """Tools 节点：执行工具调用。"""
        messages = state["messages"]
        last_message = messages[-1]

        results = []
        for tool_call in last_message.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            tool_to_run = tools_by_name.get(tool_name)
            if tool_to_run:
                result = tool_to_run.invoke(tool_args)
            else:
                result = f"工具 '{tool_name}' 不存在"

            results.append(
                {"role": "tool", "tool_call_id": tool_call["id"], "content": result}
            )

        return {"messages": results}

    # 4. 条件边：决定是否继续调用工具
    def should_continue(state: State):
        messages = state["messages"]
        last_message = messages[-1]

        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END

    # 5. 创建 Graph
    graph = StateGraph(State)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", tools_node)

    graph.add_edge(START, "agent")
    graph.add_conditional_edges("agent", should_continue, {
        "tools": "tools",
        END: END,
    })
    graph.add_edge("tools", "agent")

    # 6. 编译 + 运行
    app = graph.compile()

    print("=" * 60)
    print("Agent Graph")
    print("=" * 60)

    result = app.invoke({
        "messages": [HumanMessage(content="今天北京天气怎么样")]
    })

    print(f"\n✅ 最终回复: {result['messages'][-1].content}")

    # 打印所有消息
    print(f"\n📋 消息历史:")
    for msg in result["messages"]:
        print(f"   {type(msg).__name__}: {msg.content[:60]}...")

    return result


if __name__ == "__main__":
    agent_graph()
