"""
Day 11: Checkpoint Demo.

演示 LangGraph 的 Checkpoint 机制。

Usage:
    python checkpoint_demo.py
"""


def checkpoint_demo():
    """Checkpoint 演示。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI
    from langgraph.checkpoint.memory import MemorySaver

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        step: int

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def step_node(state: State):
        step = state.get("step", 0) + 1
        return {
            "step": step,
            "messages": [f"Step {step} executed"],
        }

    graph = StateGraph(State)
    graph.add_node("step", step_node)
    graph.add_edge(START, "step")
    graph.add_edge("step", END)

    # 使用 MemorySaver 保存 Checkpoint
    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer)

    print("=" * 60)
    print("Checkpoint Demo")
    print("=" * 60)

    # 会话 1
    config1 = {"configurable": {"thread_id": "session_1"}}
    result1 = app.invoke({"messages": ["Hello"], "step": 0}, config1)
    print(f"会话1 结果: {result1}")

    # 会话 2
    config2 = {"configurable": {"thread_id": "session_2"}}
    result2 = app.invoke({"messages": ["World"], "step": 0}, config2)
    print(f"会话2 结果: {result2}")

    # 获取当前 State
    state1 = app.get_state(config1)
    print(f"\n会话1 当前 State: {state1}")

    # 获取历史
    history = list(app.get_state_history(config1))
    print(f"\n会话1 历史记录数: {len(history)}")
    for h in history:
        print(f"  - step={h.values.get('step', 0)}")

    return result1


def update_state_demo():
    """更新 State 演示。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        counter: int

    def increment(state: State):
        return {"counter": state.get("counter", 0) + 1}

    graph = StateGraph(State)
    graph.add_node("increment", increment)
    graph.add_edge(START, "increment")
    graph.add_edge("increment", END)

    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "counter_session"}}

    print("\n" + "=" * 60)
    print("Update State Demo")
    print("=" * 60)

    # 多次调用，State 会累积
    for i in range(3):
        result = app.invoke({"counter": 0}, config)
        print(f"第{i+1}次调用: counter={result['counter']}")

    return result


if __name__ == "__main__":
    checkpoint_demo()
    update_state_demo()
