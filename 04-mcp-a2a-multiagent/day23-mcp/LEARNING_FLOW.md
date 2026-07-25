# Day 23: MCP 协议详解 - 学习流程

> **今日目标**: 理解 MCP（Model Context Protocol）协议
> **核心问题**: MCP 和 Function Calling 有什么区别？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_mcp_basics.py（15分钟）
    ↓ 理解：MCP Server 的创建和工具注册
Step 4: 运行 01_mcp_tools_demo.py（15分钟）
    ↓ 理解：MCP Tools 的完整定义和调用流程
Step 5: 完成 99-boss-answer.md（30分钟）
    ↓
Step 6: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-4 | 2个代码文件 | 30min |
| 5 | Boss 问题 | 30min |
| 6 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 MCP 协议的本质和作用
- [ ] 解释 MCP 和 Function Calling 的区别
- [ ] 理解 MCP 的核心概念：Tools / Resources / Prompts
- [ ] 理解 MCP Server / Client 架构
- [ ] 能独立实现一个 MCP Server 和工具注册
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_mcp_basics.py](00_mcp_basics.py) | 理解 MCP Server 创建和工具注册 | ⭐ |
| [01_mcp_tools_demo.py](01_mcp_tools_demo.py) | 理解 MCP Tools 定义和调用流程 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
