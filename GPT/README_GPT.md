# 贾帅 · 12个月企业级 Agent 架构师进阶路线

> 目标：12个月后，能够独立完成企业级 Agent 系统从0到1的需求分析、架构设计、核心编码、部署上线、性能优化、安全治理、评测与持续迭代。
>
> 当前优势：Java / Spring Boot / 企业级后端开发经验。
>
> 核心路线：Java后端 → AI应用工程 → RAG工程 → Agent工程 → 企业级Agent → Agent Platform → Agent架构师

---

## 一、最终能力地图

- AI基础：LLM、Prompt、Token、Context、Embedding、Structured Output、Function Calling
- RAG：文档解析、Chunk、Embedding、Vector DB、Hybrid Search、Rerank、Query Rewrite、RAG Evaluation
- Agent：Tool Calling、ReAct、Planning、Workflow、Memory、Reflection
- Multi-Agent：Supervisor、Router、Delegation、Parallel Agent
- Tool / MCP：Tool Registry、Discovery、Schema、Permission、Audit
- 企业工程：高并发、限流、超时、重试、熔断、幂等、缓存、消息队列
- 安全治理：Prompt Injection、RBAC、ABAC、多租户、数据权限、工具权限、人工审批
- AgentOps：Trace、Evaluation、Observability、Cost Control、Continuous Improvement
- 平台架构：Agent Runtime、Agent Gateway、LLM Gateway、RAG Platform、Tool Platform、Memory Platform

---

# 二、12个月总路线

| 月份 | 核心主题 | 目标身份 | 核心产出 |
|---|---|---|---|
| M1 | LLM & AI 应用基础 | AI 应用开发者 | AI Chat Platform |
| M2 | RAG 基础 | RAG 工程师 | 企业知识库 |
| M3 | 企业级 RAG | 高级 RAG 工程师 | RAG Platform |
| M4 | Agent 基础 | Agent 工程师 | Tool Agent |
| M5 | Workflow & Planning | Agent 工程师 | Agent Workflow |
| M6 | Memory & Multi-Agent | 高级 Agent 工程师 | Multi-Agent |
| M7 | MCP & Tool Platform | Agent 平台工程师 | Tool/MCP Platform |
| M8 | 企业级 Agent | 企业 Agent 工程师 | AI 运维 Agent |
| M9 | Agent Platform | AI 平台工程师 | Agent Platform |
| M10 | Security & Governance | AI 架构工程师 | Agent Governance |
| M11 | Evaluation & Observability | AgentOps 工程师 | AgentOps Platform |
| M12 | 综合实战 | 企业级 Agent 架构师 | Enterprise Agent Platform |

---

# 三、M1：AI 应用开发基础

## 目标

从 Java 后端开发工程师升级为 AI 应用开发工程师。

## 学习内容

### LLM
- Transformer 基础概念
- Token
- Context Window
- Temperature
- Top-P
- Embedding
- Inference

### Prompt
- Zero Shot
- Few Shot
- Role Prompt
- System Prompt
- Structured Output

### Function Calling
理解：
LLM → Tool Schema → Function Calling → Tool Execute → Result → LLM

## 技术栈

- Java
- Spring Boot
- Spring AI
- OpenAI Compatible API
- Redis
- MySQL
- Docker

## 项目：AI Chat Platform

功能：
- 多轮对话
- 上下文管理
- Streaming
- Token 统计
- 历史记录
- 模型切换
- 异常处理

建议仓库：
`ai-chat-platform`

必须包含：
- README
- Architecture
- API
- Database
- Docker
- Tests

---

# 四、M2：RAG 基础

## 目标

成为能够独立开发 RAG 系统的工程师。

## 学习内容

PDF / Word / Markdown / HTML
→ Parser
→ Chunk
→ Embedding
→ Vector DB
→ Retrieval
→ Prompt
→ LLM

重点理解：
- Chunk 为什么重要？
- Embedding 是什么？
- Vector Search 怎么工作？
- TopK 是什么？
- 为什么会召回错误内容？

## 项目：Enterprise Knowledge Base

技术：
- Spring AI
- Milvus
- Redis
- MySQL

功能：
- 文档上传
- 文档解析
- 文档切分
- 向量化
- 向量检索
- RAG 问答
- 文档管理

---

# 五、M3：企业级 RAG

## 学习内容

- Hybrid Search
- BM25
- Rerank
- Metadata Filter
- Parent-Child Chunk
- Query Rewrite
- Multi Query
- HyDE
- RAG Evaluation
- 权限过滤
- 文档版本
- 知识更新
- 增量索引
- 删除索引
- 多租户

## 项目：Enterprise RAG Platform

架构：

Document
→ Parser
→ Chunk
→ Embedding
→ Vector DB
→ Hybrid Search
→ Rerank
→ Context
→ LLM

