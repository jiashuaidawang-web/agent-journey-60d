# Day 57: LangChain4j + ChatMemory

> **今日目标**: 掌握 LangChain4j 框架，理解 ChatMemory 记忆对话机制与多会话管理
> **核心问题**: ChatMemory 如何实现跨会话记忆？如何支持多用户隔离？

---

## 🎯 今日目标

1. 理解 LangChain4j 框架概览及其与 Spring AI 的对比
2. 掌握 ChatModel 接入（OpenAI / DeepSeek / Ollama）
3. 实现 ChatMemory 记忆对话机制
4. 实现对话隔离策略与多会话管理
5. 实现 Redis / MySQL 持久化

---

## 📚 必学知识

### 1. LangChain4j 框架概览

**LangChain4j** 是 LangChain 的 Java 移植版，由社区驱动，功能丰富。

```
LangChain4j 核心组件
│
├── AiServices           → 声明式 AI 服务（接口 + 注解）
├── ChatLanguageModel    → 对话模型接入
├── EmbeddingModel       → 向量嵌入
├── VectorStore          → 向量存储
├── ChatMemory           → 对话记忆
├── Tools                → 工具调用
└── RAG                  → 检索增强生成
```

**与 Spring AI 对比**：

| 维度 | LangChain4j | Spring AI |
|------|-------------|-----------|
| 出品方 | 社区 | Spring 官方 |
| Spring 集成 | 手动配置 | 深度集成 |
| 功能丰富度 | 高 | 中 |
| 声明式服务 | ✅ AiServices | ❌ 手动编写 |
| 学习曲线 | 中 | 低（Spring 开发者） |

### 2. ChatModel 接入

**接入 OpenAI**：
```java
ChatLanguageModel model = OpenAiChatModel.builder()
    .apiKey(System.getenv("OPENAI_API_KEY"))
    .modelName("gpt-4o-mini")
    .temperature(0.7)
    .build();

String response = model.generate("你好");
```

**接入 DeepSeek**：
```java
ChatLanguageModel model = OpenAiChatModel.builder()
    .apiKey(System.getenv("DEEPSEEK_API_KEY"))
    .baseUrl("https://api.deepseek.com/v1")
    .modelName("deepseek-chat")
    .build();
```

**接入 Ollama**：
```java
ChatLanguageModel model = OllamaChatModel.builder()
    .baseUrl("http://localhost:11434")
    .modelName("llama3.2")
    .build();
```

### 3. LangChain4j 整合 Spring Boot

**依赖**：
```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-spring-boot-starter</artifactId>
    <version>0.33.0</version>
</dependency>
```

**配置**：
```yaml
langchain4j:
  open-ai:
    chat-model:
      api-key: ${OPENAI_API_KEY}
      model-name: gpt-4o-mini
      temperature: 0.7
```

### 4. ChatMemory 记忆对话机制

**ChatMemory** 是 LangChain4j 的核心组件，用于存储和检索对话历史。

```
ChatMemory 工作流
│
├── 用户发送消息
│     ↓
├── ChatMemory 读取历史消息
│     ↓
├── 将历史 + 新消息发给 LLM
│     ↓
├── LLM 生成回复
│     ↓
├── ChatMemory 存储新消息
│     ↓
└── 返回回复
```

**核心接口**：
```java
public interface ChatMemory {
    Object id();                                    // 会话 ID
    void add(Object message);                       // 添加消息
    List<Object> messages();                        // 获取所有消息
    void clear();                                   // 清空记忆
}
```

**实现类**：
- `MessageWindowChatMemory`：滑动窗口，保留最近 N 条消息
- `TokenWindowChatMemory`：按 Token 数保留消息

**使用示例**：
```java
ChatMemory memory = MessageWindowChatMemory.withMaxMessages(10);

ChatLanguageModel model = OpenAiChatModel.builder()
    .apiKey(System.getenv("OPENAI_API_KEY"))
    .build();

// 第一轮对话
memory.add(UserMessage.from("你好，我是张三"));
String response1 = model.generate(memory.messages()).content();
memory.add(AssistantMessage.from(response1));

// 第二轮对话（带历史）
memory.add(UserMessage.from("我叫什么名字？"));
String response2 = model.generate(memory.messages()).content();
// 输出：你叫张三
```

### 5. 对话隔离策略与多会话管理

**问题**：多用户 / 多会话场景下，如何隔离对话记忆？

**解决方案**：使用 `Map<String, ChatMemory>` 维护每个会话的记忆。

