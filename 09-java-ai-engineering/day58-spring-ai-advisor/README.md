# Day 58: Spring AI Advisor 责任链

> **今日目标**: 掌握 Spring AI Advisor 责任链机制，能实现日志/安全/限流/审计/动态切模型等自定义 Advisor
> **核心问题**: Advisor 如何实现拦截器模式？它与 Java Filter / Interceptor / AOP 有什么区别？

---

## 🎯 今日目标

1. 理解 Advisor 拦截器责任链深度源码解析
2. 掌握自定义 Advisor 实现（日志 / 敏感词 / 限流 / 审计 / 动态切模型）
3. 理解 AI 应用中间件 / Pipeline / Interceptor 架构
4. 与 Java Filter / Interceptor / AOP 类比

---

## 📚 必学知识

### 1. Advisor 拦截器责任链深度源码解析

**Advisor** 是 Spring AI 的核心扩展机制，类似于 Spring MVC 的 Interceptor。

```
Advisor 责任链工作流
│
├── 用户调用 ChatClient.prompt()...call()
│     ↓
├── AdvisorChain 构建责任链
│     ↓
├── 前置处理（before）
│   ├── Advisor1.before()
│   ├── Advisor2.before()
│   └── Advisor3.before()
│     ↓
├── 核心调用（call）
│   └── ChatModel.call()
│     ↓
├── 后置处理（after）
│   ├── Advisor3.after()
│   ├── Advisor2.after()
│   └── Advisor1.after()
│     ↓
└── 返回结果
```

**核心接口**：
```java
public interface Advisor extends Ordered {
    // 前置处理
    default AdvisorResponse before(AdvisorRequest advisorRequest, AdvisorChain advisorChain) {
        return advisorChain.nextBefore(advisorRequest);
    }

    // 后置处理
    default ChatClientResponse after(ChatClientResponse chatClientResponse, AdvisorChain advisorChain) {
        return advisorChain.nextAfter(chatClientResponse);
    }

    // 执行顺序（越小越先执行）
    default int getOrder() {
        return 0;
    }
}
```

**内置 Advisor**：
- `MessageChatMemoryAdvisor`：对话记忆管理
- `QuestionAnswerAdvisor`：RAG 问答
- `SafeGuardAdvisor`：敏感词过滤
- `RetryAdvisor`：重试机制

### 2. 自定义 Advisor 实现

**日志 Advisor**：
```java
public class LoggingAdvisor implements Advisor {

    private static final Logger log = LoggerFactory.getLogger(LoggingAdvisor.class);

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        log.info("📤 请求: {}", request.userText());
        return chain.nextBefore(request);
    }

    @Override
    public ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
        log.info("📥 回复: {}", response.getResult().getOutput().getContent());
        return chain.nextAfter(response);
    }

    @Override
    public int getOrder() {
        return 0;
    }
}
```

**敏感词 Advisor**：
```java
public class SensitiveWordAdvisor implements Advisor {

    private final Set<String> sensitiveWords = Set.of("密码", "密钥", "token");

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        String text = request.userText();
        for (String word : sensitiveWords) {
            if (text.contains(word)) {
                throw new IllegalArgumentException("输入包含敏感词: " + word);
            }
        }
        return chain.nextBefore(request);
    }

    @Override
    public ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
        String content = response.getResult().getOutput().getContent();
        // 过滤输出中的敏感词
        for (String word : sensitiveWords) {
            content = content.replace(word, "***");
        }
        return chain.nextAfter(response);
    }
}
```

**限流 Advisor**：
```java
public class RateLimitAdvisor implements Advisor {

    private final RateLimiter rateLimiter = RateLimiter.create(10); // 10 QPS

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        if (!rateLimiter.tryAcquire()) {
            throw new RateLimitExceededException("请求过于频繁，请稍后再试");
        }
        return chain.nextBefore(request);
    }
}
```

**审计 Advisor**：
```java
public class AuditAdvisor implements Advisor {

    private final AuditLogRepository auditLogRepository;

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        AuditLog log = new AuditLog();
        log.setUserId(request.adviseContext().get("userId"));
        log.setUserInput(request.userText());
        log.setTimestamp(Instant.now());
        auditLogRepository.save(log);
        return chain.nextBefore(request);
    }
}
```

### 3. 动态切模型 Advisor

**场景**：根据用户等级、任务类型动态选择模型。

```java
public class ModelRouterAdvisor implements Advisor {

    private final Map<String, ChatClient> modelMap;

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        String userId = (String) request.adviseContext().get("userId");
        String userLevel = getUserLevel(userId);

        // 根据用户等级选择模型
        String model = switch (userLevel) {
            case "VIP" -> "gpt-4o";
            case "PREMIUM" -> "gpt-4o-mini";
            default -> "ollama-llama";
        };

        // 动态切换模型
        request.adviseContext().put("targetModel", model);
        return chain.nextBefore(request);
    }

    private String getUserLevel(String userId) {
        // 从数据库或缓存获取用户等级
        return "VIP";
    }
}
```

