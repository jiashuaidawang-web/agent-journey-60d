"""
Day 65: 架构图绘制 - Enterprise Agent Platform + Investment Research Platform

功能：
1. Enterprise Agent Platform 架构图（ASCII / Mermaid）
2. Investment Research Platform 架构图（ASCII / Mermaid）
3. 60 天知识串讲思维导图

示例：
    python 02_architecture_diagram.py
    python 02_architecture_diagram.py --format mermaid

实际实现需要：
- matplotlib / plotly（可视化）
- mermaid（图表）

作者：Agent Journey 60D
日期：Day 65
"""

import argparse
from typing import Optional


def print_enterprise_agent_platform_ascii() -> None:
    """打印 Enterprise Agent Platform ASCII 架构图"""
    diagram = """
┌──────────────────────────────────────────────────────────────────┐
│                     Enterprise Agent Platform                     │
├──────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                   API Gateway                            │     │
│  │         Auth / Rate Limit / Logging / Routing           │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │               Agent Orchestrator                         │     │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐      │     │
│  │  │ ReAct   │ │ Router  │ │ Plan-   │ │Reflect- │      │     │
│  │  │ Agent   │ │ Agent   │ │ Execute │ │ ion     │      │     │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘      │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                  Tool Registry                           │     │
│  │  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐    │     │
│  │  │Search │ │Database│ │ API   │ │ Code  │ │ File  │    │     │
│  │  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘    │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                   Memory Layer                           │     │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │     │
│  │  │ Short-term   │ │  Long-term   │ │   Session    │    │     │
│  │  │ (Context)    │ │ (Vector DB)  │ │   (Redis)    │    │     │
│  │  └──────────────┘ └──────────────┘ └──────────────┘    │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                   Model Layer                            │     │
│  │  ┌─────┐ ┌─────┐ ┌──────┐ ┌──────┐ ┌──────┐          │     │
│  │  │GPT- │ │Claude│ │Gemini│ │LLaMA │ │ Qwen │          │     │
│  │  │4o   │ │     │ │      │ │      │ │      │          │     │
│  │  └─────┘ └─────┘ └──────┘ └──────┘ └──────┘          │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                 Observability                            │     │
│  │  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │     │
│  │  │ LangSmith    │ │ Prometheus   │ │    ELK       │    │     │
│  │  │ / Langfuse   │ │ / Grafana    │ │   Stack      │    │     │
│  │  └──────────────┘ └──────────────┘ └──────────────┘    │     │
│  └─────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
"""
    print(diagram)


def print_investment_research_platform_ascii() -> None:
    """打印 Investment Research Platform ASCII 架构图"""
    diagram = """
┌──────────────────────────────────────────────────────────────────┐
│                Investment Research Platform                       │
├──────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                   Data Sources                           │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │     │
│  │  │ 公告 PDF │ │   研报   │ │   财报   │ │  K 线    │   │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │     │
│  │  │   新闻   │ │ 社交媒体 │ │ 宏观经济 │ │ 实时行情 │   │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                  RAG Pipeline                            │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │     │
│  │  │ Document │ │  Split   │ │Embedding │ │ Vector   │   │     │
│  │  │ Loader   │ │  ter     │ │          │ │   DB     │   │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │     │
│  │  ┌──────────┐ ┌──────────┐                             │     │
│  │  │Retrieval │ │ Reranker │                             │     │
│  │  └──────────┘ └──────────┘                             │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                   Agent Layer                            │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │     │
│  │  │ 财报分析 │ │ 行业研究 │ │ 技术面   │ │ 投资建议 │   │     │
│  │  │   Agent  │ │   Agent  │ │ 分析     │ │   Agent  │   │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │     │
│  └─────────────────────────────────────────────────────────┘     │
│                              ↓                                   │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │                    Output                               │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │     │
│  │  │ 研报生成 │ │ 投资建议 │ │ 风险提示 │ │ 组合优化 │   │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │     │
│  └─────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
"""
    print(diagram)


