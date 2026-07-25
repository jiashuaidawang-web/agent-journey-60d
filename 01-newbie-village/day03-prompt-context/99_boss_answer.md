# Day 3 Boss 答案

## 1. Context 和 Memory 有什么区别？

**Context（上下文）**：
- 范围：单次请求的所有输入
- 生命周期：当前请求/当前会话
- 内容：System Prompt + 用户输入 + 对话历史 + 检索结果 + 工具结果
- 限制：受 Context Window 限制
- 类比：Java 方法的**参数 + 局部变量**

**Memory（记忆）**：
- 范围：跨会话持久化的信息
- 生命周期：长期保存（数据库/向量库/文件）
- 内容：用户偏好、历史摘要、关键事实、实体信息
- 限制：理论上无限（但检索效率会下降）
- 类比：Java 应用的**数据库 + 缓存**

**关键区别**：

| 维度 | Context | Memory |
|------|---------|--------|
| 范围 | 单次请求 | 跨会话 |
| 生命周期 | 短期 | 长期 |
| 存储 | 内存（请求时组装） | 持久化存储 |
| 容量 | 受 Context Window 限制 | 理论上无限 |
| 变化 | 每次请求都变 | 相对稳定 |

**协作关系**：
```
Memory（长期存储）
    ↓ 检索/提取
Context（当前请求）
    ↓
LLM 推理
```

Agent 系统需要同时管理两者：
- Memory 负责"记住"
- Context 负责"使用"

## 2. 如果 Context 满了，你会怎么裁剪？

**裁剪策略（按优先级）**：

1. **不可裁剪**（必须保留）：
   - System Prompt（角色设定、行为约束）
   - 当前用户输入（最新问题）

2. **优先保留**：
   - 工具调用结果（最近的）
   - RAG 检索结果（当前问题相关的）
   - Memory（用户偏好等关键信息）

3. **优先裁剪**：
   - 远期历史消息
   - 重复/冗余信息

**具体策略**：

- **滑动窗口**：只保留最近 N 轮对话
- **摘要压缩**：把早期历史压缩成一段摘要
- **Token 预算分配**：给每个部分分配 Token 配额
  - System: 20%
  - Memory: 15%
  - Retrieved: 20%
  - History: 30%
  - 预留输出: 15%

**代码实现**：
```python
# 按优先级排序，高优先级优先保留
messages.sort(key=lambda m: m.priority, reverse=True)
for msg in messages:
    if total_tokens + msg.tokens > max_tokens:
        continue  # 裁剪
    result.append(msg)
```

## 3. Prompt Engineering 是否会被 Agent Framework 替代？

**不会完全替代，但会演化**。

**Prompt Engineering 不会消失的原因**：
- 框架（LangChain/LangGraph）内部仍然依赖 Prompt
- System Prompt 设计仍然直接影响 Agent 行为
- 框架只是把 Prompt 模板化，但模板内容仍需人工设计

**Prompt Engineering 的演化**：
- 从"手写 Prompt" → "Prompt 模板 + 变量注入"
- 从"单次 Prompt" → "多轮 Context 组装"
- 从"文本 Prompt" → "Context Engineering"（包含 Memory + Retrieved）

**新的能力要求**：
- Context 组装策略
- Memory 设计（存什么、怎么检索）
- 多 Prompt 协作（不同 Agent 不同 Prompt）
- Prompt 版本管理和 A/B 测试

**结论**：
Prompt Engineering 不会消失，而是升级为 **Context Engineering**。
这是 Agent 工程师的核心能力之一。

## 4. Lost in the Middle 是什么？如何缓解？

**Lost in the Middle**：
- 论文：https://arxiv.org/abs/2307.03172
- 现象：当 Context 很长时，模型对**开头**和**结尾**的注意力高，对**中间**的注意力低
- 原因：Transformer 的注意力分布特性

**影响**：
- 如果把关键信息放在 Context 中间，模型可能"忽略"它
- 长文档检索时，中间部分的召回信息可能不被利用

**缓解策略**：

1. **重要信息放开头或结尾**：
   - System Prompt 放最前面（最高优先级）
   - 最新问题放最后面（最相关）

2. **减少 Context 长度**：
   - 只保留最相关的信息
   - 裁剪冗余内容

3. **多次检索/重排序**：
   - 把关键信息放在多个位置
   - 通过 Reranker 确保关键信息排在前面

4. **显式标注**：
   - 用特殊标记突出关键信息
   - "[重要]" "[必须遵守]"

5. **分段处理**：
   - 长文档分段，每段单独处理
   - 避免单次输入过长 Context
