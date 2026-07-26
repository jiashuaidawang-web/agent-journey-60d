# Day 59: MCP 三种传输方式 - 学习流程

> **今日目标**: 掌握 MCP 协议的三种传输方式：STDIO、SSE、Streamable HTTP
> **核心问题**: 为什么 MCP 需要三种传输方式？它们各自适合什么场景？

---

## 学习顺序

```
Step 1: 阅读 README.md（5分钟）
    ↓
Step 2: 阅读 LEARNING_FLOW.md（2分钟）← 你在这里
    ↓
Step 3: 运行 00_stdio_transport.py（15分钟）
    ↓ 理解：STDIO 传输的进程间通信机制
Step 4: 运行 01_sse_transport.py（15分钟）
    ↓ 理解：SSE 长连接推送机制
Step 5: 运行 02_streamable_http.py（15分钟）
    ↓ 理解：Streamable HTTP 的 Session 管理
Step 6: 运行 03_transport_comparison.py（10分钟）
    ↓ 理解：三种传输方式的差异
Step 7: 完成 99-boss-answer.md（30分钟）
    ↓
Step 8: 写学习总结（15分钟）
```

## 时间分配

| 步骤 | 内容 | 时间 |
|------|------|------|
| 1-2 | 阅读文档 | 7min |
| 3-6 | 4个代码文件 | 55min |
| 7 | Boss 问题 | 30min |
| 8 | 学习总结 | 15min |
| **总计** | | **约 2h** |

---

## 验证清单

完成后，你应该能：

- [ ] 解释 MCP 协议核心原理和传输层的作用
- [ ] 解释 STDIO 传输的优缺点和适用场景
- [ ] 解释 SSE 传输的工作原理
- [ ] 解释 Streamable HTTP 的 Session 机制
- [ ] 对比三种传输方式的差异
- [ ] 能独立实现三种传输方式的 MCP Server/Client
- [ ] 能回答 Boss 5 题

---

## 快速导航

| 文件 | 目标 | 难度 |
|------|------|------|
| [00_stdio_transport.py](00_stdio_transport.py) | 理解 STDIO 传输的进程间通信 | ⭐ |
| [01_sse_transport.py](01_sse_transport.py) | 理解 SSE 长连接推送机制 | ⭐⭐ |
| [02_streamable_http.py](02_streamable_http.py) | 理解 Streamable HTTP 的 Session 管理 | ⭐⭐⭐ |
| [03_transport_comparison.py](03_transport_comparison.py) | 对比三种传输方式 | ⭐⭐ |
| [99-boss-answer.md](99-boss-answer.md) | Boss 问题答案 | ⭐⭐ |
