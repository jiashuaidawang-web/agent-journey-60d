# Day 48 Boss 答案

## 1. vLLM 的核心优化？

| 优化 | 说明 |
|------|------|
| PagedAttention | 分页管理 KV Cache，避免显存碎片 |
| Continuous Batching | 连续批处理，提高吞吐量 |
| Prefix Caching | 前缀缓存，避免重复计算 |
| Tensor Parallelism | 张量并行，支持多 GPU |

## 2. PagedAttention 的原理？

- 将 KV Cache 分页管理（类似操作系统内存分页）
- 每个请求的 KV Cache 可以非连续存储
- 避免显存碎片
- 提高显存利用率（从 20-40% 到 90%+）

## 3. Continuous Batching 的优势？

- 传统批处理：等待所有请求完成才处理下一批
- 连续批处理：有请求完成就加入新请求
- 优势：提高吞吐量，降低延迟
