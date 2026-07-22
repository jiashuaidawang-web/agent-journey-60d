# Day 4: Tool Calling

## 今日目标

理解 Agent 的核心机制：LLM 决定调用哪个Tool → 程序执行 → Tool Result 回传给 LLM。

## 📚 学习清单

### 理论 (1h)
- [ ] Function Calling / Tool Calling 协议
- [ ] Tool Schema 定义（name, description, parameters）
- [ ] Tool Call vs Tool Result 的消息格式

### 编码 (4h)
- [ ] 实现 `Tool` 基类（name, description, parameters, execute）
- [ ] 实现 `ToolRegistry`（register, get, list）
- [ ] 实现至少4个Tool：CalculatorTool, WeatherTool, StockTool, HttpTool

## 💻 项目结构

```
day04-tool-calling/
├── README.md
├── tool.py               # Tool基类
├── registry.py           # Tool注册表
├── tools/                # 具体Tool实现
│   ├── calculator.py
│   ├── weather.py
│   ├── stock.py
│   └── http.py
├── boss-answer.md
└── requirements.txt
```

## 🐉 Boss Challenge

实现多Tool连续调用场景：
```
用户："帮我查询贵州茅台当前价格，并计算上涨10%后的价格"
    ↓
Agent → StockTool("贵州茅台") → {"price": 1800}
    ↓
Agent → CalculatorTool(1800, 1.1) → {"result": 1980}
    ↓
Final Answer: "贵州茅台当前价1800元，上涨10%后为1980元"
```

回答：
1. **Tool Calling 到底是谁决定调用Tool？**
2. **Tool Schema 为什么重要？**
3. **如何保证Tool调用的安全性？**

## ✅ 提交清单

- [ ] `tool.py` + `registry.py` — Tool框架
- [ ] 至少4个Tool实现
- [ ] Boss场景能跑通
- [ ] `boss-answer.md`
- [ ] Git Commit

---

**今日积分**: ⭐ __分 | 💻 __分 | 🐉 __分 = ___/80
