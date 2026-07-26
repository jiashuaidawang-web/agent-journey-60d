# Day 58: Spring AI Advisor 责任链 - 学习流程

> **今日目标**: 掌握 Spring AI Advisor 责任链机制，能实现日志/安全/限流/审计/动态切模型等自定义 Advisor
> **核心问题**: Advisor 如何实现拦截器模式？它与 Java Filter / Interceptor / AOP 有什么区别？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 浏览 Spring AI Advisor 文档（10分钟）
    ↓ 理解：Advisor 责任链原理
Step 4: 运行 00_advisor_chain.py（15分钟）
    ↓ 理解：责任链基础
Step 5: 运行 01_logging_advisor.py（15分钟）
    ↓ 理解：日志 Advisor
Step 6: 运行 02_security_advisor.py（15分钟）
    ↓ 理解：安全 Advisor
Step 7: 运行 03_model_router_advisor.py（15分钟）
    ↓ 理解：动态切模型
Step 8: 完成 99_boss_answer.md（30分钟）
    ↓
Step 9: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 浏览官方文档 | 10min |
| 4-7 | 4个代码文件 | 60min |
| 8 | Boss 问题 | 30min |
| 9 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Advisor 责任链工作流
- [ ] 实现自定义 Advisor
- [ ] 实现日志 / 安全 / 限流 / 审计 Advisor
- [ ] 实现动态切模型 Advisor
- [ ] 与 Filter / Interceptor / AOP 类比
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_advisor_chain.py](00_advisor_chain.py) | 责任链基础 | ⭐ |
| [01_logging_advisor.py](01_logging_advisor.py) | 日志 Advisor | ⭐⭐ |
| [02_security_advisor.py](02_security_advisor.py) | 安全 Advisor | ⭐⭐ |
| [03_model_router_advisor.py](03_model_router_advisor.py) | 动态切模型 | ⭐⭐⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐ |
