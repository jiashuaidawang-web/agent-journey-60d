# Day 59 Boss 答案

## 1. MCP 协议的核心原理是什么？为什么需要传输层？

MCP（Model Context Protocol）是 Anthropic 提出的开放协议，用于标准化 LLM 应用与外部数据源的连接。

**核心原理**：
- 采用 **Client-Server 架构**：Client（LLM 应用）通过协议与 Server（工具/数据源）通信
- 使用 **JSON-RPC 2.0** 作为消息格式，定义了标准的请求/响应/通知结构
- 三大原语：**Tools**（工具，LLM 可调用）、**Resources**（资源，数据源）、**Prompts**（提示词模板）

**为什么需要传输层？**
- MCP 是应用层协议，只定义了"消息长什么样"，没有定义"消息怎么传"
- 不同场景需要不同的传输方式：本地进程间通信（STDIO）vs 远程服务通信（HTTP）
- 传输层负责 JSON-RPC 消息的实际传递：进程内、跨网络、跨设备
- MCP 3.0 规范定义了三种标准传输方式，覆盖从本地开发到生产部署的全场景

**类比理解**：
- MCP 协议 = 信封上的标准格式（收件人、寄件人、内容）
- 传输层 = 快递方式（顺丰 STDIO、EMS SSE、DHL Streamable HTTP）

## 2. STDIO 传输的优缺点是什么？适合什么场景？

**STDIO（Standard Input/Output）** 通过标准输入/输出在进程间传递 JSON-RPC 消息。

**工作原理**：
- Client 启动 MCP Server 作为子进程
- 双方通过 stdin/stdout 读写消息
- 每行一条 JSON-RPC 消息（换行符分隔）

**优点**：
1. **最简单**：无需网络配置，无需端口管理
2. **延迟最低**：进程间通信，无网络开销（实测延迟约 50ms）
3. **安全性高**：不暴露网络端口，本地通信难以被外部攻击
4. **调试方便**：可以直接看到 stdin/stdout 的内容

**缺点**：
1. **一对一**：一个 Server 只能服务一个 Client
2. **本地限制**：必须运行在同一台机器上
3. **无认证**：没有内置的认证机制（依赖进程隔离）
4. **生命周期绑定**：Client 退出则 Server 退出

**适用场景**：
- 本地 CLI 工具（如文件操作、代码搜索）
- IDE 插件（Claude Code、Cursor、VS Code）
- 单机开发调试
- 不需要多 Client 共享的场景

## 3. SSE 传输和 Streamable HTTP 传输有什么区别？

**SSE（Server-Sent Events）** 和 **Streamable HTTP** 都是基于 HTTP 的传输方式，但设计上有本质区别。

**SSE 传输**：
- 需要两个 HTTP 端点：`/sse`（建立 SSE 长连接）和 `/messages`（发送消息）
- Client → Server：HTTP POST 请求
- Server → Client：SSE 长连接单向推送
- 本质是"两个通道"：一个 POST 通道 + 一个 SSE 通道

**Streamable HTTP 传输**：
- 只需要一个 HTTP 端点：`/mcp`
- Client → Server：HTTP POST 请求
- Server → Client：HTTP 响应（可选 SSE 流）
- 本质是"一个通道"：通过 Session ID 区分不同会话

**核心区别**：

| 维度 | SSE | Streamable HTTP |
|------|-----|-----------------|
| 端点数量 | 2个（/messages + /sse） | 1个（/mcp） |
| 通信模式 | 双向通道 | 统一通道 |
| 状态管理 | 无显式 Session | Mcp-Session-Id |
| 负载均衡 | 复杂（需要粘性会话） | 简单（支持无状态） |
| MCP 3.0 状态 | 已弃用 | 推荐 |

**为什么 Streamable HTTP 更优**：
- 架构更简单，一个端点搞定
- 支持无状态模式，易于水平扩展
- 内置 Session 管理，支持多 Client
- 兼容 OAuth 2.1 认证

## 4. 为什么 MCP 3.0 推荐使用 Streamable HTTP 而不是 SSE？

MCP 3.0 将 Streamable HTTP 作为推荐的传输方式，SSE 被标记为"已弃用"，原因如下：

**1. 架构简洁性**
- SSE 需要两个端点（/messages + /sse），增加部署复杂度
- Streamable HTTP 只需一个端点（/mcp），简化运维

**2. 负载均衡友好**
- SSE 依赖长连接，需要粘性会话（Sticky Session）
- Streamable HTTP 支持无状态模式，可以轻松水平扩展

**3. 认证集成**
- SSE 的认证机制不标准
- Streamable HTTP 原生支持 OAuth 2.1，适合企业级部署

**4. 流式灵活性**
- SSE 强制使用 SSE 协议推送
- Streamable HTTP 支持流式（SSE 流）和普通 HTTP 响应，可以降级

**5. Session 管理**
- SSE 没有显式的 Session 概念
- Streamable HTTP 通过 Mcp-Session-Id 管理会话状态

**实际影响**：
- 新项目应直接使用 Streamable HTTP
- 已有 SSE 项目建议迁移到 Streamable HTTP
- STDIO 仍然适用于本地开发场景

## 5. Spring AI 集成 MCP 时，开发阶段和生产阶段应该分别选择哪种传输方式？

**Spring AI 提供了完整的 MCP 集成支持**，包括 `spring-ai-mcp`（Client）和 `spring-ai-mcp-server`（Server）。

**开发阶段：STDIO**
- **原因**：无需启动网络服务，快速迭代
- **配置**：使用 `spring-ai-mcp-client-stdio` 依赖
- **优势**：
  - 启动快，无需端口管理
  - 调试方便，可以直接看日志
  - 适合本地 IDE 开发

**生产阶段：Streamable HTTP**
- **原因**：支持远程部署、负载均衡、OAuth 认证
- **配置**：使用 `spring-ai-mcp-client-http` 依赖
- **优势**：
  - 支持多实例部署
  - 集成 Spring Security（OAuth 2.1）
  - 支持 Session 管理和恢复

**最佳实践**：
1. **开发环境**：STDIO + 本地 MCP Server
2. **测试环境**：Streamable HTTP（模拟生产）
3. **生产环境**：Streamable HTTP + OAuth 2.1 + 负载均衡
4. **配置抽象**：使用 Spring Profile 切换传输方式

**代码示例**：
```yaml
# application-dev.yml
spring:
  ai:
    mcp:
      client:
        stdio:
          servers:
            my-server:
              command: python
              args: ["-m", "my_mcp_server"]

# application-prod.yml
spring:
  ai:
    mcp:
      client:
        http:
          base-url: http://mcp-server:8000
```
