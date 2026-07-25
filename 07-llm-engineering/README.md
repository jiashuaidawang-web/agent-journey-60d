# 07-llm-engineering · Day 46-52 执行版 v3.0

> **定位**: LLM Engineering —— P2 快速过，理解原理和选型
> **目标**: 知道什么时候用、怎么用，不深入训练代码

---

## 7天总览

```
Day 46  LoRA / QLoRA（高效参数微调）
Day 47  SFT / DPO（监督微调 / 偏好对齐）
Day 48  vLLM（推理加速框架）
Day 49  KV Cache / PagedAttention（推理优化）
Day 50  Model Gateway / Model Router（模型网关）
```

## 学习策略

**P2 快速过**：
- 理解原理（是什么、为什么）
- 知道选型（什么时候用）
- 不深入训练代码（不是训练工程师）

**面试重点**：
- Prompt / RAG / SFT / DPO 的选型
- 推理优化的原理
- 模型路由的设计

## 核心技术栈

| 技术 | 用途 | 深度 |
|------|------|------|
| LoRA / QLoRA | 高效微调 | L2 |
| SFT / DPO | 微调和对齐 | L2 |
| vLLM | 推理加速 | L2-L3 |
| KV Cache / PagedAttention | 推理优化 | L2 |
| Model Router | 模型路由 | L3 |

## Java 类比

| 概念 | Java 类比 |
|------|-----------|
| LoRA | 增量更新（只改部分代码） |
| SFT | 带答案的学习 |
| DPO | 对比学习（哪个好哪个差） |
| vLLM | 高性能 Web 服务器 |
| KV Cache | 缓存（避免重复计算） |
| Model Router | 负载均衡器 |

---

**准备好了吗？从 Day 46 开始 LLM Engineering 快速过。**
