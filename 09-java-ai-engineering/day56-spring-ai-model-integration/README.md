# Day 56: Spring AI 模型接入实战

> **今日目标**: 掌握主流模型平台的接入方式，能根据业务需求做模型选型决策
> **核心问题**: 不同模型平台有什么区别？如何动态切换模型？

---

## 🎯 今日目标

1. 盘点主流模型平台（OpenAI / DeepSeek / 阿里百炼 / 通义 / 硅基流动 / 月之暗面 / 智谱 / 百度 / Azure / Groq / Ollama）
2. 掌握模型选型决策表（价格 / 速度 / 窗口 / 中文能力 / 多模态 / 工具调用）
3. 实现 Ollama 本地模型完整接入
4. 实现多模型动态切换

---

## 📚 必学知识

### 1. 主流模型平台全盘点

| 平台 | 代表模型 | 接入方式 | 价格区间 | 特点 |
|------|----------|----------|----------|------|
| OpenAI | GPT-4o / GPT-5 | 官方 SDK | $$$ | 最强通用 |
| DeepSeek | DeepSeek V3 | OpenAI 兼容 | $ | 性价比之王 |
| 阿里百炼 | 通义千问 Qwen3 | 官方 SDK | ¥ | 国内合规 |
| 硅基流动 | 聚合 API | OpenAI 兼容 | $ | 一站式接入 |
| 月之暗面 | Kimi | OpenAI 兼容 | ¥ | 长文本 |
| 智谱 | GLM-4 | OpenAI 兼容 | ¥ | 开源友好 |
| 百度 | 文心一言 | 官方 SDK | ¥ | 国内合规 |
| Azure | OpenAI 托管 | Azure SDK | $$$ | 企业级 |
| Groq | 推理加速 | OpenAI 兼容 | $ | 超快推理 |
| Ollama | 本地模型 | 本地 API | 免费 | 隐私优先 |

### 2. 模型选型决策表

```
模型选型决策树
│
├── 需要国内合规？
│   ├── 是 → 阿里百炼 / 百度 / 智谱
│   └── 否 → 继续
│
├── 需要最强能力？
│   ├── 是 → OpenAI GPT-4o / GPT-5
│   └── 否 → 继续
│
├── 需要性价比？
│   ├── 是 → DeepSeek V3 / 硅基流动
│   └── 否 → 继续
│
├── 需要本地部署？
│   ├── 是 → Ollama + Llama / Qwen
│   └── 否 → 继续
│
└── 需要长文本？
    ├── 是 → Kimi / Claude 4
    └── 否 → 根据预算选择
```

**详细对比**：

| 维度 | OpenAI | DeepSeek | 阿里百炼 | Ollama |
|------|--------|----------|----------|--------|
| 价格 | 高 | 低 | 中 | 免费 |
| 速度 | 中 | 快 | 中 | 取决于硬件 |
| 中文能力 | 中 | 强 | 强 | 取决于模型 |
| 工具调用 | 强 | 强 | 强 | 取决于模型 |
| 多模态 | 强 | 弱 | 中 | 取决于模型 |
| 合规 | 海外 | 海外 | 国内 | 本地 |

### 3. Ollama 本地模型完整接入

**Ollama 简介**：
- 本地模型管理工具，支持 Llama / Mistral / Qwen / CodeLlama 等
- 提供 OpenAI 兼容 API
- 适合隐私优先、离线场景

**Spring AI 接入 Ollama**：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-ollama-spring-boot-starter</artifactId>
</dependency>
```

```yaml
spring:
  ai:
    ollama:
      base-url: http://localhost:11434
      chat:
        options:
          model: llama3.2
          temperature: 0.7
```

**Java 代码**：
```java
@Autowired
private ChatClient.Builder chatClientBuilder;

public String chatWithOllama(String input) {
    return chatClientBuilder.build()
        .prompt()
        .user(input)
        .call()
        .content();
}
```

### 4. 多模型动态切换

**场景**：
- 简单任务 → 便宜模型（DeepSeek / Ollama）
- 复杂任务 → 强模型（GPT-4o / Claude）
- 敏感任务 → 本地模型（Ollama）

**实现方式**：

```java
@Service
public class ModelRouterService {

    private final Map<String, ChatClient> modelMap;

    public ModelRouterService(ChatClient.Builder builder) {
        this.modelMap = Map.of(
            "gpt-4o", builder.build(),  // 默认配置
            "ollama", builder.build()   // Ollama 配置
        );
    }

    public String chat(String model, String input) {
        ChatClient client = modelMap.getOrDefault(model, modelMap.get("gpt-4o"));
        return client.prompt().user(input).call().content();
    }
}
```

**配置多模型**：
```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
    ollama:
      base-url: http://localhost:11434
