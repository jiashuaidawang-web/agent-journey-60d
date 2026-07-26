# Day 61: LoRA/QLoRA 微调实战

> **今日目标**: 掌握 LoRA/QLoRA 微调的核心理论和实战流程
> **核心问题**: 为什么 LoRA 能高效微调大模型？QLoRA 又是如何进一步降低显存的？

---

## 🎯 今日目标

1. 理解 LoRA 核心理论与数学原理（低秩分解）
2. 掌握微调流程全解析（数据准备→模型选择→训练→评估）
3. 掌握微调数据获取策略（开源数据集/自定义数据）
4. 掌握数据清洗与预处理
5. 掌握微调关键参数详解（learning rate/batch size/epochs/LoRA rank/alpha）
6. 理解 QLoRA 量化微调
7. 掌握 LoRA 实现（PyTorch + PEFT）
8. 掌握微调模型评估与优化

---

## 📚 必学知识

### 1. LoRA 核心理论与数学原理

**LoRA（Low-Rank Adaptation）**：
- 微软 2021 年提出的高效微调方法
- 核心思想：**低秩分解**（Low-Rank Decomposition）
- 不修改原始模型参数，而是注入可训练的低秩矩阵

**数学原理**：
- 原始权重矩阵 $W \in \mathbb{R}^{d \times k}$
- LoRA 引入两个低秩矩阵：$A \in \mathbb{R}^{r \times k}$，$B \in \mathbb{R}^{d \times r}$
- 其中 $r \ll \min(d, k)$（秩远小于原始维度）
- 前向传播：$h = Wx + BAx$（$W$ 冻结，$A$ 和 $B$ 可训练）
- 参数量从 $d \times k$ 降到 $r \times (d + k)$

**为什么有效？**
- 大模型是过参数化的，权重变化集中在低维子空间
- 低秩近似足以捕获任务相关的变化
- 实验表明 $r=8$ 或 $r=16$ 就能达到全量微调 90%+ 的效果

### 2. 微调流程全解析

**标准微调流程**：
```
数据准备 → 模型选择 → 训练配置 → 训练执行 → 模型评估 → 部署上线
```

**各阶段详解**：
1. **数据准备**：收集、清洗、格式化数据
2. **模型选择**：选择预训练基座模型
3. **训练配置**：设置 LoRA 参数、学习率、批次大小等
4. **训练执行**：运行训练循环
5. **模型评估**：评估生成质量
6. **部署上线**：合并权重、导出、部署

### 3. 微调数据获取策略

**开源数据集**：
- **Alpaca**：52K 条指令数据
- **ShareGPT**：真实对话数据
- **OpenAssistant**：多轮对话
- **Chinese-LLaMA-Alpaca**：中文指令数据
- **bellkeat/alpaca-gpt4-data**：GPT-4 生成的高质量数据

**自定义数据**：
- 从业务日志提取
- 人工标注
- LLM 辅助生成（Self-Instruct）
- 数据增强（回译、改写）

**数据格式**：
```json
{
    "instruction": "翻译成英文",
    "input": "你好世界",
    "output": "Hello World"
}
```

### 4. 数据清洗与预处理

**清洗步骤**：
1. **去重**：删除重复样本
2. **去噪**：删除低质量、乱码、广告
3. **长度过滤**：删除过长或过短样本
4. **格式统一**：统一数据格式
5. **质量评分**：使用规则或模型评分，过滤低质量

**预处理**：
- Tokenization
- 添加特殊 token（BOS、EOS）
- 构建输入-输出对
- 按 max_length 截断或填充

### 5. 微调关键参数详解

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| learning rate | 学习率 | 1e-4 ~ 5e-4 |
| batch size | 批次大小 | 8 ~ 32 |
| epochs | 训练轮数 | 3 ~ 10 |
| LoRA rank (r) | 低秩维度 | 8 ~ 64 |
| LoRA alpha | 缩放因子 | 通常 = rank |
| LoRA dropout | Dropout 率 | 0.05 ~ 0.1 |
| target_modules | 应用 LoRA 的层 | q_proj, v_proj |
| max_length | 最大序列长度 | 512 ~ 2048 |