def print_enterprise_agent_platform_mermaid() -> None:
    """打印 Enterprise Agent Platform Mermaid 架构图"""
    diagram = """
graph TD
    A[API Gateway] --> B[Agent Orchestrator]
    B --> C[Tool Registry]
    C --> D[Memory Layer]
    D --> E[Model Layer]
    E --> F[Observability]

    B --> B1[ReAct Agent]
    B --> B2[Router Agent]
    B --> B3[Plan-Execute Agent]
    B --> B4[Reflection Agent]

    C --> C1[Search]
    C --> C2[Database]
    C --> C3[API]
    C --> C4[Code]

    D --> D1[Short-term Memory]
    D --> D2[Long-term Memory]
    D --> D3[Session Memory]

    E --> E1[GPT-4o]
    E --> E2[Claude]
    E --> E3[Gemini]
    E --> E4[LLaMA]
    E --> E5[Qwen]

    F --> F1[LangSmith]
    F --> F2[Prometheus]
    F --> F3[ELK]
"""
    print(diagram)


def print_knowledge_map() -> None:
    """打印 60 天知识串讲思维导图"""
    diagram = """
Agent Journey 60D - 知识串讲
├── Phase 1: LLM Foundation（Day 1-7）
│   ├── LLM API / Message / Token / Context
│   ├── Sync / Stream / Async / Async Stream
│   ├── Structured Output / Pydantic
│   ├── Prompt Engineering
│   ├── Tool Calling / Function Calling
│   └── Agent Loop / Mini Agent Runtime
├── Phase 2: LangChain & LangGraph（Day 8-14）
│   ├── LangChain Basics（Chain / LCEL）
│   ├── LangGraph State / Node / Edge
│   ├── Conditional Routing
│   ├── Persistence / Checkpoint
│   ├── Human-in-the-loop
│   └── Long-running Agent
├── Phase 3: RAG（Day 15-22）
│   ├── Embedding / Vector DB
│   ├── Chunking / Splitting
│   ├── Dense Retrieval / BM25 / Hybrid
│   ├── Reranker
│   ├── Query Rewrite / HyDE
│   └── RAG Pipeline
├── Phase 4: MCP / A2A / Multi-Agent（Day 23-30）
│   ├── MCP Protocol（工具标准化）
│   ├── A2A Protocol（Agent 通信）
│   ├── Multi-Agent Collaboration
│   └── Supervisor / Hierarchical
├── Phase 5: Production Agent（Day 31-40）
│   ├── Observability / Tracing
│   ├── Evaluation / Testing
│   ├── Deployment / Scaling
│   └── Security / Guardrails
├── Phase 6: GraphRAG & Advanced RAG（Day 41-50）
│   ├── Knowledge Graph
│   ├── GraphRAG / Hybrid RAG
│   ├── Multi-hop Retrieval
│   └── Agentic RAG
├── Phase 7: LLM Engineering（Day 51-54）
│   ├── Fine-tuning / LoRA / QLoRA
│   ├── SFT / DPO / RLHF
│   └── Deployment / Optimization
└── Phase 8: Java AI Engineering（Day 55-66）
    ├── Spring AI / LangChain4j
    ├── MCP Transports
    ├── Memory Deep Dive
    ├── LoRA / QLoRA / SFT / DPO
    ├── Multimodal Agent
    ├── RAG Internals
    ├── Architecture Review
    └── Final Review
"""
    print(diagram)


def main():
    parser = argparse.ArgumentParser(description="架构图绘制")
    parser.add_argument("--format", type=str, default="ascii", choices=["ascii", "mermaid"])
    parser.add_argument("--diagram", type=str, default="all",
                        choices=["enterprise", "investment", "knowledge", "all"])
    args = parser.parse_args()

    if args.diagram in ["enterprise", "all"]:
        print("🏢 Enterprise Agent Platform")
        print("=" * 60)
        if args.format == "mermaid":
            print_enterprise_agent_platform_mermaid()
        else:
            print_enterprise_agent_platform_ascii()

    if args.diagram in ["investment", "all"]:
        print("\n📈 Investment Research Platform")
        print("=" * 60)
        print_investment_research_platform_ascii()

    if args.diagram in ["knowledge", "all"]:
        print("\n📚 60 天知识串讲思维导图")
        print("=" * 60)
        print_knowledge_map()


if __name__ == "__main__":
    main()
