# Day 32: Observability - 学习流程

> **今日目标**: 实现 Agent 系统的可观测性
> **核心问题**: 如何监控 Agent 的运行状态？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_metrics_demo.py（45分钟）
    ↓ 理解：Token/Cost/Latency 指标统计
Step 4: 运行 01_trace_demo.py（60分钟）
    ↓ 理解：Trace 完整执行链路追踪
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 105min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 2.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释为什么 Agent 需要可观测性
- [ ] 理解 Trace / Token / Latency / Cost 等核心指标
- [ ] 实现 Token/Cost/Latency 的统计逻辑
- [ ] 实现 Trace 和 Span 的追踪机制
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_metrics_demo.py](00_metrics_demo.py) | Token/Cost/Latency 指标统计 | ⭐⭐ |
| [01_trace_demo.py](01_trace_demo.py) | Trace 完整执行链路追踪 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