```

---

## 🔗 官方资料

| 知识点 | 地址 | 军哥课程 |
|--------|------|----------|
| Spring AI OpenAI | https://docs.spring.io/spring-ai/reference/api/chat/openai-chat.html | 模块1: 5 |
| Spring AI Ollama | https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html | 模块1: 6 |
| DeepSeek API | https://platform.deepseek.com/ | 模块3: 18 |
| 阿里百炼 | https://bailian.console.aliyun.com/ | 模块3: 19 |
| Ollama 官网 | https://ollama.com/ | 模块1: 6 |
| 硅基流动 | https://siliconflow.cn/ | 模块3: 18 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 主流模型平台特点与接入方式
- [ ] 模型选型决策树
- [ ] Ollama 本地模型接入
- [ ] 多模型动态切换实现

### 只需理解（L2）
- [ ] 各平台价格细节
- [ ] 模型能力差异
- [ ] 国内合规要求

### 今天不深入（后面会讲）
- [ ] 模型网关（LiteLLM / OneAPI）
- [ ] 模型评估
- [ ] 模型微调

---

## 💻 今日编码任务

### 文件结构

```
day56-spring-ai-model-integration/
├── README.md
├── LEARNING_FLOW.md
├── 00_model_platforms.py          # 平台对比表
├── 01_ollama_integration.py       # 本地模型接入
├── 02_model_decision.py           # 选型决策代码
├── 99_boss_answer.md
└── requirements.txt
```

### Task 1: 00_model_platforms.py（30min）

整理主流模型平台对比表，理解各平台特点。

**关键代码提示**：
```python
# 模型平台数据模型
@dataclass
class ModelPlatform:
    name: str
    models: List[str]
    price_level: str  # $ / $$ / $$$
    chinese_ability: int  # 1-5
    tool_calling: bool
    compliance: str  # 国内 / 海外
```

**验收标准**：
```bash
python 00_model_platforms.py
# 输出：
# 📊 主流模型平台对比
# ├── OpenAI: GPT-4o / GPT-5 | 价格: $$$ | 中文: ⭐⭐⭐
# ├── DeepSeek: V3 | 价格: $ | 中文: ⭐⭐⭐⭐⭐
# ├── 阿里百炼: Qwen3 | 价格: ¥ | 中文: ⭐⭐⭐⭐⭐
# └── Ollama: Llama / Qwen | 价格: 免费 | 中文: 取决于模型
```

### Task 2: 01_ollama_integration.py（45min）

实现 Ollama 本地模型接入，理解本地部署流程。

**关键代码提示**：
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-ollama-spring-boot-starter</artifactId>
</dependency>
```

```yaml
# application.yml
spring:
  ai:
    ollama:
      base-url: http://localhost:11434
      chat:
        options:
          model: llama3.2
```

**验收标准**：
```bash
python 01_ollama_integration.py
# 输出：
# 🏠 Ollama 本地模型接入
# ├── 模型: llama3.2
# ├── 地址: http://localhost:11434
# └── 状态: ✅ 连接成功
```

### Task 3: 02_model_decision.py（45min）

实现模型选型决策代码，根据业务需求选择模型。

**关键代码提示**：
```python
def select_model(requirements: dict) -> str:
    """根据需求选择模型。"""
    if requirements.get("compliance") == "国内":
        return "阿里百炼"
    if requirements.get("budget") == "低":
        return "DeepSeek"
    if requirements.get("privacy") == "高":
        return "Ollama"
    return "OpenAI"
```

**验收标准**：
```bash
python 02_model_decision.py
# 输出：
# 🎯 模型选型决策
# ├── 需求: 国内合规 → 推荐: 阿里百炼
# ├── 需求: 低成本 → 推荐: DeepSeek
# ├── 需求: 隐私优先 → 推荐: Ollama
# └── 需求: 最强能力 → 推荐: OpenAI
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释各模型平台接入方式
- 帮你调试 Spring AI 配置
- 解释 Ollama 部署流程
- 帮你对比模型能力

### 今天 AI 不能帮你
- 替你理解模型选型逻辑（你必须自己理解）
- 替你回答 Boss（你必须自己回答）
- 替你记忆各平台价格（你必须自己比较）

### 正确用法
> "我需要为国内金融客户选择模型，要求合规、中文能力强、支持工具调用。请帮我分析各平台优劣势。"

### 错误用法
> "帮我写一个完整的模型接入系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day56-spring-ai-model-integration/
    ├── README.md
    ├── LEARNING_FLOW.md
    ├── 00_model_platforms.py
    ├── 01_ollama_integration.py
    ├── 02_model_decision.py
    ├── 99_boss_answer.md
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 56 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 模型选型 | ... | ... |
| Ollama | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day56-spring-ai-model-integration/
git commit -m "feat(day56): Spring AI 模型接入实战 - 多模型动态切换"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **OpenAI 和 DeepSeek 有什么区别？各适合什么场景？**
2. **Ollama 本地部署的优势和劣势是什么？什么场景下应该用 Ollama？**
3. **如何设计一个多模型动态切换系统？需要考虑哪些因素？**
4. **国内合规要求下，应该选择哪些模型平台？**
5. **模型选型的核心决策因素是什么？请按优先级排序。**

### 验收标准
- 每个答案 **不少于100字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合业务场景** 来讲

---

## 🎤 面试题

1. **Spring AI 如何支持多模型切换？请描述实现方式。**
2. **Ollama 和云端模型有什么区别？各自的适用场景是什么？**
3. **如果需要支持模型降级（主模型故障时切换备用），你会怎么设计？**
4. **模型选型的核心指标有哪些？如何量化评估？**
5. **国内合规对模型选型有什么影响？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_model_platforms.py | 15分 | 完整对比表 + 各平台特点 |
| 01_ollama_integration.py | 20分 | 接入流程 + 配置说明 |
| 02_model_decision.py | 20分 | 决策逻辑 + 多场景覆盖 |
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

**解锁后进入 Day 57: LangChain4j + ChatMemory**

---

## 📊 今日检查清单

- [ ] 读了 Spring AI OpenAI 文档
- [ ] 读了 Spring AI Ollama 文档
- [ ] 读了 DeepSeek / 阿里百炼 文档
- [ ] 写了 00_model_platforms.py
- [ ] 写了 01_ollama_integration.py
- [ ] 写了 02_model_decision.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99_boss_answer.md
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
