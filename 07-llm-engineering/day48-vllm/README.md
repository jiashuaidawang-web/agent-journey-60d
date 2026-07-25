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
├── LEARNING_FLOW.md            # 学习流程
├── 00_vllm_demo.py             # vLLM 演示
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_vllm_demo.py（60min）

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

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 vLLM 推理加速的核心优化原理
- 解释 PagedAttention 与操作系统虚拟内存的类比
- 帮你调试 vLLM 部署报错
- 对比 vLLM 与其他推理框架的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我了解操作系统虚拟内存分页，请用这个类比解释一下 PagedAttention 如何管理 KV Cache 并避免显存碎片。"

### 错误用法
> "帮我写一个完整的 vLLM 推理服务。"

---

## 📝 GitHub 提交规范

### 提交结构
```
07-llm-engineering/
└── day48-vllm/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_vllm_demo.py      # vLLM 演示
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 48 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| PagedAttention | ... | ... |
| Continuous Batching | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 07-llm-engineering/day48-vllm/
git commit -m "feat(day48): vLLM - 推理加速框架原理完成"
```

---

## 📊 今日检查清单

- [ ] 读了 vLLM 文档（docs.vllm.ai）
- [ ] 读了 vLLM GitHub（github.com/vllm-project/vllm）
- [ ] 写了 00_vllm_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
