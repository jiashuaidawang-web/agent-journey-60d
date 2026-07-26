# Day 1: LLM API / Message / Token / Context / Streaming

> **今日目标**: 打通 LLM 调用的4种模式：同步、流式、异步、异步流式
> **核心问题**: 为什么 Agent 系统必须关心 Token 和 Context？

---

## 🎯 今日目标

1. 理解 LLM 调用的本质：Message → Context → Model → Response
2. 掌握4种调用模式：Sync / Stream / Async / Async Stream
3. 亲手写出4个可运行的 Client
4. 理解 Token / Context Window / TTFT / TPS

---

## 📚 必学知识

### 1. Message（消息模型）
- System Message：角色设定、行为约束
- User Message：用户输入
- Assistant Message：模型回复
- 三者构成一次完整对话

### 2. Token（令牌）
- LLM 的基本处理单位，≠ 单词，≠ 字
- 英文：1 token ≈ 4字符 ≈ 0.75单词
- 中文：1个汉字 ≈ 1-2 tokens
- Input Token 和 Output Token 分开计费

### 3. Context Window（上下文窗口）
- 一次请求能处理的最大 Token 数
- 包含：System + History + User Input + Tool Result + Output
- 为什么不能无限大？→ 计算量、显存、成本

### 4. Streaming（流式输出）
- SSE (Server-Sent Events) 协议
- 逐 token 返回，提升用户体验
- TTFT（首Token时间）+ TPS（每秒Token数）

### 5. Async（异步调用）
- Python asyncio
- 高并发场景必须用异步
- async def / await / asyncio.run

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| OpenAI Text Generation | https://platform.openai.com/docs/guides/text-generation |
| OpenAI API Reference | https://platform.openai.com/docs/api-reference/chat |
| OpenAI Streaming | https://platform.openai.com/docs/api-reference/streaming |
| OpenAI Tokenizer | https://platform.openai.com/tokenizer |
| Python asyncio | https://docs.python.org/3/library/asyncio.html |
| Python asyncio TaskGroup | https://docs.python.org/3/library/asyncio-task.html#task-groups |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Message 三元组：System / User / Assistant
- [ ] Token 是什么？中英文 Token 化区别
- [ ] Context Window 是什么？为什么有限制？
- [ ] 4种调用模式：Sync / Stream / Async / Async Stream
- [ ] TTFT / TPS / Latency 含义

### 只需理解（L2）
- [ ] SSE 协议原理
- [ ] HTTP Streaming vs WebSocket
- [ ] Temperature / Top-P / Max Tokens 参数

### 今天不深入（后面会讲）
- [ ] Transformer 架构
- [ ] Attention 机制
- [ ] KV Cache
- [ ] MoE

---

## 💻 今日编码任务

### 文件结构

```
day01-llm-foundation/
├── README.md
├── model_config.py       # 模型配置抽象
├── sync_chat.py          # 同步调用
├── stream_chat.py        # 流式调用
├── async_chat.py         # 异步调用
├── async_stream.py       # 异步流式调用
├── requirements.txt
└── boss-answer.md
```

### Task 1: model_config.py（30min）

实现一个模型配置类，支持：
- api_key / base_url / model_name
- temperature / max_tokens / timeout
- 从环境变量加载
- 支持 OpenAI / 国产模型（通义、DeepSeek、智谱）

**关键代码提示**：
```python
from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    api_key: str
    base_url: str = "https://api.openai.com/v1"
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 2048
    timeout: int = 60
```

### Task 2: sync_chat.py（30min）

实现同步调用：
- 用户输入 → LLM → 完整返回
- 打印 Token 使用量
- 打印耗时

**验收标准**：
```bash
python sync_chat.py "你好，请介绍一下你自己"
# 输出：
# ✅ Response (input: 15 tokens, output: 45 tokens, total: 60 tokens, 耗时: 1.2s)
#    你好！我是一个AI助手...
```

### Task 3: stream_chat.py（40min）

实现流式调用：
- 逐字打印
- 统计 TTFT（首Token时间）
- 统计 TPS（每秒Token数）

