# Day 2 Boss 答案

## 1. 为什么 Agent 系统需要 Structured Output？

Agent 系统中，LLM 的输出不是给人看的，是给**程序消费**的。

**自由文本的问题**：
- 格式不稳定："好的我来帮你" vs "我来帮你分析" vs "没问题"
- 程序难以解析：需要再用 LLM 提取，增加延迟和成本
- 容易出错：边界情况多，字符串匹配脆弱

**Structured Output 的优势**：
- 格式确定：JSON Schema 保证每次输出结构一致
- 程序可用：直接反序列化为对象，无需再解析
- 可验证：Pydantic 自动校验数据类型和范围
- 可组合：ToolCall → ToolResult → AgentResponse 形成链路

**实际场景**：
- Agent Router：根据 intent 字段决定路由到哪个 Agent
- Tool Calling：根据 tool_name + arguments 调用工具
- State Update：根据结构化结果更新 Agent 状态

## 2. JSON Mode 和 Structured Output 有什么区别？

**JSON Mode**（`response_format={"type": "json_object"}`）：
- 只保证输出是**合法 JSON**
- 不保证 JSON 的**结构**（字段名、类型都可能变）
- 可能出现 `{"intent": "xxx"}` 也可能出现 `{"type": "xxx", "value": "yyy"}`

**Structured Output**（`response_format={"type": "json_schema", "json_schema": {...}}`）：
- 保证输出是合法 JSON
- **并且**符合指定的 Schema（字段名、类型、枚举值都固定）
- 通过语法约束（Constrained Decoding）在解码阶段限制 token 生成

**对比**：

| 维度 | JSON Mode | Structured Output |
|------|-----------|-------------------|
| 格式保证 | 只保证 JSON 合法 | 保证符合 Schema |
| 字段名 | 不固定 | 固定 |
| 类型 | 不固定 | 固定 |
| 枚举值 | 不限制 | 限制 |
| 可靠性 | 中等 | 高 |
| 适用场景 | 调试、探索 | 生产系统 |

## 3. Pydantic 在这个过程起什么作用？

Pydantic 在 Structured Output 中扮演**双重角色**：

**角色1：Schema 定义**
- Pydantic Model 可以直接生成 JSON Schema
- `model.model_json_schema()` → 传给 OpenAI API

**角色2：输出验证**
- 收到 LLM 输出后，用 Pydantic 反序列化 + 验证
- 类型错误、范围越界、必填缺失都会报错
- 保证下游代码拿到的数据是干净的

**角色3：业务建模**
- IntentResult / ToolCall / ToolResult / AgentResponse
- 这些模型就是 Agent 系统的"领域模型"
- 和 Java DTO 一样，定义了系统的数据契约

**工作流**：
```
Pydantic Model
    ↓
JSON Schema → OpenAI API（约束解码）
    ↓
LLM 输出 JSON
    ↓
Pydantic 验证 → 强类型对象
    ↓
程序消费
```

## 4. 如果 LLM 输出了不符合 Schema 的数据怎么办？

**OpenAI Structured Outputs 的情况**：
- 理论上不会，因为语法约束在解码阶段就限制了
- 但如果 Schema 太复杂或模型能力不足，仍可能失败

**处理策略**（生产系统必备）：

1. **重试**：重新发送请求，可能加更强的约束
2. **降级**：回退到 JSON Mode + 手动解析
3. **默认值**：给未知意图一个 default handler
4. **告警**：记录异常，监控 Structured Output 失败率
5. **人工介入**：高价值任务转人工

**代码示例**：
```python
try:
    result = IntentResult(**llm_output)
except ValidationError as e:
    # 降级处理
    logger.warning(f"Structured output failed: {e}")
    result = IntentResult(intent="unknown", confidence=0.0)
```
