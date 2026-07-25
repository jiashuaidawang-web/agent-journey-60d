"""
Day 10: Multi-Branch Graph.

多分支 Graph：根据条件走不同路径，支持循环。

Usage:
    python multi_branch_graph.py
"""


def multi_branch_graph():
    """多分支 Graph。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        step_count: int
        result: str

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def process_node(state: State):
        """处理节点。"""
        step = state.get("step_count", 0) + 1

        # 模拟处理
        messages = state["messages"]
        last_msg = messages[-1].content if messages else ""

        if "天气" in last_msg:
            result = "天气相关处理完成"
        elif "计算" in last_msg:
            result = "计算相关处理完成"
        else:
            result = "通用处理完成"

        return {
            "step_count": step,
            "result": result,
            "messages": [f"Step {step}: {result}"],
        }

    def should_continue(state: State) -> str:
        """决定是否继续循环。"""
        step = state.get("step_count", 0)
        if step >= 3:
            return "finish"
        return "continue"

    def continue_node(state: State):
        """继续处理。"""
        return {"messages": ["继续处理..."]}

    def finish_node(state: State):
        """结束节点。"""
        return {"result": f"处理完成，共 {state['step_count']} 步"}

    # 创建 Graph
    graph = StateGraph(State)
    graph.add_node("process", process_node)
    graph.add_node("continue", continue_node)
    graph.add_node("finish", finish_node)

    graph.add_edge(START, "process")
    graph.add_conditional_edges("process", should_continue, {
        "continue": "continue",
        "finish": "finish",
    })
    graph.add_edge("continue", "process")  # 循环回 process
    graph.add_edge("finish", END)

    app = graph.compile()

    print("=" * 60)
    print("Multi-Branch Graph")
    print("=" * 60)

    result = app.invoke({
        "messages": [HumanMessage(content="查询天气")],
        "step_count": 0,
    })

    print(f"结果: {result['result']}")
    print(f"步骤: {result['step_count']}")

    return result


if __name__ == "__main__":
    multi_branch_graph()
