# Day 24: MCP Server 实现 - 学习流程

> **今日目标**: 实现一个完整的 MCP Server
> **核心问题**: MCP Server 如何暴露工具给外部调用？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_mcp_server.py（30分钟）
    ↓ 理解：MCP Server 实现、工具注册和资源暴露
Step 4: 完成 99-boss-answer.md（30分钟）
    ↓
Step 5: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3 | 1个代码文件 | 30min |
| 4 | Boss 问题 | 30min |
| 5 | 学习总结 | 15min |
| **总计** | | **约 1.5h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 MCP Server 的职责
- [ ] 理解工具注册的方式（FastMCP / 底层 SDK）
- [ ] 理解 MCP Server 如何被 Client 调用
- [ ] 理解 stdio / HTTP 传输方式
- [ ] 能独立实现一个 MCP Server
- [ ] 能回答 Boss 3 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_mcp_server.py](00_mcp_server.py) | 实现完整 MCP Server + 工具注册 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
