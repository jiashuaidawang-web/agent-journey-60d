# Day 12: LangGraph Human-in-the-loop

> **今日目标**: 实现人工审批流程
> **核心问题**: Agent 如何在关键步骤暂停等待人工确认？

---

## 🎯 今日目标

1. 理解 interrupt 机制
2. 实现人工审批节点
3. 实现 interrupt_after / interrupt_before
4. 实现动态人工介入

---

## 📚 必学知识

### 1. interrupt 机制

- LangGraph 可以在指定节点**前/后**暂停
- 等待人工输入后继续执行
- 通过 `checkpointer` 保存暂停时的 State

### 2. interrupt_after

```python
# 在 "agent" 节点执行后暂停
app = graph.compile(checkpointer=checkpointer, interrupt_after=["agent"])
```

### 3. interrupt_before

```python
# 在 "tools" 节点执行前暂停
app = graph.compile(checkpointer=checkpointer, interrupt_before=["tools"])
```

### 4. 恢复执行

```python
# 人工审批后，传入 None 继续
app.invoke(None, config)
```

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Human-in-the-loop | https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/ |
| interrupts | https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/ |

---

## 🧠 学习深度

### 必须掌握（L4）
- [ ] interrupt 机制
- [ ] 人工审批流程
- [ ] 恢复执行

---

## 💻 今日编码任务

### 文件结构

```
day12-langgraph-human-in-loop/
├── README.md
├── LEARNING_FLOW.md           # 学习流程
├── 00_approval_demo.py        # 人工审批演示
├── 01_tool_approval.py        # 工具调用审批
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: approval_demo.py（60min）

实现人工审批：
- Agent 生成方案
- 暂停等待审批
- 审批通过/拒绝
- 继续执行

### Task 2: tool_approval.py（45min）

实现工具调用审批：
- 工具执行前暂停
- 人工确认后执行

---

## 🐉 今日 Boss

1. **interrupt 和 Checkpoint 的关系？**
2. **什么场景需要 Human-in-the-loop？**
3. **如何实现审批通过/拒绝的不同处理？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| approval_demo.py | 50分 |
| tool_approval.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 13: Long-running Agent**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 interrupt 机制和 Checkpoint 的关系
- 解释 interrupt_after 和 interrupt_before 的区别
- 帮你调试代码报错
- 解释什么场景需要 Human-in-the-loop

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "interrupt 和 Checkpoint 是什么关系？请用 Java 的线程挂起和恢复类比解释一下。"

### 错误用法
> "帮我写一个完整的审批流程。"

---

## 📝 GitHub 提交规范

### 提交结构
```
02-langchain-academy/
└── day12-langgraph-human-in-loop/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_approval_demo.py        # 人工审批演示
    ├── 01_tool_approval.py        # 工具调用审批
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 12 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| interrupt | ... | ... |
| Human-in-the-loop | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 02-langchain-academy/day12-langgraph-human-in-loop/
git commit -m "feat(day12): LangGraph Human-in-the-loop - 审批流程完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Human-in-the-loop 文档
- [ ] 读了 interrupts 文档
- [ ] 写了 00_approval_demo.py
- [ ] 写了 01_tool_approval.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
