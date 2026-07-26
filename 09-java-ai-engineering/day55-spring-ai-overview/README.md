# Day 55: Spring AI 总览与生态定位

> **今日目标**: 理解 Spring AI 的设计哲学，掌握 ChatClient / EmbeddingClient / VectorStore 三大核心抽象
> **核心问题**: Spring AI 和 LangChain4j 有什么区别？为什么 Java 架构师必须掌握 Spring AI？

---

## 🎯 今日目标

1. 理解 Spring AI 的定位：Spring 生态的 AI 框架，为 Java 开发者提供 AI 工程化标准
2. 掌握三大核心抽象：ChatClient / EmbeddingClient / VectorStore
3. 理解 Spring Boot 3 Starter 自动配置机制
4. 了解 2026 年 AI 应用开发生态全景

---

## 📚 必学知识

### 1. Spring AI 定位

Spring AI 是 Spring 官方团队推出的 AI 应用框架，定位与 Spring Boot / Spring Cloud / Spring Data 一致：

- **设计哲学**：Spring 的"约定优于配置"理念延伸到 AI 领域
- **目标用户**：Java / Spring 开发者，无需切换到 Python
- **核心价值**：把 AI 能力无缝集成到 Spring 生态中
- **与 LangChain4j 的关系**：两者竞争互补，Spring AI 更深绑定 Spring 生态

### 2. 三大核心抽象

```
Spring AI 三大核心抽象
│
├── ChatClient      → 对话模型（类比 OpenAI Client）
│      ├── 同步调用: .call()
│      ├── 流式调用: .stream()
│      └── 工具调用: .tools()
│
├── EmbeddingClient → 向量嵌入（类比 OpenAI Embedding）
│      ├── embed(text) → float[]
│      └── embed(List<String>) → List<float[]>
│
└── VectorStore     → 向量存储（类比 Milvus / Redis）
       ├── add(List<Document>)
       ├── similaritySearch(query)
       └── delete(ids)
```

**ChatClient 核心 API**：
```java
// 同步调用
String response = chatClient.prompt()
    .user("你好")
    .call()
    .content();

// 流式调用
Flux<String> stream = chatClient.prompt()
    .user("写一首诗")
    .stream()
    .content();

// 带工具调用
String response = chatClient.prompt()
    .user("北京天气")
    .tools(new WeatherTool())
    .call()
    .content();
```

### 3. Spring Boot 3 Starter 详解

Spring AI 通过 Starter 实现自动配置：

| Starter | 依赖 | 用途 |
|---------|------|------|
| `spring-ai-openai-spring-boot-starter` | OpenAI | 接入 GPT 系列 |
| `spring-ai-ollama-spring-boot-starter` | Ollama | 本地模型 |
| `spring-ai-qdrant-spring-boot-starter` | Qdrant | 向量存储 |
| `spring-ai-redis-spring-boot-starter` | Redis | 向量/记忆存储 |
| `spring-ai-milvus-spring-boot-starter` | Milvus | 向量存储 |

**自动配置原理**：
```yaml
# application.yml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      chat:
        options:
          model: gpt-4o-mini
          temperature: 0.7
```

Spring Boot 自动创建 `ChatClient` Bean，开发者直接注入使用。

### 4. 2026 大模型应用开发生态

```
2026 AI 应用开发生态
│
├── Python 生态
│   ├── LangChain / LangGraph（主流）
│   ├── LlamaIndex（RAG 专精）
│   └── AutoGen（多 Agent）
│
├── Java 生态
│   ├── Spring AI（Spring 官方）
│   ├── LangChain4j（社区驱动）
│   └── Semantic Kernel（微软）
│
├── 模型层
│   ├── OpenAI GPT-5
│   ├── Claude 4
│   ├── DeepSeek V3
│   ├── 通义千问 Qwen3
│   └── 开源 Llama 4 / Mistral
│
└── 基础设施
    ├── 向量数据库（Milvus / Qdrant / Redis）
    ├── 模型网关（LiteLLM / OneAPI）
    └── 可观测性（LangSmith / Langfuse）
```

