# Day 61: LoRA/QLoRA 微调实战 - 学习流程

> **今日目标**: 掌握 LoRA/QLoRA 微调的核心理论和实战流程
> **核心问题**: 为什么 LoRA 能高效微调大模型？QLoRA 又是如何进一步降低显存的？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_lora_theory.py（15分钟）
    ↓ 理解：LoRA 低秩分解的数学原理
Step 4: 运行 01_data_preparation.py（15分钟）
    ↓ 理解：数据获取和清洗流程
Step 5: 运行 02_lora_training.py（20分钟）
    ↓ 理解：LoRA 训练流程
Step 6: 运行 03_qlora_demo.py（15分钟）
    ↓ 理解：QLoRA 量化原理
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4个代码文件 | 65min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 LoRA 的核心思想和数学原理
- [ ] 解释低秩分解的参数量计算
- [ ] 解释微调的关键参数及其影响
- [ ] 解释 QLoRA 的量化原理
- [ ] 解释数据获取和清洗的流程
- [ ] 解释微调模型的评估方法
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_lora_theory.py](00_lora_theory.py) | 理解 LoRA 低秩分解数学原理 | ⭐⭐ |
| [01_data_preparation.py](01_data_preparation.py) | 理解数据获取和清洗流程 | ⭐⭐ |
| [02_lora_training.py](02_lora_training.py) | 理解 LoRA 训练流程 | ⭐⭐⭐ |
| [03_qlora_demo.py](03_qlora_demo.py) | 理解 QLoRA 量化原理 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