**验收标准**：
```bash
python stream_chat.py "写一首关于编程的诗"
# 输出：
# 📡 连接建立，等待首Token...
# 编程...（逐字出现）
# 
# 📊 TTFT: 0.3s | Tokens: 85 | TPS: 45.2 | 耗时: 2.1s
```

### Task 4: async_chat.py（40min）

实现异步调用：
- async def
- asyncio.gather 并发多个请求
- 对比同步 vs 异步耗时

**验收标准**：
```bash
python async_chat.py
# 输出：
# 🚀 并发发送 3 个请求...
# ✅ 请求1完成 (1.5s)
# ✅ 请求2完成 (1.3s)
# ✅ 请求3完成 (1.4s)
# 📊 总耗时: 1.5s (同步预计: 4.2s)
```

### Task 5: async_stream.py（40min）

实现异步流式调用：
- 这是生产级 Agent 的基础
- 多个请求同时流式输出

**验收标准**：
```bash
python async_stream.py
# 输出：
# [请求1] 编程是...
# [请求2] 代码如诗...
# [请求3] 逻辑之美...
# （交错流式输出）
```

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Python 语法（async/await、generator）
- 解释 OpenAI SDK 参数含义
- 帮你调试代码报错
- 解释 Token 计算逻辑

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我有10年Java经验，Python的async/await我不太熟。请用Java的CompletableFuture类比解释一下，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 LLM Client。"

---

## 📝 GitHub 提交规范

### 提交结构
```
01-newbie-village/
└── day01-llm-foundation/
    ├── README.md           # 学习总结
    ├── model_config.py     # 配置抽象
    ├── sync_chat.py        # 同步
    ├── stream_chat.py      # 流式
    ├── async_chat.py       # 异步
    ├── async_stream.py     # 异步流式
    ├── requirements.txt
    └── boss-answer.md      # Boss答案
```

### README.md 必须包含
```markdown
# Day 1 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）
 今天学到了 LLM 相关的概念及openAi提供的各种接口调用 及LLM执行的过程
概念相关的:
token: LLM接受的最小单位, 英文字符一般4个字符一个token,中文一般一个字,1~3个token
token分词器:将用户输出的文本,分割成若干个token,然后序列化 ,开头101,结尾102
向量嵌入层:将token分词器分过后的 一个个token,按照向量维度去向量化,比如GPT-4是12288维度,则将每个token转为容量为12288浮点数的向量数组
prompt:用户发送的文本,统一叫做提示词
user system instructions: system 跟 instructions 都是系统预置的,优先级高于user
windows context: 窗口上下文,包含用户输入的问题,模型的回答,工具调用,输出等所有的定西,窗口就算是118k也是有限的,可以用缓存机制缓存到本地,随用随调取,或者用动态窗口方式,只保留最近几轮
asyncio: 异步架构,可以异步执行N多任务,用协程的方式,共享内存,有一个错误可能会导致整体失败
gather: 等到都结束后一起返回
BaseModel:来自Pydantic库，主要用于数据校验、序列化和类型提示：
Consumer: 消费者,用于消费,只有输入没有输出Consumer<T>
supplier: 生产者,只有输出没有输入 
Function: 加工者,有输入也有输出Function<T,R>
Predicate: 条件判断者 返回 bolean



## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Token | 原来模糊不清 | 现在知道,他就是一个被切割成的一个 最小向量单位,用于向量化以及意图识别跟上下文关联 |
| Context | 上下文 | 现在理解的也是上下文 |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 01-newbie-village/day01-llm-foundation/
git commit -m "feat(day01): LLM Foundation - 4种调用模式完成"
```

---

## 🐉 今日 Boss

### Boss 问题

1. **Token 是什么？中英文 Token 化有什么区别？**
    LLM 接受处理的的最小单位,英文一般是4个字符为一个token,一个中文字大概1~3个token,所以用中文提示词还是有点费的