**参数关系**：
- `scaling = alpha / rank`，控制 LoRA 更新的强度
- rank 越大，表达能力越强，但参数量越多
- learning rate 通常比全量微调大 10-100 倍

### 6. QLoRA 量化微调

**QLoRA（Quantized LoRA）**：
- 2023 年提出，进一步降低显存
- 核心：4-bit 量化基座模型 + LoRA 微调
- 显存降低 3 倍，性能损失 < 1%

**关键技术**：
1. **4-bit NormalFloat（NF4）**：非均匀量化，适合正态分布权重
2. **Double Quantization**：量化常数再量化，进一步节省显存
3. **Paged Optimizers**：分页优化器，防止梯度检查点尖峰OOM

**对比**：

| 方法 | 显存（7B 模型） | 性能 |
|------|-----------------|------|
| 全量微调 | ~100GB | 100% |
| LoRA | ~20GB | ~95% |
| QLoRA | ~6GB | ~94% |

### 7. LoRA 实现（PyTorch + PEFT）

**PEFT（Parameter-Efficient Fine-Tuning）**：
- Hugging Face 提供的微调库
- 支持 LoRA、QLoRA、Prefix Tuning 等方法
- 与 Transformers 无缝集成

**核心代码**：
```python
from peft import LoraConfig, get_peft_model, TaskType

config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"]
)
model = get_peft_model(model, config)
```

### 8. 微调模型评估与优化

**评估指标**：
- **BLEU**：机器翻译质量
- **ROUGE**：文本摘要质量
- **人工评估**：主观评分（1-5 分）
- **任务指标**：准确率、召回率、F1

**优化策略**：
- 调整 LoRA rank 和 alpha
- 增加训练数据
- 调整学习率和 batch size
- 使用更好的基座模型
- 数据增强

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LoRA 论文 | https://arxiv.org/abs/2106.09685 |
| QLoRA 论文 | https://arxiv.org/abs/2305.14314 |
| PEFT 官方文档 | https://huggingface.co/docs/peft/ |
| Hugging Face Transformers | https://huggingface.co/docs/transformers/ |
| LLaMA-Factory | https://github.com/hiyouga/LLaMA-Factory |
| Alpaca 数据集 | https://huggingface.co/datasets/tatsu-lab/alpaca |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] LoRA 核心理论与数学原理（低秩分解）
- [ ] 微调流程全解析
- [ ] 数据获取策略
- [ ] 数据清洗与预处理
- [ ] 微调关键参数详解
- [ ] QLoRA 量化微调原理
- [ ] PEFT 库的使用

### 只需理解（L2）
- [ ] LoRA 的数学推导细节
- [ ] QLoRA 的量化实现细节
- [ ] 评估指标的计算方法
- [ ] 优化策略的选择

### 今天不深入（后面会讲）
- [ ] Prefix Tuning
- [ ] Adapter Tuning
- [ ] RLHF 强化学习
- [ ] DPO 偏好对齐

---

## 💻 今日编码任务

### 文件结构

