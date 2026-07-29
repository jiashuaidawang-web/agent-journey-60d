# Day 3: Prompt Engineering / Context Engineering

> **今日目标**: 掌握 Context 组装技术，这是 Agent 面试最重要的问题
> **核心问题**: Context 和 Memory 有什么区别？

---

## 🎯 今日目标

1. 理解 Prompt Engineering 六要素
   2. 角色设定、指令Intres、背景context、示例、output返回格式、约束
2. 理解 Context Engineering 的本质
   3. Context Engineering 的本质其实是Agent的核心瓶颈之一
   4. 工程师设计的方法论,关注放这么,这么组织,来构建Agent系统
   5. 关注的是System prompt写多长,规则放多少
   6. 历史消息全放还是放最近5论
   7. Rag检索的top-k 这么选,top-3还是top5
   8. 工具结果只放摘要还是放原始json
   9. 长期记忆提取哪些关键事实
3. 实现 ContextBuilder：组装 System + History + Memory + Retrieved + Tool Result
   4. 
4. 实现 Prompt Experiment：对比不同 Prompt 的效果

---

## 📚 必学知识

### 1. Prompt Engineering 六要素

| 要素 | 说明 | 示例 |
|------|------|------|
| Role | 角色设定 | "你是一个Java架构师" |
| Instruction | 任务指令 | "请解释 Spring Boot 自动配置" |
| Context | 背景信息 | "我们的系统有100万DAU" |
| Example | 示例（Few-shot） | "例如：@Autowired 注解..." |
| Output Format | 输出格式 | "请用 Markdown 列表输出" |
| Constraint | 约束条件 | "回答不超过200字" |

### 2. Zero-shot vs Few-shot vs CoT

- **Zero-shot**：不给示例
- **Few-shot**：给 2-5 个示例
- **Chain-of-Thought (CoT)**：让模型"一步步推理"

### 3. Context Engineering（重点）

```
Final Context = System Prompt
              + User Input
              + Conversation History
              + Memory（长期记忆）
              + Retrieved Context（RAG检索结果）
              + Tool Result（工具调用结果）
```

**Context 和 Memory 的区别**：
- **Context**：一次请求的所有输入（短期，当前会话）
- **Memory**：跨会话持久化的信息（长期，用户偏好/历史摘要）

### 4. Context 管理策略

- **Token 限制**：不能超过 Context Window
- **优先级**：System > 当前问题 > 近期历史 > 远期历史
- **裁剪策略**：滑动窗口 / 摘要压缩 / 关键信息提取
- **Lost in the Middle**：模型对中间部分注意力下降

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| OpenAI Prompt Engineering | https://platform.openai.com/docs/guides/prompt-engineering |
| OpenAI Best Practices | https://platform.openai.com/docs/guides/gpt-best-practices |
| Lost in the Middle 论文 | https://arxiv.org/abs/2307.03172 |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Prompt 六要素
- [ ] Context 组装流程
- [ ] Context vs Memory 区别
- [ ] Token 裁剪策略

### 只需理解（L2）
- [ ] Lost in the Middle 现象
- [ ] Context Compression
- [ ] Summarization 策略

---

## 💻 今日编码任务

### 文件结构

```
day03-prompt-context/
├── README.md
├── context_builder.py      # Context 组装器
├── prompt_experiment.py    # Prompt 对比实验
├── requirements.txt
└── boss-answer.md
```

### Task 1: context_builder.py（60min）

实现 ContextBuilder：
- 支持添加 System / History / Memory / Retrieved / Tool Result
- 支持 Token 限制（超出时裁剪）
- 支持优先级排序
- 输出最终 messages 列表

### Task 2: prompt_experiment.py（40min）

实现 Prompt 对比实验：
- 同一个任务，3种 Prompt
- 对比：准确率、Token 消耗、延迟

---

## 🐉 今日 Boss

1. **Context 和 Memory 有什么区别？**
   2. Context包含所有的上下文内容,系统prompt,用户输入,LLM输出,工具调用,rag返回结果,mcp,skill等
   3. Memory 只是长期记忆,缓存下来的
2. **如果 Context 满了，你会怎么裁剪？**
   3. 系统提示词不可以裁剪 
   3. 有多种选择,滑动窗口,只保存最近几轮的回话,如果用户问的问题比较炸乱无章的话,可以使用这个策略
   4. summary 压缩,当碰到用户的问题多,且专一,且轮数多的时候,可以考虑用压缩
   5. 关键字提取,如果有结合rag的话,可以用这个,然后内容放到rag,只保留摘要,如果需要,再去rag中提取原文
