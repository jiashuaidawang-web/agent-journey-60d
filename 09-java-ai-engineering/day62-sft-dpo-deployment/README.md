# Day 62: SFT/DPO + 微调部署

> **今日目标**: 掌握 SFT/DPO 微调方法，以及微调模型的部署与最佳实践
> **核心问题**: SFT 和 DPO 有什么区别？微调后的模型如何部署到生产环境？

---

## 🎯 今日目标

1. 理解监督微调 SFT 原理与流程
2. 理解偏好对齐 DPO 原理
3. 掌握微调模型评估指标（BLEU/ROUGE/人工评估）
4. 掌握微调模型部署与使用（vLLM/OLLAMA 部署）
5. 掌握企业级微调最佳实践（成本控制/效果监控）
6. 掌握 LoRA 模型合并与导出

---

## 📚 必学知识

### 1. 监督微调 SFT 原理与流程

**SFT（Supervised Fine-Tuning）**：
- 最常用的微调方法
- 使用标注的"指令-回答"数据训练
- 目标是让模型学会遵循指令

**SFT 流程**：
```
数据准备 → 模型选择 → 训练配置 → SFT 训练 → 模型评估
```

**SFT 训练细节**：
- 输入：instruction + input
- 目标：output（计算 loss 时只计算 output 部分）
- 损失函数：CrossEntropyLoss
- 训练目标：最小化模型输出与标注回答的差异

**SFT 数据格式**：
```json
{
    "instruction": "翻译成英文",
    "input": "你好世界",
    "output": "Hello World"
}
```

**SFT 的局限性**：
- 需要大量标注数据
- 模型可能过拟合标注风格
- 无法处理"多个回答哪个更好"的情况

### 2. 偏好对齐 DPO 原理

**DPO（Direct Preference Optimization）**：
- 2023 年提出的偏好对齐方法
- 不需要训练奖励模型（Reward Model）
- 直接使用偏好数据优化模型

**DPO vs RLHF**：

| 维度 | RLHF | DPO |
|------|------|-----|
| 步骤 | 训练 RM → PPO 训练 | 直接优化 |
| 复杂度 | 高 | 低 |
| 稳定性 | 差（PPO 不稳定） | 好 |
| 数据需求 | 偏好对 | 偏好对 |
| 效果 | 好 | 接近 RLHF |

