# Day 49: KV Cache / PagedAttention - 学习流程

> **今日目标**: 深入理解 KV Cache 和 PagedAttention
> **核心问题**: 为什么需要 KV Cache？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_kv_cache_demo.py（30分钟）
    ↓ 理解：KV Cache 如何避免重复计算
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 30min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 KV Cache 的作用和原理
- [ ] 解释 PagedAttention 如何避免显存碎片
- [ ] 解释 Prefix Caching 如何提高吞吐量
- [ ] 理解推理优化的整体思路
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_kv_cache_demo.py](00_kv_cache_demo.py) | 理解 KV Cache 原理演示 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