```java
@Component
public class ChatMemoryManager {

    private final Map<String, ChatMemory> memoryMap = new ConcurrentHashMap<>();

    public ChatMemory getMemory(String sessionId) {
        return memoryMap.computeIfAbsent(sessionId,
            id -> MessageWindowChatMemory.withMaxMessages(10));
    }

    public void clearMemory(String sessionId) {
        memoryMap.remove(sessionId);
    }
}
```

**隔离策略**：
- **按 Session ID 隔离**：每个会话独立记忆
- **按 User ID 隔离**：同一用户多设备共享记忆
- **按 Tenant ID 隔离**：多租户场景

### 6. Redis / MySQL 持久化

**问题**：内存中的 ChatMemory 重启后丢失，如何持久化？

**Redis 持久化**：
```java
public class RedisChatMemory implements ChatMemory {

    private final String sessionId;
    private final RedisTemplate<String, Object> redisTemplate;

    @Override
    public void add(Object message) {
        redisTemplate.opsForList().rightPush(sessionId, message);
        redisTemplate.expire(sessionId, Duration.ofHours(24));
    }

    @Override
    public List<Object> messages() {
        return redisTemplate.opsForList().range(sessionId, 0, -1);
    }
}
```

**MySQL 持久化**：
```java
@Entity
@Table(name = "chat_message")
public class ChatMessageEntity {
    @Id
    @GeneratedValue
    private Long id;
    private String sessionId;
    private String role;      // user / assistant
    private String content;
    private LocalDateTime timestamp;
}
```

### 7. Function Calling 工具调用

**LangChain4j 工具定义**：
```java
@Tool("获取指定城市的天气")
public String getWeather(@P("城市名称") String city) {
    return city + "今天晴，25°C";
}

// 绑定工具
Assistant assistant = AiServices.builder(Assistant.class)
    .chatLanguageModel(model)
    .chatMemory(memory)
    .tools(new WeatherTool())
    .build();
```

### 8. 系统提示词配置

**@SystemMessage 注解**：
```java
public interface Assistant {
    @SystemMessage("你是一个Java架构师，回答要简洁专业")
    String chat(String userMessage);
}

Assistant assistant = AiServices.builder(Assistant.class)
    .chatLanguageModel(model)
    .build();
```

---

## 🔗 官方资料

| 知识点 | 地址 | 军哥课程 |
|--------|------|----------|
| LangChain4j 官方文档 | https://docs.langchain4j.dev/ | 模块2: 7 |
| LangChain4j ChatMemory | https://docs.langchain4j.dev/tutorials/memory/ | 模块2: 8 |
| LangChain4j 工具调用 | https://docs.langchain4j.dev/tutorials/tools/ | 模块2: 9 |
| LangChain4j Spring Boot | https://docs.langchain4j.dev/integrations/spring-boot/ | 模块2: 10 |
| LangChain4j RAG | https://docs.langchain4j.dev/tutorials/rag/ | 模块2: 11 |
| LangChain4j AiServices | https://docs.langchain4j.dev/tutorials/ai-services/ | 模块2: 12 |
| LangChain4j 多模型 | https://docs.langchain4j.dev/category/language-models/ | 模块2: 13 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] LangChain4j 框架概览与 Spring AI 对比
- [ ] ChatMemory 核心接口与实现
- [ ] 对话隔离策略与多会话管理
- [ ] Redis / MySQL 持久化实现
- [ ] 工具调用与系统提示词配置

### 只需理解（L2）
- [ ] LangChain4j 与 Spring AI 的优劣势
- [ ] 声明式 AiServices 原理
- [ ] TokenWindowChatMemory 实现

### 今天不深入（后面会讲）
- [ ] LangChain4j RAG 完整实现
- [ ] 多模态支持
- [ ] 模型评估

---

## 💻 今日编码任务

### 文件结构

```
day57-langchain4j-memory/
├── README.md
├── LEARNING_FLOW.md
├── 00_langchain4j_basics.py        # 框架基础
├── 01_chatmemory_demo.py           # 记忆对话
├── 02_persistence.py               # Redis/MySQL 持久化
├── 99_boss_answer.md
└── requirements.txt
```

### Task 1: 00_langchain4j_basics.py（30min）

理解 LangChain4j 框架基础，掌握 ChatModel 接入。

**关键代码提示**：
```java
// OpenAI 接入
ChatLanguageModel model = OpenAiChatModel.builder()
    .apiKey(System.getenv("OPENAI_API_KEY"))
    .modelName("gpt-4o-mini")
    .build();

// DeepSeek 接入
ChatLanguageModel model = OpenAiChatModel.builder()
    .apiKey(System.getenv("DEEPSEEK_API_KEY"))
    .baseUrl("https://api.deepseek.com/v1")
    .modelName("deepseek-chat")
    .build();

// Ollama 接入
ChatLanguageModel model = OllamaChatModel.builder()
    .baseUrl("http://localhost:11434")
    .modelName("llama3.2")
    .build();
```

