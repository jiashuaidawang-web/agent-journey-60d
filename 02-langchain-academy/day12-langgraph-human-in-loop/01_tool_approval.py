"""
Day 12: Tool Approval.

工具调用前的人工审批。

Usage:
    python tool_approval.py
"""


def tool_approval_demo():
    """工具调用审批演示。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_core.messages import HumanMessage
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI

    @tool
    def send_email(to: str, content: str) -> str:
        """发送邮件。"""
        return f"邮件已发送给 {to}"

    @tool
    def delete_file(path: str) -> str:
        """删除文件。"""
        return f"文件 {path} 已删除"

    tools = [send_email, delete_file]

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        pending_tool_calls: list
        approved_calls: list

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)

    def agent_node(state: State):
        """Agent 节点。"""
        messages = state["messages"]
        response = model.invoke(messages)
        return {"messages": [response]}

    def approval_node(state: State):
        """审批节点。"""
        messages = state["messages"]
        last_message = messages[-1]

        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            print(f"\n🔧 待审批的工具调用:")
            for tc in last_message.tool_calls:
                print(f"   - {tc['name']}({tc.get('args', {})})")

            # 模拟审批：高风险操作需要审批
            approved = []
            for tc in last_message.tool_calls:
                if tc["name"] == "delete_file":
                    print(f"   ⚠️ {tc['name']} 是高风险操作，需要审批")
                    # 模拟批准
                    approved.append(tc)
                else:
                    approved.append(tc)

            return {"approved_calls": approved}

        return {"approved_calls": []}

    def execute_tools(state: State):
        """执行审批通过的工具。"""
        results = []
        for tc in state.get("approved_calls", []):
            tool_name = tc["name"]
            tool_args = tc.get("args", {})

            tool_map = {t.name: t for t in tools}
            tool_to_run = tool_map.get(tool_name)

            if tool_to_run:
                result = tool_to_run.invoke(tool_args)
                results.append(result)

        return {"messages": [str(results)]}

    graph = StateGraph(State)
    graph.add_node("agent", agent_node)
    graph.add_node("approval", approval_node)
    graph.add_node("execute", execute_tools)

    graph.add_edge(START, "agent")
    graph.add_edge("agent", "approval")
    graph.add_edge("approval", "execute")
    graph.add_edge("execute", END)

    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer, interrupt_after=["approval"])

    print("=" * 60)
    print("Tool Approval Demo")
    print("=" * 60)

    config = {"configurable": {"thread_id": "tool_approval_session"}}

    result = app.invoke({
        "messages": [HumanMessage(content="请发送邮件给张三，内容：你好")]
    }, config)

    print(f"\n结果: {result}")

    return result


if __name__ == "__main__":
    tool_approval_demo()
