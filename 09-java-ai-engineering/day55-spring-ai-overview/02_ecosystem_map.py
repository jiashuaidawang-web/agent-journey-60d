"""
================================================================================
Day 55 - 2026 AI 开发生态全景 | 02_ecosystem_map.py
================================================================================

【学习目标】
梳理 2026 AI 开发生态全景，理解各框架定位和模型平台特点

【前置知识】
- 01_chatclient_basics.py（ChatClient API）

【操作步骤】
1. 阅读本文件，理解生态分层
2. 整理各框架的定位和优劣势
3. 画出自己的生态全景图

【预期输出】
🌍 2026 AI 开发生态全景
├── Python: LangChain / LangGraph / LlamaIndex
├── Java: Spring AI / LangChain4j / Semantic Kernel
├── 模型层: OpenAI / Claude / DeepSeek / Qwen
└── 基础设施: Milvus / Redis / Langfuse

【验证标准】
□ 能画出完整生态图
□ 能说出各框架定位
□ 能对比 Python / Java 生态差异

【代码要点】
- 生态分层：框架层 / 模型层 / 基础设施层
- Python 生态：LangChain / LangGraph / LlamaIndex
- Java 生态：Spring AI / LangChain4j / Semantic Kernel

================================================================================
"""

import sys


def show_python_ecosystem():
    """展示 Python AI 开发生态。"""
    print("🐍 Python AI 开发生态：")
    print("""
├── LangChain          → 主流 AI 应用框架（链式调用）
├── LangGraph          → 状态图驱动的多 Agent 框架
├── LlamaIndex         → RAG 专精框架
├── AutoGen            → 微软出品，多 Agent 协作
├── Haystack           → 企业级 RAG 框架
└── Semantic Kernel    → 微软出品的 Java/Python/AI 框架
""")
    print("   优势：社区活跃、功能丰富、文档完善")
    print("   劣势：Python 性能、企业级集成相对弱")
    print()


def show_java_ecosystem():
    """展示 Java AI 开发生态。"""
    print("☕ Java AI 开发生态：")
    print("""
├── Spring AI         → Spring 官方出品，与 Spring 生态深度集成
├── LangChain4j        → LangChain 的 Java 移植版
├── Semantic Kernel    → 微软出品，Java 支持良好
└── OpenNLP / DL4J    → 传统机器学习框架（不推荐新项目）
""")
    print("   优势：企业级、性能好、与现有系统集成")
    print("   劣势：功能相对 Python 少、社区相对小")
    print()


def show_model_platforms():
    """展示主流模型平台。"""
    print("🤖 主流模型平台：")
    print("""
├── 海外
│   ├── OpenAI          → GPT-4o / GPT-5（最强通用）
│   ├── Anthropic       → Claude 4（长上下文）
│   ├── Google          → Gemini（多模态）
│   ├── Meta            → Llama 4（开源）
│   └── Mistral         → Mistral（欧洲开源）
│
├── 国内
│   ├── DeepSeek        → DeepSeek V3（性价比之王）
│   ├── 阿里百炼        → 通义千问 Qwen3（国内合规）
│   ├── 智谱            → GLM-4（开源友好）
│   ├── 月之暗面        → Kimi（长文本）
│   └── 硅基流动        → 聚合 API（一站式）
│
└── 本地部署
    ├── Ollama          → 本地模型管理工具
    ├── vLLM            → 高性能推理引擎
    └── LM Studio       → 本地模型 GUI
""")
    print()


def show_infrastructure():
    """展示 AI 基础设施。"""
    print("🏗️ AI 基础设施：")
    print("""
├── 向量数据库
│   ├── Milvus          → 分布式向量数据库
│   ├── Qdrant          → Rust 编写，高性能
│   ├── Redis           → 向量 + 缓存 + 记忆
│   ├── Pinecone        → 托管向量数据库
│   └── Chroma          → 轻量级向量数据库
│
├── 模型网关
│   ├── LiteLLM         → 统一 API 网关
│   ├── OneAPI          → 国产模型网关
│   └── Helicone        → AI 应用可观测性
│
└── 可观测性
    ├── LangSmith        → LangChain 官方
    ├── Langfuse         → 开源可观测性
    └── Arize Pheonix    → 开源 LLM 追踪
""")
    print()


def draw_ecosystem_map():
    """绘制 2026 AI 开发生态全景图。"""
    print("🌍 2026 AI 开发生态全景图：")
    print("""
                        AI 应用层
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    Python 生态         Java 生态        前端/移动端
         │                  │                  │
   LangChain          Spring AI          Vercel AI SDK
   LangGraph          LangChain4j        Flutter AI
   LlamaIndex         Semantic Kernel    React Native AI
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                        模型接入层
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    海外模型            国内模型           本地模型
         │                  │                  │
   OpenAI             DeepSeek          Ollama
   Claude             Qwen              vLLM
   Gemini             GLM               LM Studio
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                        基础设施层
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    向量存储           模型网关          可观测性
         │                  │                  │
   Milvus             LiteLLM           LangSmith
   Qdrant             OneAPI            Langfuse
   Redis              Helicone          Arize
""")


def main():
    """主函数：展示 2026 AI 开发生态全景。"""
    print("=" * 60)
    print("🌍 2026 AI 开发生态全景")
    print("=" * 60)
    print()

    show_python_ecosystem()
    show_java_ecosystem()
    show_model_platforms()
    show_infrastructure()
    draw_ecosystem_map()

    print("=" * 60)
    print("✅ 2026 AI 开发生态全景展示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