3. **Prompt Engineering 是否会被 Agent Framework 替代？**
   4. 不会替代但会演化
   5. 框架内部像langchain,langgraph 还是高度依赖prompt,prompt还是可以影响agent的质量
   6. 后面会变成 prompt模版,只需要动态组装+变量替换,但是模版的设计还是需要人工
4. **Lost in the Middle 是什么？如何缓解？**
   5. 尽量把重要信息放到头跟尾
   6. 使用ropc把transform的注意力平均一下,因为transform天然的就是对首尾有注意力权重高的特性,使用ropc可以平均一下

---

## 🎤 面试题

1. **Agent 的 Context 包含哪些部分？**
   2. 系统提示词 System prompt 放什么：角色定义 + 行为规则 + 输出格式
      3.  你是一个 Java 架构师助手。
        规则：
      - 回答必须包含代码示例
      - 优先使用 Spring Boot 3.x
      - 不确定的事情说"需要确认"
        特点：每个对话都一样，通常固定不变
   3. User Input 用户输入 
      4. 放什么：用户当前这条消息
   4. Conversation history 对话历史
      5. 之前几轮的对话
         6.   特点：
            - 占用最大（随对话增长）
            - 是 Context Engineering 的主要优化对象
            - 常见策略：只保留最近 N 轮 / 历史摘要压缩
   5. Memory 长期记忆
      6.   放什么：跨会话持久化的用户偏好、关键事实
        用户偏好：
  - 主要用 Java 17 + Spring Boot 3
  - 数据库偏好 PostgreSQL
  - 不喜欢用 Lombok

  历史决策：
  - 2026-07-20 决定用 Redisson 而非自研分布式锁

  特点：
  - 跨会话（关掉对话再打开还在）
    - 从历史对话中提取出来的精华（不是原文存储）
      - 类似"用户画像"
        6. Retrieved Context Rag检索结果
           7. 放什么：从外部知识库检索到的相关内容

             用户问："公司内部 RPC 框架怎么用？"

             → 去向量数据库检索 top-3：
                [Doc1] JRPC 快速开始 v2.3 ... 1500 tokens
                [Doc2] JRPC 配置参数详解 ... 2000 tokens
                [Doc3] JRPC 与 Dubbo 对比 ... 1800 tokens

              → 把这 3 段塞进 Context

        特点：
        - 按需检索，不存本地
        - 占用空间大（top-K 直接线性增长）
        - Context Engineering 重点优化：top-K 选几个？摘要还是原文？
   7. Tool Result 工具调用结果
      8.   放什么：Agent 调用工具后返回的数据
    特点：
  - 可能很大（比如数据库查询返回 100 条记录）
  - 常见优化：只放摘要、只放前 N 条
