"""
================================================================================
Day 7 - Mini Agent Runtime - 测试 | tests/test_runtime.py
================================================================================

【学习目标】
测试核心模块，确保 Runtime 正常工作

【前置知识】
- 所有 mini_agent_runtime 模块

【操作步骤】
1. 运行: python tests/test_runtime.py
2. 观察输出：所有测试通过

【预期输出】
Mini Agent Runtime 测试
============================================================
✅ AgentState 测试通过
✅ ContextManager 测试通过
✅ ToolRegistry 测试通过
✅ Memory 测试通过
✅ TokenCounter 测试通过
✅ CalculatorTool 测试通过

============================================================
所有测试通过！
============================================================

【验证标准】
□ 所有测试通过
□ 理解每个测试的作用

================================================================================
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from mini_agent_runtime.core import AgentState, ContextManager, AgentLoop
from mini_agent_runtime.tools import ToolRegistry, CalculatorTool, WeatherTool
from mini_agent_runtime.memory import Memory
from mini_agent_runtime.observability import TokenCounter


def test_agent_state():
    """测试 AgentState。"""
    state = AgentState(max_iterations=5)
    assert state.iteration == 0
    assert state.finished is False
    assert state.is_max_iterations_reached() is False

    state.increment_iteration()
    assert state.iteration == 1

    state.mark_finished("完成")
    assert state.finished is True
    assert state.final_response == "完成"

    print("✅ AgentState 测试通过")


def test_context_manager():
    """测试 ContextManager。"""
    cm = ContextManager(system_prompt="你是助手")
    messages = cm.build(
        history=[{"role": "user", "content": "你好"}],
        memory=["用户喜欢简洁回答"],
    )

    assert len(messages) == 3
    assert messages[0]["role"] == "system"
    assert "Memory" in messages[1]["content"]
    assert messages[2]["content"] == "你好"

    print("✅ ContextManager 测试通过")


def test_tool_registry():
    """测试 ToolRegistry。"""
    registry = ToolRegistry()
    registry.register(CalculatorTool())
    registry.register(WeatherTool())

    assert len(registry) == 2
    assert "calculator" in registry

    # 测试执行
    result = registry.execute("calculator", {"expression": "1 + 2"})
    assert "3" in result

    result = registry.execute("get_weather", {"city": "北京"})
    assert "北京" in result

    # 测试不存在的工具
    result = registry.execute("nonexistent", {})
    assert "错误" in result

    print("✅ ToolRegistry 测试通过")


def test_memory():
    """测试 Memory。"""
    memory = Memory(max_entries=3)

    memory.add("记忆1")
    memory.add("记忆2")
    memory.add("记忆3")
    assert len(memory) == 3

    # 超出限制
    memory.add("记忆4")
    assert len(memory) == 3
    assert "记忆1" not in memory.get_all()

    print("✅ Memory 测试通过")


def test_token_counter():
    """测试 TokenCounter。"""
    counter = TokenCounter()

    counter.add(100, 50)
    counter.add(200, 100)

    assert counter.input_tokens == 300
    assert counter.output_tokens == 150
    assert counter.total_tokens == 450

    print("✅ TokenCounter 测试通过")


def test_calculator_tool():
    """测试 CalculatorTool。"""
    tool = CalculatorTool()

    result = tool.execute(expression="1 + 2")
    assert "3" in result

    result = tool.execute(expression="10 * 5")
    assert "50" in result

    # 错误表达式
    result = tool.execute(expression="abc")
    assert "错误" in result or "Error" in result

    print("✅ CalculatorTool 测试通过")


def run_all_tests():
    """运行所有测试。"""
    print("=" * 60)
    print("Mini Agent Runtime 测试")
    print("=" * 60)

    test_agent_state()
    test_context_manager()
    test_tool_registry()
    test_memory()
    test_token_counter()
    test_calculator_tool()

    print(f"\n{'=' * 60}")
    print("所有测试通过！")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run_all_tests()
