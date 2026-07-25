"""
Day 14: Research Agent - LangGraph Mini Project.

综合运用 LangGraph 核心概念的完整项目。

架构：
    研究 → 分析 → 报告 → 审批 → 发布/修改

Usage:
    python research_agent.py
"""


def research_agent():
    """Research Agent 完整实现。"""
    from typing import TypedDict, Annotated, Literal
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    # 1. 定义 State
    class State(TypedDict):
        messages: Annotated[list, add_messages]
        topic: str              # 研究主题
        research_data: str      # 研究数据
        analysis_result: str    # 分析结果
        report: str             # 报告
        approved: bool | None   # 审批结果
        final_output: str       # 最终输出

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 2. 定义 Node
    def research_node(state: State):
        """研究节点：搜索信息。"""
        topic = state.get("topic", "")
        response = model.invoke([
            ("system", f"你是一个研究员。请搜索关于 '{topic}' 的信息，列出关键点。"),
        ])
        return {"research_data": response.content}

    def analysis_node(state: State):
        """分析节点：分析信息。"""
        research_data = state.get("research_data", "")
        response = model.invoke([
            ("system", f"你是一个分析师。请分析以下研究数据，给出见解：\n{research_data}"),
        ])
        return {"analysis_result": response.content}

    def report_node(state: State):
        """报告节点：生成报告。"""
        analysis = state.get("analysis_result", "")
        response = model.invoke([
            ("system", f"你是一个报告撰写人。请根据以下分析结果撰写报告：\n{analysis}"),
        ])
        return {"report": response.content}

    def approval_node(state: State):
        """审批节点：模拟人工审批。"""
        report = state.get("report", "")
        print(f"\n📋 生成的报告:\n{report[:200]}...")
        print("\n⏳ 等待人工审批...")

        # 模拟审批：自动通过
        approved = True
        print(f"✅ 审批结果: {'通过' if approved else '拒绝'}")

        return {"approved": approved}

    def publish_node(state: State):
        """发布节点。"""
        report = state.get("report", "")
        return {"final_output": f"报告已发布:\n{report}"}

    def revise_node(state: State):
        """修改节点。"""
        return {"final_output": "报告被拒绝，请修改后重新提交"}

    # 3. 路由函数
    def route_approval(state: State) -> Literal["publish", "revise"]:
        if state.get("approved"):
            return "publish"
        return "revise"

    # 4. 创建 Graph
    graph = StateGraph(State)
    graph.add_node("research", research_node)
    graph.add_node("analysis", analysis_node)
    graph.add_node("report", report_node)
    graph.add_node("approval", approval_node)
    graph.add_node("publish", publish_node)
    graph.add_node("revise", revise_node)

    graph.add_edge(START, "research")
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "report")
    graph.add_edge("report", "approval")
    graph.add_conditional_edges("approval", route_approval, {
        "publish": "publish",
        "revise": "revise",
    })
    graph.add_edge("publish", END)
    graph.add_edge("revise", END)

    # 5. 编译（带 Checkpoint 和 interrupt）
    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer, interrupt_after=["approval"])

    # 6. 运行
    print("=" * 60)
    print("Research Agent")
    print("=" * 60)

    config = {"configurable": {"thread_id": "research_session"}}

    result = app.invoke({
        "topic": "AI Agent 发展趋势",
    }, config)

    print(f"\n📊 最终结果:")
    print(f"   研究数据: {result.get('research_data', '')[:100]}...")
    print(f"   分析结果: {result.get('analysis_result', '')[:100]}...")
    print(f"   报告: {result.get('report', '')[:100]}...")
    print(f"   审批: {'通过' if result.get('approved') else '拒绝'}")
    print(f"   最终输出: {result.get('final_output', '')[:100]}...")

    return result


if __name__ == "__main__":
    research_agent()
