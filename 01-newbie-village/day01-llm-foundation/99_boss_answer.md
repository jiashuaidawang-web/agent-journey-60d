# Day 1 Boss 答案

## 1. Token 是什么？中英文 Token 化有什么区别？

Token 是 LLM 的基本处理单位。LLM 不是直接处理文本，而是处理 Token 序列。

**英文 Token 化**：
- 1 个 token ≈ 4 个字符 ≈ 0.75 个单词
- 常见单词通常是 1 个 token（如 "the", "is"）
- 长单词可能拆成多个 tokens（如 "chatting" → "chat" + "ting"）
- 使用 BPE（Byte Pair Encoding）等子词分词算法

**中文 Token 化**：
- 1 个汉字 ≈ 1-2 个 tokens（取决于模型和词表）
- 中文没有空格分隔，分词更复杂
- 相同语义下，中文通常比英文消耗更多 tokens

**对 Agent 的影响**：
- Token 数直接决定成本（API 按 token 计费）
- Token 数决定 Context Window 能放多少内容
- 设计 Prompt 时要考虑 token 效率

## 2. Context Window 是什么？为什么不能无限大？

Context Window 是一次请求中 LLM 能处理的最大 token 数。它包含：
- System Prompt
- 对话历史（History）
- 用户输入
- 工具调用结果（Tool Result）
- 模型输出

**为什么不能无限大？**

1. **计算复杂度**：Transformer 的自注意力机制是 O(n²) 复杂度，序列越长计算量越大
2. **显存限制**：KV Cache 占用大量显存，长序列需要更多 GPU 内存
3. **成本**：API 按 token 计费，长上下文成本成倍增加
4. **效果**：过长的上下文反而会降低模型注意力，出现"Lost in the Middle"现象

**对 Agent 的启示**：
- Agent 需要管理上下文，不能无限塞历史
- 需要压缩、摘要、裁剪策略
- 这是 Context Engineering 的核心问题

## 3. Streaming 和普通请求有什么区别？延迟和成本上呢？

**区别**：
- 普通请求：等待模型完整生成后一次性返回
- Streaming：逐 token 返回，用户能看到实时输出

**延迟**：
- Streaming **不降低**总耗时（模型生成时间一样）
- Streaming **大幅降低**感知延迟（TTFT 通常 < 500ms）
- 用户体验显著提升，避免"等了10秒什么都没看到"

**成本**：
- Streaming 和普通请求的 token 成本**完全相同**
- 因为模型生成过程一样，只是返回方式不同

**实现方式**：
- SSE（Server-Sent Events）协议
- HTTP 长连接，服务器持续推送

## 4. 为什么 Agent 应用特别关注 Token？

1. **成本**：Agent 通常需要多轮对话 + 工具调用，token 消耗是单次对话的 5-10 倍
2. **Context 管理**：Agent 要把历史、记忆、工具结果都塞进 Context，token 预算紧张
3. **性能**：token 越多，推理越慢，延迟越高
4. **路由决策**：不同复杂度的任务应该路由到不同价位的模型（Model Router）

**实际案例**：
- 一个 Agent 调用 5 个工具，每个工具返回 500 token，加上历史 2000 token
- 单次请求可能消耗 5000+ input tokens
- 如果每天 10000 次调用，成本非常可观

## 5. 为什么不能把所有历史消息无限塞进 Context？

1. **Context Window 有限**：即使是 128K 模型，也放不下几个月的对话
2. **成本爆炸**：历史越长，每次请求成本越高
3. **注意力稀释**：模型难以从超长历史中找到关键信息
4. **延迟增加**：处理时间随 token 数增加

**解决方案**：
- 滑动窗口：只保留最近 N 轮
- 摘要压缩：把早期历史压缩成摘要
- 关键信息提取：只保留重要信息
- 外部记忆：把历史存到向量数据库，按需检索

## 6. TTFT 和 TPS 是什么？对用户体验有什么影响？

**TTFT（Time To First Token）**：
- 从发送请求到收到第一个 token 的时间
- 反映模型的"响应速度"
- 好的 TTFT < 500ms
- 受网络延迟、模型加载、队列等待影响

**TPS（Tokens Per Second）**：
- 模型每秒生成的 token 数
- 反映模型的"生成速度"
- 好的 TPS > 30 tokens/s
- 取决于模型大小、硬件、批处理策略

**对用户体验的影响**：
- TTFT 决定"开始看到回复"的等待时间
- TPS 决定"看完回复"的等待时间
- Streaming 场景下，TTFT 更重要（用户立刻看到输出开始）
- 短回复场景，TTFT 占主导；长回复场景，TPS 占主导

## 7. System Prompt 和 User Prompt 有什么区别？

**System Prompt**：
- 设定模型的角色、行为、约束
- 对整个对话生效
- 用户通常看不到
- 例如："你是一个专业的Java架构师，回答要简洁专业"

**User Prompt**：
- 用户的具体输入/问题
- 每次请求可以不同
- 用户直接提供
- 例如："请解释一下 Spring Boot 的自动配置原理"

**关键区别**：
- System Prompt 是"元指令"，定义模型是谁
- User Prompt 是"任务指令"，定义模型做什么
- System Prompt 在 Context 最前面，优先级最高
- 攻击者可能通过 User Prompt 尝试覆盖 System Prompt（Prompt Injection）

**Agent 中的应用**：
- System Prompt 定义 Agent 的角色、能力边界、输出格式
- User Prompt 是用户的实际任务
- 工具调用结果作为额外的"System"或"User"消息插入