2. **如何设计一个 Context 组装策略？**
   3. 🎯 设计 Context 组装策略的 4 个核心问题

  1. 放什么？（内容选择）
  2. 放多少？（数量控制）
  3. 怎么排？（顺序布局）
  4. 超了怎么办？（溢出处理）

  ---
  一、内容选择策略（放什么）
  
  各组件的取舍原则

  ┌──────────────────────┬─────────────┬────────────────────────────┐
  │         组件         │   优先级    │            策略            │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ System Prompt        │ 🔴 必放     │ 不可省略，但可压缩         │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ User Input           │ 🔴 必放     │ 当前问题，必须放           │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ Memory               │ 🟡 按需     │ 只放与当前问题相关的记忆   │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ Conversation History │ 🟡 策略性放 │ 按时间/重要性筛选          │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ Retrieved Context    │ 🟡 按需     │ 按相关性阈值过滤           │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ Retrieved Context    │ 🟡 按需     │ 按相关性阈值过滤           │
  ├──────────────────────┼─────────────┼────────────────────────────┤
  │ Tool Result          │ 🟡 策略性放 │ 只放关键结果，丢弃中间过程 │
  └──────────────────────┴─────────────┴────────────────────────────┘

  Memory 的选择策略

  # 错误做法：全量塞入
  memory = get_all_memories(user_id)  # 可能有 100 条

  # 正确做法：按当前问题检索相关记忆
  relevant_memories = search_memories(
      query=user_input,      # 用当前问题去检索
      top_k=5,               # 只取最相关的 5 条
      threshold=0.7          # 相似度低于 0.7 的丢弃
  )

  ---
  二、数量控制策略（放多少）

  1. Conversation History — 3 种策略

  策略 A：滑动窗口（最常用）
  ─────────────────────────────
  只保留最近 N 轮（如 N=10）
  优点：简单、稳定
  缺点：可能丢失早期关键信息

  策略 B：摘要压缩
  ─────────────────────────────
  旧对话 → 用 LLM 生成摘要 → 只保留摘要
  优点：保留关键信息，节省空间
  缺点：摘要可能丢失细节

  策略 C：混合策略（推荐）
  ─────────────────────────────
  最近 5 轮：完整保留（细节不丢失）
  5 轮之前：压缩为摘要

  def assemble_history(messages: list, max_rounds: int = 5):
      """混合策略：近期完整 + 远期摘要"""
      recent = messages[-max_rounds:]           # 最近 5 轮完整保留
      older = messages[:-max_rounds]            # 更早的

      if older:
          summary = summarize(older)           # 压缩成一段摘要
          return [summary] + recent
      return recent

  2. Retrieved Context — 动态 top-K

  def assemble_rag(query: str, free_space: int) -> list:
      """根据剩余空间动态决定 top-K"""
      # 先检索多一些
      candidates = retrieve(query, top_k=20)

      # 按相关性排序，逐个塞入，直到空间用完
      selected = []
      used_tokens = 0

      for doc in candidates:
          doc_tokens = count_tokens(doc)
          if used_tokens + doc_tokens > free_space * 0.8:  # 留 20% buffer
              break
          selected.append(doc)
          used_tokens += doc_tokens

      return selected

  3. Tool Result — 截断 + 摘要

  def assemble_tool_result(result: dict, max_tokens: int = 2000) -> str:
      """太大的工具结果做截断或摘要"""
      raw = json.dumps(result, ensure_ascii=False)

      if count_tokens(raw) <= max_tokens:
          return raw  # 放得下，原样放

      # 放不下，做摘要
      return summarize_tool_result(result, max_tokens)

  ---
  三、顺序布局策略（怎么排）
  
  LLM 的位置偏见（Position Bias）

  LLM 对 Context 中不同位置的信息注意力不均匀：

  注意力强度
    ↑
    │  ██████████ ← 开头（System Prompt）记得最牢
    │  ████████
    │  ██████     ← 中间（容易遗忘，"迷失在中间"）
    │  ████████
    │  ██████████ ← 结尾（User Input / 最近消息）记得最牢
    └──────────────────────────→ 位置

  推荐布局

  ┌─────────────────────────────────────────┐
  │ 位置 1: System Prompt                    │ ← 放角色 + 核心规则（开头注意力强）
  ├─────────────────────────────────────────┤
  │ 位置 2: Memory（长期记忆）               │ ← 放用户偏好、关键事实
  ├─────────────────────────────────────────┤
  │ 位置 3: Retrieved Context（RAG）         │ ← 放检索到的参考资料
  ├─────────────────────────────────────────┤
  │ 位置 4: Conversation History（近期）     │ ← 放最近几轮对话
  ├─────────────────────────────────────────┤
  │ 位置 5: User Input（当前问题）           │ ← 放最后（离回答最近，记得最牢）
  └─────────────────────────────────────────┘

  原则：
  - 最重要的规则 → 放 System Prompt
  - 当前问题 → 放最后（Recency Bias）
  - 参考资料 → 放中间，但开头加一句总结
  
  ---
  四、溢出处理策略（超了怎么办）

  Token 预算分配

  class ContextBudget:
      """Context 预算分配器"""

      def __init__(self, max_tokens: int = 20000):
          self.max_tokens = max_tokens
          self.allocations = {
              "system_prompt": 0.15,     # 15% → 3000 tokens
              "memory": 0.10,            # 10% → 2000 tokens
              "rag_context": 0.30,       # 30% → 6000 tokens
              "conversation_history": 0.25,  # 25% → 5000 tokens
              "tool_result": 0.10,       # 10% → 2000 tokens
              "user_input": 0.05,        # 5%  → 1000 tokens（通常用不完）
              "buffer": 0.05,            # 5%  → 预留 buffer
          }

      def get_budget(self, component: str) -> int:
          return int(self.max_tokens * self.allocations[component])

  溢出时的降级链

  第 1 步：裁剪 Tool Result（摘要替代原文）
      ↓ 还超？
  第 2 步：降低 RAG top-K（10 → 5 → 3）
      ↓ 还超？
  第 3 步：压缩 Conversation History（完整 → 摘要）
      ↓ 还超？
  第 4 步：精简 System Prompt（删掉不重要的规则）
      ↓ 还超？
  第 5 步：拒绝处理（返回"问题太复杂，请拆分"）

  def assemble_with_fallback(self, components: dict) -> list:
      """带降级策略的组装"""
      # 尝试完整组装
      context = self.assemble(components)

      # 逐级降级
      while count_tokens(context) > self.max_tokens:
          if components["tool_result"]:
              components["tool_result"] = summarize(components["tool_result"])
          elif len(components["rag"]) > 3:
              components["rag"] = components["rag"][:3]
          elif len(components["history"]) > 5:
              components["history"] = compress_history(components["history"])
          else:
              raise ContextOverflowError("无法压缩到限制内")

          context = self.assemble(components)

      return context

  ---
  五、完整设计：ContextAssembler 类
  
  class ContextAssembler:
      """Context 组装器"""

      def __init__(self, max_tokens: int = 20000):
          self.max_tokens = max_tokens
          self.budget = ContextBudget(max_tokens)

      def assemble(self,
                   system_prompt: str,
                   user_input: str,
                   history: list = None,
                   memories: list = None,
                   rag_docs: list = None,
                   tool_results: list = None,
                   ) -> list[dict]:
          """组装最终 Context"""

          messages = []
          used_tokens = 0

          # 1. System Prompt（必放）
          messages.append({"role": "system", "content": system_prompt})
          used_tokens += count_tokens(system_prompt)

          # 2. Memory（按需，检索相关记忆）
          if memories:
              relevant = self._select_relevant_memories(memories, user_input)
              if relevant:
                  mem_str = self._format_memories(relevant)
                  messages.append({"role": "system", "content": f"用户记忆：{mem_str}"})
                  used_tokens += count_tokens(mem_str)

          # 3. RAG（按预算动态选择）
          if rag_docs:
              free = self.budget.get_budget("rag_context") - used_tokens
              selected = self._select_rag_docs(rag_docs, free)
              rag_str = self._format_rag(selected)
              messages.append({"role": "system", "content": f"参考资料：{rag_str}"})
              used_tokens += count_tokens(rag_str)

          # 4. History（混合策略：近期完整 + 远期摘要）
          if history:
              free = self.budget.get_budget("conversation_history")
              trimmed = self._trim_history(history, free)
              messages.extend(trimmed)
              used_tokens += sum(count_tokens(m["content"]) for m in trimmed)

          # 5. User Input（必放，放最后）
          messages.append({"role": "user", "content": user_input})

          return messages

  ---
  📌 策略总结表

  ┌──────────┬───────────────────────────────────┬─────────────────────────┐
  │   维度   │               策略                │        适用场景         │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 内容选择 │ 相关性过滤                        │ Memory、RAG             │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 数量控制 │ 滑动窗口                          │ History                 │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 数量控制 │ 动态 top-K                        │ RAG                     │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 数量控制 │ 摘要压缩                          │ Tool Result、旧 History │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 顺序布局 │ 重要规则开头、当前问题结尾        │ 所有场景                │
  ├──────────┼───────────────────────────────────┼─────────────────────────┤
  │ 溢出处理 │ 降级链（Tool→RAG→History→System） │ 空间不足时              │
  └──────────┴───────────────────────────────────┴─────────────────────────┘

  ---
  💡 一句话记住

  ▎ Context 组装 = 按相关性选内容 + 按预算控数量 + 按位置排布局 + 按优先级做降级
   4. 
   5. 
   6. 
      3. 各部分在 Context Window 中的占比（典型场景）

  System Prompt     ████ 10K（5%）
  User Input        █ 2K（1%）
  Conversation Hist ████████████ 60K（30%）    ← 最大头
  Memory            ████ 10K（5%）
  Retrieved Context ████████ 40K（20%）        ← RAG 容易膨胀
  Tool Result       ██████ 25K（12.5%）
  ─────────────────────────────────
  Free Space        53K（26.5%）

