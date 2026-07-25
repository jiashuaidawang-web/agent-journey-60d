# Day 3: Prompt Engineering / Context Engineering

> **今日目标**: 掌握 Context 组装技术，这是 Agent 面试最重要的问题
> **核心问题**: Context 和 Memory 有什么区别？

---

## 🎯 今日目标

1. 理解 Prompt Engineering 六要素
2. 理解 Context Engineering 的本质
3. 实现 ContextBuilder：组装 System + History + Memory + Retrieved + Tool Result
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
2. **如果 Context 满了，你会怎么裁剪？**
3. **Prompt Engineering 是否会被 Agent Framework 替代？**
4. **Lost in the Middle 是什么？如何缓解？**

---

## 🎤 面试题

1. **Agent 的 Context 包含哪些部分？**
2. **如何设计一个 Context 组装策略？**
3. **Memory 有哪几种类型？如何实现？**
4. **Prompt Engineering 在 Agent 时代还重要吗？**

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
