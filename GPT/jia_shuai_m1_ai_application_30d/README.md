# 贾帅 · M1 AI应用开发基础 · 30天作战手册

> 这是《贾帅 · 12个月企业级 Agent 架构师进阶路线》的第一个月。
>
> **本月目标：** 从 Java / Spring Boot 企业后端开发者，完成第一次 AI 应用工程能力升级。
>
> **毕业项目：** `ai-chat-platform`
>
> **核心原则：** 20% 理论 + 30% 源码/官方文档 + 40% 编码实战 + 10% 总结复盘。
>
> **最终验收：** 不是“看完课程”，而是能独立设计、实现、运行、排查一个具备多轮对话、流式输出、模型抽象、会话持久化、Token统计、Tool Calling 和基础可观测能力的 AI Chat Platform。

---

## 1. 你当前的位置

你已有：
- Java
- Spring Boot
- 企业级后端开发
- MySQL
- Redis
- MQ
- Docker / Linux 等工程经验

因此本月**不重复学习 Java 和 Spring Boot 基础**，重点补齐：
- LLM 工作原理与 API 使用
- Prompt Engineering
- Token / Context
- Structured Output
- Function Calling / Tool Calling
- Embedding 基础认知
- Spring AI 工程实践
- AI 应用的异常、超时、重试、成本和可观测性

---

## 2. 30天最终能力目标

30天结束后，你必须能够独立解释并实现：

### LLM
- LLM 是什么
- Token 是什么
- Context Window 是什么
- Temperature / Top-P 有什么作用
- 为什么同一个 Prompt 结果可能不同
- 为什么上下文太长会影响效果和成本

### Prompt
- System / User / Assistant 消息的作用
- Zero-shot / Few-shot
- 结构化输出
- Prompt 模板
- Prompt 版本管理

### AI应用工程
- Streaming
- 多轮会话
- Conversation Memory
- Token Usage
- Model Abstraction
- Timeout / Retry / Fallback
- Rate Limit
- 日志与 Trace

### Tool Calling
- LLM 为什么需要 Tool
- Tool Schema
- Tool Calling 完整生命周期
- 参数校验
- Tool 执行失败处理
- Tool 权限意识

### 最终项目
能够运行：

User
→ API Gateway
→ Chat Service
→ LLM
→ Memory
→ Tool
→ Response

并具备：
- REST API
- SSE 流式输出
- 会话管理
- Redis / MySQL 持久化
- 模型抽象
- Tool Calling
- Token统计
- 日志
- 基础测试
- Docker运行

---

# 3. 技术栈

建议主线：

- Java 21（如果当前公司项目使用 Java 17，可使用 Java 17）
- Spring Boot 3.x
- Spring AI
- Maven
- MySQL
- Redis
- Docker
- Git / GitHub

AI Provider 建议使用：
- 一个 OpenAI-compatible API 作为主模型入口
- 保留模型切换能力

> 不要在第一个月纠结“哪个模型最好”。你的重点是掌握模型抽象和 AI 应用工程能力。

---

# 4. 项目仓库

建议：

`ai-chat-platform`

目录：

```text
ai-chat-platform/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── database.md
│   ├── llm.md
│   ├── prompt.md
│   ├── tool-calling.md
│   └── troubleshooting.md
├── ai-chat-api/
├── ai-chat-core/
├── ai-chat-infrastructure/
├── ai-chat-memory/
├── ai-chat-tool/
├── ai-chat-observability/
├── deploy/
│   ├── docker/
│   └── docker-compose.yml
└── tests/
```

如果第一版希望降低复杂度，也可以先使用单体：

```text
src/main/java/
src/main/resources/
docs/
deploy/
```

第一个月重点是**能力，不是为了拆微服务而拆微服务**。

---

# 5. 每日固定学习模板

每天建议 2～3 小时：

```text
30分钟：理论
30分钟：官方文档 / 源码
60～90分钟：编码
20分钟：实验 / Debug
10分钟：Git Commit + 学习记录
```

每天必须留下：

```text
DayXX/
├── README.md
├── code/
├── experiment/
└── notes.md
```

如果不想真的创建 DayXX 目录，也可以统一写到：

`docs/learning-log.md`

---

# 6. Git Commit 规范

建议：

```text
feat: add chat completion
feat: add streaming response
feat: add conversation memory
feat: add model abstraction
feat: add tool calling
fix: handle llm timeout
test: add chat service tests
docs: add llm notes
refactor: extract model gateway
```

每天至少一次有效提交。

不要为了凑次数提交：

```text
update
test
aaa
123
```

---

# 7. 30天路线总览

