# Day 46: LoRA / QLoRA（高效参数微调）

> **今日目标**: 理解 LoRA 和 QLoRA 原理
> **核心问题**: 为什么需要高效微调？

---

## 🎯 今日目标

1. 理解全量微调的问题
2. 理解 LoRA 原理
3. 理解 QLoRA 原理
4. 知道什么时候用

---

## 📚 必学知识

### 1. 全量微调的问题

- 参数量大（7B、13B、70B）
- 显存占用高
- 训练成本高

### 2. LoRA（Low-Rank Adaptation）

**原理**：
```
原始权重 W（冻结）
    +
低秩矩阵 A × B（可训练）

ΔW = A × B
```

**优势**：
- 只训练少量参数（<1%）
- 显存占用低
- 可插拔（不同任务不同 LoRA）

### 3. QLoRA

**原理**：
- 基础模型量化到 4-bit
- LoRA 部分保持 16-bit
- 进一步降低显存

### 4. 什么时候用

| 场景 | 方案 |
|------|------|
| 快速适配新任务 | LoRA |
| 显存有限 | QLoRA |
| 需要最佳效果 | 全量微调 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LoRA 论文 | https://arxiv.org/abs/2106.09685 |
| QLoRA 论文 | https://arxiv.org/abs/2305.14314 |
| PEFT 文档 | https://huggingface.co/docs/peft/ |

---

## 🧠 学习深度

### 只需理解（L2）
- [ ] LoRA 原理
- [ ] QLoRA 原理
- [ ] 什么时候用

---

## 💻 今日编码任务

### 文件结构

```
day46-lora-qlora/
├── README.md
├── lora_demo.py             # LoRA 原理演示
├── requirements.txt
└── boss-answer.md
```

### Task: lora_demo.py（60min）

演示 LoRA 原理

---

## 🐉 今日 Boss

1. **全量微调的问题？**
2. **LoRA 的原理？**
3. **LoRA 和 QLoRA 的区别？**

---

## 🎤 面试题

1. **什么时候用 LoRA？**
2. **LoRA 的优缺点？**
3. **QLoRA 的优势？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| lora_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 47: SFT / DPO**
