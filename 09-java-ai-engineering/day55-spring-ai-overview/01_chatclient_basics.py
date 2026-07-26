"""
================================================================================
Day 55 - ChatClient 核心 API | 01_chatclient_basics.py
================================================================================

【学习目标】
掌握 ChatClient 核心 API：同步调用、流式调用、System Prompt 配置

【前置知识】
- 00_spring_ai_intro.py（项目初始化）
- Spring Boot 基础

【操作步骤】
1. 阅读本文件，理解 ChatClient 三种调用模式
2. 在 Java 项目中实现三种调用
3. 观察输出差异

【预期输出】
📤 同步调用: 你好！我是...
📡 流式调用: Java是一门...（逐字出现）
🎭 System Prompt: 作为Java架构师...

【验证标准】
□ 能实现同步调用
□ 能实现流式调用
□ 能配置 System Prompt
□ 理解三种调用模式的区别

【代码要点】
- .call(): 同步调用，返回完整结果
- .stream(): 流式返回 Flux<String>
- .system(): 设置系统提示词
- .user(): 设置用户输入

================================================================================
"""

import sys
import time


def demo_sync_call():
    """演示 ChatClient 同步调用。

    Java 代码：
    ```java
    String response = chatClient.prompt()
        .user("你好，请介绍一下你自己")
        .call()
        .content();
    System.out.println(response);
    ```
    """
    print("📤 同步调用示例：")
    print("   Java 代码：")
    print("   String response = chatClient.prompt()")
    print("       .user(\"你好，请介绍一下你自己\")")
    print("       .call()")
    print("       .content();")
    print()
    print("   预期输出：")
    print("   ✅ Response: 你好！我是一个AI助手，可以回答你的问题...")
    print()


def demo_stream_call():
    """演示 ChatClient 流式调用。

    Java 代码：
    ```java
    Flux<String> response = chatClient.prompt()
        .user("写一首关于Java的诗")
        .stream()
        .content();

    response.doOnNext(chunk -> System.out.print(chunk))
            .blockLast();
    ```
    """
    print("📡 流式调用示例：")
    print("   Java 代码：")
    print("   Flux<String> response = chatClient.prompt()")
    print("       .user(\"写一首关于Java的诗\")")
    print("       .stream()")
    print("       .content();")
    print()
    print("   预期输出：")
    print("   Java是一门...（逐字出现）")
    print("   ...优雅的语言")
    print("   ...面向对象的世界")
    print()


def demo_system_prompt():
    """演示 System Prompt 配置。

    Java 代码：
    ```java
    String response = chatClient.prompt()
        .system("你是一个资深Java架构师，回答要简洁专业")
        .user("请解释 Spring Boot 自动配置原理")
        .call()
        .content();
    ```
    """
    print("🎭 System Prompt 示例：")
    print("   Java 代码：")
    print("   String response = chatClient.prompt()")
    print("       .system(\"你是一个资深Java架构师，回答要简洁专业\")")
    print("       .user(\"请解释 Spring Boot 自动配置原理\")")
    print("       .call()")
    print("       .content();")
    print()
    print("   预期输出：")
    print("   ✅ Response: Spring Boot 自动配置通过 @EnableConfigurationProperties")
    print("       + 条件装配实现，核心是 spring.factories 中...")
    print()


def demo_chatclient_api_structure():
    """展示 ChatClient API 结构。"""
    print("📚 ChatClient API 结构：")
    print("""
ChatClient
├── prompt()                    → 创建 Prompt
│   ├── .system(String)         → 设置 System Prompt
│   ├── .user(String)           → 设置 User Input
│   ├── .messages(Message...)   → 设置完整消息列表
│   └── .tools(Object...)       → 绑定工具
│
├── call()                      → 同步调用
│   └── .content()              → 获取文本内容
│
└── stream()                    → 流式调用
    └── .content()              → 获取 Flux<String>
""")


def main():
    """主函数：展示 ChatClient 核心 API。"""
    print("=" * 60)
    print("💻 ChatClient 核心 API 演示")
    print("=" * 60)
    print()

    # 同步调用
    demo_sync_call()

    # 流式调用
    demo_stream_call()

    # System Prompt
    demo_system_prompt()

    # API 结构
    demo_chatclient_api_structure()

    print("=" * 60)
    print("✅ ChatClient API 演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
