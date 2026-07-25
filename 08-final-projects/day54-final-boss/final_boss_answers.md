# Final Boss 10 道面试题答案

## Boss 1：设计一个企业级 Agent Platform

**考察点**：架构设计能力、生产级思维

**参考答案**：

1. **需求分析**
   - 多租户支持
   - 成本控制
   - 高可用
   - 可观测性

2. **架构设计**
   - Java 控制平面：租户管理、权限鉴权、任务调度、成本核算、模型路由
   - Python AI 服务：Agent 编排（LangGraph）、RAG
   - 混合检索：Dense + BM25 + Reranker

3. **关键设计**
   - 多租户隔离：数据、配额、性能、安全四个维度
   - 成本优化：模型路由、Token 统计、配额限制
   - 全链路追踪：Trace、Metrics、Logging、Alert

4. **扩展性**
   - 新增 Agent：注册到平台
   - 新增 Skill：添加到 Registry
   - 新增 Tool：通过 MCP 注册

---

## Boss 2：设计一个 Multi-Agent Research System

**考察点**：多 Agent 协作、领域建模

**参考答案**：

1. **需求分析**
   - 多维度分析（行业、公司、市场、风险）
   - Agent 协作
   - 报告生成

2. **架构设计**
   - Supervisor Agent：任务分解、Agent 调度、结果汇总
   - 专业 Agent：行业、公司、市场、风险
   - Skills 层：业务能力封装
   - MCP 层：工具标准化

3. **关键设计**
   - Agent 协作：Supervisor 统一协调
   - 能力复用：Skills 层封装
   - 工具标准化：MCP 协议

4. **数据层**
   - RAG：向量检索
   - GraphRAG：多跳推理
   - 外部数据：行情、财报

---

## Boss 3：LangChain vs LangGraph

**考察点**：框架理解

**参考答案**：

| 维度 | LangChain | LangGraph |
|------|-----------|-----------|
| 抽象 | Chain（链式） | Graph（图） |
| 适用 | 线性流程 | 复杂 Agent |
| 状态管理 | 弱 | 强 |
| 循环 | 不支持 | 原生支持 |
| 多 Agent | 不支持 | 原生支持 |
| Human-in-the-loop | 复杂 | 原生支持 |

**选择**：
- 简单任务（一次调用）：LangChain
- 复杂 Agent（多步、分支、循环）：LangGraph

---

## Boss 4：MCP vs Function Calling

**考察点**：协议理解

**参考答案**：

| 维度 | Function Calling | MCP |
|------|------------------|-----|
| 定义 | LLM 输出工具调用 | 工具标准化协议 |
| 范围 | LLM → 工具 | LLM ↔ 工具 ↔ 数据源 |
| 标准化 | 各家不同 | 统一开放协议 |
| 复用性 | 低 | 高 |

**关系**：
- Function Calling 是 LLM 的"能力"
- MCP 是"协议"（标准化工具如何被定义、发现、调用）
- MCP 使用 Function Calling 实现

---

## Boss 5：Agent vs Workflow

**考察点**：场景选择

**参考答案**：

| 维度 | Agent | Workflow |
|------|-------|----------|
| 决策者 | LLM | 开发者 |
| 确定性 | 低 | 高 |
| 灵活性 | 高 | 低 |
| 适用 | 开放任务 | 明确流程 |

**选择**：
- 流程明确（如审批流程）：Workflow
- 需要推理（如研究分析）：Agent
- 实际系统通常是混合：Workflow 框架 + Agent 节点

---

## Boss 6：RAG vs Fine-tuning

**考察点**：技术选型

**参考答案**：

| 维度 | RAG | Fine-tuning |
|------|-----|-------------|
| 知识更新 | 快 | 慢 |
| 成本 | 低 | 高 |
| 幻觉 | 较少 | 可能较多 |
| 适用 | 知识密集型 | 风格/格式适配 |

**选型指南**：
- Prompt Engineering：快速适配
- RAG：需要知识
- SFT：需要特定格式/风格
- DPO：需要对齐人类偏好

---

## Boss 7：Agent 如何做到可恢复？

**考察点**：生产级能力

**参考答案**：

1. **Checkpoint 机制**
   - 每个节点执行后保存 State
   - 保存到 Checkpoint Saver（内存/数据库）

2. **状态持久化**
   - State 序列化到数据库
   - 支持跨进程恢复

3. **断点续跑**
   - 从任意 Checkpoint 恢复
   - 通过 thread_id 标识会话

4. **幂等性**
   - 重复执行结果一致
   - 通过任务 ID 去重

---

## Boss 8：Agent 如何控制成本？

**考察点**：成本优化

**参考答案**：

1. **模型路由**
   - 根据任务复杂度选择模型
   - 简单任务 → 便宜模型（GPT-4o-mini）
   - 复杂任务 → 强模型（GPT-4o）

2. **Token 统计**
   - 监控每次调用的 Token 消耗
   - 分析成本分布

3. **配额限制**
   - 设置 Token 上限
   - 超出后拒绝或降级

4. **缓存**
   - 缓存相同请求结果
   - Prefix Caching（前缀缓存）

5. **Prompt 优化**
   - 减少 Prompt Token
   - 精简上下文

---

## Boss 9：Agent 如何保证安全？

**考察点**：安全意识

**参考答案**：

1. **Prompt Injection 防护**
   - 检测恶意输入模式
   - 拒绝恶意请求

2. **权限控制**
   - RBAC（基于角色的访问控制）
   - API Key 认证

3. **输出过滤**
   - 过滤敏感信息
   - 防止数据泄露

4. **审计日志**
   - 记录所有操作
   - 支持事后审计

5. **Rate Limiting**
   - 限流
   - 防止 DoS

---

## Boss 10：你的项目有什么亮点？

**考察点**：项目总结、差异化竞争力

**参考答案**：

**项目一：Enterprise Agent Platform**
1. **Java + Python 混合架构**：发挥各自优势
2. **多租户隔离**：数据、配额、性能、安全四个维度
3. **成本优化**：模型路由、Token 统计
4. **全链路追踪**：Trace、Metrics、Logging、Alert

**项目二：AI Investment Research Platform**
1. **Supervisor 多 Agent 架构**：协作、复用
2. **Skills 层能力封装**：业务逻辑复用
3. **MCP 工具标准化**：统一接口
4. **GraphRAG**：多跳推理能力

**差异化竞争力**：
- 10年 Java 经验 + Agent 编排
- 企业级架构能力
- 生产级稳定性设计
