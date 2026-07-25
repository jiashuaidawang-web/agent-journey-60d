# Day 47: SFT / DPO（监督微调 / 偏好对齐）

> **今日目标**: 理解 SFT 和 DPO 原理
> **核心问题**: 如何让模型对齐人类偏好？

---

## 🎯 今日目标

1. 理解 SFT 原理
2. 理解 RLHF 流程
3. 理解 DPO 原理
4. 知道 Prompt / RAG / SFT / DPO 选型

---

## 📚 必学知识

### 1. SFT（Supervised Fine-Tuning）

**原理**：
- 使用标注数据（问题-答案对）微调
- 类似"带答案的学习"

**数据格式**：
```json
{"instruction": "...", "input": "...", "output": "..."}
```

### 2. RLHF（Reinforcement Learning from Human Feedback）

**流程**：
```
SFT → Reward Model → PPO 微调
```

**问题**：
- 流程复杂
- Reward Model 难训练
- PPO 不稳定

### 3. DPO（Direct Preference Optimization）

**原理**：
- 跳过 Reward Model
- 直接使用偏好数据优化
- 更简单、更稳定

**数据格式**：
```json
{"prompt": "...", "chosen": "...", "rejected": "..."}
```

### 4. 选型指南

| 场景 | 方案 |
|------|------|
| 快速适配 | Prompt Engineering |
| 需要知识 | RAG |
| 需要特定格式/风格 | SFT |
| 需要对齐人类偏好 | DPO |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| SFT | https://huggingface.co/docs/trl/sft_trainer |
| DPO 论文 | https://arxiv.org/abs/2305.18290 |
| TRL 文档 | https://huggingface.co/docs/trl/ |

---

## 🧠 学习深度

### 只需理解（L2）
- [ ] SFT 原理
- [ ] DPO 原理
- [ ] 选型指南

---

## 💻 今日编码任务

### 文件结构

```
day47-sft-dpo/
├── README.md
├── sft_dpo_demo.py          # SFT/DPO 原理演示
├── requirements.txt
└── boss-answer.md
```

### Task: sft_dpo_demo.py（60min）

演示 SFT/DPO 原理

---

## 🐉 今日 Boss

1. **SFT 的数据格式？**
2. **RLHF 的流程？**
3. **DPO 的优势？**

---

## 🎤 面试题

1. **Prompt / RAG / SFT / DPO 的选型？**
2. **DPO 和 RLHF 的区别？**
3. **什么时候用 SFT？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| sft_dpo_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 48: vLLM**
