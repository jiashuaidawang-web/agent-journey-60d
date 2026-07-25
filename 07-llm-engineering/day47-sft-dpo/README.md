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
├── LEARNING_FLOW.md            # 学习流程
├── 00_sft_dpo_demo.py          # SFT/DPO 原理演示
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_sft_dpo_demo.py（60min）

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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 SFT 数据格式和训练流程
- 解释 DPO 偏好优化的数学原理
- 帮你调试 TRL 库的使用报错
- 对比 RLHF 与 DPO 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我了解监督学习，但对 DPO 如何跳过 Reward Model 直接优化不太熟。请用分类损失类比解释一下 DPO 的损失函数含义。"

### 错误用法
> "帮我写一个完整的 DPO 训练脚本。"

---

## 📝 GitHub 提交规范

### 提交结构
```
07-llm-engineering/
└── day47-sft-dpo/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_sft_dpo_demo.py   # SFT/DPO 原理演示
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 47 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| SFT | ... | ... |
| DPO | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 07-llm-engineering/day47-sft-dpo/
git commit -m "feat(day47): SFT/DPO - 监督微调与偏好对齐原理完成"
```

---

## 📊 今日检查清单

- [ ] 读了 SFT 文档（huggingface.co/docs/trl/sft_trainer）
- [ ] 读了 DPO 论文（arxiv.org/abs/2305.18290）
- [ ] 写了 00_sft_dpo_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
