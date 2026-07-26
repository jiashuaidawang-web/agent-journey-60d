# Day 59: MCP 三种传输方式

> **今日目标**: 掌握 MCP 协议的三种传输方式：STDIO、SSE、Streamable HTTP
> **核心问题**: 为什么 MCP 需要三种传输方式？它们各自适合什么场景？

---

## 🎯 今日目标

1. 理解 MCP 协议核心原理（回顾）
2. 掌握 STDIO 传输的完整实现与演示
3. 掌握 SSE 传输的实现与演示
4. 掌握 Streamable HTTP 传输的实现与演示
5. 对比三种传输方式的优缺点和适用场景
6. 了解 Spring AI MCP 集成最佳实践

---

## 📚 必学知识

### 1. MCP 协议核心原理回顾

**MCP（Model Context Protocol）**：
- Anthropic 提出的开放协议，标准化 LLM 应用与外部数据源的连接
- 核心架构：Client ↔ Server，通过 JSON-RPC 2.0 通信
- 三大原语：Tools（工具）、Resources（资源）、Prompts（提示词模板）

**为什么需要传输层？**
- MCP 协议是应用层协议，需要依赖传输层传递 JSON-RPC 消息
- 不同场景需要不同的传输方式：本地进程间通信 vs 远程服务通信
- MCP 3.0 规范定义了三种标准传输方式

### 2. STDIO 传输（Standard Input/Output）

**原理**：
- 通过标准输入/stdout 在进程间传递 JSON-RPC 消息
- Client 启动 MCP Server 作为子进程
- 每行一条 JSON-RPC 消息（换行符分隔）

**特点**：
- 最简单、最直接的传输方式
- 无需网络，适合本地开发
- 一对一通信，Server 只能服务一个 Client

**适用场景**：
- 本地 CLI 工具
- IDE 插件（如 Claude Code、Cursor）
- 单机开发调试

### 3. SSE 传输（Server-Sent Events）

**原理**：
- 基于 HTTP 协议
- Client → Server：HTTP POST 请求
- Server → Client：SSE 长连接推送
- 需要两个 HTTP 端点：`/sse`（建立 SSE 连接）和 `/messages`（发送消息）

**特点**：
- 支持远程通信
- Server 可以服务多个 Client
- 单向推送（Server → Client 通过 SSE，Client → Server 通过 POST）

**适用场景**：
- 远程 MCP Server
- 需要多 Client 共享 Server 的场景
- 注意：SSE 在 MCP 3.0 中已被 Streamable HTTP 取代

### 4. Streamable HTTP 传输

**原理**：
- MCP 3.0 推荐的传输方式
- 基于标准 HTTP 协议
- 支持流式响应（可选 SSE 流）
- 支持 Session 管理（Mcp-Session-Id）

**特点**：
- 最灵活的传输方式
- 支持有状态（Session）和无状态（Stateless）模式
- 支持 OAuth 2.1 认证
- 可以降级为普通 HTTP（不支持流式时）

**适用场景**：
- 生产环境部署
- 需要认证的场景
- 需要负载均衡的场景

### 5. 三种传输方式对比

| 维度 | STDIO | SSE | Streamable HTTP |
|------|-------|-----|-----------------|
| 通信方式 | 进程内 | HTTP | HTTP |
| 网络要求 | 无 | 需要 | 需要 |
| 多 Client | 不支持 | 支持 | 支持 |
| 认证 | 无 | 可选 | OAuth 2.1 |
| 复杂度 | 低 | 中 | 高 |
| 适用场景 | 本地工具 | 远程服务 | 生产部署 |
| MCP 3.0 状态 | 保留 | 已弃用 | 推荐 |

### 6. Spring AI MCP 集成最佳实践

**Spring AI MCP 支持**：
- `spring-ai-mcp`：MCP Client 支持
- `spring-ai-mcp-server`：MCP Server 支持
- 自动工具注册和调用

**最佳实践**：
- 开发阶段用 STDIO（快速迭代）
- 测试阶段用 Streamable HTTP（模拟生产）
- 生产环境用 Streamable HTTP + OAuth 2.1
- 使用 Spring Boot 的自动配置简化集成

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| MCP 官方文档 | https://modelcontextprotocol.io/ |
| MCP 3.0 规范（传输） | https://modelcontextprotocol.io/specification/2025-03-26/basic/transports |
| MCP Python SDK | https://github.com/modelcontextprotocol/python-sdk |
| MCP Java SDK | https://github.com/modelcontextprotocol/java-sdk |
| Spring AI MCP | https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html |
| SSE 协议规范 | https://html.spec.whatwg.org/multipage/server-sent-events.html |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] MCP 协议核心原理（JSON-RPC 2.0、Client-Server 架构）
- [ ] STDIO 传输原理和实现
- [ ] SSE 传输原理和实现
- [ ] Streamable HTTP 传输原理和实现
- [ ] 三种传输方式的优缺点对比
- [ ] 适用场景选择

### 只需理解（L2）
- [ ] MCP 3.0 规范细节
- [ ] OAuth 2.1 认证流程
- [ ] Session 管理机制
- [ ] Spring AI MCP 自动配置

### 今天不深入（后面会讲）
- [ ] MCP Resources 深入
- [ ] MCP Prompts 深入
- [ ] MCP 安全最佳实践
- [ ] MCP 生态工具链

---

## 💻 今日编码任务

### 文件结构

