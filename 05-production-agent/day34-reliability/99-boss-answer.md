# Day 34 Boss 答案

## 1. Retry 机制的关键参数？

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| max_retries | 最大重试次数 | 3 |
| base_delay | 基础延迟 | 1s |
| max_delay | 最大延迟 | 60s |
| exponential_backoff | 指数退避 | true |

## 2. Circuit Breaker 的三种状态？

| 状态 | 说明 |
|------|------|
| Closed | 正常，允许调用 |
| Open | 断开，拒绝调用 |
| Half-Open | 半开，尝试恢复 |

**状态转换**：
```
Closed → (连续失败 N 次) → Open → (等待恢复时间) → Half-Open → (成功) → Closed
                                              → (失败) → Open
```

## 3. 如何实现幂等性？

1. **唯一请求 ID**：每个请求有唯一 ID
2. **去重表**：记录已处理的请求
3. **状态机**：状态转换只允许一次
4. **Token 机制**：客户端生成唯一 Token
