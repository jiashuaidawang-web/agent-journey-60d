# Day 36: Java Control Plane（Java 控制平面）

> **今日目标**: 设计 Java 控制平面，发挥你的 Java 优势
> **核心问题**: 为什么 Agent 平台需要 Java 控制平面？

---

## 🎯 今日目标

1. 理解 Java 控制平面的价值
2. 设计 Java + Python 混合架构
3. 实现租户管理
4. 实现成本核算

---

## 📚 必学知识

### 1. 为什么需要 Java 控制平面？

```
Python AI Service（LLM 编排）    Java Control Plane（企业级能力）
─────────────────────────        ─────────────────────────────
LangGraph Agent                  租户管理
RAG 检索                         权限控制
LLM 调用                         成本核算
Tool Calling                     任务调度
                                 全链路追踪
                                 多租户隔离
```

**Python 擅长**：AI 编排、快速迭代
**Java 擅长**：企业级架构、稳定性、生态

### 2. Java + Python 混合架构

```
┌─────────────────────────────────────────────────────┐
│                 前端 / API Gateway                    │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│          Java Control Plane (Spring Boot)            │
│  ┌─────────┬──────────┬───────────┬──────────────┐  │
│  │ 租户管理 │ 权限鉴权  │ 任务调度   │ 成本核算      │  │
│  │ Tenant  │ Auth     │ Scheduler │ Cost Tracker │  │
│  └─────────┴──────────┴───────────┴──────────────┘  │
│  ┌─────────┬──────────┬──────────────────────────┐  │
│  │ 状态存储 │ 消息队列  │ 模型路由                 │  │
│  │ MySQL   │ RocketMQ │ Model Router             │  │
│  └─────────┴──────────┴──────────────────────────┘  │
└───────────────────────┬─────────────────────────────┘
                        │ HTTP/gRPC
┌───────────────────────▼─────────────────────────────┐
│            Python AI Service (LangGraph)             │
│  ┌──────────────────────────────────────────────┐   │
│  │           Agent Runtime (LangGraph)           │   │
│  │  ┌────────┬────────┬────────┬────────┐       │   │
│  │  │Research│ Analysis│ Writing│ Review │       │   │
│  │  │ Agent  │ Agent  │ Agent  │ Agent  │       │   │
│  │  └────────┴────────┴────────┴────────┘       │   │
│  └──────────────────────────────────────────────┘   │
│  ┌─────────┬──────────┬───────────┬──────────────┐  │
│  │  RAG    │  MCP     │  Skill    │  Evaluation  │  │
│  │ 混合检索 │ 工具协议  │  技能库   │  评测        │  │
│  └─────────┴──────────┴───────────┴──────────────┘  │
└─────────────────────────────────────────────────────┘
```

### 3. Spring AI

- Spring 官方的 AI 框架
- 支持 OpenAI、Ollama、Anthropic 等
- 与 Spring Boot 无缝集成
- 文档：https://docs.spring.io/spring-ai/reference/

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Spring AI | https://docs.spring.io/spring-ai/reference/ |
| Spring Boot | https://spring.io/projects/spring-boot |
| Spring Security | https://spring.io/projects/spring-security |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Java 控制平面设计
- [ ] 租户管理
- [ ] 成本核算

---

## 💻 今日编码任务

### 文件结构

```
day36-java-control-plane/
├── README.md
├── 00_cost_tracker.py          # 成本核算
├── 01_tenant_management.py     # 租户管理
├── architecture.md             # 架构说明
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: tenant_management.py（60min）

实现租户管理

### Task 2: cost_tracker.py（60min）

实现成本核算

---

## 🐉 今日 Boss

1. **为什么 Agent 平台需要 Java 控制平面？**
2. **Java + Python 混合架构的优势？**
3. **如何实现多租户隔离？**

---

## 🎤 面试题

1. **请描述你设计的 Agent 平台架构**
2. **Java 和 Python 各自负责什么？**
3. **如何实现多租户隔离？**
4. **如何核算成本？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| tenant_management.py | 40分 |
| cost_tracker.py | 30分 |
| architecture.md | 10分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 37: Multi-tenant**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Java 控制平面的核心概念
- 解释 Spring AI 的用法
- 帮你调试代码报错
- 对比 Java + Python 混合架构的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 10 年 Java 经验，想设计一个 Agent 平台的 Java 控制平面。请帮我梳理租户管理、成本核算、任务调度的模块划分，然后给我一个 Python 端的模拟实现示例。"

### 错误用法
> "帮我写一个完整的 Java 控制平面系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
05-production-agent/
└── day36-java-control-plane/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_cost_tracker.py   # 成本核算
    ├── 01_tenant_management.py   # 租户管理
    ├── architecture.md     # 架构说明
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 36 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Java 控制平面 | ... | ... |
| 成本核算 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 05-production-agent/day36-java-control-plane/
git commit -m "feat(day36): Java Control Plane - 租户管理和成本核算完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Spring AI / Spring Boot 官方文档
- [ ] 写了 00_cost_tracker.py
- [ ] 写了 01_tenant_management.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