2. **Context Window 是什么？为什么不能无限大？**
   上下文窗口,因为最大目前也是100多k,也是有限的,如果一直保持长上下文窗口的话,那LLM的注意力会被稀释,且耗费的token量会越来越多,结果质量会变差
3. **Streaming 和普通请求有什么区别？延迟和成本上呢？**
   区别是在创建clent的时候需要指定stream = true
   steaming的FTT会短,一般在500ms以内,给用户的感觉好,不会让用户等好几秒都没结果
   成本是一样的
    还是那句话,总消耗时间是一样的,只不过通过的话用户会等很长时间才能一次性的结果
4. **为什么 Agent 应用特别关注 Token？**
    成本:因为agent会调用多工具完成任务,token消耗是之前的5~10倍
   因为 要保证持续稳定的输出质量高的答案,token是要一直提示的
5. **为什么不能把所有历史消息无限塞进 Context？**
   因为context是有上限的,无限塞的话,注意力会分散,导致回答的效果不好
6. **TTFT 和 TPS 是什么？对用户体验有什么影响？**
   TTFT是首次token 返回的时长,TPS 是 返回的总token数/时间
7. **System Prompt 和 User Prompt 有什么区别？**
    System prompt 是工程师预设的模型角色,比如java开发工程师,优先级高于用户,定于我是谁
    User prompt 是用户的输出,他想要什么

### 验收标准
- 每个答案 **不少于50字**
- 必须 **用自己的话**，不能抄文档
- 必须 **结合代码运行结果** 来讲

---

## 🎤 面试题

1. **LLM、Chat Model、Agent 有什么区别？**
    LLM是经过大型参数,内存,算力训练出来的大语言模型LaragerLanageModel,默认的参数都是随机的,通过不断的学习跟训练,建立不同向量的关联关系,比如 猫狗可能就比较近, 猫 铃铛 可能就没那么近
    Chat Model 语言聊天模型,比如GPT.GPT的。client.chat.completions.create 就是创建一个聊天的过程
    Agent 可以执行很多复杂的任务,支持工具调用,更像是一个融合了很多功能的全能瘦
2. **Message 和 Prompt 是什么关系？**
    Message 有两种,一种
    System Message:系统预设消息,角色,行为,对整个对话都是有效的,用户通常看不到
    User Message: 用户的问题
3. **Context Window 是什么？**
    窗口上下文,包含用户的问题,模型的回答输出,工具的调用,记录等
4. **Streaming 为什么提升用户体验？Streaming 是否降低模型总耗时？**
    感官上模型一直在不断的输出,等待时长就是FFTT这个时长
    但是总耗时上是跟同步一股脑返回是一样
5. **TTFT 和 TPS 是什么？如何优化？**
    TTFT是首次token 返回的时长,TPS 是 返回的总token数/时间

---

## ⭐ 通关评分（100分）

| 项目 | 分值 | 评分标准 |
|------|------|----------|
| sync_chat.py | 15分 | 能运行 + 打印Token + 打印耗时 |
| stream_chat.py | 15分 | 能流式输出 + 统计TTFT/TPS |
| async_chat.py | 15分 | 能并发 + 对比同步/异步 |
| async_stream.py | 15分 | 能异步流式 + 多请求交错 |
| README 学习总结 | 15分 | 有自己的理解，不是抄的 |
| Boss 答案 | 15分 | 7题全部完成 + 用自己的话 |
| 代码质量 | 10分 | 命名清晰 + 注释 + 结构 |

---

## 🔓 解锁条件

- [ ] 4个代码文件全部能运行
- [ ] Boss 7题全部完成
- [ ] README 学习总结完成
- [ ] Git Commit 完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 2: Structured Output**

---

## 📊 今日检查清单

- [ ] 读了 OpenAI Text Generation 文档
- [ ] 读了 OpenAI Streaming 文档
- [ ] 写了 model_config.py
- [ ] 写了 sync_chat.py
- [ ] 写了 stream_chat.py
- [ ] 写了 async_chat.py
- [ ] 写了 async_stream.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 boss-answer.md
- [ ] Git Commit

---

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
