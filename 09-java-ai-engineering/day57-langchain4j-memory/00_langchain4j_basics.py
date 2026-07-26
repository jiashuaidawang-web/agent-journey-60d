"""
================================================================================
Day 57 - LangChain4j 框架基础 | 00_langchain4j_basics.py
================================================================================

【学习目标】
理解 LangChain4j 框架基础，掌握 ChatModel 接入方式

【前置知识】
- Day 55 Spring AI 总览

【操作步骤】
1. 阅读本文件，理解 LangChain4j 核心组件
2. 在 Java 项目中接入 OpenAI / DeepSeek / Ollama
3. 运行代码，观察输出

【预期输出】
☕ LangChain4j 框架基础
├── OpenAI 接入: ✅
├── DeepSeek 接入: ✅
└── Ollama 接入: ✅

【验证标准】
□ 能接入 OpenAI
□ 能接入 DeepSeek
□ 能接入 Ollama
□ 理解 ChatModel 接口

【代码要点】
- OpenAiChatModel: OpenAI 接入
- OllamaChatModel: Ollama 接入
- ChatLanguageModel: 统一接口

================================================================================
"""

import sys
import time


def show_langchain4j_overview():
    """展示 LangChain4j 框架概览。"""
    print("☕ LangChain4j 框架概览：")
    print("""
├── AiServices           → 声明式 AI 服务（接口 + 注解）
├── ChatLanguageModel    → 对话模型接入
├── EmbeddingModel       → 向量嵌入
├── VectorStore          → 向量存储
├── ChatMemory           → 对话记忆
├── Tools                → 工具调用
└── RAG                  → 检索增强生成
""")
    print("   与 Spring AI 对比：")
    print("   ├── Spring AI: Spring 官方，深度集成 Spring 生态")
    print("   └── LangChain4j: 社区驱动，功能丰富，声明式服务")
    print()


def show_openai_integration():
    """展示 OpenAI 接入。"""
    print("🔌 OpenAI 接入：")
    print("   Java 代码：")
    print("   ChatLanguageModel model = OpenAiChatModel.builder()")
    print("       .apiKey(System.getenv(\"OPENAI_API_KEY\"))")
    print("       .modelName(\"gpt-4o-mini\")")
    print("       .temperature(0.7)")
    print("       .build();")
    print()
    print("   String response = model.generate(\"你好\");")
    print()


def show_deepseek_integration():
    """展示 DeepSeek 接入。"""
    print("🔌 DeepSeek 接入：")
    print("   Java 代码：")
    print("   ChatLanguageModel model = OpenAiChatModel.builder()")
    print("       .apiKey(System.getenv(\"DEEPSEEK_API_KEY\"))")
    print("       .baseUrl(\"https://api.deepseek.com/v1\")")
    print("       .modelName(\"deepseek-chat\")")
    print("       .build();")
    print()


def show_ollama_integration():
    """展示 Ollama 接入。"""
    print("🔌 Ollama 接入：")
    print("   Java 代码：")
    print("   ChatLanguageModel model = OllamaChatModel.builder()")
    print("       .baseUrl(\"http://localhost:11434\")")
    print("       .modelName(\"llama3.2\")")
    print("       .build();")
    print()


def show_spring_boot_integration():
    """展示 Spring Boot 整合。"""
    print("📝 Spring Boot 整合：")
    print()
    print("   pom.xml 依赖：")
    print("   <dependency>")
    print("       <groupId>dev.langchain4j</groupId>")
    print("       <artifactId>langchain4j-spring-boot-starter</artifactId>")
    print("       <version>0.33.0</version>")
    print("   </dependency>")
    print()
    print("   application.yml 配置：")
    print("   langchain4j:")
    print("     open-ai:")
    print("       chat-model:")
    print("         api-key: ${OPENAI_API_KEY}")
    print("         model-name: gpt-4o-mini")
    print("         temperature: 0.7")
    print()


def main():
    """主函数：展示 LangChain4j 框架基础。"""
    print("=" * 60)
    print("☕ LangChain4j 框架基础")
    print("=" * 60)
    print()

    show_langchain4j_overview()
    show_openai_integration()
    show_deepseek_integration()
    show_ollama_integration()
    show_spring_boot_integration()

    print("=" * 60)
    print("✅ LangChain4j 框架基础演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
