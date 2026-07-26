# Day 60: Memory 深度体系

> **今日目标**: 掌握 Agent Memory 的完整体系：短期/长期/工作/情景记忆
> **核心问题**: 为什么 Agent 需要记忆？记忆体系是如何分层的？

---

## 🎯 今日目标

1. 理解 Memory 体系总览（Short-term/Long-term/Working/Episodic）
2. 掌握 MessageHistory 机制
3. 掌握 TokenWindow 滑动窗口
4. 掌握 SummaryMemory 摘要记忆
5. 掌握 Redis 实现分布式记忆（Spring AI 官方 RedisChatMemory）
6. 掌握 MySQL + JDBC 持久化
7. 掌握多用户会话隔离（UserId + ConversationId）
8. 掌握记忆容量控制与遗忘机制
9. 掌握自定义 MemoryAdvisor 实现分层记忆
10. 掌握记忆安全与 PII 脱敏

---

## 📚 必学知识

### 1. Memory 体系总览

**为什么 Agent 需要记忆？**
- 多轮对话需要上下文连续性
- 用户偏好需要跨会话持久化
- 任务执行需要中间状态记录

**四种记忆类型**：

| 记忆类型 | 说明 | 示例 | 生命周期 |
|----------|------|------|----------|
| Short-term Memory | 短期记忆（当前会话） | 当前对话内容 | 单次会话 |
| Long-term Memory | 长期记忆（跨会话） | 用户偏好、历史摘要 | 跨会话持久化 |
| Working Memory | 工作记忆（任务执行） | 工具调用中间结果 | 单次任务 |
| Episodic Memory | 情景记忆（事件记录） | 用户历史事件 | 长期持久化 |

### 2. MessageHistory 机制

**MessageHistory**：
- Spring AI 的核心记忆接口
- 存储对话消息列表（List<Message>）
- 支持添加、获取、清除消息

**核心方法**：
```java
public interface MessageHistory {
    void add(Message message);      // 添加消息
    List<Message> get();            // 获取所有消息
    void clear();                   // 清除消息
}
```

### 3. TokenWindow 滑动窗口

**问题**：Context Window 有限，不能无限塞历史

**解决方案**：滑动窗口
- 只保留最近 N 轮对话
- 超出窗口的旧消息被丢弃
- 平衡上下文连续性和 token 成本

**实现方式**：
- `MessageChatMemoryAdvisor` + `maxMessages` 参数
- 按消息数量裁剪
- 按 token 数量裁剪（需要 TokenCounter）

### 4. SummaryMemory 摘要记忆

**问题**：滑动窗口会丢失早期重要信息

**解决方案**：摘要压缩
- 将早期对话压缩成摘要
- 保留摘要 + 最近 N 轮原文
- 平衡信息保留和 token 成本

**实现方式**：
- 使用 LLM 生成对话摘要
- 摘要作为 System Message 或特殊消息插入
- 触发条件：消息数超过阈值时自动摘要

### 5. Redis 实现分布式记忆

**为什么用 Redis？**
- 支持多实例部署（共享记忆）
- 自动过期（TTL）
- 高性能读写
- Spring AI 官方提供 `RedisChatMemory`

**核心配置**：
```java
@Bean
public MessageChatMemory chatMemory(RedisTemplate<String, String> redisTemplate) {
    return new RedisChatMemory(redisTemplate, "chat:memory:", 100);
}
```

### 6. MySQL + JDBC 持久化

**为什么用 MySQL？**
- 数据持久化（重启不丢失）
- 支持复杂查询
- 适合审计和分析

**Spring AI 官方提供**：
- `JdbcChatMemoryRepository`
- 支持 MySQL、PostgreSQL、SQLite 等
- 自动建表、CRUD 操作

### 7. 多用户会话隔离

**问题**：多用户共享系统，记忆必须隔离

**解决方案**：UserId + ConversationId
- **UserId**：标识用户（跨会话）
- **ConversationId**：标识会话（单次对话）
- 组合键：`userId:conversationId`

**实现方式**：
- 自定义 `MessageChatMemory` 实现
- 使用 `MessageHistoryFactory` 按 ID 创建记忆
- 在 Advisor 中注入当前用户和会话 ID

