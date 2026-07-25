# 模拟面试

## Boss 1：设计一个企业级 Agent Platform

### 参考答案

**1. 需求分析**
- 多租户支持
- 成本控制
- 高可用
- 可观测性

**2. 架构设计**
- Java 控制平面：租户、权限、调度、成本、路由
- Python AI 服务：Agent 编排、RAG
- 混合检索：Dense + BM25 + Reranker

**3. 关键设计**
- 多租户隔离：数据、配额、性能、安全
- 成本优化：模型路由、Token 统计
- 全链路追踪：Trace、Metrics

**4. 扩展性**
- 新增 Agent：注册到 Supervisor
- 新增 Skill：添加到 Registry
- 新增 Tool：通过 MCP 注册

---

## Boss 2：设计一个 Multi-Agent Research System

### 参考答案

**1. 需求分析**
- 多维度分析（行业、公司、市场、风险）
- Agent 协作
- 报告生成

**2. 架构设计**
- Supervisor Agent：任务分解、Agent 调度
- 专业 Agent：行业、公司、市场、风险
- Skills 层：业务能力封装
- MCP 层：工具标准化

**3. 关键设计**
- Agent 协作：Supervisor 统一协调
- 能力复用：Skills 层封装
- 工具标准化：MCP 协议

**4. 数据层**
- RAG：向量检索
- GraphRAG：多跳推理
- 外部数据：行情、财报

---

## Boss 3：LangChain vs LangGraph

### 参考答案

| 维度 | LangChain | LangGraph |
|------|-----------|-----------|
| 抽象 | Chain（链） | Graph（图） |
| 流程 | 线性 | 任意图 |
| 状态 | 弱 | 强 |
| 循环 | 不支持 | 支持 |
| 多 Agent | 不支持 | 支持 |

**选择**：
- 简单任务：LangChain
- 复杂 Agent：LangGraph

---

## Boss 4：MCP vs Function Calling

### 参考答案

| 维度 | Function Calling | MCP |
|------|------------------|-----|
| 定义 | LLM 输出工具调用 | 工具标准化协议 |
| 范围 | LLM → 工具 | LLM ↔ 工具 ↔ 数据源 |
| 标准化 | 各家不同 | 统一协议 |
| 复用性 | 低 | 高 |

**关系**：
- Function Calling 是能力
- MCP 是协议
- MCP 使用 Function Calling 实现

---

## Boss 5：Agent vs Workflow

### 参考答案

| 维度 | Agent | Workflow |
|------|-------|----------|
| 决策者 | LLM | 开发者 |
| 确定性 | 低 | 高 |
| 灵活性 | 高 | 低 |

**选择**：
- 流程明确：Workflow
- 需要推理：Agent
- 实际系统：混合

---

## Boss 6：RAG vs Fine-tuning

### 参考答案

| 维度 | RAG | Fine-tuning |
|------|-----|-------------|
| 知识更新 | 快 | 慢 |
| 成本 | 低 | 高 |
| 幻觉 | 较少 | 可能较多 |
| 适用 | 知识密集型 | 风格/格式适配 |

**选择**：
- 知识更新频繁：RAG
- 需要特定风格：Fine-tuning
- 最佳实践：RAG + SFT

---

## Boss 7：Agent 如何做到可恢复？

### 参考答案

1. **Checkpoint**：每个节点后保存状态
2. **持久化**：状态保存到数据库
3. **恢复**：从任意 Checkpoint 恢复
4. **幂等**：重复执行结果一致

---

## Boss 8：Agent 如何控制成本？

### 参考答案

1. **模型路由**：根据复杂度选择模型
2. **Token 统计**：监控 Token 消耗
3. **配额限制**：设置 Token 上限
4. **缓存**：缓存相同请求结果
5. **Prompt 优化**：减少 Prompt Token

---

## Boss 9：Agent 如何保证安全？

### 参考答案

1. **Prompt Injection 防护**：检测恶意输入
2. **权限控制**：RBAC、API Key
3. **输出过滤**：过滤敏感信息
4. **审计日志**：记录所有操作
5. **Rate Limiting**：限流

---

## Boss 10：你的项目有什么亮点？

### 参考答案

1. **Java + Python 混合架构**：发挥各自优势
2. **多租户隔离**：数据、配额、性能、安全四个维度
3. **成本优化**：模型路由、Token 统计
4. **全链路追踪**：Trace、Metrics
5. **Supervisor 多 Agent**：协作、复用
6. **GraphRAG**：多跳推理能力
