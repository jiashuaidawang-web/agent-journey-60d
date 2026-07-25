# Day 52: Investment Research Platform - 学习流程

> **今日目标**: 完成项目二的核心开发，实现 Supervisor 多 Agent 投研平台
> **核心问题**: Supervisor 模式如何协调多个专业 Agent 完成投研任务？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_investment_research_platform.py（60分钟）
    ↓ 理解：Supervisor 调度多 Agent、Tool/Skill 封装、投研报告生成的完整流程
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

---

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 60min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 理解 Supervisor 多 Agent 架构（协调层 + 执行层 + 能力层 + 工具层）
- [ ] 掌握 Tool / Skill 的封装与复用模式
- [ ] 理解 Supervisor 如何接收任务、分解任务、调度 Agent、汇总结果
- [ ] 掌握投研 Skills 的实现（行业、公司、市场、风险）
- [ ] 能独立实现 Supervisor + 多 Agent 的投研平台
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_investment_research_platform.py](00_investment_research_platform.py) | 实现 Supervisor 多 Agent 投研平台 | ⭐⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
