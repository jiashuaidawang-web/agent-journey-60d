# Day 35: Async + MQ（异步 + 消息队列）

> **今日目标**: 实现 Agent 系统的异步处理
> **核心问题**: 长任务为什么要异步处理？

---

## 🎯 今日目标

1. 理解异步处理的必要性
2. 实现 Async Agent
3. 实现消息队列集成
4. 实现长任务处理

---

## 📚 必学知识

### 1. 为什么需要异步？

- Agent 执行时间长（几十秒到几分钟）
- 同步等待用户体验差
- 需要支持大量并发

### 2. 异步架构

```
用户请求 → API Gateway → MQ → Worker → 执行 Agent → 结果存储
    ↓                                  ↓
  立即返回                         轮询/WebSocket
  任务ID                           获取结果
```

### 3. 消息队列

| MQ | 特点 |
|----|------|
| RocketMQ | 阿里开源，支持事务消息 |
| Kafka | 高吞吐量 |
| RabbitMQ | 功能丰富 |

### 4. Java 实现

- Spring Boot + RocketMQ
- 异步任务：@Async
- 任务状态：Redis / MySQL

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| RocketMQ | https://rocketmq.apache.org/ |
| Spring Async | https://docs.spring.io/spring-framework/reference/integration/scheduling.html |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] 异步处理架构
- [ ] MQ 集成
- [ ] 长任务处理

---

## 💻 今日编码任务

### 文件结构

```
day35-async-mq/
├── README.md
├── async_agent.py           # 异步 Agent
├── mq_demo.py               # 消息队列
├── requirements.txt
└── boss-answer.md
```

### Task 1: async_agent.py（60min）

实现异步 Agent

### Task 2: mq_demo.py（45min）

实现消息队列集成

---

## 🐉 今日 Boss

1. **为什么 Agent 需要异步处理？**
2. **异步架构的流程？**
3. **如何实现任务状态追踪？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| async_agent.py | 50分 |
| mq_demo.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 36: Java Control Plane**
