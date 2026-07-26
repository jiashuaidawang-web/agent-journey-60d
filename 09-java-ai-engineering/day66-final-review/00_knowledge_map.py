"""
Day 66: 知识图谱可视化 - 60 天知识串讲思维导图

功能：
1. 60 天知识串讲思维导图
2. 各 Phase 核心知识点
3. 输出 Mermaid / ASCII

示例：
    python 00_knowledge_map.py
    python 00_knowledge_map.py --format mermaid

实际实现需要：
- matplotlib / plotly（可视化）
- mermaid（图表）

作者：Agent Journey 60D
日期：Day 66
"""

import argparse
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class KnowledgeNode:
    """知识节点"""
    name: str
    description: str = ""
    children: list["KnowledgeNode"] = field(default_factory=list)
    level: int = 0


def build_knowledge_map() -> KnowledgeNode:
    """构建 60 天知识图谱

    Returns:
        知识图谱根节点
    """
    root = KnowledgeNode("Agent Journey 60D", "60 天 AI Agent 学习路线")

    # Phase 1: LLM Foundation
    phase1 = KnowledgeNode("Phase 1: LLM Foundation（Day 1-7）")
    phase1.children = [
        KnowledgeNode("LLM API / Message / Token / Context"),
        KnowledgeNode("Sync / Stream / Async / Async Stream"),
        KnowledgeNode("Structured Output / Pydantic"),
        KnowledgeNode("Prompt Engineering"),
        KnowledgeNode("Tool Calling / Function Calling"),
        KnowledgeNode("Agent Loop / Mini Agent Runtime"),
    ]

    # Phase 2: LangChain & LangGraph
    phase2 = KnowledgeNode("Phase 2: LangChain & LangGraph（Day 8-14）")
    phase2.children = [
        KnowledgeNode("LangChain Basics（Chain / LCEL）"),
        KnowledgeNode("LangGraph State / Node / Edge"),
        KnowledgeNode("Conditional Routing"),
        KnowledgeNode("Persistence / Checkpoint"),
        KnowledgeNode("Human-in-the-loop"),
        KnowledgeNode("Long-running Agent"),
    ]

    # Phase 3: RAG
    phase3 = KnowledgeNode("Phase 3: RAG（Day 15-22）")
    phase3.children = [
        KnowledgeNode("Embedding / Vector DB"),
        KnowledgeNode("Chunking / Splitting"),
        KnowledgeNode("Dense Retrieval / BM25 / Hybrid"),
        KnowledgeNode("Reranker"),
        KnowledgeNode("Query Rewrite / HyDE"),
        KnowledgeNode("RAG Pipeline"),
    ]

    # Phase 4: MCP / A2A / Multi-Agent
    phase4 = KnowledgeNode("Phase 4: MCP / A2A / Multi-Agent（Day 23-30）")
    phase4.children = [
        KnowledgeNode("MCP Protocol（工具标准化）"),
        KnowledgeNode("A2A Protocol（Agent 通信）"),
        KnowledgeNode("Multi-Agent Collaboration"),
        KnowledgeNode("Supervisor / Hierarchical"),
    ]

    # Phase 5: Production Agent
    phase5 = KnowledgeNode("Phase 5: Production Agent（Day 31-40）")
    phase5.children = [
        KnowledgeNode("Observability / Tracing"),
        KnowledgeNode("Evaluation / Testing"),
        KnowledgeNode("Deployment / Scaling"),
        KnowledgeNode("Security / Guardrails"),
    ]

    # Phase 6: GraphRAG & Advanced RAG
    phase6 = KnowledgeNode("Phase 6: GraphRAG & Advanced RAG（Day 41-50）")
    phase6.children = [
        KnowledgeNode("Knowledge Graph"),
        KnowledgeNode("GraphRAG / Hybrid RAG"),
        KnowledgeNode("Multi-hop Retrieval"),
        KnowledgeNode("Agentic RAG"),
    ]

    # Phase 7: LLM Engineering
    phase7 = KnowledgeNode("Phase 7: LLM Engineering（Day 51-54）")
    phase7.children = [
        KnowledgeNode("Fine-tuning / LoRA / QLoRA"),
        KnowledgeNode("SFT / DPO / RLHF"),
        KnowledgeNode("Deployment / Optimization"),
    ]

    # Phase 8: Java AI Engineering
    phase8 = KnowledgeNode("Phase 8: Java AI Engineering（Day 55-66）")
    phase8.children = [
        KnowledgeNode("Spring AI / LangChain4j"),
        KnowledgeNode("MCP Transports"),
        KnowledgeNode("Memory Deep Dive"),
        KnowledgeNode("LoRA / QLoRA / SFT / DPO"),
        KnowledgeNode("Multimodal Agent"),
        KnowledgeNode("RAG Internals"),
        KnowledgeNode("Architecture Review"),
        KnowledgeNode("Final Review"),
    ]

    root.children = [phase1, phase2, phase3, phase4, phase5, phase6, phase7, phase8]
    return root


def print_ascii(node: KnowledgeNode, indent: int = 0, prefix: str = "") -> None:
    """打印 ASCII 知识图谱

    Args:
        node: 知识节点
        indent: 缩进
        prefix: 前缀
    """
    if indent == 0:
        print(f"📚 {node.name}")
    else:
        connector = "├── " if prefix else "└── "
        print(f"{'│   ' * (indent - 1)}{connector}{node.name}")

    for i, child in enumerate(node.children):
        is_last = i == len(node.children) - 1
        print_ascii(child, indent + 1, "└── " if is_last else "├── ")


def print_mermaid(node: KnowledgeNode) -> None:
    """打印 Mermaid 知识图谱

    Args:
        node: 知识节点
    """
    print("```mermaid")
    print("graph TD")

    def _print_mermaid(n: KnowledgeNode, parent_id: str = "") -> None:
        node_id = n.name.replace(" ", "_").replace("（", "").replace("）", "").replace("/", "_")
        if parent_id:
            print(f"    {parent_id} --> {node_id}")
        print(f'    {node_id}["{n.name}"]')
        for child in n.children:
            _print_mermaid(child, node_id)

    _print_mermaid(node)
    print("```")


def print_markdown(node: KnowledgeNode, indent: int = 0) -> None:
    """打印 Markdown 知识图谱

    Args:
        node: 知识节点
        indent: 缩进
    """
    prefix = "  " * indent + "- "
    print(f"{prefix}**{node.name}**")
    for child in node.children:
        print_markdown(child, indent + 1)


def main():
    parser = argparse.ArgumentParser(description="知识图谱可视化")
    parser.add_argument("--format", type=str, default="ascii", choices=["ascii", "mermaid", "markdown"])
    args = parser.parse_args()

    root = build_knowledge_map()

    if args.format == "mermaid":
        print_mermaid(root)
    elif args.format == "markdown":
        print_markdown(root)
    else:
        print_ascii(root)


if __name__ == "__main__":
    main()