**验收标准**：
```bash
python 00_langchain4j_basics.py
# 输出：
# ☕ LangChain4j 框架基础
# ├── OpenAI 接入: ✅
# ├── DeepSeek 接入: ✅
# └── Ollama 接入: ✅
```

### Task 2: 01_chatmemory_demo.py（45min）

实现 ChatMemory 记忆对话，理解多会话管理。

**关键代码提示**：
```java
// 创建记忆
ChatMemory memory = MessageWindowChatMemory.withMaxMessages(10);

// 添加消息
memory.add(UserMessage.from("你好，我是张三"));
memory.add(AssistantMessage.from("你好张三"));

// 获取历史
List<ChatMessage> history = memory.messages();
```

**验收标准**：
```bash
python 01_chatmemory_demo.py
# 输出：
# 🧠 ChatMemory 记忆对话
# ├── 第一轮: 你好，我是张三
# ├── 第二轮: 我叫什么名字？
# └── 回复: 你叫张三 ✅
```

### Task 3: 02_persistence.py（45min）

实现 Redis / MySQL 持久化，理解持久化策略。

**关键代码提示**：
```java
// Redis 持久化
public class RedisChatMemory implements ChatMemory {
    private final String sessionId;
    private final RedisTemplate<String, Object> redisTemplate;

    @Override
    public void add(Object message) {
        redisTemplate.opsForList().rightPush(sessionId, message);
    }
}
```

**验收标准**：
```bash
python 02_persistence.py
# 输出：
# 💾 ChatMemory 持久化
# ├── Redis: ✅ 支持
# └── MySQL: ✅ 支持
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 LangChain4j API 用法
- 帮你调试 Spring Boot 配置
- 解释 ChatMemory 实现原理
- 帮你对比 LangChain4j 与 Spring AI

### 今天 AI 不能帮你
- 替你理解 ChatMemory 设计（你必须自己理解）
- 替你回答 Boss（你必须自己回答）
- 替你记忆持久化策略（你必须自己比较）

### 正确用法
> "LangChain4j 的 ChatMemory 和 Spring AI 的 Conversation 有什么区别？请用 Java 的 Session/Cookie 类比解释。"

### 错误用法
> "帮我写一个完整的 LangChain4j 项目。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day57-langchain4j-memory/
    ├── README.md
    ├── LEARNING_FLOW.md
    ├── 00_langchain4j_basics.py
    ├── 01_chatmemory_demo.py
    ├── 02_persistence.py
    ├── 99_boss_answer.md
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 57 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| ChatMemory | ... | ... |
| 多会话管理 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day57-langchain4j-memory/
git commit -m "feat(day57): LangChain4j + ChatMemory - 多会话管理与持久化"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **ChatMemory 和 Spring AI 的 Conversation 有什么区别？**
2. **如何实现多用户对话隔离？请描述设计方案。**
3. **Redis 和 MySQL 持久化 ChatMemory 各有什么优劣势？**
4. **ChatMemory 的滑动窗口和 Token 窗口有什么区别？**
5. **Function Calling 在 LangChain4j 中如何实现？**

### 验收标准
- 每个答案 **不少于100字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码场景** 来讲

---

## 🎤 面试题

1. **LangChain4j 和 Spring AI 有什么区别？各适合什么场景？**
2. **ChatMemory 的核心接口有哪些？请描述其职责。**
3. **如何实现跨会话记忆持久化？请描述 Redis 和 MySQL 方案。**
4. **Function Calling 的原理是什么？LangChain4j 如何实现？**
5. **系统提示词在 LangChain4j 中如何配置？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_langchain4j_basics.py | 15分 | 框架基础 + 模型接入 |
| 01_chatmemory_demo.py | 20分 | 记忆对话 + 多会话管理 |
| 02_persistence.py | 20分 | Redis + MySQL 持久化 |
| README 学习总结 | 15分 | 有自己的理解，不是抄的 |
| Boss 答案 | 20分 | 5题全部完成 + 用自己的话 |
| 代码质量 | 10分 | 命名清晰 + 注释 + 结构 |

---

## 🔓 解锁条件

- [ ] 3个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 58: Spring AI Advisor 责任链**

---

## 📊 今日检查清单

- [ ] 读了 LangChain4j 官方文档
- [ ] 读了 LangChain4j ChatMemory 文档
- [ ] 读了 LangChain4j 工具调用文档
- [ ] 写了 00_langchain4j_basics.py
- [ ] 写了 01_chatmemory_demo.py
- [ ] 写了 02_persistence.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99_boss_answer.md
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
