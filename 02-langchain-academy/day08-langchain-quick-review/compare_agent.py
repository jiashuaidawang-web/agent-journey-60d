"""
Day 8: Compare Hand-written vs LangChain Agent.

对比手写 Agent Runtime 和 LangChain Agent 的差异。

Usage:
    python compare_agent.py
"""


def comparison():
    """对比分析。"""
    print("=" * 60)
    print("手写 Agent Runtime vs LangChain Agent 对比")
    print("=" * 60)

    comparison_table = """
┌─────────────────┬──────────────────────┬──────────────────────┐
│ 维度            │ 手写 Runtime          │ LangChain Agent       │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 代码量          │ ~300 行              │ ~30 行               │
│ 抽象程度        │ 低（自己造轮子）      │ 高（框架封装）        │
│ 理解深度        │ 高（知道每行在干嘛）  │ 低（黑盒）            │
│ 扩展性          │ 低（改很多地方）      │ 高（加工具就行）      │
│ 可维护性        │ 低（自己维护）        │ 高（社区维护）        │
│ 调试难度        │ 低（代码在手）        │ 高（框架内部）        │
│ 生产就绪        │ 低（缺很多功能）      │ 高（久经考验）        │
│ 面试价值        │ 高（展示理解）        │ 中（展示会用）        │
└─────────────────┴──────────────────────┴──────────────────────┘
"""
    print(comparison_table)

    print("\n💡 结论:")
    print("  - 学习阶段：手写 Runtime 帮助理解原理")
    print("  - 生产阶段：LangChain/LangGraph 提高效率")
    print("  - 面试阶段：两者都要会，手写展示深度，框架展示效率")
    print("  - 最佳实践：理解原理 + 使用框架")


def langchain_architecture():
    """LangChain 架构概览。"""
    print("\n" + "=" * 60)
    print("LangChain 架构")
    print("=" * 60)

    architecture = """
LangChain 核心抽象:

1. Runnable
   └── 所有组件的基础接口
   └── invoke() / ainvoke() / stream() / batch()

2. LCEL (LangChain Expression Language)
   └── 链式调用: prompt | model | parser
   └── 自动支持流式、批处理、并行

3. Chain
   └── 多个 Runnable 的组合
   └── LLMChain, RetrievalQA, SequentialChain

4. Agent
   └── create_tool_calling_agent() + AgentExecutor
   └── 自动处理工具调用循环

5. Tool
   @tool 装饰器定义
   └── 自动转换为 OpenAI Function Calling 格式

6. Memory
   └── ConversationBufferMemory
   └── ConversationSummaryMemory

7. Retriever
   └── 向量检索抽象
   └── 支持多种向量数据库
"""
    print(architecture)


if __name__ == "__main__":
    comparison()
    langchain_architecture()
