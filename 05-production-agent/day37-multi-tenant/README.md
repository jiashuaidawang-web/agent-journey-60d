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
├── tenant_context.py        # 租户上下文
├── data_isolation.py        # 数据隔离
├── requirements.txt
└── boss-answer.md
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
