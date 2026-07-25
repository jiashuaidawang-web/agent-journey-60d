# Day 47 Boss 答案

## 1. SFT 的数据格式？

```json
{
  "instruction": "请分析以下股票",
  "input": "贵州茅台",
  "output": "贵州茅台是白酒行业龙头..."
}
```

## 2. RLHF 的流程？

```
1. SFT（监督微调）
2. 训练 Reward Model（奖励模型）
3. PPO 微调（使用 Reward Model 优化）
```

## 3. DPO 的优势？

- **无需 Reward Model**：简化流程
- **训练稳定**：比 PPO 更稳定
- **效果更好**：通常优于 RLHF
- **数据高效**：只需要偏好数据
