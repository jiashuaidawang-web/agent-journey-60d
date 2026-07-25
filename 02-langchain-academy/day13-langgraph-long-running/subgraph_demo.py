"""
Day 13: Subgraph Demo.

演示子图的使用。

Usage:
    python subgraph_demo.py
"""


def subgraph_demo():
    """子图演示。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    # 子图 State
    class SubState(TypedDict):
        sub_messages: Annotated[list, add_messages]
        sub_result: str

    # 子图节点
    def sub_node_1(state: SubState):
        return {"sub_messages": ["子图节点1执行"]}

    def sub_node_2(state: SubState):
        return {"sub_result": "子图处理完成"}

    # 创建子图
    sub_graph = StateGraph(SubState)
    sub_graph.add_node("sub_1", sub_node_1)
    sub_graph.add_node("sub_2", sub_node_2)
    sub_graph.add_edge(START, "sub_1")
    sub_graph.add_edge("sub_1", "sub_2")
    sub_graph.add_edge("sub_2", END)

    subgraph = sub_graph.compile()

    # 父图 State
    class ParentState(TypedDict):
        messages: Annotated[list, add_messages]
        sub_result: str
        final_result: str

    # 父图节点
    def parent_start(state: ParentState):
        return {"messages": ["父图开始"]}

    def parent_end(state: ParentState):
        return {"final_result": f"完成: {state.get('sub_result', '')}"}

    # 创建父图
    parent_graph = StateGraph(ParentState)
    parent_graph.add_node("start", parent_start)
    parent_graph.add_node("sub_task", subgraph)  # 子图作为节点
    parent_graph.add_node("end", parent_end)

    parent_graph.add_edge(START, "start")
    parent_graph.add_edge("start", "sub_task")
    parent_graph.add_edge("sub_task", "end")
    parent_graph.add_edge("end", END)

    app = parent_graph.compile()

    print("=" * 60)
    print("Subgraph Demo")
    print("=" * 60)

    result = app.invoke({"messages": ["Hello"]})

    print(f"结果: {result}")
    return result


if __name__ == "__main__":
    subgraph_demo()
