# Day 48: vLLM（推理加速框架）

> **今日目标**: 理解 vLLM 原理和使用
> **核心问题**: vLLM 如何加速推理？

---

## 🎯 今日目标

1. 理解推理加速的必要性
2. 理解 vLLM 核心优化
3. 理解 PagedAttention
4. 知道如何部署

---

## 📚 必学知识

### 1. 推理加速的必要性

- LLM 推理慢（生成式，逐 token）
- 高并发场景需要加速
- 降低成本

### 2. vLLM 核心优化

| 优化 | 说明 |
|------|------|
| PagedAttention | 分页管理 KV Cache |
| Continuous Batching | 连续批处理 |
| Prefix Caching | 前缀缓存 |
| Tensor Parallelism | 张量并行 |

### 3. PagedAttention

- 将 KV Cache 分页管理
- 避免显存碎片
- 提高显存利用率

### 4. 部署方式

```bash
# 启动 vLLM 服务
python -m vllm.entrypoints.openai.api_server \
    --model Qwen2.5-7B \
    --port 8000
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| vLLM 文档 | https://docs.vllm.ai/ |
| vLLM GitHub | https://github.com/vllm-project/vllm |

---

## 🧠 学习深度

### 只需理解（L2）
- [ ] vLLM 核心优化
- [ ] PagedAttention 原理

---

## 💻 今日编码任务

### 文件结构

```
day48-vllm/
├── README.md
├── vllm_demo.py             # vLLM 演示
├── requirements.txt
└── boss-answer.md
```

### Task: vllm_demo.py（60min）

演示 vLLM 使用

---

## 🐉 今日 Boss

1. **vLLM 的核心优化？**
2. **PagedAttention 的原理？**
3. **Continuous Batching 的优势？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| vllm_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 49: KV Cache / PagedAttention**