```
day61-lora-qlora/
├── README.md
├── LEARNING_FLOW.md
├── 00_lora_theory.py             # LoRA 数学原理可视化
├── 01_data_preparation.py         # 数据准备
├── 02_lora_training.py            # LoRA 训练
├── 03_qlora_demo.py               # QLoRA 量化演示
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_lora_theory.py（45min）

可视化 LoRA 数学原理：
- 模拟权重矩阵 $W$
- 生成低秩矩阵 $A$ 和 $B$
- 计算 $BA$ 并可视化
- 对比参数量

**验收标准**：
```bash
python 00_lora_theory.py
# 输出：
# 📐 LoRA 数学原理可视化
# 📊 原始权重矩阵 W: 1024x1024 = 1,048,576 参数
# 📊 LoRA 矩阵 A: 16x1024 = 16,384 参数
# 📊 LoRA 矩阵 B: 1024x16 = 16,384 参数
# 📊 压缩率: 96.9%
```

### Task 2: 01_data_preparation.py（45min）

实现数据准备：
- 加载开源数据集（Alpaca）
- 数据清洗（去重、去噪、长度过滤）
- 格式统一
- 保存处理后的数据

**验收标准**：
```bash
python 01_data_preparation.py
# 输出：
# 📦 加载数据集: 52002 条
# 🧹 去重后: 51800 条
# 🧹 去噪后: 51500 条
# 🧹 长度过滤后: 50000 条
# 💾 保存到: processed_data.json
```

### Task 3: 02_lora_training.py（60min）

实现 LoRA 训练：
- 加载预训练模型
- 配置 LoRA 参数
- 训练循环
- 保存 LoRA 权重

**验收标准**：
```bash
python 02_lora_training.py
# 输出：
# 🚀 开始 LoRA 训练
# 📊 Epoch 1/3 - Loss: 1.234
# 📊 Epoch 2/3 - Loss: 0.987
# 📊 Epoch 3/3 - Loss: 0.876
# 💾 LoRA 权重已保存
```

### Task 4: 03_qlora_demo.py（45min）

演示 QLoRA 量化：
- 模拟 4-bit 量化
- 对比 FP16 和 4-bit 的显存占用
- 演示 QLoRA 训练流程

**验收标准**：
```bash
python 03_qlora_demo.py
# 输出：
# 🔢 QLoRA 量化演示
# 📊 FP16 显存: 14.0 GB
# 📊 4-bit 显存: 3.5 GB
# 📊 显存节省: 75%
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 LoRA 的数学原理
- 解释 PEFT 库的用法
- 帮你调试代码报错
- 对比 LoRA 和 QLoRA 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有深度学习基础，LoRA 的低秩分解我不太熟。请用 PCA 降维类比解释 LoRA 的数学原理，然后给我一个 PyTorch 实现示例。"

### 错误用法
> "帮我写一个完整的 LoRA 训练脚本。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day61-lora-qlora/
    ├── README.md                    # 学习总结
    ├── LEARNING_FLOW.md             # 学习流程
    ├── 00_lora_theory.py            # LoRA 数学原理
    ├── 01_data_preparation.py       # 数据准备
    ├── 02_lora_training.py          # LoRA 训练
    ├── 03_qlora_demo.py             # QLoRA 量化
    ├── requirements.txt
    └── 99-boss-answer.md            # Boss 答案
```

### README.md 必须包含
```markdown
# Day 61 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| LoRA | ... | ... |
| QLoRA | ... | ... |
| 低秩分解 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day61-lora-qlora/
git commit -m "feat(day61): LoRA/QLoRA 微调实战 - 原理/数据/训练/量化完成"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **LoRA 的核心思想是什么？低秩分解的数学原理是什么？**
2. **微调的关键参数有哪些？它们是如何影响训练效果的？**
3. **QLoRA 是如何进一步降低显存的？它的核心技术是什么？**
4. **微调数据应该如何获取和清洗？**
5. **如何评估微调模型的效果？**

### 验收标准
- 每个答案 **不少于50字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **LoRA 和全量微调有什么区别？**
2. **LoRA 的 rank 参数有什么作用？**
3. **QLoRA 的 4-bit 量化是如何实现的？**
4. **微调数据的质量对效果有什么影响？**
5. **如何选择合适的基座模型进行微调？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_lora_theory.py | 20分 | 能运行 + 数学原理可视化 |
| 01_data_preparation.py | 20分 | 能运行 + 数据清洗流程 |
| 02_lora_training.py | 20分 | 能运行 + LoRA 训练 |
| 03_qlora_demo.py | 15分 | 能运行 + 量化演示 |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 62: SFT/DPO + 微调部署**

---

## 📊 今日检查清单

- [ ] 读了 LoRA 论文（或中文解读）
- [ ] 读了 QLoRA 论文（或中文解读）
- [ ] 读了 PEFT 官方文档
- [ ] 写了 00_lora_theory.py
- [ ] 写了 01_data_preparation.py
- [ ] 写了 02_lora_training.py
- [ ] 写了 03_qlora_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
