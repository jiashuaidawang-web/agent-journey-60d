"""
Day 9: Simple LangGraph.

最简单的 LangGraph：理解 State + Node + Edge。

Usage:
    python simple_graph.py
"""


def simple_graph():
    """最简单的 Graph：一个节点。"""
    from typing import TypedDict
    from langgraph.graph import StateGraph, START, END

    # 1. 定义 State
    class State(TypedDict):
        message: str

    # 2. 定义 Node
    def greet_node(state: State):
        print(f"收到 State: {state}")
        return {"message": f"Hello, {state['message']}!"}

    # 3. 创建 Graph
    graph = StateGraph(State)
    graph.add_node("greet", greet_node)
    graph.add_edge(START, "greet")
    graph.add_edge("greet", END)

    # 4. 编译 + 运行
    app = graph.compile()
    result = app.invoke({"message": "World"})

    print(f"结果: {result}")
    return result


def two_node_graph():
    """两个节点的 Graph。"""
    from typing import TypedDict
    from langgraph.graph import StateGraph, START, END

    class State(TypedDict):
        input_text: str
        processed: str
        final: str

    def process_node(state: State):
        processed = state["input_text"].upper()
        print(f"处理: {state['input_text']} → {processed}")
        return {"processed": processed}

    def final_node(state: State):
        final = f"[{state['processed']}]"
        print(f"最终: {final}")
        return {"final": final}

    graph = StateGraph(State)
    graph.add_node("process", process_node)
    graph.add_node("final", final_node)
    graph.add_edge(START, "process")
    graph.add_edge("process", "final")
    graph.add_edge("final", END)

    app = graph.compile()
    result = app.invoke({"input_text": "hello world"})

    print(f"结果: {result}")
    return result


def graph_with_state_accumulation():
    """State 累积更新。"""
    from typing import TypedDict
    from langgraph.graph import StateGraph, START, END

    class State(TypedDict):
        messages: list

    def node_a(state: State):
        return {"messages": [*state["messages"], "A"]}

    def node_b(state: State):
        return {"messages": [*state["messages"], "B"]}

    def node_c(state: State):
        return {"messages": [*state["messages"], "C"]}

    graph = StateGraph(State)
    graph.add_node("a", node_a)
    graph.add_node("b", node_b)
    graph.add_node("c", node_c)
    graph.add_edge(START, "a")
    graph.add_edge("a", "b")
    graph.add_edge("b", "c")
    graph.add_edge("c", END)

    app = graph.compile()
    result = app.invoke({"messages": []})

    print(f"结果: {result}")
    assert result["messages"] == ["A", "B", "C"]
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("Simple Graph")
    print("=" * 60)
    simple_graph()

    print("\n" + "=" * 60)
    print("Two Node Graph")
    print("=" * 60)
    two_node_graph()

    print("\n" + "=" * 60)
    print("State Accumulation")
    print("=" * 60)
    graph_with_state_accumulation()
