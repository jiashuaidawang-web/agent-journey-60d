# Day 58 Boss 答案

## 1. Spring AI 的 Advisor 和 Spring MVC 的 Interceptor 有什么区别？

**Spring MVC Interceptor**：
- 拦截 HTTP 请求，在控制器执行前后执行
- 实现 `HandlerInterceptor` 接口
- 三个方法：`preHandle`、`postHandle`、`afterCompletion`
- 通过 `WebMvcConfigurer.addInterceptors()` 注册
- 典型场景：权限校验、日志、国际化

**Spring AI Advisor**：
- 拦截 AI 调用（ChatClient.prompt()...call()）
- 实现 `Advisor` 接口
- 两个方法：`before`、`after`
- 通过 `ChatClient.Builder.defaultAdvisors()` 注册
- 典型场景：日志、限流、安全、模型路由

**对比**：

| 维度 | Interceptor | Advisor |
|------|-------------|---------|
| 拦截对象 | HTTP 请求 | AI 调用 |
| 接口 | HandlerInterceptor | Advisor |
| 方法 | preHandle / postHandle | before / after |
| 注册方式 | WebMvcConfigurer | ChatClient.Builder |
| 上下文 | HttpServletRequest | AdvisorRequest |
| 典型场景 | 权限、日志 | 日志、限流、安全 |

**共同点**：
- 都是责任链模式
- 都支持多个拦截器按顺序执行
- 都可以在前置处理中中断请求（抛出异常）

**核心区别**：
- Interceptor 面向 HTTP 请求，Advisor 面向 AI 调用
- Advisor 可以访问 AI 上下文（messages、tools、model 等）
- Advisor 不依赖 Web 环境，可以在非 Web 场景使用

## 2. Advisor 责任链的执行顺序是怎样的？如何控制多个 Advisor 的执行顺序？

**执行顺序**：

```
用户调用 ChatClient.prompt()...call()
    ↓
构建 AdvisorChain（包含所有注册的 Advisor）
    ↓
前置处理（before）：
    Advisor1.before() → Advisor2.before() → Advisor3.before() → LLM.call()
    ↓
后置处理（after）：
    LLM.call() → Advisor3.after() → Advisor2.after() → Advisor1.after()
    ↓
返回结果
```

**特点**：
- before 正序执行（1 → 2 → 3）
- after 逆序执行（3 → 2 → 1）
- 类似栈结构：先进后出

**控制执行顺序**：

1. **实现 `Ordered` 接口**：
```java
public class LoggingAdvisor implements Advisor {
    @Override
    public int getOrder() {
        return 0;  // 数字越小，越先执行
    }
}
```

2. **使用 `@Order` 注解**：
```java
@Order(10)
public class SecurityAdvisor implements Advisor {
    // ...
}
```

3. **注册顺序**：
```java
ChatClient client = builder
    .defaultAdvisors(
        new LoggingAdvisor(),    // 第一个注册
        new SecurityAdvisor(),   // 第二个注册
        new RateLimitAdvisor()   // 第三个注册
    )
    .build();
```

**最佳实践**：
- 日志 Advisor：order = 0（最先执行，记录完整请求）
- 安全 Advisor：order = 10（安全检查在日志之后）
- 限流 Advisor：order = 20（限流在安全检查之后）
- 记忆 Advisor：order = 100（记忆管理在最后）

## 3. 如何实现一个敏感词过滤 Advisor？请描述完整流程。

**完整流程**：

1. **定义敏感词库**：
```java
private final Set<String> sensitiveWords = Set.of(
    "密码", "密钥", "token", "api-key", "secret"
);
```

2. **前置处理（输入过滤）**：
```java
@Override
public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
    String userText = request.userText();

    // 检查输入是否包含敏感词
    for (String word : sensitiveWords) {
        if (userText.contains(word)) {
            throw new SensitiveWordException("输入包含敏感词: " + word);
        }
    }

    // 替换敏感词（可选）
    String filteredText = userText;
    for (String word : sensitiveWords) {
        filteredText = filteredText.replace(word, "***");
    }

    // 继续执行链
    return chain.nextBefore(request);
}
```

