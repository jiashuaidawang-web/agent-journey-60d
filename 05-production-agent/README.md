# 05-production-agent · Day 32-38 执行版 v3.0

> **定位**: Production Agent —— 你的 Java 优势真正发力的地方
> **目标**: 从 Observability 到 Agent Platform 生产级能力全链路

---

## 7天总览

```
Day 32  Observability（可观测性）
Day 33  Security（安全）
Day 34  Reliability（可靠性）
Day 35  Async + MQ（异步 + 消息队列）
Day 36  Java Control Plane（Java 控制平面） ★ 你的优势
Day 37  Multi-tenant（多租户）
Day 38  Agent Platform（Agent 平台架构）
```

## 为什么这是你发力的地方？

```
3年LLM工程师的优势：训练、微调、底层算法
你的优势：        Java + 分布式 + 高并发 + 生产稳定性 + Agent编排

面试时：
  他们讲"我做了CPT+SFT+DPO"
  你讲"我设计了一个Agent平台，Java控制平面+Python AI服务，
       支持多租户、断点续跑、成本路由、全链路追踪"
  
  后者的岗位 = Senior Agent Engineer / Agent Platform Architect
```

## 核心技术栈

| 技术 | 用途 | 深度 |
|------|------|------|
| LangSmith / Phoenix | 追踪和监控 | L3 |
| OpenTelemetry | 分布式追踪 | L2 |
| Prompt Injection 防护 | 安全 | L3 |
| Retry / Circuit Breaker | 可靠性 | L3 |
| RocketMQ / Kafka | 消息队列 | L3 |
| Spring Boot | Java 控制平面 | L4 |
| 多租户隔离 | 资源隔离 | L4 |

## Java 类比

| 概念 | Java 实现 |
|------|-----------|
| Observability | Micrometer + Prometheus + Grafana |
| Security | Spring Security + JWT |
| Reliability | Resilience4j + Retry |
| MQ | RocketMQ / Kafka |
| Control Plane | Spring Boot + Spring Cloud |
| Multi-tenant | TenantContext + 数据隔离 |

---

**准备好了吗？从 Day 32 开始 Production Agent 闯关。**