必须能够回答：
1. 为什么 RAG 会产生幻觉？
2. 为什么检索到了正确文档，LLM 仍然答错？
3. 100 万份企业文档如何做 RAG？
4. 如何实现知识库权限隔离？
5. 如何评估 RAG 效果？

---

# 六、M4：Agent 基础

## 学习内容

- Agent
- Tool Calling
- ReAct
- Agent Loop
- State
- Observation
- Action

核心理解：

Agent
→ Thinking
→ Tool
→ Observation
→ Thinking
→ Tool
→ Answer

## 项目：Personal AI Agent

Agent 能够：
- 查询天气
- 查询数据库
- 搜索知识库
- 调用 API
- 执行计算

重点回答：

> Agent 和普通 Chatbot 的本质区别是什么？

---

# 七、M5：Workflow & Planning

## 学习内容

- Workflow
- State Machine
- Planning
- Plan-Execute
- Reflection
- Retry
- Human-in-the-loop

## 项目：AI 软件开发 Agent

流程：

用户需求
→ 需求分析 Agent
→ PRD
→ 架构设计
→ 数据库设计
→ 代码生成
→ 测试
→ Code Review

重点回答：
- 什么任务应该由 Workflow 做？
- 什么任务应该由 Agent 自主决策？
- 什么时候需要人工介入？

---

# 八、M6：Memory & Multi-Agent

## Memory

- Short-term Memory
- Long-term Memory
- Semantic Memory
- Episodic Memory
- User Profile

## Multi-Agent

- Supervisor
- Router
- Delegation
- Parallel Agent

## 项目：AI Research Team

架构：

Supervisor
├── Research Agent
├── Data Agent
├── Analyst Agent
└── Report Agent

可以与 A 股 AI 专家项目结合：

Research Agent
→ Market Data Agent
→ News Agent
→ Sentiment Agent
→ Quant Agent
→ Risk Agent
→ Report Agent

重点回答：
- 什么情况下应该使用 Multi-Agent？
- Agent 之间如何通信？
- 如何避免上下文污染？
- 如何处理 Agent 失败？

---

# 九、M7：MCP & Tool Platform

## 学习内容

- Tool
- Tool Registry
- Tool Discovery
- Tool Schema
- MCP
- Permission
- Audit

## 项目：Enterprise Tool Platform

接入：
- MySQL
- Redis
- GitLab
- Jira
- Kubernetes
- Jenkins
- HTTP API

架构：

Agent
→ Tool Registry
→ Permission Check
→ Tool Execute
→ Result Validation
→ Audit

重点理解：

> Agent 如何安全地操作真实世界？

---

# 十、M8：Enterprise Agent

## 项目：AI 运维 Agent

接入：
- CMDB
- Prometheus
- Elasticsearch
- Kubernetes
- GitLab
- Jira
- 企业知识库

流程：

告警
→ Agent
→ CMDB
→ Prometheus
→ Elasticsearch
→ Kubernetes
→ 历史知识库
→ 根因分析
→ 解决方案
→ 人工审批
→ 执行
→ 验证
→ 报告

加入企业级能力：
- Retry
- Timeout
- Circuit Breaker
- Idempotency
- Rate Limit
- Fallback
- Audit

目标：

> 完成第一个真正意义上的企业级 Agent。

---

# 十一、M9：Agent Platform

从“开发 Agent”升级为“开发 Agent 平台”。

平台提供：
- Agent 创建
- Agent 配置
- Agent 发布
- 模型选择
- Prompt 配置
- 知识库绑定
- Tool 绑定
- Workflow 配置
- 权限配置

核心架构：

Agent Platform
├── Agent Runtime
├── LLM Gateway
├── RAG Platform
├── Tool Platform
├── Memory Platform
└── Workflow Engine

目标：

> 让业务团队能够低代码/配置化创建企业 Agent。

---

# 十二、M10：Security & Governance

## 学习内容

- Prompt Injection
- Data Leakage
- RBAC
- ABAC
- Multi-Tenant
- Data Permission
- Tool Permission
- Audit
- Human Approval

权限模型：

User
→ Identity
→ RBAC / ABAC
→ Agent Permission
→ Tool Permission
→ Data Permission
→ Execute
→ Audit

重点解决：
- 谁可以使用 Agent？
- 谁可以调用 Tool？
- 谁可以查询数据？
- 谁可以执行生产操作？
- 谁批准了危险操作？

---

# 十三、M11：Evaluation & AgentOps

## Evaluation

指标：
- Answer Correctness
- Faithfulness
- Relevance
- Task Success
- Tool Accuracy
- Hallucination
- Latency
- Token Cost

链路：

Agent
→ Trace
→ Evaluation
→ Score
→ Feedback
→ Optimization

## Observability

实现完整 Trace：

Request
→ Agent
→ LLM
→ RAG
→ Tool
→ Result

必须能够回答：

> Agent 为什么失败？

> 失败发生在哪一步？

