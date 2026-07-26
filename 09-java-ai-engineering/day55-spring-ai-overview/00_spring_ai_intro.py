"""
================================================================================
Day 55 - Spring AI 快速初始化 | 00_spring_ai_intro.py
================================================================================

【学习目标】
理解 Spring AI 项目骨架和依赖结构，快速初始化一个 Spring AI 项目

【前置知识】
- Spring Boot 基础
- Maven / Gradle 基础

【操作步骤】
1. 创建 Spring Boot 项目（推荐 https://start.spring.io）
2. 添加 spring-ai-openai-spring-boot-starter 依赖
3. 配置 application.yml
4. 运行项目，观察 ChatClient 自动配置

【预期输出】
🚀 Spring AI 项目启动成功
📝 ChatClient 自动配置完成
✅ Response: Spring AI 是 Spring 官方推出的 AI 应用框架...

【验证标准】
□ 项目能正常启动
□ ChatClient Bean 自动创建
□ 能调用 LLM 并获取回复

【代码要点】
- spring-ai-openai-spring-boot-starter: 核心依赖
- application.yml: 配置 API Key 和模型
- ChatClient.Builder: 自动注入构建器

================================================================================
"""

import sys
import time


def check_spring_ai_dependencies():
    """检查 Spring AI 依赖结构。

    本函数演示 Spring AI 项目的核心依赖结构。
    实际项目中通过 pom.xml 或 build.gradle 管理。
    """
    print("📦 Spring AI 项目依赖结构：")
    print("├── spring-boot-starter-web")
    print("├── spring-ai-openai-spring-boot-starter  ← 核心依赖")
    print("├── spring-boot-starter-test")
    print("└── lombok (可选)")
    print()

    # 依赖版本信息
    deps = {
        "spring-ai": "1.0.0-M1",
        "spring-boot": "3.3.0",
        "java": "17+",
    }

    print("📋 版本要求：")
    for name, version in deps.items():
        print(f"   {name}: {version}")
    print()


def show_application_yml():
    """展示 application.yml 配置。"""
    print("📝 application.yml 配置：")
    print("""spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      base-url: https://api.openai.com/v1
      chat:
        options:
          model: gpt-4o-mini
          temperature: 0.7
          max-tokens: 2048
""")


def demo_chatclient_usage():
    """演示 ChatClient 基本用法（伪代码）。

    实际 Java 代码如下：
    ```java
    @Autowired
    private ChatClient.Builder chatClientBuilder;

    public String chat(String userInput) {
        ChatClient client = chatClientBuilder.build();
        return client.prompt()
            .user(userInput)
            .call()
            .content();
    }
    ```
    """
    print("💻 ChatClient 使用示例（Java 伪代码）：")
    print("""
@Autowired
private ChatClient.Builder chatClientBuilder;

public String chat(String userInput) {
    ChatClient client = chatClientBuilder.build();
    return client.prompt()
        .user(userInput)
        .call()
        .content();
}
""")
    print("✅ 核心要点：")
    print("   - ChatClient.Builder 自动注入")
    print("   - 链式调用: prompt().user().call().content()")
    print("   - 与 Spring 生态无缝集成")


def main():
    """主函数：展示 Spring AI 项目初始化流程。"""
    print("=" * 60)
    print("🚀 Spring AI 项目快速初始化")
    print("=" * 60)
    print()

    # 步骤1: 展示依赖结构
    check_spring_ai_dependencies()

    # 步骤2: 展示配置
    show_application_yml()

    # 步骤3: 演示 ChatClient 用法
    demo_chatclient_usage()

    print("=" * 60)
    print("✅ Spring AI 项目初始化完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
