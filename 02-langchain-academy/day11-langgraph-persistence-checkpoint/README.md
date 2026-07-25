# Day 11: LangGraph Persistence + Checkpoint

> **今日目标**: 实现 Agent 的断点续跑
> **核心问题**: Agent 如何从中断中恢复？

---

## 🎯 今日目标

1. 理解 Checkpoint 机制
2. 实现状态持久化
3. 实现断点续跑
4. 理解 Thread 和多会话

---

## 📚 必学知识

### 1. Checkpoint（检查点）

- LangGraph 在每个节点执行后自动保存 State
- 保存到 Checkpoint Saver（内存 / 数据库）
- 支持从任意 Checkpoint 恢复

### 2. MemorySaver

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)
```

### 3. Thread（线程/会话）

```python
# 每个会话有唯一的 thread_id
config = {"configurable": {"thread_id": "user_123"}}
app.invoke(input, config)
```

### 4. 获取历史

```python
# 获取某个会话的所有 State
history = list(app.get_state_history(config))
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Persistence | https://langchain-ai.github.io/langgraph/concepts/persistence/ |
| LangGraph Checkpoint | https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints |
| MemorySaver | https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.MemorySaver |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] Checkpoint 机制
- [ ] MemorySaver 使用
- [ ] Thread 和多会话
- [ ] 断点续跑
- [ ] 历史查询

---

## 💻 今日编码任务

### 文件结构

```
day11-langgraph-persistence-checkpoint/
├── README.md
├── LEARNING_FLOW.md           # 学习流程
├── 00_checkpoint_demo.py      # Checkpoint 演示
├── 01_resume_demo.py          # 断点续跑
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: checkpoint_demo.py（45min）

演示 Checkpoint：
- 使用 MemorySaver
- 保存多个会话
- 查询历史

### Task 2: resume_demo.py（60min）

演示断点续跑：
- 中断执行
- 从 Checkpoint 恢复
- 继续执行

---

## 🐉 今日 Boss

1. **Checkpoint 是什么？为什么需要？**
2. **Thread 的作用是什么？**
3. **如何实现断点续跑？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| checkpoint_demo.py | 40分 |
| resume_demo.py | 40分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 12: Human-in-the-loop**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Checkpoint 机制及其作用
- 解释 Thread 和多会话隔离
- 帮你调试代码报错
- 解释断点续跑的实现方式

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "Checkpoint 和 Thread 是什么关系？请用 Java 的 Session 和 Redis 持久化类比解释一下。"

### 错误用法
> "帮我写一个完整的断点续跑 Demo。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day11-langgraph-persistence-checkpoint/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_checkpoint_demo.py      # Checkpoint 演示
    ├── 01_resume_demo.py          # 断点续跑
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 11 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Checkpoint | ... | ... |
| Thread | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day11-langgraph-persistence-checkpoint/
git commit -m "feat(day11): LangGraph Persistence+Checkpoint - 断点续跑完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Persistence 文档
- [ ] 读了 LangGraph Checkpoint 文档
- [ ] 写了 00_checkpoint_demo.py
- [ ] 写了 01_resume_demo.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
