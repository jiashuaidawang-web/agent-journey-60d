"""
Day 10: Router Graph.

根据用户意图路由到不同 Agent。

Usage:
    python router_graph.py
"""


def router_graph():
    """Router Graph：根据意图路由。"""
    from typing import TypedDict, Annotated, Literal
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langchain_core.messages import HumanMessage
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI

    # 工具
    @tool
    def get_weather(city: str) -> str:
        """获取城市天气。"""
        data = {"北京": "晴，25°C", "上海": "多云，28°C"}
        return data.get(city, f"暂无{city}天气")

    @tool
    def get_stock_price(stock: str) -> str:
        """获取股票价格。"""
        data = {"贵州茅台": "1680元", "宁德时代": "210元"}
        return data.get(stock, f"暂无{stock}行情")

    # State
    class State(TypedDict):
        messages: Annotated[list, add_messages]
        intent: str
        result: str

    # 节点
    def detect_intent(state: State):
        """意图识别节点。"""
        model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        messages = state["messages"]

        response = model.invoke([
            ("system", "识别用户意图：weather/stock/unknown。只输出意图名称。"),
            *messages,
        ])
        intent = response.content.strip().lower()
        return {"intent": intent}

    def weather_agent(state: State):
        """天气 Agent。"""
        model = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools([get_weather])
        response = model.invoke(state["messages"])
        return {"result": response.content or "已查询天气"}

    def stock_agent(state: State):
        """股票 Agent。"""
        model = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools([get_stock_price])
        response = model.invoke(state["messages"])
        return {"result": response.content or "已查询股票"}

    def fallback(state: State):
        """兜底节点。"""
        return {"result": "抱歉，我不太确定你的意思"}

    # 路由函数
    def route_intent(state: State) -> Literal["weather_agent", "stock_agent", "fallback"]:
        intent = state.get("intent", "unknown")
        if "weather" in intent or "天气" in intent:
            return "weather_agent"
        elif "stock" in intent or "股票" in intent:
            return "stock_agent"
        return "fallback"

    # 创建 Graph
    graph = StateGraph(State)
    graph.add_node("detect_intent", detect_intent)
    graph.add_node("weather_agent", weather_agent)
    graph.add_node("stock_agent", stock_agent)
    graph.add_node("fallback", fallback)

    graph.add_edge(START, "detect_intent")
    graph.add_conditional_edges("detect_intent", route_intent, {
        "weather_agent": "weather_agent",
        "stock_agent": "stock_agent",
        "fallback": "fallback",
    })
    graph.add_edge("weather_agent", END)
    graph.add_edge("stock_agent", END)
    graph.add_edge("fallback", END)

    # 编译 + 运行
    app = graph.compile()

    print("=" * 60)
    print("Router Graph")
    print("=" * 60)

    result = app.invoke({
        "messages": [HumanMessage(content="今天北京天气怎么样")]
    })

    print(f"意图: {result['intent']}")
    print(f"结果: {result['result']}")

    return result


if __name__ == "__main__":
    router_graph()