3. **后置处理（输出过滤）**：
```java
@Override
public ChatClientResponse after(ChatClientResponse response, AdvisorChain chain) {
    String content = response.getResult().getOutput().getContent();

    // 过滤输出中的敏感词
    for (String word : sensitiveWords) {
        content = content.replace(word, "***");
    }

    // 继续执行链
    return chain.nextAfter(response);
}
```

4. **注册 Advisor**：
```java
ChatClient client = ChatClient.builder()
    .defaultAdvisors(new SensitiveWordAdvisor())
    .build();
```

**注意事项**：
- 敏感词库应该从配置文件或数据库加载
- 支持正则表达式匹配（更灵活）
- 记录敏感词命中日志（审计）
- 考虑性能（使用 Trie 树优化匹配）

## 4. 动态切模型 Advisor 的实现思路是什么？需要考虑哪些因素？

**实现思路**：

1. **获取用户上下文**：从请求中获取用户 ID、用户等级等信息
2. **查询用户等级**：从数据库或缓存获取用户等级
3. **选择模型**：根据用户等级、任务类型、成本等因素选择模型
4. **设置目标模型**：将目标模型设置到请求上下文中
5. **继续执行链**：调用 `chain.nextBefore()` 继续执行

**核心代码**：
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

        // 设置目标模型
        request.adviseContext().put("targetModel", model);
        return chain.nextBefore(request);
    }

    private String getUserLevel(String userId) {
        // 从数据库或缓存获取用户等级
        return "VIP";
    }
}
```

**考虑因素**：
- **用户等级**：VIP / 普通用户使用不同模型
- **任务类型**：简单任务用便宜模型，复杂任务用强模型
- **成本控制**：按预算分配模型
- **延迟要求**：实时场景用快速模型
- **合规要求**：敏感数据用本地模型
- **降级策略**：主模型故障时切换备用

## 5. AI 应用中间件架构应该如何设计？请画出分层架构图。

**分层架构图**：

```
AI 应用中间件架构
═══════════════════════════════════════════════════════

                     接入层
        ┌──────────────┼──────────────┐
        │              │              │
   API Gateway    Load Balancer   Auth Service
        │              │              │
        └──────────────┼──────────────┘
                       │
                   中间件层（Advisor 责任链）
        ┌──────────────┼──────────────┐
        │              │              │
   认证 Advisor    日志 Advisor    限流 Advisor
        │              │              │
   安全 Advisor   审计 Advisor   模型路由 Advisor
        │              │              │
        └──────────────┼──────────────┘
                       │
                   AI 服务层
        ┌──────────────┼──────────────┐
        │              │              │
   ChatClient    EmbeddingClient  VectorStore
        │              │              │
        └──────────────┼──────────────┘
                       │
                    模型层
        ┌──────────────┼──────────────┐
        │              │              │
     OpenAI        DeepSeek       Ollama
        │              │              │
        └──────────────┼──────────────┘
                       │
                   基础设施层
        ┌──────────────┼──────────────┐
        │              │              │
     Redis          MySQL         Milvus
        │              │              │
        └──────────────┼──────────────┘
```

**各层职责**：

| 层级 | 职责 | 组件 |
|------|------|------|
| 接入层 | 请求路由、负载均衡、认证 | API Gateway、Nginx |
| 中间件层 | 日志、限流、安全、审计 | Advisor 责任链 |
| AI 服务层 | AI 能力封装 | ChatClient、EmbeddingClient |
| 模型层 | 模型接入 | OpenAI、DeepSeek、Ollama |
| 基础设施层 | 存储、缓存、向量 | Redis、MySQL、Milvus |

**设计原则**：
- 单一职责：每层只负责一类功能
- 可扩展：通过 Advisor 链灵活扩展
- 可替换：各层组件可独立替换
- 可观测：全链路日志和监控