| 天数 | 主题 | 核心产出 |
|---|---|---|
| Day 01 | AI应用工程全景 | AI应用架构图 |
| Day 02 | LLM基础 | LLM知识卡 |
| Day 03 | Token与Context | Token实验 |
| Day 04 | Model参数 | 参数实验 |
| Day 05 | API调用 | 第一个LLM API |
| Day 06 | Prompt基础 | Prompt实验 |
| Day 07 | 周验收1 | AI基础答辩 |
| Day 08 | Spring AI | 项目初始化 |
| Day 09 | Chat Client | Chat API |
| Day 10 | Streaming | SSE流式 |
| Day 11 | Conversation | 会话模型 |
| Day 12 | Memory | Redis Memory |
| Day 13 | 持久化 | MySQL |
| Day 14 | 周验收2 | Chat MVP |
| Day 15 | Structured Output | JSON输出 |
| Day 16 | Prompt Template | Prompt模板 |
| Day 17 | Function Calling | Tool基础 |
| Day 18 | Tool设计 | Calculator Tool |
| Day 19 | Tool异常 | Tool容错 |
| Day 20 | Tool安全 | 权限意识 |
| Day 21 | 周验收3 | Tool Agent |
| Day 22 | Token统计 | Usage |
| Day 23 | 成本控制 | Cost估算 |
| Day 24 | Timeout/Retry | 稳定性 |
| Day 25 | 日志Trace | 可观测 |
| Day 26 | 测试 | 自动化测试 |
| Day 27 | Docker | 容器运行 |
| Day 28 | 架构优化 | 重构 |
| Day 29 | 毕业验收 | 全链路测试 |
| Day 30 | 毕业答辩 | Final Release |

---

# 8. Day 01：AI应用工程全景

## 学习

理解：

```text
用户
 ↓
Frontend
 ↓
API
 ↓
AI Application
 ↓
Prompt
 ↓
LLM
 ↓
Tool / RAG / Memory
 ↓
Response
```

重点理解：

```text
LLM ≠ AI应用
AI应用 = LLM + 工程系统 + 数据 + 工具 + 业务逻辑
```

## 实践

画一张自己的 AI Chat Platform 架构图。

至少包含：

```text
Client
API
Chat Service
LLM Gateway
Memory
Tool
MySQL
Redis
```

## 输出

`docs/architecture.md`

## 验收

回答：

1. LLM 在系统中的位置是什么？
2. 为什么不能直接让前端调用 LLM？
3. 为什么需要 LLM Gateway？
4. Redis 和 MySQL 分别存什么？

---

# 9. Day 02：LLM基础

## 学习

理解：
- Transformer 只需要知道基本结构
- Token
- Embedding
- Attention 基础概念
- Inference

## 实践

画：

```text
用户文本
↓
Tokenizer
↓
Tokens
↓
LLM
↓
Next Token Prediction
↓
输出文本
```

## 输出

`docs/llm.md`

## 验收

能够解释：

> LLM 为什么不是传统数据库？

---

# 10. Day 03：Token & Context

## 学习

理解：
- Token
- Input Tokens
- Output Tokens
- Context Window
- Conversation History

## 实践

设计：

```text
messages
├── system
├── user
├── assistant
└── tool
```

观察不同上下文长度的影响。

## 输出

`experiment/token-context.md`

## 验收

回答：

> 为什么聊天记录越来越长后，成本越来越高？

---

# 11. Day 04：Model Parameters

## 学习

实验：
- Temperature
- Top-P
- Max Tokens

## 实践

同一个 Prompt 重复运行：

```text
请生成一个Java项目名称。
```

分别测试：
- Temperature低
- Temperature高

记录结果。

## 输出

`experiment/model-parameters.md`

## 验收

回答：

> Temperature 越高是不是一定越智能？

---

# 12. Day 05：第一个LLM API

## 目标

Spring Boot 调用 LLM。

流程：

```text
HTTP Request
↓
Controller
↓
Service
↓
Chat Client
↓
LLM
↓
Response
```

## API

```http
POST /api/chat
```

Request：

```json
{
  "message": "解释一下什么是RAG"
}
```

Response：

```json
{
  "content": "..."
}
```

## 输出

第一个可运行 AI API。

---

# 13. Day 06：Prompt基础

## 学习

- System Prompt
- User Prompt
- Role
- Few-shot

## 实践

设计三个 Prompt：

1. Java专家
2. RAG专家
3. 企业架构师

比较输出差异。

## 输出

`docs/prompt.md`

---

# 14. Day 07：周验收1

## 必须完成

```text
Spring Boot
↓
LLM
↓
Chat API
```

## 答辩

不看资料回答：