**DPO 数学原理**：
- 目标函数：最大化偏好回答的概率，最小化非偏好回答的概率
- 损失函数：
  $$\mathcal{L}_{DPO} = -\mathbb{E}\left[\log\sigma\left(\beta\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]$$
- $y_w$：偏好回答（win）
- $y_l$：非偏好回答（lose）
- $\pi_{ref}$：参考模型（SFT 模型）
- $\pi_\theta$：当前训练模型

**DPO 数据格式**：
```json
{
    "prompt": "翻译成英文：你好世界",
    "chosen": "Hello World",
    "rejected": "Hi World"
}
```

### 3. 微调模型评估指标

**自动指标**：

| 指标 | 适用场景 | 说明 |
|------|----------|------|
| **BLEU** | 机器翻译 | n-gram 精确率，0-100 分 |
| **ROUGE** | 文本摘要 | n-gram 召回率，0-100 分 |
| **Perplexity** | 语言模型 | 困惑度，越低越好 |
| **Accuracy** | 分类任务 | 准确率 |

**人工评估**：
- **流畅度**：生成文本是否通顺（1-5 分）
- **相关性**：是否回答了问题（1-5 分）
- **准确性**：信息是否准确（1-5 分）
- **一致性**：是否与上下文一致（1-5 分）

**评估方法**：
- 单轮评估：给定输入，评估输出
- 多轮评估：模拟多轮对话
- 对比评估：微调模型 vs 基座模型 vs GPT-4

### 4. 微调模型部署（vLLM/OLLAMA）

**vLLM 部署**：
- 高性能推理引擎
- 支持 PagedAttention（分页注意力）
- 支持 Tensor Parallelism（张量并行）
- 适合高并发场景

**vLLM 部署步骤**：
1. 合并 LoRA 权重到基座模型
2. 导出为 Hugging Face 格式
3. 启动 vLLM 服务
4. 通过 OpenAI 兼容 API 调用

**OLLAMA 部署**：
- 轻量级本地部署工具
- 支持 Mac/Windows/Linux
- 一键拉取和运行模型
- 适合本地开发和小规模部署

**OLLAMA 部署步骤**：
1. 安装 OLLAMA
2. 创建 Modelfile
3. 导入模型
4. 运行模型

### 5. 企业级微调最佳实践

**成本控制**：
- 使用 LoRA/QLoRA 降低训练成本
- 选择合适规模的基座模型（7B/13B/70B）
- 使用 Spot 实例降低 GPU 成本
- 数据质量 > 数据数量

**效果监控**：
- 训练过程中监控 loss 曲线
- 定期评估模型效果
- A/B 测试对比新旧模型
- 收集用户反馈

**安全合规**：
- 数据隐私保护
- 模型输出审核
- 防止有害内容生成
- 记录审计日志

### 6. LoRA 模型合并与导出

**为什么需要合并？**
- LoRA 权重是增量（$\Delta W$），不是完整权重
- 部署时需要将 LoRA 合并到基座模型
- 合并后可以直接部署，无需 PEFT 库

**合并方法**：
```python
from peft import PeftModel

# 加载基座模型
model = AutoModelForCausalLM.from_pretrained(base_model)

# 加载 LoRA 权重
model = PeftModel.from_pretrained(model, lora_path)

# 合并权重
model = model.merge_and_unload()

# 保存合并后的模型
model.save_pretrained(merged_path)
```

**导出格式**：
- Hugging Face 格式（safetensors）
- GGUF 格式（OLLAMA 使用）
- ONNX 格式（跨平台部署）

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| SFT 教程 | https://huggingface.co/docs/trl/en/sft_trainer |
| DPO 论文 | https://arxiv.org/abs/2305.18290 |
| DPO 教程 | https://huggingface.co/docs/trl/en/dpo_trainer |
| vLLM 文档 | https://docs.vllm.ai/ |
| OLLAMA 文档 | https://github.com/ollama/ollama |
| TRL 库 | https://github.com/huggingface/trl |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] SFT 原理与流程
- [ ] DPO 原理与流程
- [ ] SFT vs DPO 的区别
- [ ] 微调模型评估指标
- [ ] vLLM 部署方法
- [ ] OLLAMA 部署方法
- [ ] LoRA 模型合并与导出

### 只需理解（L2）
- [ ] DPO 的数学推导
- [ ] BLEU/ROUGE 的计算方法
- [ ] vLLM 的 PagedAttention 原理
- [ ] 企业级最佳实践

### 今天不深入（后面会讲）
- [ ] RLHF 完整流程
- [ ] 多轮对话评估
- [ ] 模型量化部署（GPTQ/AWQ）
- [ ] 模型安全对齐

---

## 💻 今日编码任务

### 文件结构

```
day62-sft-dpo-deployment/
├── README.md
├── LEARNING_FLOW.md
├── 00_sft_training.py            # SFT 训练
├── 00_sft_dpo.py                 # SFT + DPO 训练
├── 01_model_evaluation.py        # 模型评估
├── 02_model_deployment.py        # 模型部署
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_sft_training.py（45min）

实现 SFT 训练：
- 加载预训练模型
- 准备 SFT 数据
- 配置训练参数
- 执行 SFT 训练

**验收标准**：
```bash
python 00_sft_training.py
# 输出：
# 🚀 SFT 训练开始
# 📊 Epoch 1/3 - Loss: 1.234
# 📊 Epoch 2/3 - Loss: 0.987
# 📊 Epoch 3/3 - Loss: 0.876
# 💾 SFT 模型已保存
```

### Task 2: 00_sft_dpo.py（45min）

实现 SFT + DPO 训练：
- 先 SFT 训练
- 再 DPO 偏好对齐
- 对比 SFT 和 SFT+DPO 的效果

**验收标准**：
```bash
python 00_sft_dpo.py
# 输出：
# 🚀 SFT 训练完成
# 🎯 DPO 训练开始
# 📊 DPO Epoch 1/3 - Loss: 0.654
# 📊 DPO Epoch 2/3 - Loss: 0.543
# 📊 DPO Epoch 3/3 - Loss: 0.432
# 💾 DPO 模型已保存
```

### Task 3: 01_model_evaluation.py（30min）

实现模型评估：
- 加载测试集
- 计算 BLEU/ROUGE 指标
- 输出评估报告

**验收标准**：
```bash
python 01_model_evaluation.py
# 输出：
# 📊 模型评估报告
# | 指标 | 基座模型 | SFT 模型 | SFT+DPO |
# |------|----------|----------|---------|
# | BLEU | 15.2 | 28.5 | 32.1 |
# | ROUGE| 35.4 | 52.3 | 58.7 |
```

### Task 4: 02_model_deployment.py（30min）

演示模型部署：
- 合并 LoRA 权重
- 导出模型
- 演示 vLLM/OLLAMA 部署

**验收标准**：
```bash
python 02_model_deployment.py
# 输出：
# 📦 合并 LoRA 权重
# 💾 导出模型到: ./merged_model
# 🚀 启动 vLLM 服务: http://localhost:8000
# ✅ 部署成功
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 SFT 和 DPO 的原理
- 解释 TRL 库的用法
- 帮你调试代码报错
- 对比 SFT vs DPO 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有深度学习基础，DPO 的数学原理我不太熟。请用 RLHF 对比解释 DPO 的优势，然后给我一个 TRL 库的 DPO 训练示例。"

### 错误用法
> "帮我写一个完整的 SFT+DPO 训练脚本。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day62-sft-dpo-deployment/
    ├── README.md                    # 学习总结
    ├── LEARNING_FLOW.md             # 学习流程
    ├── 00_sft_training.py           # SFT 训练
    ├── 00_sft_dpo.py                # SFT + DPO 训练
    ├── 01_model_evaluation.py       # 模型评估
    ├── 02_model_deployment.py       # 模型部署
    ├── requirements.txt
    └── 99-boss-answer.md            # Boss 答案
```

### README.md 必须包含
```markdown
# Day 62 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| SFT | ... | ... |
| DPO | ... | ... |
| vLLM | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day62-sft-dpo-deployment/
git commit -m "feat(day62): SFT/DPO + 微调部署 - 训练/评估/部署完成"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **SFT 的原理是什么？它有什么局限性？**
2. **DPO 和 RLHF 有什么区别？DPO 的优势是什么？**
3. **微调模型的评估指标有哪些？各适用于什么场景？**
4. **vLLM 和 OLLAMA 部署有什么区别？各自适合什么场景？**
5. **企业级微调有哪些最佳实践？**

### 验收标准
- 每个答案 **不少于50字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **SFT 和 DPO 的区别是什么？**
2. **DPO 为什么不需要训练奖励模型？**
3. **BLEU 和 ROUGE 分别适用于什么场景？**
4. **vLLM 的 PagedAttention 是什么？**
5. **LoRA 模型如何合并和导出？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_sft_training.py | 20分 | 能运行 + SFT 训练 |
| 00_sft_dpo.py | 20分 | 能运行 + DPO 训练 |
| 01_model_evaluation.py | 15分 | 能运行 + 评估指标 |
| 02_model_deployment.py | 15分 | 能运行 + 部署演示 |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 20分 | 5题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 63: Multimodal Agent**

---

## 📊 今日检查清单

- [ ] 读了 SFT 教程
- [ ] 读了 DPO 论文（或中文解读）
- [ ] 读了 vLLM 文档
- [ ] 读了 OLLAMA 文档
- [ ] 写了 00_sft_training.py
- [ ] 写了 00_sft_dpo.py
- [ ] 写了 01_model_evaluation.py
- [ ] 写了 02_model_deployment.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
