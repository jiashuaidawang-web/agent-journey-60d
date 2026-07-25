"""
Day 12: Human-in-the-loop Demo.

演示人工审批流程。

Usage:
    python approval_demo.py
"""


def approval_demo():
    """人工审批演示。"""
    from typing import TypedDict, Annotated, Literal
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        plan: str
        approved: bool | None
        result: str

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def plan_node(state: State):
        """生成计划。"""
        messages = state["messages"]
        response = model.invoke([
            ("system", "你是一个助手。根据用户请求生成一个执行计划。"),
            *messages,
        ])
        return {"plan": response.content}

    def human_approval(state: State):
        """人工审批节点（这里模拟）。"""
        # 实际场景中，这里会暂停等待人工输入
        # 这里模拟自动审批
        print(f"\n📋 生成的计划: {state['plan']}")
        print("⏳ 等待人工审批...")

        # 模拟：自动批准
        approved = True
        print(f"✅ 审批结果: {'通过' if approved else '拒绝'}")

        return {"approved": approved}

    def execute_node(state: State):
        """执行计划。"""
        return {"result": f"计划已执行: {state['plan']}"}

    def reject_node(state: State):
        """拒绝处理。"""
        return {"result": "计划被拒绝"}

    def route_approval(state: State) -> Literal["execute_node", "reject_node"]:
        if state.get("approved"):
            return "execute_node"
        return "reject_node"

    graph = StateGraph(State)
    graph.add_node("plan", plan_node)
    graph.add_node("approval", human_approval)
    graph.add_node("execute", execute_node)
    graph.add_node("reject", reject_node)

    graph.add_edge(START, "plan")
    graph.add_edge("plan", "approval")
    graph.add_conditional_edges("approval", route_approval, {
        "execute_node": "execute",
        "reject_node": "reject",
    })
    graph.add_edge("execute", END)
    graph.add_edge("reject", END)

    # 在 approval 节点后暂停
    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer, interrupt_after=["approval"])

    print("=" * 60)
    print("Human-in-the-loop Demo")
    print("=" * 60)

    config = {"configurable": {"thread_id": "approval_session"}}

    # 第一次执行（会在 approval 后暂停）
    result = app.invoke({"messages": [HumanMessage(content="帮我写一份报告")]}, config)
    print(f"\n暂停时 State: {result}")

    # 人工审批后继续
    # 实际场景：获取人工输入，更新 State
    app.update_state(config, {"approved": True})

    # 继续执行
    result = app.invoke(None, config)
    print(f"\n✅ 最终结果: {result.get('result', '')}")

    return result


if __name__ == "__main__":
    approval_demo()