```
day59-mcp-transports/
├── README.md
├── LEARNING_FLOW.md
├── 00_stdio_transport.py          # STDIO 传输演示
├── 01_sse_transport.py            # SSE 传输演示
├── 02_streamable_http.py          # Streamable HTTP 传输演示
├── 03_transport_comparison.py     # 三种传输方式对比
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: 00_stdio_transport.py（45min）

实现 STDIO 传输：
- 创建 MCP Server（使用 FastMCP）
- 注册一个工具（如 `get_weather`）
- 使用 STDIO 传输启动 Server
- 创建 Client 连接并调用工具

**验收标准**：
```bash
python 00_stdio_transport.py
# 输出：
# 🔌 STDIO 传输启动
# 📡 Server 已启动（子进程模式）
# 🔧 工具注册：get_weather
# ✅ 调用结果：{city: "北京", temp: "25°C"}
```

### Task 2: 01_sse_transport.py（45min）

实现 SSE 传输：
- 创建 MCP Server
- 使用 SSE 传输启动（指定 host/port）
- Client 通过 HTTP 连接
- 演示 SSE 长连接推送

**验收标准**：
```bash
python 01_sse_transport.py
# 输出：
# 🌐 SSE 传输启动
# 📡 Server 监听: http://localhost:8000/sse
# 📨 Messages 端点: http://localhost:8000/messages
# ✅ SSE 连接建立，收到工具调用结果
```

### Task 3: 02_streamable_http.py（45min）

实现 Streamable HTTP 传输：
- 创建 MCP Server
- 使用 Streamable HTTP 传输启动
- Client 通过 HTTP 连接
- 演示 Session 管理和流式响应

**验收标准**：
```bash
python 02_streamable_http.py
# 输出：
# 🌐 Streamable HTTP 传输启动
# 📡 Server 监听: http://localhost:8000/mcp
# 🔑 Session ID: xxx-xxx-xxx
# ✅ 流式响应接收完成
```

### Task 4: 03_transport_comparison.py（30min）

对比三种传输方式：
- 创建三种传输的 Client
- 调用相同工具，对比延迟
- 输出对比表格

**验收标准**：
```bash
python 03_transport_comparison.py
# 输出：
# 📊 三种传输方式对比
# | 传输方式 | 延迟 | 多Client | 认证 | 复杂度 |
# | STDIO    | 50ms | 否      | 无   | 低     |
# | SSE      | 80ms | 是      | 可选 | 中     |
# | Streamable HTTP | 85ms | 是 | OAuth | 高 |
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 MCP 三种传输方式的原理
- 解释 JSON-RPC 2.0 协议
- 帮你调试代码报错
- 对比 STDIO/SSE/Streamable HTTP 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有 HTTP API 开发经验，MCP 的 STDIO 传输我不太熟。请用 Java 的 ProcessBuilder 类比解释 STDIO 传输的进程间通信，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 MCP Server，支持三种传输方式。"

---

## 📝 GitHub 提交规范

### 提交结构
```
09-java-ai-engineering/
└── day59-mcp-transports/
    ├── README.md                    # 学习总结
    ├── LEARNING_FLOW.md             # 学习流程
    ├── 00_stdio_transport.py        # STDIO 传输演示
    ├── 01_sse_transport.py          # SSE 传输演示
    ├── 02_streamable_http.py        # Streamable HTTP 传输演示
    ├── 03_transport_comparison.py   # 三种传输方式对比
    ├── requirements.txt
    └── 99-boss-answer.md            # Boss 答案
```

### README.md 必须包含
```markdown
# Day 59 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| STDIO | ... | ... |
| SSE | ... | ... |
| Streamable HTTP | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 09-java-ai-engineering/day59-mcp-transports/
git commit -m "feat(day59): MCP 三种传输方式 - STDIO/SSE/Streamable HTTP 完成"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **MCP 协议的核心原理是什么？为什么需要传输层？**
2. **STDIO 传输的优缺点是什么？适合什么场景？**
3. **SSE 传输和 Streamable HTTP 传输有什么区别？**
4. **为什么 MCP 3.0 推荐使用 Streamable HTTP 而不是 SSE？**
5. **Spring AI 集成 MCP 时，开发阶段和生产阶段应该分别选择哪种传输方式？**

### 验收标准
- 每个答案 **不少于50字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **MCP 协议和 Function Calling 有什么区别？**
2. **MCP 的三种传输方式分别是什么？**
3. **STDIO 传输为什么适合本地开发？**
4. **Streamable HTTP 的 Session 机制是如何工作的？**
5. **生产环境部署 MCP Server 应该选择哪种传输方式？为什么？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| 00_stdio_transport.py | 20分 | 能运行 + STDIO 传输 + 工具调用 |
| 01_sse_transport.py | 20分 | 能运行 + SSE 传输 + 工具调用 |
| 02_streamable_http.py | 20分 | 能运行 + Streamable HTTP + Session |
| 03_transport_comparison.py | 15分 | 对比表格 + 延迟测试 |
| README 学习总结 | 10分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 5题全部完成 + 用自己的话 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 5题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 60: Memory 深度体系**

---

## 📊 今日检查清单

- [ ] 读了 MCP 3.0 规范（传输部分）
- [ ] 读了 MCP Python SDK 文档
- [ ] 读了 Spring AI MCP 文档
- [ ] 写了 00_stdio_transport.py
- [ ] 写了 01_sse_transport.py
- [ ] 写了 02_streamable_http.py
- [ ] 写了 03_transport_comparison.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
