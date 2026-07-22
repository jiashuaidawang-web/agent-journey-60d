# Agent Journey 60d

> 10年Java架构师 → Agentic AI Engineer 的60天闯关式转型计划

## 🎯 目标

两个月内，从Java架构师转型为具备生产级Agent开发能力的AI应用工程师，完成：

- **8个章节**、**30个关卡**、**7个Boss Challenge**
- **2个企业级项目**（知识库Agent平台 + A股投研多Agent平台）
- **60次Git Commit**（每天至少一个提交）
- **完整的架构能力地图**

## 📁 目录结构

```
agent-journey-60d/
│
├── 00-roadmap/              # 路线图、技能地图、进度追踪
│   ├── 60-day-roadmap.md    # 完整60天路线
│   ├── skill-map.md         # 技能优先级评估
│   └── progress.md          # 每日打卡+积分系统
│
├── 01-newbie-village/       # 第一章：新手村 (Day 1-7)
│   ├── day01-llm-foundation/
│   ├── day02-prompt-context/
│   ├── day03-structured-output/
│   ├── day04-tool-calling/
│   ├── day05-agent-loop/
│   ├── day06-mini-agent-runtime/
│   └── day07-boss-challenge/
│
├── 02-langchain-academy/    # 第二章：LangChain学院 (Day 8-14)
├── 03-rag-dungeon/          # 第三章：RAG副本 (Day 15-21)
├── 04-langgraph-abyss/      # 第四章：LangGraph深渊 (Day 22-30)
├── 05-mcp-city/             # 第五章：MCP城 (Day 31-37)
├── 06-multi-agent-arena/    # 第六章：Multi-Agent竞技场 (Day 38-44)
├── 07-production-hell/      # 第七章：Production地狱 (Day 45-52)
├── 08-final-boss/           # 第八章：最终Boss (Day 53-60)
│   ├── project1/             # Enterprise Knowledge Agent Platform
│   └── project2/             # AI Investment Research Multi-Agent Platform
│
└── docs/
    ├── architecture/         # 架构图
    ├── notes/                # 学习笔记
    ├── interview/            # 面试题库+答案
    └── weekly-review/        # 每周复盘
```

## 🚀 快速开始

1. 创建 `.env` 文件配置API密钥
2. 阅读 `00-roadmap/60-day-roadmap.md` 了解完整路线
3. 从 `01-newbie-village/day01-llm-foundation/` 开始
4. 每天编码 → 每天Commit → 每周Boss Challenge

## 📊 技术栈

- **语言**: Python 3.12+, 类型注解, async/await
- **框架**: FastAPI, Pydantic
- **核心**: LangChain, LangGraph, MCP
- **数据库**: PostgreSQL, Redis, Vector DB
- **工具**: uv, pytest, httpx

## 🏆 闯关规则

- 每天 20%理论 + 60%编码 + 20%总结
- 不看视频，主线是官方文档 + GitHub源码
- Boss Challenge 禁止使用框架（除非特别说明）
- 每天必须 Git Commit

## 📝 评分体系

每关满分100分，由导师从4个维度评分：

| 维度 | 权重 |
|------|------|
| Knowledge 知识理解 | 20% |
| Engineering 代码质量 | 15% |
| Architecture 架构能力 | 15% |
| Boss 面试表达 | 5% |