> 是 Prompt、RAG、Tool、Model、Planning 还是 Memory 的问题？

---

# 十四、M12：最终毕业项目

# Enterprise Agent Platform

最终架构：

User
→ Agent Gateway
→ Agent Runtime

Agent Runtime
├── Planner
├── Memory
├── RAG
├── Tool Registry
├── MCP
├── Workflow
└── Multi-Agent

企业系统：
- MySQL
- Redis
- Kubernetes
- GitLab
- Jira
- Elasticsearch
- Prometheus

治理：
- Security
- Permission
- Audit
- Observability
- Evaluation
- Cost Control

最终实现：
- Agent 创建
- Agent 配置
- Agent 发布
- Agent 运行
- Agent 监控
- Agent 评估
- Agent 优化
- Agent 权限
- Agent 审计

---

# 十五、技术栈路线

## 后端

- Java
- Spring Boot
- Spring AI

## AI

- LLM
- Embedding
- Rerank
- Prompt
- Function Calling
- Structured Output

## RAG

- Milvus
- Redis
- Elasticsearch

## Agent

- Spring AI
- LangGraph 思想
- MCP

## 工程

- MySQL
- Redis
- Kafka / RabbitMQ
- Docker
- Kubernetes

## Observability

- OpenTelemetry
- Prometheus
- Grafana

## DevOps

- Linux
- Docker
- Kubernetes
- CI/CD

原则：

> 主线技术栈不要频繁切换。

---

# 十六、学习方法

每个阶段采用：

- 20% 理论
- 30% 源码
- 40% 项目
- 10% 总结

不要：
“看100小时课程”。

要：
“看10小时 → 写20小时 → Debug 20小时 → 设计10小时”。

真正能力来自：

> 写代码 + 犯错 + Debug + 重构。

---

# 十七、每周固定节奏

## 周一
理论学习

## 周二
源码阅读

## 周三
功能开发

## 周四
功能开发

## 周五
Debug + 性能优化

## 周六
项目实战

## 周日
总结 + GitHub

每周至少产生：
- 1 个知识总结
- 1 个架构图
- 1 个代码模块
- 1 次 Git Commit
- 1 个问题复盘

12个月约：
- 52 周
- 52 篇技术总结
- 52 个核心模块
- 52 次架构思考

---

# 十八、GitHub 最终作品体系

建议逐步形成：

agent-journey-60d
↓
ai-chat-platform
↓
enterprise-rag-platform
↓
agent-runtime
↓
multi-agent-system
↓
enterprise-tool-platform
↓
enterprise-agent-platform
↓
agent-evaluation-platform
↓
agentops-platform

最终汇聚：

enterprise-agent-platform

目标不是证明：

> “我学过 Agent。”

而是证明：

> “这是我独立设计并实现的一套企业级 Agent 平台。”

---

# 十九、12个月能力验收

必须能够独立回答并实践：

1. 如何设计企业级 Agent Runtime？
2. 1000 万文档如何做 RAG？
3. Agent 和 Workflow 如何选择？
4. 为什么需要 Multi-Agent？
5. MCP 如何解决企业 Tool 集成？
6. Agent 长期记忆如何设计？
7. 如何防止 Agent 越权访问生产数据？
8. 如何证明 Agent 做得越来越好？
9. 10000 用户同时调用 Agent 怎么办？
10. 如何降低 LLM 成本？
11. Agent 线上出现死循环怎么办？
12. 从 0 设计一个企业 Agent 平台怎么做？

最终要求：

> 现场画架构图 + 写核心代码 + 解释技术决策 + 解决线上故障。

---

# 二十、最终职业升级路线

Java 开发工程师
↓
AI 应用工程师
↓
RAG 工程师
↓
Agent 工程师
↓
企业级 Agent 工程师
↓
Agent Platform 工程师
↓
AI 架构师

---

# 二十一、最重要的原则

不要把目标理解为：

> 我要学完100个技术。

而要理解成：

> 我要完成10次能力跃迁。

1. Java → AI
2. AI → RAG
3. RAG → Agent
4. Agent → Workflow
5. 单 Agent → Multi-Agent
6. Agent → Tool/MCP
7. Agent → 企业级
8. Agent → Agent Platform
9. Agent → AgentOps
10. 开发者 → 架构师

---

# 二十二、建议的下一步

这份 12 个月路线作为总纲。

当前的 `Agent Journey 60D` 作为第一个里程碑。

下一步开始：

> M1：AI 应用开发基础 · 30天作战计划

每天明确：
- 学习什么
- 看什么
- 写什么代码
- 做什么实验
- GitHub 提交什么
- 每周验收标准
- 每周面试题
- 每周架构题
- Day 30 毕业项目

第一阶段毕业项目：

> `AI Chat Platform`

目标：

> 从 Java 后端开发者，完成第一次 AI 应用工程能力升级。
