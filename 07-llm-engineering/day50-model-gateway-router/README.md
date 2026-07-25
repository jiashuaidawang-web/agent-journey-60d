# Day 50: Model Gateway / Model Router（模型网关）

> **今日目标**: 实现模型路由和网关
> **核心问题**: 如何根据成本/延迟/能力选择模型？

---

## 🎯 今日目标

1. 理解模型路由的价值
2. 实现 Model Router
3. 实现 Model Gateway
4. 理解成本优化策略

---

## 📚 必学知识

### 1. 为什么需要模型路由？

| 模型 | 成本 | 延迟 | 能力 |
|------|------|------|------|
| GPT-4o | 高 | 慢 | 强 |
| GPT-4o-mini | 低 | 快 | 中 |
| DeepSeek | 很低 | 快 | 中 |

**问题**：不同任务需要不同模型

### 2. 路由策略

| 策略 | 说明 |
|------|------|
| Cost-based | 根据成本选择 |
| Latency-based | 根据延迟选择 |
| Capability-based | 根据能力选择 |
| Hybrid | 混合策略 |

### 3. Model Gateway

- 统一入口
- 自动路由
- 失败降级
- 成本统计

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LiteLLM | https://docs.litellm.ai/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 模型路由策略
- [ ] Model Gateway 设计

---

## 💻 今日编码任务

### 文件结构

```
day50-model-gateway-router/
├── README.md
├── LEARNING_FLOW.md            # 学习流程
├── 00_model_router.py          # 模型路由
├── requirements.txt
└── 99-boss-answer.md
```

### Task: 00_model_router.py（90min）

实现模型路由

---

## 🐉 今日 Boss

1. **为什么需要模型路由？**
2. **路由策略有哪些？**
3. **如何实现失败降级？**

---

## 🎤 面试题

1. **如何优化 Agent 系统的成本？**
2. **模型路由的设计？**
3. **如何实现模型降级？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| model_router.py | 80分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**通关后，LLM Engineering 毕业！进入下一章：Final Projects**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释模型路由策略的设计思路
- 解释 Model Gateway 与 API Gateway 的区别
- 帮你调试路由逻辑的代码报错
- 对比不同路由策略的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我了解 API Gateway 的设计，请用 Nginx 反向代理类比解释一下 Model Router 的路由策略，然后给一个最小示例。"

### 错误用法
> "帮我写一个完整的 Model Gateway 系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
07-llm-engineering/
└── day50-model-gateway-router/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_model_router.py   # 模型路由
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 50 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Model Router | ... | ... |
| Model Gateway | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 07-llm-engineering/day50-model-gateway-router/
git commit -m "feat(day50): Model Gateway/Router - 模型网关与路由完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LiteLLM 文档（docs.litellm.ai）
- [ ] 写了 00_model_router.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
