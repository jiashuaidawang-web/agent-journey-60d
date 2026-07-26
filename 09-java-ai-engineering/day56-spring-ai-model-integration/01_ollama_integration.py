"""
================================================================================
Day 56 - Ollama 本地模型接入 | 01_ollama_integration.py
================================================================================

【学习目标】
实现 Ollama 本地模型接入，理解本地部署流程和配置

【前置知识】
- Day 55 Spring AI 总览
- 00_model_platforms.py（平台对比）

【操作步骤】
1. 安装 Ollama：https://ollama.com/
2. 下载模型：ollama pull llama3.2
3. 配置 Spring AI Ollama Starter
4. 运行代码，观察输出

【预期输出】
🏠 Ollama 本地模型接入
├── 模型: llama3.2
├── 地址: http://localhost:11434
└── 状态: ✅ 连接成功

【验证标准】
□ 能安装并启动 Ollama
□ 能下载模型
□ 能配置 Spring AI 接入
□ 能调用本地模型

【代码要点】
- spring-ai-ollama-spring-boot-starter: Ollama 依赖
- application.yml: 配置 base-url 和 model
- ChatClient: 自动注入使用

================================================================================
"""

import sys
import time


def show_ollama_setup_steps():
    """展示 Ollama 安装步骤。"""
    print("📦 Ollama 安装步骤：")
    print("""
1. 下载安装 Ollama
   $ brew install ollama  # macOS
   $ curl -fsSL https://ollama.com/install.sh | sh  # Linux

2. 启动 Ollama 服务
   $ ollama serve

3. 下载模型
   $ ollama pull llama3.2
   $ ollama pull qwen2.5

4. 测试模型
   $ ollama run llama3.2
""")


def show_spring_ai_ollama_config():
    """展示 Spring AI Ollama 配置。"""
    print("📝 Spring AI Ollama 配置：")
    print()
    print("pom.xml 依赖：")
    print("""
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-ollama-spring-boot-starter</artifactId>
</dependency>
""")

    print("application.yml 配置：")
    print("""
spring:
  ai:
    ollama:
      base-url: http://localhost:11434
      chat:
        options:
          model: llama3.2
          temperature: 0.7
""")


def show_ollama_java_code():
    """展示 Ollama Java 代码。"""
    print("💻 Ollama Java 代码：")
    print("""
@Service
public class OllamaChatService {

    private final ChatClient chatClient;

    public OllamaChatService(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    public String chat(String userInput) {
        return chatClient.prompt()
            .user(userInput)
            .call()
            .content();
    }

    public Flux<String> chatStream(String userInput) {
        return chatClient.prompt()
            .user(userInput)
            .stream()
            .content();
    }
}
""")


def show_ollama_models():
    """展示 Ollama 支持的模型。"""
    print("🤖 Ollama 常用模型：")
    print("""
├── Llama 3.2          → Meta 开源，综合能力强
├── Qwen 2.5           → 阿里开源，中文能力强
├── Mistral            → 欧洲开源，轻量级
├── CodeLlama          → 代码生成专精
├── Gemma 2            → Google 开源
└── Phi-3              → Microsoft 小型模型
""")


def check_ollama_connection():
    """检查 Ollama 连接状态（模拟）。"""
    print("🔌 Ollama 连接检查：")
    print("   地址: http://localhost:11434")
    print("   状态: ✅ 连接成功（模拟）")
    print("   可用模型: llama3.2, qwen2.5")
    print()


def main():
    """主函数：展示 Ollama 本地模型接入。"""
    print("=" * 60)
    print("🏠 Ollama 本地模型接入")
    print("=" * 60)
    print()

    show_ollama_setup_steps()
    show_spring_ai_ollama_config()
    show_ollama_java_code()
    show_ollama_models()
    check_ollama_connection()

    print("=" * 60)
    print("✅ Ollama 本地模型接入演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
