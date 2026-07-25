"""
Day 13: Long-running Agent.

长时间运行 Agent：多步骤任务 + 中断恢复。

Usage:
    python long_running_agent.py
"""


def long_running_agent():
    """长时间运行 Agent。"""
    from typing import TypedDict, Annotated
    from langgraph.graph import StateGraph, START, END
    from langgraph.graph.message import add_messages
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI

    class State(TypedDict):
        messages: Annotated[list, add_messages]
        step: int
        results: list
        final_report: str

    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def research_step(state: State):
        """研究步骤。"""
        step = state.get("step", 0) + 1
        results = state.get("results", [])
        results.append(f"研究步骤 {step} 完成")
        return {"step": step, "results": results}

    def analysis_step(state: State):
        """分析步骤。"""
        results = state.get("results", [])
        results.append("分析完成")
        return {"results": results}

    def report_step(state: State):
        """生成报告。"""
        results = state.get("results", [])
        report = f"报告: 共 {len(results)} 个步骤完成"
        return {"final_report": report, "results": results + ["报告生成"]}

    graph = StateGraph(State)
    graph.add_node("research", research_step)
    graph.add_node("analysis", analysis_step)
    graph.add_node("report", report_step)

    graph.add_edge(START, "research")
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "report")
    graph.add_edge("report", END)

    checkpointer = MemorySaver()
    app = graph.compile(checkpointer=checkpointer)

    print("=" * 60)
    print("Long-running Agent")
    print("=" * 60)

    config = {"configurable": {"thread_id": "long_running_session"}}

    result = app.invoke({"step": 0, "results": []}, config)

    print(f"结果: {result}")
    print(f"报告: {result.get('final_report', '')}")

    return result


if __name__ == "__main__":
    long_running_agent()