1. Token是什么？
2. Context是什么？
3. Temperature做什么？
4. Prompt为什么重要？
5. LLM和传统API有什么区别？

## 周成果

Git Tag：

`v0.1.0`

---

# 15. Day 08：Spring AI

## 学习

理解：
- ChatClient
- ChatModel
- Prompt
- Message
- Advisor 基础概念

## 实践

重构 Day05。

目标：

```text
Controller
↓
ChatService
↓
ChatClient
↓
Model
```

---

# 16. Day 09：Chat Client

## 实现

```http
POST /api/conversations/{id}/messages
```

数据库设计：

```text
conversation
message
```

至少包含：

```text
conversation_id
role
content
created_at
```

---

# 17. Day 10：Streaming

## 学习

SSE。

实现：

```text
POST /api/chat/stream
```

流程：

```text
User
↓
Backend
↓
LLM
↓
Token Stream
↓
SSE
↓
Browser
```

## 验收

浏览器能看到 AI 内容逐步输出。

---

# 18. Day 11：Conversation

实现：

```text
创建会话
查询会话
删除会话
发送消息
查询消息
```

API：

```text
POST /conversations
GET /conversations
GET /conversations/{id}
DELETE /conversations/{id}
POST /conversations/{id}/messages
```

---

# 19. Day 12：Memory

## 学习

区分：

```text
Conversation History
Short-term Memory
Long-term Memory
```

本月只实现短期记忆。

建议：

```text
Redis
```

保存：

```text
conversation:{id}:messages
```

---

# 20. Day 13：MySQL持久化

设计：

```text
conversation
message
llm_usage
```

建议：

```text
conversation
├── id
├── user_id
├── title
├── model
├── created_at
└── updated_at

message
├── id
├── conversation_id
├── role
├── content
├── token_count
└── created_at
```

---

# 21. Day 14：周验收2

完成：

```text
AI Chat MVP
```

必须支持：

```text
创建会话
↓
发送消息
↓
LLM
↓
Memory
↓
保存MySQL
↓
Redis缓存
↓
Streaming
```

Git Tag：

`v0.2.0`

---

# 22. Day 15：Structured Output

目标：

让 LLM 输出：

```json
{
  "name": "AI Chat Platform",
  "difficulty": "medium",
  "tags": ["AI", "Java"]
}
```

而不是自然语言。

理解：

```text
Natural Language
vs
Structured Output
```

---

# 23. Day 16：Prompt Template

设计：

```text
PromptTemplate
```

支持：

```text
systemPrompt
userPrompt
variables
```

实现 Prompt 版本：

```text
prompt_name
version
content
status
```

目标：

Prompt 不再硬编码。

---

# 24. Day 17：Function Calling

理解：

```text
User
↓
LLM
↓
Tool Call
↓
Application
↓
Tool
↓
Result
↓
LLM
↓
Answer
```

重点：

> LLM 不是真的执行 Java 方法，而是决定“调用哪个 Tool + 传什么参数”。

---

# 25. Day 18：Calculator Tool

实现：

```text
calculate(expression)
```

例如：

```text
用户：
计算 123 * 456

Agent
↓
Calculator Tool
↓
56088
↓
LLM
↓
回答
```

必须做参数校验。

---

# 26. Day 19：Tool异常

模拟：
- Tool Timeout
- 参数错误
- Tool内部异常
- LLM调用错误

实现：

```text
try
↓
retry
↓
fallback
↓
error response
```

注意：

> 不要无限重试。

---

# 27. Day 20：Tool安全

设计：

```text
Tool
├── name
├── description
├── inputSchema
├── permission
└── riskLevel
```

例如：

```text
查询订单：LOW
修改订单：MEDIUM
删除订单：HIGH
生产重启：CRITICAL
```

思考：

```text
Agent
↓
Risk Assessment
↓
Human Approval
↓
Execute
```

---

# 28. Day 21：周验收3

完成：

# Tool Agent

流程：

```text
User
↓
LLM
↓
Tool Calling
↓
Calculator
↓
LLM
↓
Answer
```

Git Tag：

`v0.3.0`

必须能够解释：

> Function Calling 为什么是 Agent 的基础能力？

---

# 29. Day 22：Token Usage

记录：

```text
promptTokens
completionTokens
totalTokens
```

数据库：

```text
llm_usage
```

字段：

```text
conversation_id
model
prompt_tokens
completion_tokens
total_tokens
created_at
```

---

# 30. Day 23：Cost Control

设计：

```text
Model
↓
Price Config
↓
Token Usage
↓
Cost
```

实现：

```text
CostService
```

支持估算单次请求成本。

重点：