### 4. AI 应用中间件 / Pipeline / Interceptor 架构

**架构分层**：

```
AI 应用中间件架构
│
├── 接入层
│   ├── API Gateway
│   └── Load Balancer
│
├── 中间件层（Advisor 责任链）
│   ├── 认证 Advisor
│   ├── 限流 Advisor
│   ├── 日志 Advisor
│   ├── 安全 Advisor
│   └── 模型路由 Advisor
│
├── AI 服务层
│   ├── ChatClient
│   ├── EmbeddingClient
│   └── VectorStore
│
└── 模型层
    ├── OpenAI
    ├── DeepSeek
    └── Ollama
```

**设计模式**：
- **责任链模式**：每个 Advisor 处理请求并传递给下一个
- **装饰器模式**：Advisor 在不修改原代码的情况下增强功能
- **观察者模式**：可以注册多个 Advisor 监听请求

### 5. 与 Java Filter / Interceptor / AOP 类比

| 维度 | Servlet Filter | Spring Interceptor | Spring AOP | Spring AI Advisor |
|------|---------------|--------------------|------------|------------------|
| 作用层 | Web 请求 | MVC 控制器 | 任意方法 | AI 调用 |
| 触发时机 | 请求前后 | 控制器前后 | 方法前后 | AI 调用前后 |
| 配置方式 | web.xml / 注解 | WebMvcConfigurer | @Aspect | ChatClient 配置 |
| 典型场景 | 编码、权限 | 日志、权限 | 事务、日志 | 日志、限流、安全 |
| 执行顺序 | FilterChain | InterceptorChain | AdvisorChain | AdvisorChain |

**类比**：
- Advisor ≈ Spring MVC Interceptor：都是拦截器模式
- Advisor ≈ Servlet Filter：都是责任链模式
- Advisor ≈ AOP Around 通知：都在方法前后执行

**核心区别**：
- Filter / Interceptor 拦截 HTTP 请求
- Advisor 拦截 AI 调用（不一定是 HTTP）
- Advisor 可以访问 AI 上下文（messages、tools、model 等）

---

## 🔗 官方资料

| 知识点 | 地址 | 军哥课程 |
|--------|------|----------|
| Spring AI Advisor | https://docs.spring.io/spring-ai/reference/api/advisors.html | 模块8: 67 |
| Spring AI 自定义 Advisor | https://docs.spring.io/spring-ai/reference/api/advisors.html#custom-advisor | 模块8: 68 |
| Spring AI MessageChatMemoryAdvisor | https://docs.spring.io/spring-ai/reference/api/advisors.html#memory | 模块8: 67 |
| Spring AI QuestionAnswerAdvisor | https://docs.spring.io/spring-ai/reference/api/advisors.html#rag | 模块8: 68 |
| 设计模式：责任链 | https://refactoringguru.cn/design-patterns/chain-of-responsibility | 模块8: 67 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Advisor 责任链工作流
- [ ] 自定义 Advisor 实现
- [ ] 日志 / 敏感词 / 限流 / 审计 Advisor
- [ ] 动态切模型 Advisor
- [ ] 与 Filter / Interceptor / AOP 类比

### 只需理解（L2）
- [ ] AdvisorChain 源码结构
- [ ] 内置 Advisor 实现
- [ ] Advisor 排序机制

### 今天不深入（后面会讲）
- [ ] Advisor 性能优化
- [ ] Advisor 测试
- [ ] Advisor 与 Reactor 集成

---

## 💻 今日编码任务

### 文件结构

```
day58-spring-ai-advisor/
├── README.md
├── LEARNING_FLOW.md
├── 00_advisor_chain.py            # 责任链基础
├── 01_logging_advisor.py          # 日志 Advisor
├── 02_security_advisor.py         # 安全 Advisor
├── 03_model_router_advisor.py     # 动态切模型
├── 99_boss_answer.md
└── requirements.txt
```

### Task 1: 00_advisor_chain.py（30min）

理解 Advisor 责任链基础，掌握核心接口。

**关键代码提示**：
```java
public interface Advisor extends Ordered {
    default AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        return chain.nextBefore(request);
    }

    default ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
        return chain.nextAfter(response);
    }
}
```

**验收标准**：
```bash
python 00_advisor_chain.py
# 输出：
# 🔗 Advisor 责任链基础
# ├── before → Advisor1 → Advisor2 → Advisor3 → LLM
# └── after  → Advisor3 → Advisor2 → Advisor1 → 返回
```

### Task 2: 01_logging_advisor.py（40min）

实现日志 Advisor，理解前置后置处理。

