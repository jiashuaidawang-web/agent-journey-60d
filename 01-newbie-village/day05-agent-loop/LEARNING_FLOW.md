# Day 5: Agent Loop - 学习流程

> **今日目标**: 实现 Agent Loop —— Agent 的心脏
> **核心问题**: Agent Loop 为什么可能死循环？如何防止？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_state.py（10分钟）
    ↓ 理解：状态管理
Step 4: 运行 01_registry.py（15分钟）
    ↓ 理解：工具注册表
Step 5: 运行 02_agent_executor.py（20分钟）
    ↓ 理解：Agent 执行器
Step 6: 完成 99_boss_answer.md（30分钟）
    ↓
Step 7: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-5 | 3个代码文件 | 45min |
| 6 | Boss 问题 | 30min |
| 7 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 Agent Loop 核心流程
- [ ] 理解 Max Iterations 必要性
- [ ] 能实现 ToolRegistry
- [ ] 能实现 AgentExecutor
- [ ] 能回答 Boss 4 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_state.py](00_state.py) | 状态管理 | ⭐ |
| [01_registry.py](01_registry.py) | 工具注册表 | ⭐⭐ |
| [02_agent_executor.py](02_agent_executor.py) | Agent 执行器 | ⭐⭐⭐ |
| [99_boss_answer.md](99_boss_answer.md) | Boss 问题答案 | ⭐⭐ |
