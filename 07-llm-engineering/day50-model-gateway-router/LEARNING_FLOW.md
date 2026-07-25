# Day 50: Model Gateway / Model Router - 学习流程

> **今日目标**: 实现模型路由和网关
> **核心问题**: 如何根据成本/延迟/能力选择模型？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_model_router.py（45分钟）
    ↓ 理解：模型路由策略与网关设计
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 45min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释模型路由的价值（成本/延迟/能力）
- [ ] 解释 4 种路由策略（Cost/Latency/Capability/Hybrid）
- [ ] 解释 Model Gateway 的设计要点
- [ ] 解释失败降级的实现方式
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_model_router.py](00_model_router.py) | 实现模型路由与网关 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
