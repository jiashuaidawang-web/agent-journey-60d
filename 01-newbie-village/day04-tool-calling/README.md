# Day 4: Tool Calling / Function Calling

> **今日目标**: 理解 Tool Calling 的完整链路，这是 Agent 的核心
> **核心问题**: Tool 是谁执行的？LLM 能不能直接执行 Tool？

---

## 🎯 今日目标

1. 理解 Tool Calling 的本质：LLM 选择工具 → 程序执行工具 → 结果反馈给 LLM
2. 掌握 Function Calling 协议（tool definitions + tool calls）
3. 实现 CalculatorTool / WeatherTool / StockTool
4. 理解 LLM 不能直接执行工具

---

## 📚 必学知识

### 1. Tool Calling 完整链路

```
用户输入: "今天北京天气怎么样"
    ↓
LLM 看到: [get_weather, get_stock_price, calculate]
    ↓
LLM 输出: {"tool": "get_weather", "arguments": {"city": "北京"}}
    ↓
程序执行: get_weather(city="北京") → "北京今天晴，25°C"
    ↓
结果反馈: 把工具结果作为新消息发给 LLM
    ↓
LLM 生成: "北京今天天气晴朗，气温25°C，适合出行。"
    ↓
返回给用户
```

### 2. 关键概念

- **Tool Definition**：告诉 LLM 有哪些工具可用（名称、描述、参数 Schema）
- **Tool Call**：LLM 决定调用哪个工具（只是"决定"，不执行）
- **Tool Execution**：程序真正执行工具
- **Tool Result**：执行结果反馈给 LLM

### 3. 重要认知

> **LLM 不能直接执行 Tool！**
>
> LLM 只能输出"我想调用 XX 工具，参数是 YY"。
> 真正的执行必须由程序完成。
> 这是 Agent 系统的核心设计原则。

### 4. Tool Definition 格式

```json
{
  "name": "get_weather",
  "description": "获取指定城市的天气",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {"type": "string", "description": "城市名称"}
    },
    "required": ["city"]
  }
}
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| OpenAI Function Calling | https://platform.openai.com/docs/guides/function-calling |
| OpenAI Tools API | https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools |
| Anthropic Tool Use | https://docs.anthropic.com/en/docs/build-with-claude/tool-use |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Tool Calling 完整链路
- [ ] Tool Definition 怎么写
- [ ] LLM 只选择不执行
- [ ] 工具结果如何反馈给 LLM

### 只需理解（L2）
- [ ] Parallel Tool Calls（并行调用多个工具）
- [ ] Tool Choice（auto / none / specific）

---

## 💻 今日编码任务

### 文件结构

```
day04-tool-calling/
├── README.md
├── tool.py                   # 工具定义 + 实现
├── function_calling_demo.py  # Function Calling 演示
├── requirements.txt
└── boss-answer.md
```

### Task 1: tool.py（40min）

实现 3 个工具：
- `CalculatorTool`：数学计算
- `WeatherTool`：天气查询（模拟）
- `StockTool`：股票查询（模拟）

每个工具包含：name / description / parameters / execute()

### Task 2: function_calling_demo.py（60min）

实现完整的 Function Calling 流程：
- 定义 tools
- 发送带 tools 的请求
- 解析 LLM 返回的 tool_calls
- 执行工具
- 把结果反馈给 LLM
- 获取最终回复

---

## 🐉 今日 Boss

1. **Tool 是谁执行的？LLM 能不能直接执行 Tool？**
2. **Tool Definition 的作用是什么？**
3. **如果 LLM 决定调用一个不存在的工具怎么办？**
4. **工具执行出错了怎么处理？**

---

## 🎤 面试题

1. **Function Calling 的原理是什么？**
2. **LLM 是如何"学会"使用工具的？**
3. **Tool Calling 和 MCP 有什么关系？**
4. **如何设计一个好的 Tool Description？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| tool.py | 30分 |
| function_calling_demo.py | 40分 |
| README 学习总结 | 15分 |
| Boss 答案 | 15分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 4题完成
- [ ] README 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 5: Tool Registry + Agent Loop**
