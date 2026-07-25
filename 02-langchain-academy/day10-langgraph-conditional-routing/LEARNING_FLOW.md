# Day 10: LangGraph Conditional Routing - 学习流程

> **今日目标**: 掌握条件路由，实现复杂分支逻辑
> **核心问题**: 如何根据 State 动态决定执行路径？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_router_graph.py（60分钟）
    ↓ 理解：Router Graph 根据意图路由到不同 Agent
Step 4: 运行 01_multi_branch_graph.py（45分钟）
    ↓ 理解：多分支 Graph + 循环控制
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 105min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 2.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释条件路由函数的作用和返回值
- [ ] 理解路由映射的作用
- [ ] 理解如何实现循环和终止条件
- [ ] 能独立实现 Router Graph
- [ ] 能独立实现多分支 Graph
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_router_graph.py](00_router_graph.py) | 根据意图路由到不同 Agent | ⭐⭐ |
| [01_multi_branch_graph.py](01_multi_branch_graph.py) | 多分支 + 循环控制 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