**关键代码提示**：
```java
public class LoggingAdvisor implements Advisor {
    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        log.info("📤 请求: {}", request.userText());
        return chain.nextBefore(request);
    }

    @Override
    public ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
        log.info("📥 回复: {}", response.getResult().getOutput().getContent());
        return chain.nextAfter(response);
    }
}
```

**验收标准**：
```bash
python 01_logging_advisor.py
# 输出：
# 📝 日志 Advisor
# ├── before: 📤 请求: 你好
# └── after: 📥 回复: 你好！我是...
```

### Task 3: 02_security_advisor.py（40min）

实现安全 Advisor，理解敏感词过滤和限流。

**关键代码提示**：
```java
public class SensitiveWordAdvisor implements Advisor {
    private final Set<String> sensitiveWords = Set.of("密码", "密钥");

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        for (String word : sensitiveWords) {
            if (request.userText().contains(word)) {
                throw new IllegalArgumentException("敏感词: " + word);
            }
        }
        return chain.nextBefore(request);
    }
}
```

**验收标准**：
```bash
python 02_security_advisor.py
# 输出：
# 🔒 安全 Advisor
# ├── 敏感词过滤: ✅
# └── 限流: ✅
```

### Task 4: 03_model_router_advisor.py（40min）

实现动态切模型 Advisor，理解模型路由。

**关键代码提示**：
```java
public class ModelRouterAdvisor implements Advisor {
    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        String userLevel = getUserLevel(request);
        String model = switch (userLevel) {
            case "VIP" -> "gpt-4o";
            default -> "gpt-4o-mini";
        };
        request.adviseContext().put("targetModel", model);
        return chain.nextBefore(request);
    }
}
```

**验收标准**：
```bash
python 03_model_router_advisor.py
# 输出：
# 🎯 动态切模型 Advisor
# ├── VIP 用户 → gpt-4o
# └── 普通用户 → gpt-4o-mini
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Advisor 责任链原理
- 帮你调试 Advisor 实现
- 解释 Filter / Interceptor / AOP 区别
- 帮你对比 Advisor 与中间件模式

### 今天 AI 不能帮你
- 替你理解 Advisor 设计思想（你必须自己理解）
- 替你回答 Boss（你必须自己回答）
- 替你记忆责任链模式（你必须自己比较）

### 正确用法
> "Spring AI 的 Advisor 和 Spring MVC 的 Interceptor 有什么异同？请用类比的方式解释。"

### 错误用法
> "帮我写一个完整的 Advisor 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day58-spring-ai-advisor/
    ├── README.md
    ├── LEARNING_FLOW.md
    ├── 00_advisor_chain.py
    ├── 01_logging_advisor.py
    ├── 02_security_advisor.py
    ├── 03_model_router_advisor.py
    ├── 99_boss_answer.md
    └── requirements.txt
```

### README.md 必须包含
```markdown
# Day 58 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Advisor | ... | ... |
| 责任链 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day58-spring-ai-advisor/
git commit -m "feat(day58): Spring AI Advisor 责任链 - 自定义 Advisor 实现"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **Spring AI 的 Advisor 和 Spring MVC 的 Interceptor 有什么区别？**
2. **Advisor 责任链的执行顺序是怎样的？如何控制多个 Advisor 的执行顺序？**
3. **如何实现一个敏感词过滤 Advisor？请描述完整流程。**
4. **动态切模型 Advisor 的实现思路是什么？需要考虑哪些因素？**
5. **AI 应用中间件架构应该如何设计？请画出分层架构图。**

### 验收标准
- 每个答案 **不少于100字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码场景** 来讲

---

## 🎤 面试题

1. **Spring AI 的 Advisor 是什么？它的核心接口有哪些方法？**
2. **请描述 Advisor 责任链的工作流程。**
3. **如何实现一个日志 Advisor？请写出核心代码。**
4. **动态切模型 Advisor 的实现思路是什么？**
5. **AI 应用中间件架构应该如何设计？请描述各层职责。**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_advisor_chain.py | 15分 | 责任链基础 + 核心接口 |
| 01_logging_advisor.py | 15分 | 日志 Advisor 实现 |
| 02_security_advisor.py | 15分 | 安全 Advisor 实现 |
| 03_model_router_advisor.py | 15分 | 动态切模型实现 |
| README 学习总结 | 15分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5题全部完成 + 用自己的话 |
| 代码质量 | 10分 | 命名清晰 + 注释 + 结构 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 59: MCP Transports**

---

## 📊 今日检查清单

- [ ] 读了 Spring AI Advisor 文档
- [ ] 读了 Spring AI 自定义 Advisor 文档
- [ ] 写了 00_advisor_chain.py
- [ ] 写了 01_logging_advisor.py
- [ ] 写了 02_security_advisor.py
- [ ] 写了 03_model_router_advisor.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99_boss_answer.md
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
