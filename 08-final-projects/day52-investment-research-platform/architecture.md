# Investment Research Platform 架构说明

## 整体架构

```
                    ┌──────────────┐
                    │  Supervisor  │
                    │   Agent      │
                    └──────┬───────┘
                           │
        ┌────────┬─────────┼─────────┬────────┐
        ▼        ▼         ▼        ▼        ▼
   ┌────────┐┌────────┐┌────────┐┌────────┐┌────────┐
   │Industry││Company ││Financial││Market  ││  Risk  │
   │Research││Research││Analysis││Sentiment││Analysis│
   │ Agent  ││ Agent  ││ Agent  ││ Agent  ││ Agent  │
   └───┬────┘└───┬────┘└───┬────┘└───┬────┘└───┬────┘
       │         │         │         │         │
       └─────────┴────┬────┴─────────┴─────────┘
                      │
              ┌───────▼───────┐
              │  MCP + A2A    │
              │  Tool Layer   │
              └───────┬───────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   ┌─────────┐  ┌─────────┐  ┌──────────┐
   │  RAG    │  │ GraphRAG│  │ 外部数据  │
   │ 知识库  │  │ 图谱    │  │ 行情/财报 │
   └─────────┘  └─────────┘  └──────────┘
```

## 核心模块说明

### 1. Supervisor Agent

| 职责 | 说明 |
|------|------|
| 任务接收 | 接收用户投研需求 |
| 任务分解 | 分解为子任务 |
| Agent 调度 | 调用合适的 Agent |
| 结果汇总 | 汇总各 Agent 结果 |
| 报告生成 | 生成投研报告 |

### 2. 专业 Agent

| Agent | 职责 | Skills |
|-------|------|--------|
| Industry Agent | 行业研究 | IndustryResearchSkill |
| Company Agent | 公司研究 | CompanyResearchSkill |
| Market Agent | 市场情绪 | MarketSentimentSkill |
| Risk Agent | 风险分析 | RiskAnalysisSkill |

### 3. Skills 层

| Skill | 工具 | 说明 |
|-------|------|------|
| IndustryResearchSkill | industry_research | 行业概况研究 |
| CompanyResearchSkill | company_research, financial_analysis | 公司+财务研究 |
| MarketSentimentSkill | market_sentiment | 市场情绪分析 |
| RiskAnalysisSkill | risk_analysis | 风险因素分析 |

### 4. Tools 层（MCP）

| Tool | 说明 |
|------|------|
| industry_research | 行业研究工具 |
| company_research | 公司研究工具 |
| financial_analysis | 财务分析工具 |
| market_sentiment | 市场情绪工具 |
| risk_analysis | 风险分析工具 |

## 面试时的讲法

> "我设计了一个 AI 投研多 Agent 平台。
>
> Supervisor Agent 负责任务分解和协调，根据用户需求调用不同的专业 Agent。
>
> 每个专业 Agent 封装了对应的 Skill，Skill 内部调用 MCP 标准化的工具。
>
> 底层使用 RAG + GraphRAG 混合检索，支持多跳推理。
>
> 这个架构的优势是：
> 1. 关注点分离：每个 Agent 专注一个领域
> 2. 可扩展：新增 Agent 不影响现有系统
> 3. 可复用：Skills 可以在多个 Agent 中使用
> 4. 标准化：MCP 协议统一工具接口"
