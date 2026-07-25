"""
Day 40: Agent Evaluation.

演示 Agent 系统的评测。

Usage:
    python task_success_eval.py
"""


def task_success_rate(results: list[dict]) -> float:
    """任务完成率。"""
    success = sum(1 for r in results if r.get("success", False))
    return success / len(results) if results else 0


def tool_call_accuracy(calls: list[dict]) -> float:
    """工具调用准确率。"""
    correct = sum(1 for c in calls if c.get("correct", False))
    return correct / len(calls) if calls else 0


def avg_steps_to_completion(results: list[dict]) -> float:
    """平均完成步数。"""
    steps = [r.get("steps", 0) for r in results if r.get("success", False)]
    return sum(steps) / len(steps) if steps else 0


def agent_eval_demo():
    """Agent 评测演示。"""
    print("=" * 60)
    print("Agent Evaluation Demo")
    print("=" * 60)

    # 模拟 Agent 执行结果
    task_results = [
        {"task": "查询天气", "success": True, "steps": 2},
        {"task": "计算数学", "success": True, "steps": 1},
        {"task": "分析股票", "success": True, "steps": 3},
        {"task": "生成报告", "success": False, "steps": 5},
        {"task": "搜索信息", "success": True, "steps": 2},
    ]

    # 工具调用记录
    tool_calls = [
        {"tool": "get_weather", "correct": True},
        {"tool": "calculator", "correct": True},
        {"tool": "search_stock", "correct": True},
        {"tool": "generate_report", "correct": False},
        {"tool": "search_info", "correct": True},
    ]

    print(f"\n📊 Agent 评测结果:")

    # 任务完成率
    success_rate = task_success_rate(task_results)
    print(f"   任务完成率: {success_rate:.1%}")

    # 工具调用准确率
    tool_acc = tool_call_accuracy(tool_calls)
    print(f"   工具调用准确率: {tool_acc:.1%}")

    # 平均完成步数
    avg_steps = avg_steps_to_completion(task_results)
    print(f"   平均完成步数: {avg_steps:.1f}")

    print("\n✅ Agent 评测完成")


if __name__ == "__main__":
    agent_eval_demo()
