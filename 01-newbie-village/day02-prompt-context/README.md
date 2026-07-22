# Day 2: Prompt & Context Engineering

## 今日目标

理解 Agent 的 Context 是如何组装的。

System Prompt + User Input + History + Memory + Retrieved Context + Tool Result → Final Context

## 📚 学习清单

### 理论 (1.5h)
- [ ] Prompt Template 是什么？Jinja2 vs f-string vs LangChain PromptTemplate
- [ ] Context Assembly 策略：如何拼接所有信息源
- [ ] Context Window 管理：Token裁剪、消息压缩
- [ ] System Prompt 设计原则

### 编码 (3h)
- [ ] 实现 `ContextBuilder` 类
- [ ] 支持消息优先级
- [ ] 支持最大Token限制下的裁剪
- [ ] 支持历史消息管理

## 💻 项目结构

```
day02-prompt-context/
├── README.md
├── context_builder.py    # Context组装器
└── boss-answer.md        # Boss问题答案
```

## 🐉 Boss Challenge

回答：
1. **Agent为什么不是简单的LLM API调用？** 从Context/State/Memory/Tool/Loop五个维度回答。
2. **Context和Memory有什么区别？**
3. **如果Context满了，你会怎么裁剪？**

## ✅ 提交清单

- [ ] `context_builder.py` — 能组装完整Context
- [ ] `boss-answer.md` — Boss问题答案
- [ ] Git Commit

---

**今日积分**: ⭐ __分 | 💻 __分 | 🐉 __分 = ___/80
