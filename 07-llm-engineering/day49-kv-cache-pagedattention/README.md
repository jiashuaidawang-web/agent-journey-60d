# Day 49: KV Cache / PagedAttention（推理优化）

> **今日目标**: 深入理解 KV Cache 和 PagedAttention
> **核心问题**: 为什么需要 KV Cache？

---

## 🎯 今日目标

1. 理解 KV Cache 原理
2. 理解 PagedAttention 原理
3. 理解 Prefix Caching
4. 理解推理优化的整体思路

---

## 📚 必学知识

### 1. KV Cache

**问题**：生成式模型每生成一个 token 都要计算所有历史 token 的 Attention

**解决**：缓存已计算的 Key 和 Value

```
生成 token_n 时：
- 使用缓存的 KV（token_1 到 token_n-1）
- 只计算 token_n 的 KV
- 避免重复计算
```

### 2. PagedAttention

- 传统 KV Cache 是连续的，容易产生显存碎片
- PagedAttention 将 KV Cache 分页管理
- 类似操作系统虚拟内存

### 3. Prefix Caching

- 多个请求可能有相同前缀（如 System Prompt）
- 缓存前缀的 KV，避免重复计算
- 显著提高吞吐量

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| PagedAttention 论文 | https://arxiv.org/abs/2309.17453 |
| vLLM 博客 | https://blog.vllm.ai/ |

---

## 🧠 学习深度

### 只需理解（L2）
- [ ] KV Cache 原理
- [ ] PagedAttention 原理
- [ ] Prefix Caching

---

## 💻 今日编码任务

### 文件结构

```
day49-kv-cache-pagedattention/
├── README.md
├── kv_cache_demo.py         # KV Cache 演示
├── requirements.txt
└── boss-answer.md
```

### Task: kv_cache_demo.py（60min）

演示 KV Cache 原理

---

## 🐉 今日 Boss

1. **KV Cache 的作用？**
2. **PagedAttention 的优势？**
3. **Prefix Caching 的原理？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| kv_cache_demo.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 50: Model Gateway / Model Router**
