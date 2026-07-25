# Day 35 Boss 答案

## 1. 为什么 Agent 需要异步处理？

- **执行时间长**：Agent 多步执行可能需要几十秒
- **用户体验**：同步等待用户体验差
- **并发处理**：需要支持大量并发请求
- **资源利用**：避免阻塞等待

## 2. 异步架构的流程？

```
用户请求 → API Gateway → 创建任务 → 返回任务 ID
                ↓
            消息队列
                ↓
            Worker 消费 → 执行 Agent → 存储结果
                ↓
用户轮询/WebSocket → 获取结果
```

## 3. 如何实现任务状态追踪？

1. **任务 ID**：每个任务有唯一 ID
2. **状态存储**：Redis / MySQL 存储状态
3. **状态流转**：pending → running → completed/failed
4. **轮询/WebSocket**：客户端获取状态
