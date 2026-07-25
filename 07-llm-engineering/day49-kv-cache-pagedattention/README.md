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
├── LEARNING_FLOW.md            # 学习流程
├── 00_kv_cache_demo.py         # KV Cache 演示
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_kv_cache_demo.py（60min）

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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 KV Cache 在 Attention 计算中的作用
- 解释 PagedAttention 如何提升显存利用率
- 帮你调试推理优化相关代码报错
- 对比 KV Cache / PagedAttention / Prefix Caching 的适用场景

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我了解 Transformer 的 Attention 机制，请解释一下为什么生成式模型需要 KV Cache，以及它如何把复杂度从 O(n²) 降到 O(n)。"

### 错误用法
> "帮我写一个完整的 KV Cache 推理引擎。"

---

## 📝 GitHub 提交规范

### 提交结构
```
07-llm-engineering/
└── day49-kv-cache-pagedattention/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_kv_cache_demo.py  # KV Cache 演示
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 49 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| KV Cache | ... | ... |
| PagedAttention | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 07-llm-engineering/day49-kv-cache-pagedattention/
git commit -m "feat(day49): KV Cache/PagedAttention - 推理优化原理完成"
```

---

## 📊 今日检查清单

- [ ] 读了 PagedAttention 论文（arxiv.org/abs/2309.17453）
- [ ] 读了 vLLM 博客（blog.vllm.ai）
- [ ] 写了 00_kv_cache_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