### 5. 主流模型平台盘点

| 平台 | 代表模型 | 特点 | 中文能力 |
|------|----------|------|----------|
| OpenAI | GPT-4o / GPT-5 | 最强通用 | ⭐⭐⭐ |
| Anthropic | Claude 4 | 长上下文 | ⭐⭐⭐ |
| DeepSeek | DeepSeek V3 | 性价比之王 | ⭐⭐⭐⭐⭐ |
| 阿里百炼 | 通义千问 | 国内合规 | ⭐⭐⭐⭐⭐ |
| 智谱 | GLM-4 | 开源友好 | ⭐⭐⭐⭐ |
| 月之暗面 | Kimi | 长文本 | ⭐⭐⭐⭐ |
| 硅基流动 | 聚合 API | 一站式 | ⭐⭐⭐⭐ |
| Ollama | 本地部署 | 隐私优先 | 取决于模型 |

---

## 🔗 官方资料

| 知识点 | 地址 | 军哥课程 |
|--------|------|----------|
| Spring AI 官方文档 | https://docs.spring.io/spring-ai/reference/ | 模块1: 1 |
| Spring AI GitHub | https://github.com/spring-projects/spring-ai | 模块1: 2 |
| Spring AI ChatClient | https://docs.spring.io/spring-ai/reference/api/chatclient.html | 模块1: 3 |
| Spring Boot Starter | https://docs.spring.io/spring-ai/reference/getting-started.html | 模块1: 4 |
| LangChain4j 对比 | https://docs.langchain4j.dev/ | 模块1: 2 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Spring AI 的设计哲学与定位
- [ ] ChatClient / EmbeddingClient / VectorStore 三大抽象
- [ ] Spring Boot Starter 自动配置机制
- [ ] Spring AI vs LangChain4j 区别

### 只需理解（L2）
- [ ] 2026 AI 开发生态全景
- [ ] 主流模型平台特点
- [ ] Spring AI 源码结构

### 今天不深入（后面会讲）
- [ ] Spring AI Advisor 责任链
- [ ] RAG 完整实现
- [ ] 多模态支持

---

## 💻 今日编码任务

### 文件结构

```
day55-spring-ai-overview/
├── README.md
├── LEARNING_FLOW.md
├── 00_spring_ai_intro.py          # 快速初始化项目
├── 01_chatclient_basics.py        # ChatClient 核心 API
├── 02_ecosystem_map.py            # 生态全景图
├── 99_boss_answer.md
└── requirements.txt
```

### Task 1: 00_spring_ai_intro.py（30min）

快速初始化 Spring AI 项目，理解项目骨架和依赖结构。

**关键代码提示**：
```xml
<!-- pom.xml 核心依赖 -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
</dependency>
```

```java
// 最简单的 Spring AI 应用
@SpringBootApplication
public class SpringAiIntroApplication {
    @Bean
    CommandLineRunner demo(ChatClient.Builder builder) {
        return args -> {
            ChatClient client = builder.build();
            String response = client.prompt()
                .user("Spring AI 是什么？")
                .call()
                .content();
            System.out.println(response);
        };
    }
}
```

**验收标准**：
```bash
mvn spring-boot:run
# 输出：
# 🚀 Spring AI 项目启动成功
# 📝 ChatClient 自动配置完成
# ✅ Response: Spring AI 是 Spring 官方推出的 AI 应用框架...
```

### Task 2: 01_chatclient_basics.py（45min）

掌握 ChatClient 核心 API：同步调用、流式调用、工具调用。

**关键代码提示**：
```java
// 1. 同步调用
String content = chatClient.prompt()
    .user("你好")
    .call()
    .content();

// 2. 流式调用
Flux<String> stream = chatClient.prompt()
    .user("写一首关于Java的诗")
    .stream()
    .content();

// 3. 带 System Prompt
String content = chatClient.prompt()
    .system("你是一个Java架构师")
    .user("解释 Spring Boot 自动配置")
    .call()
    .content();
```