> 你现在不需要精确支持所有模型，只需要理解成本计算架构。

---

# 31. Day 24：Timeout / Retry

设计：

```text
LLM Gateway
├── Timeout
├── Retry
├── Circuit Breaker
└── Fallback
```

重点：
- Retry次数
- Retry间隔
- 哪些异常可以重试
- 哪些异常不能重试

---

# 32. Day 25：Logging & Trace

记录：

```text
request_id
conversation_id
user_id
model
latency
token_usage
tool
error
```

日志：

```text
Request
↓
LLM
↓
Tool
↓
Response
```

目标：

> 能根据 request_id 找到一次完整请求链路。

---

# 33. Day 26：自动化测试

至少实现：

### Unit Test

```text
ChatService
PromptService
ToolService
CostService
```

### Integration Test

```text
Controller
↓
Service
↓
LLM Mock
```

不要让测试依赖真实 LLM。

---

# 34. Day 27：Docker

实现：

```text
docker-compose.yml
```

至少运行：

```text
AI Chat
MySQL
Redis
```

要求：

```text
docker compose up
```

即可启动。

---

# 35. Day 28：架构重构

检查：

```text
Controller
Service
Domain
Infrastructure
```

重点：

```text
LLM Provider
Memory
Tool
Storage
```

是否耦合？

目标：

> 更换 LLM Provider 时，不应该修改业务核心代码。

---

# 36. Day 29：毕业验收

模拟：

```text
100次Chat
100次Streaming
10个Conversation
Tool Calling
LLM Timeout
Redis故障
MySQL故障
```

记录：

```text
成功率
平均延迟
P95
Token
Cost
错误类型
```

输出：

`docs/performance.md`

---

# 37. Day 30：Final Release

Git Tag：

`v1.0.0`

必须包含：

```text
README
Architecture
API
Database
Prompt
Tool Calling
Observability
Troubleshooting
Docker
Test
Performance
```

最终演示：

```text
创建Conversation
↓
发送Message
↓
Streaming
↓
Memory
↓
Tool Calling
↓
Token Usage
↓
Cost
↓
Trace
```

---

# 38. Day 30毕业答辩题

必须能够回答：

## LLM
1. Token是什么？
2. Context Window是什么？
3. Temperature是什么？
4. 为什么LLM会幻觉？

## AI应用
5. 为什么要做LLM Gateway？
6. 为什么不能把Prompt全部写死？
7. Streaming如何实现？

## Memory
8. Redis为什么适合短期Memory？
9. MySQL和Redis如何分工？

## Tool
10. Function Calling是什么？
11. Tool失败怎么办？
12. 如何防止Agent调用危险Tool？

## 工程
13. LLM超时怎么办？
14. LLM限流怎么办？
15. 如何统计Token？
16. 如何降低成本？

## 架构
17. 如何支持多个LLM？
18. 如何切换模型？
19. 如何保证业务代码不绑定某一个模型？
20. 如果1000用户同时调用怎么办？

---

# 39. 本月最终验收标准

达到以下标准才能进入 M2：

### Level 1
能调用LLM。

### Level 2
能完成多轮Chat。

### Level 3
能实现Streaming。

### Level 4
能实现Memory。

### Level 5
能实现Structured Output。

### Level 6
能实现Tool Calling。

### Level 7
能处理Timeout / Retry / Fallback。

### Level 8
能记录Token / Cost。

### Level 9
能Docker部署。

### Level 10
能独立解释完整架构。

最终要求：

> 不看教程，从空项目开始，2～3小时内搭建一个简化版 AI Chat Platform。

---

# 40. M1完成后的能力跃迁

```text
Java Backend Engineer
        ↓
会调用LLM
        ↓
AI Application Engineer
        ↓
会做Chat
        ↓
会做Streaming
        ↓
会做Memory
        ↓
会做Tool Calling
        ↓
理解AI应用工程
        ↓
进入M2
RAG Engineer
```

---

# 41. 绝对不要做的事情

1. 不要第一天就学Fine-tuning。
2. 不要同时学习10个Agent框架。
3. 不要只看视频不写代码。
4. 不要复制Demo后就认为学会了。
5. 不要只会调用API。
6. 不要为了复杂而拆微服务。
7. 不要一开始追求完美架构。
8. 不要忽略日志、异常和测试。
9. 不要只学习概念不做实验。
10. 不要因为一天没完成任务就放弃。

---

# 42. 本月最重要的一句话

> **你不是在学习如何调用大模型。**
>
> **你是在学习如何把大模型变成一个可靠的软件系统。**

这将是你从 Java 后端工程师走向企业级 Agent 架构师的第一步。