### 8. 记忆容量控制与遗忘机制

**容量控制策略**：
1. **滑动窗口**：只保留最近 N 轮
2. **Token 限制**：只保留最近 N 个 token
3. **摘要压缩**：旧消息压缩成摘要
4. **重要性评分**：保留高重要性消息

**遗忘机制**：
- TTL 过期（Redis）
- 定期清理（定时任务）
- 用户主动清除
- 容量上限淘汰（LRU）

### 9. 自定义 MemoryAdvisor 实现分层记忆

**分层记忆架构**：
```
Layer 1: Working Memory（当前轮次）
Layer 2: Short-term Memory（最近 N 轮）
Layer 3: Summary Memory（历史摘要）
Layer 4: Long-term Memory（用户画像）
```

**实现方式**：
- 继承 `BaseChatMemoryAdvisor`
- 重写 `adviseCall` 方法
- 按层级组装上下文

### 10. 记忆安全与 PII 脱敏

**PII（Personally Identifiable Information）**：
- 姓名、电话、邮箱、身份证号
- 银行卡号、地址
- 健康信息、生物特征

**脱敏策略**：
1. **存储前脱敏**：写入记忆前替换 PII
2. **读取时脱敏**：从记忆读取时替换
3. **加密存储**：敏感字段加密
4. **访问控制**：基于角色控制访问

**实现方式**：
- 正则表达式匹配 PII
- 使用 NLP 模型识别 PII
- 脱敏后存储占位符（如 `[PHONE]`）

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Spring AI Memory 文档 | https://docs.spring.io/spring-ai/reference/api/chatclient.html |
| Spring AI RedisChatMemory | https://docs.spring.io/spring-ai/reference/api/chatmemory/redis.html |
| Spring AI JDBC ChatMemory | https://docs.spring.io/spring-ai/reference/api/chatmemory/jdbc.html |
| Spring AI Advisors | https://docs.spring.io/spring-ai/reference/api/advisors.html |
| Redis 官方文档 | https://redis.io/docs/latest/ |
| PII 脱敏最佳实践 | https://owasp.org/www-project-top-ten/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Memory 体系总览（四种记忆类型）
- [ ] MessageHistory 机制
- [ ] TokenWindow 滑动窗口
- [ ] SummaryMemory 摘要记忆
- [ ] Redis 实现分布式记忆
- [ ] MySQL + JDBC 持久化
- [ ] 多用户会话隔离

### 只需理解（L2）
- [ ] 自定义 MemoryAdvisor
- [ ] 分层记忆架构
- [ ] 记忆容量控制与遗忘机制
- [ ] PII 脱敏策略

### 今天不深入（后面会讲）
- [ ] 向量数据库记忆（VectorStore）
- [ ] RAG 与记忆的结合
- [ ] 记忆压缩算法
- [ ] 记忆安全与合规

---

## 💻 今日编码任务

### 文件结构