一次完整的 Agent 推理流程

  用户输入 "帮我分析贵州茅台"
          ↓
  ┌─────────────────────────────────────┐
  │ 组装 Context：                       │
  │  1. System Prompt（角色定义）        │
  │  2. User Input "帮我分析贵州茅台"    │
  │  3. 最近 10 轮对话                   │
  │  4. Memory（用户偏好：关注白酒板块） │
  │  5. RAG（检索茅台相关研报 top-3）    │
  │  6. （暂无 Tool Result）             │
  └─────────────────────────────────────┘
          ↓
    塞进 Context Window
          ↓
      LLM 推理
          ↓
    输出："调用 stock_tool(贵州茅台)"
          ↓
    工具执行 → 返回行情数据
          ↓
    把 Tool Result 加入 Context
          ↓
     再次推理 → 输出最终回答
 记忆口诀
  
  ┌──────────────────────┬──────────────────┬──────────────┐
  │         组件         │      一句话      │     来源     │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ System Prompt        │ "你是谁"         │ 开发者写死   │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ User Input           │ "现在问什么"     │ 用户实时输入 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Conversation History │ "刚才聊了啥"     │ 本次会话累积 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Memory               │ "记得你是谁"     │ 跨会话持久化 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Retrieved Context    │ "查到的资料"     │ RAG 检索     │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ System Prompt        │ "你是谁"         │ 开发者写死   │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ User Input           │ "现在问什么"     │ 用户实时输入 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Conversation History │ "刚才聊了啥"     │ 本次会话累积 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Memory               │ "记得你是谁"     │ 跨会话持久化 │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Retrieved Context    │ "查到的资料"     │ RAG 检索     │
  ├──────────────────────┼──────────────────┼──────────────┤
  │ Tool Result          │ "工具返回的数据" │ 函数调用     │
  └──────────────────────┴──────────────────┴──────────────┘

