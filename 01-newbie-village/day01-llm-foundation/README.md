# Day 1: LLM Foundation

## 今日目标

理解 LLM API 的本质：Prompt、Token、Context Window、Streaming、Temperature。

亲手写出第一个 Python LLM Client。

## 📚 学习清单

### 理论 (1.5h)
- [ ] Token 是什么？为什么 Token ≠ Word？
- [ ] Context Window 是什么？为什么有限制？
- [ ] Streaming vs 普通请求的区别
- [ ] Temperature / Top-P / Max Tokens 参数含义
- [ ] System Prompt vs User Prompt vs Assistant Message

### 官方文档
- [ ] OpenAI API Text Generation: https://platform.openai.com/docs/guides/text-generation
- [ ] OpenAI API Streaming: https://platform.openai.com/docs/api-reference/streaming
- [ ] OpenAI API Messages Format: https://platform.openai.com/docs/api-reference/messages

### 编码 (3h)
- [ ] 实现同步调用 (`sync_chat.py`)
- [ ] 实现流式调用 (`stream_chat.py`)
- [ ] 实现模型配置抽象 (`model_config.py`)

## 💻 项目结构

```
day01-llm-foundation/
├── README.md
├── sync_chat.py          # 同步聊天调用
├── stream_chat.py        # 流式聊天调用
├── model_config.py       # 模型配置抽象
└── requirements.txt      # 依赖
```

## 🔧 技术栈

- Python 3.12+
- `openai` SDK (或任意兼容OpenAI格式的SDK)
- Pydantic (用于配置)

## 🐉 Boss Challenge (1h)

回答以下问题（写入 `boss-answer.md`）：

1. **Token 是什么？** 中英文Token化有什么区别？
2. **Context Window 是什么？** 为什么不能无限大？
3. **Streaming 和普通请求有什么区别？** 延迟和成本上呢？
4. **为什么 Agent 应用特别关注 Token？**
5. **为什么不能把所有历史消息无限塞进 Context？**
6. **Temperature 是什么？** 对 Agent 有什么影响？
7. **System Prompt 和 User Prompt 有什么区别？**

## 📌 Java 类比

| Python | Java |
|--------|------|
| `async def` | `CompletableFuture.supplyAsync()` |
| `from typing import Protocol` | `interface` |
| `Pydantic BaseModel` | `DTO + Bean Validation` |
| `List[dict]` messages | `Message[]` |

## ✅ 提交清单

- [x] `README.md` — 今天学到了什么 + 原来以为是什么 + 现在理解是什么
- [x] `sync_chat.py` — 能同步调用LLM并拿到完整回复
- [x] `stream_chat.py` — 能流式逐字输出
- [x] `model_config.py` — 配置可切换不同模型/provider
- [x] `boss-answer.md` — 7个Boss问题答案
- [x] Git Commit

## 🤖 AI辅助规则

第一天不要直接让AI写完整代码。

正确用法：
> "我有10年Java经验，正在学Python。这个概念我不懂，能解释一下吗？然后给我提示，但不要给完整代码。"

错误用法：
> "帮我写一个完整的LLM Client。"

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/80
