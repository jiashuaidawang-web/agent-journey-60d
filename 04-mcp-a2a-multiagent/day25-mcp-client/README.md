# Day 25: MCP Client

> **今日目标**: 实现 MCP Client 调用 Server
> **核心问题**: Client 如何发现和调用 Server 的工具？

---

## 🎯 今日目标

1. 实现 MCP Client
2. 发现 Server 工具
3. 调用 Server 工具
4. 集成到 LangChain Agent

---

## 📚 必学知识

### 1. MCP Client 职责

- 连接 Server
- 发现工具（tools/list）
- 调用工具（tools/call）
- 读取资源（resources/read）

### 2. 集成到 LangChain

```python
from langchain_mcp_adapters import MultiServerMCPClient

client = MultiServerMCPClient({
    "research": {
        "url": "http://localhost:8000",
        "transport": "streamable_http",
    }
})

tools = await client.get_tools()
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| MCP Client SDK | https://modelcontextprotocol.io/docs/sdk/python |
| LangChain MCP Adapter | https://github.com/langchain-ai/langchain-mcp-adapters |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] MCP Client 实现
- [ ] 工具发现和调用
- [ ] LangChain 集成

---

## 💻 今日编码任务

### 文件结构

```
day25-mcp-client/
├── README.md
├── 00_mcp_client.py          # MCP Client
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: mcp_client.py（60min）

实现 MCP Client

### Task 2: langchain_integration.py（45min）

集成到 LangChain

---

## 🐉 今日 Boss

1. **MCP Client 的职责？**
2. **Client 如何发现工具？**
3. **如何集成到 LangChain？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| mcp_client.py | 50分 |
| langchain_integration.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 26: Skill Architecture**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 MCP Client 的实现原理
- 解释 LangChain MCP Adapter 的用法
- 帮你调试 MCP Client 代码报错
- 对比 MCP 与直接 RESTful API 调用的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解 HTTP Client 的请求/响应模式，MCP Client 的 tools/list 发现机制我不太熟。请用服务发现（Service Discovery）类比解释 MCP Client 如何动态获取工具列表，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 MCP Client。"

---

## 📝 GitHub 提交规范

### 提交结构
```
04-mcp-a2a-multiagent/
└── day25-mcp-client/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_mcp_client.py    # MCP Client
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 25 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| MCP Client | ... | ... |
| 工具发现 | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 04-mcp-a2a-multiagent/day25-mcp-client/
git commit -m "feat(day25): MCP Client - Client 实现和 LangChain 集成完成"
```

---

## 📊 今日检查清单

- [ ] 读了 MCP Client SDK 文档
- [ ] 读了 LangChain MCP Adapter 资料
- [ ] 写了 00_mcp_client.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
