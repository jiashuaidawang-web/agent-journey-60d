# Day 37: Multi-tenant（多租户）

> **今日目标**: 实现多租户隔离
> **核心问题**: 如何实现数据、配额、性能的多租户隔离？

---

## 🎯 今日目标

1. 理解多租户隔离维度
2. 实现数据隔离
3. 实现配额隔离
4. 实现性能隔离

---

## 📚 必学知识

### 1. 多租户隔离维度

| 维度 | 说明 |
|------|------|
| 数据隔离 | 每个租户独立数据 |
| 配额隔离 | 每个租户独立配额 |
| 性能隔离 | 避免互相影响 |
| 安全隔离 | 权限控制 |

### 2. 数据隔离方案

| 方案 | 说明 | 适用 |
|------|------|------|
| 独立数据库 | 每个租户一个数据库 | 高隔离 |
| 共享数据库独立 Schema | 每个租户一个 Schema | 中隔离 |
| 共享表 + 租户 ID | 所有租户共享表 | 低隔离 |

### 3. Java 实现

- TenantContext：ThreadLocal 存储当前租户
- MyBatis 拦截器：自动添加租户过滤
- Spring Security：租户级权限

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| Spring Multi-tenant | https://docs.spring.io/spring-framework/reference/core/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] 多租户隔离维度
- [ ] 数据隔离方案
- [ ] 配额隔离

---

## 💻 今日编码任务

### 文件结构

```
day37-multi-tenant/
├── README.md
├── 00_tenant_context.py        # 租户上下文 + 数据/配额隔离
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: tenant_context.py（60min）

实现租户上下文

### Task 2: data_isolation.py（45min）

实现数据隔离

---

## 🐉 今日 Boss

1. **多租户隔离的维度？**
2. **数据隔离的方案？**
3. **如何实现配额隔离？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| tenant_context.py | 50分 |
| data_isolation.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 38: Agent Platform**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释多租户隔离的核心概念
- 解释数据隔离方案的优劣
- 帮你调试代码报错
- 对比 Java ThreadLocal 和 Python 上下文管理的异同

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 Java 经验，对 Python 的上下文管理器不太熟。请用 Java 的 ThreadLocal 和 MyBatis 拦截器类比解释一下租户上下文和数据隔离的实现，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的多租户隔离系统。"

---

## 📝 GitHub 提交规范

### 提交结构
```
05-production-agent/
└── day37-multi-tenant/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_tenant_context.py   # 租户上下文 + 数据/配额隔离
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 37 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| 租户上下文 | ... | ... |
| 数据隔离 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 05-production-agent/day37-multi-tenant/
git commit -m "feat(day37): Multi-tenant - 租户上下文和数据隔离完成"
```

---

## 📊 今日检查清单

- [ ] 读了 Spring Multi-tenant 官方文档
- [ ] 写了 00_tenant_context.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
