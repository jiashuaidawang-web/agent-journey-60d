# Day 32 Boss 答案

## 1. Agent 可观测性需要哪些指标？

| 指标 | 说明 | 作用 |
|------|------|------|
| Trace | 完整执行链路 | 排查问题 |
| Token | Token 消耗 | 成本优化 |
| Latency | 延迟 | 性能优化 |
| Cost | 成本 | 成本控制 |
| Tool Call | 工具调用 | 监控工具使用 |
| Agent Step | Agent 步骤 | 监控执行流程 |
| Error Rate | 错误率 | 稳定性监控 |

## 2. Trace 的作用是什么？

**Trace（追踪）** 记录 Agent 的完整执行链路：

1. **问题排查**：定位哪个步骤出错
2. **性能分析**：找出耗时步骤
3. **成本分析**：分析 Token 消耗分布
4. **审计**：记录完整的执行历史

## 3. 如何统计 Token 消耗？

**统计维度**：
1. **单次调用**：input_tokens + output_tokens
2. **总计**：所有调用的 Token 累加
3. **按步骤**：每个步骤的 Token 消耗
4. **按模型**：每个模型的 Token 消耗

**成本计算**：
```
cost = (input_tokens / 1000) * input_price + (output_tokens / 1000) * output_price
```