**验收标准**：
```bash
python 01_chatclient_basics.py
# 输出：
# 📤 同步调用: 你好！我是...
# 📡 流式调用: Java是一门...（逐字出现）
# 🎭 System Prompt: 作为Java架构师...
```

### Task 3: 02_ecosystem_map.py（30min）

梳理 2026 AI 开发生态全景，理解各框架定位。

**验收标准**：
```bash
python 02_ecosystem_map.py
# 输出：
# 🌍 2026 AI 开发生态全景
# ├── Python: LangChain / LangGraph / LlamaIndex
# ├── Java: Spring AI / LangChain4j / Semantic Kernel
# ├── 模型层: OpenAI / Claude / DeepSeek / Qwen
# └── 基础设施: Milvus / Redis / Langfuse
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Spring AI 与 LangChain4j 的区别
- 解释 Spring Boot Starter 自动配置原理
- 帮你调试 Maven / Gradle 依赖冲突
- 解释 ChatClient API 用法

### 今天 AI 不能帮你
- 替你理解 Spring AI 设计哲学（你必须自己理解）
- 替你回答 Boss（你必须自己回答）
- 替你记忆各模型平台特点（你必须自己比较）

### 正确用法
> "我有10年Java架构经验，Spring AI 的 ChatClient 和 OpenAI 的 SDK 有什么设计上的区别？请用 Spring Data 的 Repository 抽象类比解释。"

### 错误用法
> "帮我写一个完整的 Spring AI 项目。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day55-spring-ai-overview/
    ├── README.md
    ├── LEARNING_FLOW.md
    ├── 00_spring_ai_intro.py
    ├── 01_chatclient_basics.py
    ├── 02_ecosystem_map.py
    ├── 99_boss_answer.md
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 55 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Spring AI | ... | ... |
| ChatClient | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day55-spring-ai-overview/
git commit -m "feat(day55): Spring AI 总览与生态定位 - 三大核心抽象"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **Spring AI 和 LangChain4j 有什么区别？各有什么优劣势？**
2. **ChatClient 和 OpenAI SDK 的 Client 有什么设计上的区别？**
3. **Spring Boot Starter 自动配置的原理是什么？Spring AI 如何利用它？**
4. **EmbeddingClient 和 VectorStore 的职责分别是什么？为什么分开设计？**
5. **为什么 Java 架构师应该掌握 Spring AI 而不是只用 Python？**

### 验收标准
- 每个答案 **不少于100字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合 Java / Spring 生态经验** 来讲

---

## 🎤 面试题

1. **Spring AI 的核心设计思想是什么？它和 Spring Data 有什么相似之处？**
2. **ChatClient 支持哪些调用模式？流式调用和同步调用在实现上有什么不同？**
3. **如果要支持多模型切换，Spring AI 应该怎么设计？**
4. **EmbeddingClient 的作用是什么？它和 ChatClient 的关系是什么？**
5. **Spring AI 的 VectorStore 和 RAG 的关系是什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_spring_ai_intro.py | 15分 | 能初始化项目 + 理解依赖结构 |
| 01_chatclient_basics.py | 20分 | 同步 + 流式 + System Prompt |
| 02_ecosystem_map.py | 15分 | 完整生态图 + 各框架定位 |
| README 学习总结 | 15分 | 有自己的理解，不是抄的 |
| Boss 答案 | 20分 | 5题全部完成 + 用自己的话 |
| 代码质量 | 15分 | 命名清晰 + 注释 + 结构 |

---

## 🔓 解锁条件

- [ ] 3个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 56: Spring AI 模型接入实战**

---

## 📊 今日检查清单

- [ ] 读了 Spring AI 官方文档
- [ ] 读了 Spring AI GitHub README
- [ ] 写了 00_spring_ai_intro.py
- [ ] 写了 01_chatclient_basics.py
- [ ] 写了 02_ecosystem_map.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99_boss_answer.md
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
