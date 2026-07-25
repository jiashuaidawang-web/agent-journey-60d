# Day 3: Structured Output

## 今日目标

理解 LLM 如何从"聊天机器人"变成"程序的一部分"。

JSON Schema + Pydantic = LLM 输出结构化数据，让 Agent 可以路由和决策。

## 📚 学习清单

### 理论 (1h)
- [ ] JSON Mode vs Structured Output
- [ ] JSON Schema 作为 LLM 的契约
- [ ] Pydantic 作为验证层

### 编码 (3.5h)
- [ ] 定义 `UserIntent` Pydantic Model
- [ ] 实现 Intent Classifier：自然语言 → 结构化意图
- [ ] 实现 Router：根据 intent 路由到不同处理逻辑

## 💻 项目结构

```
day03-structured-output/
├── README.md
├── intent_classifier.py  # 意图分类器
├── router.py             # 路由器
└── boss-answer.md
```

## 🐉 Boss Challenge

实现：
```
"帮我分析贵州茅台"
    ↓
Intent Classifier
    ↓
{"intent": "stock_analysis", "confidence": 0.95, "entities": {"stock": "贵州茅台"}}
    ↓
Router → stock_analysis_handler()
```

回答：
1. **为什么Agent需要Structured Output？**
2. **JSON Schema和Pydantic的关系是什么？**
3. **如果LLM返回了不符合Schema的数据怎么办？**

## ✅ 提交清单

- [ ] `intent_classifier.py` — 能解析意图
- [ ] `router.py` — 能根据意图路由
- [ ] `boss-answer.md`
- [ ] Git Commit

---

**今日积分**: ⭐ __分 | 💻 __分 | 🐉 __分 = ___/80
