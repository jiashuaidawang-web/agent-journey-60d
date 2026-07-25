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
├── retry_demo.py            # Retry 机制
├── circuit_breaker.py       # Circuit Breaker
├── requirements.txt
└── boss-answer.md
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
