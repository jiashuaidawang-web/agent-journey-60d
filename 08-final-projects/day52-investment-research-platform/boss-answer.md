# Day 52 Boss 答案

## 1. 请描述 Investment Research Platform 架构

**Supervisor + 多 Agent 架构**：

1. **Supervisor Agent**：任务分解、Agent 调度、结果汇总、报告生成
2. **专业 Agent**：行业研究、公司研究、市场情绪、风险分析
3. **Skills 层**：业务能力封装
4. **Tools 层**：MCP 标准化工具
5. **数据层**：RAG + GraphRAG + 外部数据

## 2. Supervisor 如何协调多个 Agent？

1. **任务接收**：接收用户投研需求
2. **任务分解**：分析需要调用哪些 Agent
3. **Agent 调度**：调用对应的专业 Agent
4. **结果汇总**：收集各 Agent 结果
5. **报告生成**：生成投研报告

## 3. 投研 Skills 有哪些？

| Skill | 说明 |
|-------|------|
| IndustryResearchSkill | 行业研究技能 |
| CompanyResearchSkill | 公司研究技能 |
| MarketSentimentSkill | 市场情绪技能 |
| RiskAnalysisSkill | 风险分析技能 |
