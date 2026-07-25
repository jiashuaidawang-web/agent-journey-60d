# Day 8 Boss 答案

## 1. LangChain 和 LangGraph 有什么区别？

**LangChain**：
- 核心抽象：Chain（链式调用）
- 适用场景：线性流程（一次调用 → 输出）
- 特点：LCEL 链式语法，简单任务很方便
- 限制：复杂分支、循环、多 Agent 支持弱

**LangGraph**：
- 核心抽象：Graph（图）
- 适用场景：复杂 Agent（多步、分支、循环、多 Agent）
- 特点：State + Node + Edge，灵活但复杂
- 优势：原生支持多 Agent、Human-in-the-loop、Checkpoint

**核心区别**：

| 维度 | LangChain | LangGraph |
|------|-----------|-----------|
| 抽象 | Chain（链） | Graph（图） |
| 流程 | 线性 | 任意图 |
| 状态 | 弱 | 强 |
| 循环 | 不支持原生 | 原生支持 |
| 多 Agent | 不支持 | 原生支持 |
| Human-in-the-loop | 复杂 | 原生支持 |

**选择建议**：
- 简单任务（一次调用）→ LangChain
- 复杂 Agent（多步、分支、循环）→ LangGraph
- 实际生产系统 → LangGraph 为主

## 2. LCEL 是什么？和 Java Stream 有什么相似？

**LCEL（LangChain Expression Language）**：
- LangChain 的链式调用语法
- 用 `|` 符号连接多个 Runnable
- 例如：`prompt | model | parser`

**和 Java Stream 的相似**：

| 概念 | Java Stream | LCEL |
|------|-------------|------|
| 数据源 | Collection / Stream | Prompt |
| 中间操作 | map / filter / flatMap | model / parser |
| 终端操作 | collect / forEach | invoke / stream |
| 链式调用 | list.stream().map().filter() | prompt \| model \| parser |
| 延迟执行 | 是（终端操作触发） | 是（invoke 触发） |

**LCEL 的优势**：
- 自动支持流式输出
- 自动支持批处理
- 自动支持并行
- 错误处理统一

## 3. 为什么 Agent 系统更倾向于用 LangGraph？

**Agent 系统的核心需求**：
1. 多步推理（需要循环）
2. 条件分支（根据情况走不同路径）
3. 状态管理（记住之前的步骤）
4. 多 Agent 协作（多个 Agent 互相调用）
5. Human-in-the-loop（人工审批）
6. 断点续跑（Checkpoint）

**LangChain 的局限**：
- Chain 是线性的，不支持循环
- 条件分支需要额外代码
- 状态管理弱
- 多 Agent 支持不完善

**LangGraph 的优势**：
- Graph 天然支持循环和分支
- State 是一等公民
- 多 Agent 是核心设计
- Human-in-the-loop 原生支持
- Checkpoint 原生支持

**结论**：
LangGraph 是为复杂 Agent 设计的，而 LangChain 更适合简单线性流程。
当前 Agent 系统的主流趋势是 LangGraph。
