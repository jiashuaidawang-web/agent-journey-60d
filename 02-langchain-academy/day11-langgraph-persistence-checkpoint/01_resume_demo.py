"""
Day 11: Resume Demo.

演示断点续跑。

Usage:
    python resume_demo.py
"""


def resume_demo():
    """断点续跑演示。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        step: int
        result: str

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def step1(state: State):
        return {"step": 1, "messages": ["Step 1 done"]}

    def step2(state: State):
        return {"step": 2, "messages": ["Step 2 done"]}

    def step3(state: State):
        return {"step": 3, "messages": ["Step 3 done"], "result": "All steps completed"}

    graph = StateGraph(State)
    graph.add_node("step1", step1)
    graph.add_node("step2", step2)
    graph.add_node("step3", step3)
    graph.add_edge(START, "step1")
    graph.add_edge("step1", "step2")
    graph.add_edge("step2", "step3")
    graph.add_edge("step3", END)

    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "resume_session"}}

    print("=" * 60)
    print("Resume Demo")
    print("=" * 60)

    # 第一次执行
    print("\n📌 第一次执行:")
    result = app.invoke({"step": 0}, config)
    print(f"   结果: {result}")

    # 查看历史
    history = list(app.get_state_history(config))
    print(f"\n📜 历史记录: {len(history)} 条")
    for h in history:
        print(f"   step={h.values.get('step', 0)}")

    # 从某个 Checkpoint 恢复（更新 State）
    print("\n🔄 从 step=1 恢复:")
    app.update_state(config, {"step": 1, "messages": ["Resumed from step 1"]})

    # 查看更新后的 State
    current = app.get_state(config)
    print(f"   当前 State: {current.values}")

    return result


if __name__ == "__main__":
    resume_demo()
