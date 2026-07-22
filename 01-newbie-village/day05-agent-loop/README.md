# Day 5: Agent Loop

## 今日目标

实现 Agent 的核心循环：

```
while not finished:
    response = llm(context)
    if response.has_tool_calls():
        results = execute_tools(response.tool_calls)
        context.append(results)
    else:
        return response.content
```

## 📚 学习清单

### 理论 (1h)
- [ ] Agent Loop 的生命周期
- [ ] Max Iterations 为什么是必须的
- [ ] Error Handling 策略
- [ ] Token 统计方法

### 编码 (4h)
- [ ] 实现 `AgentExecutor` 类
- [ ] 支持 Tool Calling 循环
- [ ] 支持 max_iterations 防止死循环
- [ ] 支持日志记录和Token统计

## 💻 项目结构

```
day05-agent-loop/
├── README.md
├── agent_executor.py     # Agent循环核心
├── state.py              # Agent状态管理
├── boss-answer.md
└── requirements.txt
```

## 🐉 Boss Challenge

实现一个 Research Agent：
```
任务："帮我分析一家上市公司"
    ↓
Agent自动：
  Search → Company Info → Financial Data → Analysis
    ↓
输出分析报告
```

回答：
1. **Agent Loop 为什么可能死循环？**
2. **如何检测并终止无效循环？**
3. **Tool执行失败时Agent应该怎么处理？**

## ✅ 提交清单

- [ ] `agent_executor.py` — 能跑通Agent Loop
- [ ] `state.py` — 状态管理
- [ ] Boss场景能跑通
- [ ] `boss-answer.md`
- [ ] Git Commit

---

**今日积分**: ⭐ __分 | 💻 __分 | 🐉 __分 = ___/80