3. **Memory 有哪几种类型？如何实现？**
   4. 长期记忆,短期记忆
   5. Memory 是 Agent 系统最复杂的部分之一。我按存储时间 + 实现方式两个维度给你讲清楚。

  ---
  🧠 Memory 的 3 种类型（按存储时间）

  ┌─────────────────────────────────────────────────────────┐
  │                                                         │
  │  1. 短期记忆（Short-term / Working Memory）              │
  │     → 当前会话，对话结束即丢失                           │
  │     → 就是 Conversation History                         │
  │                                                         │
  │  2. 长期记忆（Long-term Memory）                         │
  │     → 跨会话持久化                                       │
  │     → 分为两类：                                         │
  │                                                         │
  │     2a. 情节记忆（Episodic）                             │
  │         → "上次我们聊了什么"                             │
  │         → 事件、对话摘要                                 │
  │                                                         │
  │     2b. 语义记忆（Semantic）                             │
  │         → "用户喜欢什么、偏好是什么"                      │
  │         → 用户画像、偏好、事实                            │
  │                                                         │
  │  3. 程序性记忆（Procedural）                             │
  │     → "怎么做某件事"                                     │
  │     → 技能、工具使用流程                                 │
  │     → 通常编码在 System Prompt 或 Skill 里               │
  │                                                         │
  └─────────────────────────────────────────────────────────┘

  ---
  一、短期记忆（Short-term Memory）
  
  是什么

  就是当前会话的对话历史，放在 messages 数组里。

  对话开始 ──────────────────────────────────────→ 对话结束
  │                                                │
  │  短期记忆（存在 Context Window 里）              │
  │  会话结束 → 丢失                                 │

  实现方式

  # 最简单的实现：就是一个 list
  conversation_history = [
      {"role": "user", "content": "帮我写个 Redis 锁"},
      {"role": "assistant", "content": "好的，用 Redisson..."},
      {"role": "user", "content": "换成原生 Redis"},
      {"role": "assistant", "content": "用 SETNX..."},
  ]

  问题：对话越长，token 越多，最终溢出。

  解决：滑动窗口 / 摘要压缩（上一轮讲过）

  ---
  二、长期记忆（Long-term Memory）
  
  2a. 情节记忆（Episodic Memory）

  存什么：发生过的事件

  "2026-07-20 用户决定用 Redisson 而不是自研分布式锁"
  "2026-07-15 用户问了 Spring Boot 集成 Redis 的问题"
  "2026-07-10 用户的项目用了 PostgreSQL 而非 MySQL"

  实现方式：

  class EpisodicMemory:
      """情节记忆：存储历史事件"""

      def __init__(self, storage_path: str = "./memory/episodic.json"):
          self.storage_path = storage_path
          self.events = self._load()

      def record(self, event: str, metadata: dict = None):
          """记录一个事件"""
          self.events.append({
              "timestamp": datetime.now().isoformat(),
              "event": event,
              "metadata": metadata or {},
          })
          self._save()

      def recall(self, query: str, top_k: int = 5) -> list:
          """根据当前问题检索相关事件"""
          # 简单实现：关键词匹配
          # 生产实现：向量检索
          results = []
          for event in self.events:
              if self._is_relevant(event["event"], query):
                  results.append(event)
          return results[-top_k:]

      def summarize(self, days: int = 7) -> str:
          """生成最近 N 天的事件摘要"""
          recent = [e for e in self.events if within_days(e["timestamp"], days)]
          return f"最近 {days} 天发生了 {len(recent)} 个事件：{format_events(recent)}"

  存储结构：

  {
    "user_id": "user_001",
    "events": [
      {
        "timestamp": "2026-07-20T10:30:00",
        "event": "用户决定使用 Redisson 实现分布式锁",
        "session_id": "sess_123",
        "importance": 0.8
      },
      {
        "timestamp": "2026-07-15T14:20:00",
        "event": "用户询问 Spring Boot 集成 Redis 的方案",
        "session_id": "sess_118",
        "importance": 0.6
      }
    ]
  }

  ---
  2b. 语义记忆（Semantic Memory）
  
  存什么：用户偏好、画像、事实

  用户偏好：
  - 语言：Java 17
  - 框架：Spring Boot 3.x
  - 数据库：PostgreSQL
  - 代码风格：不喜欢 Lombok，偏好显式 Getter/Setter

  用户信息：
  - 职业：架构师
  - 关注领域：分布式系统、高并发

  实现方式：

  class SemanticMemory:
      """语义记忆：存储用户偏好和事实"""

      def __init__(self, storage_path: str = "./memory/semantic.json"):
          self.storage_path = storage_path
          self.facts = self._load()  # 事实库

      def extract_and_store(self, conversation: list):
          """从对话中提取事实"""
          # 用 LLM 从对话中提取关键事实
          prompt = f"""从以下对话中提取用户偏好和关键事实：

  对话：{conversation}

  输出 JSON 格式：
  {
    "preferences": ["偏好1", "偏好2"],
    "facts": ["事实1", "事实2"]
  }"""

          extracted = llm_extract(prompt)

          # 合并到事实库（去重）
          for pref in extracted["preferences"]:
              if pref not in self.facts["preferences"]:
                  self.facts["preferences"].append(pref)

          self._save()

      def get_relevant(self, query: str) -> list:
          """检索与当前问题相关的记忆"""
          # 生产环境用向量检索
          relevant = []
          for fact in self.facts["preferences"] + self.facts["facts"]:
              if self._similarity(fact, query) > 0.7:
                  relevant.append(fact)
          return relevant

      def format_for_context(self) -> str:
          """格式化为 System Prompt 片段"""
          return f"""用户偏好：
  {chr(10).join(f"- {p}" for p in self.facts["preferences"])}"""

  存储结构：

  {
    "user_id": "user_001",
    "preferences": [
      "使用 Java 17 + Spring Boot 3.x",
      "数据库偏好 PostgreSQL",
      "不喜欢 Lombok",
      "代码注释偏好中文"
    ],
    "facts": [
      "用户在做一个电商系统",
      "团队有 10 个后端开发",
      "项目预计 2026-12 上线"
    ],
    "last_updated": "2026-07-28T10:30:00"
  }

  ---
  三、长期记忆的完整架构

  ┌─────────────────────────────────────────────────────────┐
  │                    Memory System                         │
  │                                                         │
  │  ┌──────────────┐       ┌──────────────┐               │
  │  │  写入流程    │       │  读取流程    │               │
  │  └──────┬───────┘       └──────┬───────┘               │
  │         │                      │                        │
  │         ▼                      ▼                        │
  │  ┌──────────────┐       ┌──────────────┐               │
  │  │ 1. 对话结束  │       │ 1. 用户输入  │               │
  │  │   触发提取   │       │   触发检索   │               │
  │  └──────┬───────┘       └──────┬───────┘               │
  │         │                      │                        │
  │         ▼                      ▼                        │
  │  ┌──────────────┐       ┌──────────────┐               │
  │  │ 2. LLM 提取  │       │ 2. 向量检索  │               │
  │  │   偏好/事实  │       │   相关记忆   │               │
  │  └──────┬───────┘       └──────┬───────┘               │
  │         │                      │                        │
  │         ▼                      ▼                        │
  │  ┌──────────────┐       ┌──────────────┐               │
  │  │ 3. 存入向量  │       │ 3. 注入      │               │
  │  │   数据库     │       │   Context    │               │
  │  └──────────────┘       └──────────────┘               │
  │                                                         │
  └─────────────────────────────────────────────────────────┘

  ---
  四、向量检索实现（生产级 Memory 核心）

  为什么需要向量检索

  用户问："Redis 集群怎么配？"

  相关记忆：
  - "用户用过 Redis Cluster" ← 语义相关 ✓
  - "用户昨天吃了火锅" ← 无关 ✗
  
  关键词匹配做不了，需要语义相似度。

  实现

  import numpy as np
  from openai import OpenAI

  class VectorMemory:
      """向量记忆：基于语义相似度的记忆检索"""

      def __init__(self):
          self.client = OpenAI()
          self.memories = []       # 记忆文本
          self.embeddings = []     # 对应的向量

      def embed(self, text: str) -> list[float]:
          """文本向量化"""
          response = self.client.embeddings.create(
              model="text-embedding-3-small",
              input=text,
          )
          return response.data[0].embedding

      def store(self, text: str):
          """存入一条记忆"""
          vector = self.embed(text)
          self.memories.append(text)
          self.embeddings.append(vector)

      def recall(self, query: str, top_k: int = 5) -> list[str]:
          """检索相关记忆"""
          query_vec = self.embed(query)

          # 计算余弦相似度
          scores = []
          for idx, vec in enumerate(self.embeddings):
              sim = self._cosine_similarity(query_vec, vec)
              scores.append((idx, sim))

          # 取 top-K
          scores.sort(key=lambda x: x[1], reverse=True)
          return [self.memories[idx] for idx, _ in scores[:top_k]]

      def _cosine_similarity(self, a, b) -> float:
          """余弦相似度"""
          a, b = np.array(a), np.array(b)
          return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

  生产环境用向量数据库

  # 用 ChromaDB（轻量级，本地可用）
  import chromadb

  class ProductionMemory:
      def __init__(self):
          self.client = chromadb.PersistentClient(path="./memory/chroma")
          self.collection = self.client.get_or_create_collection("user_memories")

      def store(self, text: str, metadata: dict = None):
          self.collection.add(
              documents=[text],
              ids=[f"mem_{datetime.now().timestamp()}"],
              metadatas=[metadata or {}],
          )

      def recall(self, query: str, top_k: int = 5) -> list:
          results = self.collection.query(
              query_texts=[query],
              n_results=top_k,
          )
          return results["documents"][0]


          extracted = llm_extract(prompt)

          # 合并到事实库（去重）
          for pref in extracted["preferences"]:
              if pref not in self.facts["preferences"]:
                  self.facts["preferences"].append(pref)

          self._save()

      def get_relevant(self, query: str) -> list:
          """检索与当前问题相关的记忆"""
          # 生产环境用向量检索
          relevant = []
          for fact in self.facts["preferences"] + self.facts["facts"]:
              if self._similarity(fact, query) > 0.7:
                  relevant.append(fact)
          return relevant

      def format_for_context(self) -> str:
          """格式化为 System Prompt 片段"""
          return f"""用户偏好：
  {chr(10).join(f"- {p}" for p in self.facts["preferences"])}"""

  存储结构：

  遗忘机制（防止记忆爆炸）

  class MemoryWithDecay:
      """带衰减的记忆系统"""

      def cleanup(self):
          """定期清理"""
          for mem in self.memories:
              # 1. 时间衰减：越久远的记忆权重越低
              age_days = (now() - mem.created_at).days
              time_score = exp(-age_days / 30)  # 30天半衰期

              # 2. 使用频率：经常被检索到的记忆更重要
              access_score = log(mem.access_count + 1)

              # 3. 综合评分
              mem.score = time_score * access_score

          # 删除低分记忆
          self.memories = [m for m in self.memories if m.score > 0.1]

  ---
  六、总结对比表
  
  ┌────────────┬───────────┬──────────┬───────────────┬─────────────┐
  │    类型    │  存什么   │ 生命周期 │   实现方式    │  检索方式   │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 短期记忆   │ 对话历史  │ 当前会话 │ list[dict]    │ 滑动窗口    │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 情节记忆   │ 事件记录  │ 永久     │ JSON / DB     │ 时间 + 语义 │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 语义记忆   │ 偏好/事实 │ 永久     │ JSON / DB     │ 向量检索    │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 程序性记忆 │ 技能/流程 │ 固化     │ System Prompt │ 直接注入    │
  └────────────┴───────────┴──────────┴───────────────┴─────────────┘
  │  │   偏好/事实  │       │   相关记忆   │               │
  │  └──────┬───────┘       └──────┬───────┘               │
  │         │                      │                        │
  │         ▼                      ▼                        │
  │  ┌──────────────┐       ┌──────────────┐               │
  │  │ 3. 存入向量  │       │ 3. 注入      │               │
  │  │   数据库     │       │   Context    │               │
  │  └──────────────┘       └──────────────┘               │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
  
  ---
  四、向量检索实现（生产级 Memory 核心）
  
  为什么需要向量检索
  
  用户问："Redis 集群怎么配？"
  
  相关记忆：
  - "用户用过 Redis Cluster" ← 语义相关 ✓
  - "用户昨天吃了火锅" ← 无关 ✗
  
  关键词匹配做不了，需要语义相似度。

  实现

  import numpy as np
  from openai import OpenAI

  class VectorMemory:
      """向量记忆：基于语义相似度的记忆检索"""

      def __init__(self):
          self.client = OpenAI()
          self.memories = []       # 记忆文本
          self.embeddings = []     # 对应的向量

      def embed(self, text: str) -> list[float]:
          """文本向量化"""
          response = self.client.embeddings.create(
              model="text-embedding-3-small",
              input=text,
          )
          return response.data[0].embedding

      def store(self, text: str):
          """存入一条记忆"""
          vector = self.embed(text)
          self.memories.append(text)
          self.embeddings.append(vector)

      def recall(self, query: str, top_k: int = 5) -> list[str]:
          """检索相关记忆"""
          query_vec = self.embed(query)

          # 计算余弦相似度
          scores = []
          for idx, vec in enumerate(self.embeddings):
              sim = self._cosine_similarity(query_vec, vec)
              scores.append((idx, sim))

          # 取 top-K
          scores.sort(key=lambda x: x[1], reverse=True)
          return [self.memories[idx] for idx, _ in scores[:top_k]]

      def _cosine_similarity(self, a, b) -> float:
          """余弦相似度"""
          a, b = np.array(a), np.array(b)
          return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

  生产环境用向量数据库

  # 用 ChromaDB（轻量级，本地可用）
  import chromadb

  class ProductionMemory:
      def __init__(self):
          self.client = chromadb.PersistentClient(path="./memory/chroma")
          self.collection = self.client.get_or_create_collection("user_memories")

      def store(self, text: str, metadata: dict = None):
          self.collection.add(
              documents=[text],
              ids=[f"mem_{datetime.now().timestamp()}"],
              metadatas=[metadata or {}],
          )

      def recall(self, query: str, top_k: int = 5) -> list:
          results = self.collection.query(
              query_texts=[query],
              n_results=top_k,
          )
          return results["documents"][0]

  ---
  五、Memory 生命周期管理

  写入时机

  class Agent:
      def chat(self, user_input: str):
          # 1. 检索相关记忆
          memories = self.memory.recall(user_input)

          # 2. 组装 Context
          context = self.assemble_context(user_input, memories)

          # 3. 调用 LLM
          response = self.llm.complete(context)

          # 4. 返回结果
          return response

      def on_session_end(self):
          """会话结束时提取记忆"""
          # 用 LLM 从本次对话中提取关键信息
          new_memories = self.llm.extract_memories(self.conversation_history)

          # 存入长期记忆
          for mem in new_memories:
              self.memory.store(mem)

  遗忘机制（防止记忆爆炸）

  class MemoryWithDecay:
      """带衰减的记忆系统"""

      def cleanup(self):
          """定期清理"""
          for mem in self.memories:
              # 1. 时间衰减：越久远的记忆权重越低
              age_days = (now() - mem.created_at).days
              time_score = exp(-age_days / 30)  # 30天半衰期

              # 2. 使用频率：经常被检索到的记忆更重要
              access_score = log(mem.access_count + 1)

              # 3. 综合评分
              mem.score = time_score * access_score

          # 删除低分记忆
          self.memories = [m for m in self.memories if m.score > 0.1]

  ---
  六、总结对比表

  ┌────────────┬───────────┬──────────┬───────────────┬─────────────┐
  │    类型    │  存什么   │ 生命周期 │   实现方式    │  检索方式   │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 短期记忆   │ 对话历史  │ 当前会话 │ list[dict]    │ 滑动窗口    │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 情节记忆   │ 事件记录  │ 永久     │ JSON / DB     │ 时间 + 语义 │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 语义记忆   │ 偏好/事实 │ 永久     │ JSON / DB     │ 向量检索    │
  ├────────────┼───────────┼──────────┼───────────────┼─────────────┤
  │ 程序性记忆 │ 技能/流程 │ 固化     │ System Prompt │ 直接注入    │
  └────────────┴───────────┴──────────┴───────────────┴─────────────┘

  类比 Java 开发

  ┌──────────────┬───────────────────────────────┐
  │ Agent Memory │         Java 世界类比         │
  ├──────────────┼───────────────────────────────┤
  │ 短期记忆     │ HttpSession（会话结束即丢失） │
  ├──────────────┼───────────────────────────────┤
  │ 长期记忆     │ MySQL 用户表（持久化）        │
  ├──────────────┼───────────────────────────────┤
  │ 向量检索     │ Elasticsearch 语义搜索        │
  ├──────────────┼───────────────────────────────┤
  │ 记忆提取     │ AOP 切面，在会话结束时触发    │
  ├──────────────┼───────────────────────────────┤
  │ 记忆衰减     │ Redis TTL，过期自动删除       │
  └──────────────┴───────────────────────────────┘

  ---
  💡 一句话记住

  ▎ 短期记忆 = 对话历史（list）
  ▎ 长期记忆 = 用户偏好（向量数据库）
  ▎ 核心流程 = 会话结束提取 → 向量存储 → 下次对话检索 → 注入 Context
4. **Prompt Engineering 在 Agent 时代还重要吗？**
   5. 重要啊,刚才不是说了吗,现在重主要的框架 langchain 跟langgrauph 还高度依赖prompt
   6. 只不过不是单独的提示词了,需要提示词模版,动态注入变量,但是还需人工设计的啊

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| context_builder.py | 35分 |
| prompt_experiment.py | 25分 |
| README 学习总结 | 20分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 4题完成
- [ ] README 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 4: Tool Calling**