```
day60-memory-deep-dive/
├── README.md
├── LEARNING_FLOW.md
├── 00_memory_hierarchy.py          # Memory 分层体系演示
├── 01_redis_memory.py              # Redis 分布式记忆
├── 02_multi_user_isolation.py      # 多用户会话隔离
├── 03_pii_desensitization.py       # PII 脱敏
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_memory_hierarchy.py（45min）

实现 Memory 分层体系：
- 定义四种记忆类型（Short-term/Long-term/Working/Episodic）
- 实现滑动窗口（TokenWindow）
- 实现摘要记忆（SummaryMemory）
- 演示分层记忆的工作流程

**验收标准**：
```bash
python 00_memory_hierarchy.py
# 输出：
# 🧠 Memory 分层体系演示
# 📝 Working Memory: [当前轮次消息]
# 📝 Short-term Memory: [最近 5 轮]
# 📝 Summary Memory: [历史摘要]
# 📝 Long-term Memory: [用户画像]
```

### Task 2: 01_redis_memory.py（45min）

实现 Redis 分布式记忆：
- 连接 Redis
- 使用 RedisChatMemory 存储消息
- 演示多实例共享记忆
- 演示 TTL 过期

**验收标准**：
```bash
python 01_redis_memory.py
# 输出：
# 🔗 Redis 连接成功
# 💾 消息已存入 Redis
# 📤 从 Redis 读取消息: [...]
# ⏰ TTL 过期测试通过
```

### Task 3: 02_multi_user_isolation.py（45min）

实现多用户会话隔离：
- 定义 User 和 Conversation 实体
- 实现 UserId + ConversationId 隔离
- 演示多用户并发访问
- 验证记忆隔离

**验收标准**：
```bash
python 02_multi_user_isolation.py
# 输出：
# 👤 用户 A 会话 1: [消息 A1]
# 👤 用户 A 会话 2: [消息 A2]
# 👤 用户 B 会话 1: [消息 B1]
# ✅ 隔离验证通过
```

### Task 4: 03_pii_desensitization.py（30min）

实现 PII 脱敏：
- 定义 PII 类型（电话、邮箱、身份证号）
- 实现正则匹配脱敏
- 演示脱敏前后对比
- 实现脱敏后存储

**验收标准**：
```bash
python 03_pii_desensitization.py
# 输出：
# 🔍 检测到 PII: 13812345678
# 🔒 脱敏后: 138****5678
# 🔍 检测到 PII: test@example.com
# 🔒 脱敏后: t***@example.com
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Memory 体系的概念
- 解释 Spring AI Memory 的用法
- 帮你调试代码报错
- 解释 PII 脱敏的实现思路

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 开发经验，Spring AI 的 Memory 机制我不太熟。请用 Java 的 Repository 模式类比解释 MessageChatMemory，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Memory 体系实现。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day60-memory-deep-dive/
    ├── README.md                    # 学习总结
    ├── LEARNING_FLOW.md             # 学习流程
    ├── 00_memory_hierarchy.py       # Memory 分层体系
    ├── 01_redis_memory.py           # Redis 分布式记忆
    ├── 02_multi_user_isolation.py   # 多用户会话隔离
    ├── 03_pii_desensitization.py    # PII 脱敏
    ├── requirements.txt
    └── 99-boss-answer.md            # Boss 答案
```

### README.md 必须包含
```markdown
# Day 60 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Short-term Memory | ... | ... |
| Long-term Memory | ... | ... |
| TokenWindow | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day60-memory-deep-dive/
git commit -m "feat(day60): Memory 深度体系 - 分层/Redis/隔离/PII 完成"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **Agent 为什么需要记忆？四种记忆类型分别是什么？**
2. **TokenWindow 滑动窗口是如何工作的？有什么优缺点？**
3. **Redis 实现分布式记忆的优势是什么？Spring AI 官方是如何支持的？**
4. **多用户会话隔离是怎么实现的？为什么需要 UserId + ConversationId？**
5. **为什么需要对记忆进行 PII 脱敏？如何实现？**

### 验收标准
- 每个答案 **不少于50字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **Agent 的记忆体系包含哪些层次？**
2. **滑动窗口和摘要记忆有什么区别？**
3. **Spring AI 的 RedisChatMemory 是如何工作的？**
4. **多用户会话隔离的意义是什么？**
5. **PII 脱敏的常见策略有哪些？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_memory_hierarchy.py | 20分 | 能运行 + 四种记忆类型 + 分层演示 |
| 01_redis_memory.py | 20分 | 能运行 + Redis 存储 + TTL |
| 02_multi_user_isolation.py | 20分 | 能运行 + 隔离验证 |
| 03_pii_desensitization.py | 15分 | 能运行 + 脱敏正确 |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 61: LoRA/QLoRA 微调实战**

---

## 📊 今日检查清单

- [ ] 读了 Spring AI Memory 文档
- [ ] 读了 Spring AI RedisChatMemory 文档
- [ ] 读了 Spring AI JDBC ChatMemory 文档
- [ ] 写了 00_memory_hierarchy.py
- [ ] 写了 01_redis_memory.py
- [ ] 写了 02_multi_user_isolation.py
- [ ] 写了 03_pii_desensitization.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
