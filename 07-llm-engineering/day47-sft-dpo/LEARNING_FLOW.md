# Day 47: SFT / DPO - 学习流程

> **今日目标**: 理解 SFT 和 DPO 原理
> **核心问题**: 如何让模型对齐人类偏好？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_sft_dpo_demo.py（30分钟）
    ↓ 理解：SFT 数据格式与 DPO 偏好优化原理
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

- [ ] 解释 SFT 的数据格式（instruction / input / output）
- [ ] 解释 RLHF 的三步流程（SFT → Reward Model → PPO）
- [ ] 解释 DPO 如何跳过 Reward Model 直接优化
- [ ] 知道 Prompt / RAG / SFT / DPO 的选型场景
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_sft_dpo_demo.py](00_sft_dpo_demo.py) | 理解 SFT/DPO 原理演示 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
