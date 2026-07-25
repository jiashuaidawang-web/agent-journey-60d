# Day 14 Boss 答案

## 1. 请描述你的 Research Agent 架构

**架构**：
```
START → research → analysis → report → approval → publish/revise → END
```

**节点说明**：

| 节点 | 职责 | 输入 | 输出 |
|------|------|------|------|
| research | 搜索信息 | topic | research_data |
| analysis | 分析信息 | research_data | analysis_result |
| report | 生成报告 | analysis_result | report |
| approval | 人工审批 | report | approved |
| publish | 发布报告 | report | final_output |
| revise | 修改报告 | - | final_output |

**条件边**：
- approval → publish（approved=True）
- approval → revise（approved=False）

**Checkpoint**：
- 使用 MemorySaver 保存每个节点后的 State
- 支持断点续跑

**interrupt**：
- 在 approval 节点后暂停
- 等待人工审批后继续

## 2. 如果让你扩展支持多 Agent 协作，你会怎么改？

**扩展方案**：

1. **Supervisor 模式**：
   - 添加 Supervisor Agent 协调多个子 Agent
   - 子 Agent：ResearchAgent / AnalysisAgent / ReportAgent
   - Supervisor 分配任务、整合结果

2. **Subgraph 拆分**：
   - 每个子 Agent 是一个 Subgraph
   - 父图负责协调和流程控制

3. **A2A 通信**：
   - Agent 之间通过消息传递协作
   - 支持异步通信

4. **共享 State**：
   - 所有 Agent 共享同一个 State
   - 通过 State 传递中间结果

## 3. 如何保证长时间运行的可靠性？

**可靠性保障**：

1. **Checkpoint**：每个节点后保存状态
2. **interrupt**：关键节点暂停确认
3. **错误处理**：每个节点捕获异常
4. **超时控制**：设置最大执行时间
5. **Token 预算**：设置 Token 上限
6. **Subgraph 隔离**：子图失败不影响其他
