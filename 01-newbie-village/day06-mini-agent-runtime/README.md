# Day 6: Mini Agent Runtime

## 今日目标

把前5天全部串起来，实现一个完整的 Mini Agent Runtime。

不依赖 LangChain / LangGraph，完全自己造轮子。

## 📚 学习清单

### 理论 (0.5h)
- [ ] 回顾前5天的所有抽象
- [ ] 思考架构：哪些应该解耦？哪些可以复用？

### 编码 (4.5h)
- [ ] 搭建 `mini-agent-runtime/` 目录结构
- [ ] 实现 `core/agent.py` — Agent核心
- [ ] 实现 `core/loop.py` — Agent循环
- [ ] 实现 `core/context.py` — Context管理
- [ ] 实现 `core/state.py` — 状态管理
- [ ] 实现 `model/base.py` — 模型抽象接口
- [ ] 实现 `model/openai.py` — OpenAI兼容实现
- [ ] 实现 `tools/base.py` + `tools/registry.py` — Tool框架
- [ ] 实现 `memory/` — 简单记忆
- [ ] 实现 `observability/` — 日志和Token统计

## 💻 项目结构

```
day06-mini-agent-runtime/
├── README.md
├── mini-agent-runtime/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── loop.py
│   │   ├── context.py
│   │   └── state.py
│   ├── model/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── openai.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── registry.py
│   │   └── builtin/
│   ├── memory/
│   │   ├── __init__.py
│   │   └── simple.py
│   ├── observability/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── token_counter.py
│   └── tests/
│       └── test_agent.py
├── examples/
│   └── research_agent.py
├── architecture/
│   ├── architecture.md
│   └── architecture.png
├── boss-answer.md
└── requirements.txt
```

## 🐉 Boss Challenge

实现一个 Mini Research Agent：
```
输入："帮我研究一下新能源车行业"
    ↓
Agent能够：
  1. 分析任务
  2. 选择工具
  3. 调用工具
  4. 获取结果
  5. 根据结果继续行动
  6. 最终输出报告
```

回答：
1. **你的Agent Runtime和LangChain的Agent有什么区别？**
2. **如果让你扩展支持Multi-Agent，你会怎么改架构？**
3. **State是怎么管理的？支持恢复吗？**

## ✅ 提交清单

- [ ] 完整目录结构
- [ ] 所有模块能跑通
- [ ] 架构图 (`architecture.md` + `architecture.png`)
- [ ] Boss场景能跑通
- [ ] `boss-answer.md`
- [ ] Git Commit

---

**今日积分**: ⭐ __分 | 💻 __分 | 🐉 __分 = ___/80
