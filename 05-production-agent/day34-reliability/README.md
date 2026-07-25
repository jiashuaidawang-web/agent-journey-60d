# Day 34: Reliability（可靠性）

> **今日目标**: 实现 Agent 系统的可靠性保障
> **核心问题**: 如何保证 Agent 系统稳定运行？

---

## 🎯 今日目标

1. 实现 Retry 机制
2. 实现 Circuit Breaker
3. 实现 Timeout 控制
4. 实现 Idempotency

---

## 📚 必学知识

### 1. Retry 机制

- 失败后自动重试
- 指数退避（Exponential Backoff）
- 最大重试次数限制

### 2. Circuit Breaker

- 连续失败后断开
- 防止雪崩
- 三种状态：Closed、Open、Half-Open

### 3. Timeout

- 单次调用超时
- 整体流程超时
- 防止无限等待

### 4. Java 类比

| 概念 | Java 实现 |
|------|-----------|
| Retry | Spring Retry / Resilience4j Retry |
| Circuit Breaker | Resilience4j CircuitBreaker |
| Timeout | @Transactional(timeout) |
| Idempotency | 幂等性设计 |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Resilience4j | https://resilience4j.readme.io/ |
| Spring Retry | https://docs.spring.io/spring-retry/docs/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Retry 机制
- [ ] Circuit Breaker
- [ ] Timeout 控制

---

## 💻 今日编码任务

### 文件结构

```
day34-reliability/
├── README.md
├── 00_retry_demo.py            # Retry 机制 + Circuit Breaker
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: retry_demo.py（60min）

实现 Retry 机制

### Task 2: circuit_breaker.py（45min）

实现 Circuit Breaker

---

## 🐉 今日 Boss

1. **Retry 机制的关键参数？**
2. **Circuit Breaker 的三种状态？**
3. **如何实现幂等性？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| retry_demo.py | 50分 |
| circuit_breaker.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 35: Async + MQ**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Retry 和 Circuit Breaker 的核心概念
- 解释指数退避的实现原理
- 帮你调试代码报错
- 对比 Resilience4j 和 Python 实现的异同

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 经验，对 Python 的装饰器和重试机制不太熟。请用 Java 的 Resilience4j 类比解释一下 Retry 和 Circuit Breaker，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Agent 可靠性保障系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
05-production-agent/
└── day34-reliability/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_retry_demo.py     # Retry + Circuit Breaker
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 34 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Retry | ... | ... |
| Circuit Breaker | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 05-production-agent/day34-reliability/
git commit -m "feat(day34): Reliability - Retry 和 Circuit Breaker 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Resilience4j 官方文档
- [ ] 写了 00_retry_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
