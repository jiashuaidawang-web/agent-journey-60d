# Day 62: SFT/DPO + 微调部署 - 学习流程

> **今日目标**: 掌握 SFT/DPO 微调方法，以及微调模型的部署与最佳实践
> **核心问题**: SFT 和 DPO 有什么区别？微调后的模型如何部署到生产环境？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_sft_training.py（15分钟）
    ↓ 理解：SFT 训练流程
Step 4: 运行 00_sft_dpo.py（15分钟）
    ↓ 理解：DPO 偏好对齐流程
Step 5: 运行 01_model_evaluation.py（15分钟）
    ↓ 理解：模型评估指标
Step 6: 运行 02_model_deployment.py（15分钟）
    ↓ 理解：模型部署方法
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4个代码文件 | 60min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 SFT 的原理和流程
- [ ] 解释 DPO 的原理和优势
- [ ] 解释 SFT 和 DPO 的区别
- [ ] 解释 BLEU/ROUGE 评估指标
- [ ] 解释 vLLM 和 OLLAMA 的部署方法
- [ ] 解释 LoRA 模型合并和导出的方法
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_sft_training.py](00_sft_training.py) | 理解 SFT 训练流程 | ⭐⭐ |
| [00_sft_dpo.py](00_sft_dpo.py) | 理解 DPO 偏好对齐流程 | ⭐⭐⭐ |
| [01_model_evaluation.py](01_model_evaluation.py) | 理解模型评估指标 | ⭐⭐ |
| [02_model_deployment.py](02_model_deployment.py) | 理解模型部署方法 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
