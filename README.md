# Agent Journey 60D v3.0

> **10年Java架构师 → Agent Platform Architect 的60天闯关式转型计划**

---

## 🎯 目标

两个月内，从 Java 架构师转型为 **Agent Platform Architect**，完成：

- **9个阶段**、**54个关卡**
- **2个企业级项目**：
  - **Project 1**: Enterprise Agent Platform（Java控制平面 + Python AI服务）
  - **Project 2**: AI Investment Research Multi-Agent Platform
- **60次Git Commit**（每天至少一个提交）
- **差异化竞争力**: Java企业级架构 + Agent编排

---

## 🏷️ v3.0 核心变化

| 维度 | v2.0 (GPT版) | v3.0 (为你定制) |
|------|--------------|------------------|
| **定位** | 全栈LLM工程师 | **Agent Platform Architect** |
| **核心优势** | 没利用Java | **Java企业级架构 + Agent编排** |
| **LLM Foundation** | 5天 | **3天**（压缩） |
| **LangChain** | 5天 | **1天**（快速过） |
| **LangGraph** | 分散 | **7天深一周**（核心） |
| **Production Agent** | 5天 | **8天**（你发力） |
| **LLM Training** | 5天深入 | **7天理解**（P2快速过） |
| **GraphRAG** | 没有 | **3天**（补简历） |
| **Java控制平面** | 没有 | **新增**（差异化） |
| **A2A** | L2 Demo | **L3实战** |
| **多模态** | 没提 | **直接跳过** |

---

## 📁 目录结构（v3.0 对齐）

```
agent-journey-60d/
│
├── 00-roadmap/              # 路线图、技能地图、进度追踪
│
├── 01-newbie-village/       # Phase 1+2: 新手村 + Agent核心 (Day 1-7)
│   ├── day01-llm-foundation/       # LLM API / Message / Token / Streaming
│   ├── day02-structured-output/    # Structured Output / JSON Schema / Pydantic
│   ├── day03-prompt-context/        # Prompt Engineering / Context Engineering
│   ├── day04-tool-calling/          # Tool Calling / Function Calling
│   ├── day05-agent-loop/            # Tool Registry / Agent Loop
│   ├── day06-agent-patterns/        # ReAct / Router / Plan-Execute
│   └── day07-mini-agent-runtime/    # 纯手写 Agent Runtime（禁用框架）
│
├── 02-langchain-academy/    # Phase 3: LangChain快速过 + LangGraph深一周 (Day 8-14)
│   ├── day08-langchain-quick-review/    # LangChain 快速过
│   ├── day09-langgraph-state-node-edge/ # State + Node + Edge
│   ├── day10-langgraph-conditional-routing/ # 条件路由
│   ├── day11-langgraph-persistence-checkpoint/ # 持久化 + Checkpoint
│   ├── day12-langgraph-human-in-loop/   # 人工审批
│   ├── day13-langgraph-long-running/     # 长时间运行 + Subgraph
│   └── day14-langgraph-mini-project/    # LangGraph 综合项目
│
├── 03-rag-dungeon/          # Phase 4: RAG 全栈 (Day 15-22)
│   ├── day15-embedding/
│   ├── day16-vector-db/
│   ├── day17-chunking/
│   ├── day18-dense-retrieval/
│   ├── day19-bm25-hybrid/
│   ├── day20-reranker/
│   ├── day21-query-rewrite-hyde/
│   └── day22-rag-pipeline/
│
├── 04-mcp-a2a-multiagent/   # Phase 5: MCP + A2A + Multi-Agent (Day 23-31)
│   ├── day23-mcp/
│   ├── day24-mcp-server/
│   ├── day25-mcp-client/
│   ├── day26-skill-architecture/
│   ├── day27-a2a/
│   ├── day28-supervisor/
│   ├── day29-router/
│   ├── day30-parallel-agent/
│   └── day31-hierarchical-agent/
│
├── 05-production-agent/     # Phase 6: Production Agent (Day 32-38)
│   ├── day32-observability/
│   ├── day33-security/
│   ├── day34-reliability/
│   ├── day35-async-mq/
│   ├── day36-java-control-plane/    # ★ 你的Java优势
│   ├── day37-multi-tenant/
│   └── day38-agent-platform/
│
├── 06-evaluation-graphrag/  # Phase 7: Evaluation + GraphRAG (Day 39-45)
│   ├── day39-rag-evaluation/
│   ├── day40-agent-evaluation/
│   ├── day41-ragas/
│   ├── day42-evaluation-pipeline/
│   ├── day43-graphrag/
│   ├── day44-graphrag-hybrid/
│   └── day45-eval-graphrag-integration/
│
├── 07-llm-engineering/      # Phase 8: LLM Engineering P2快速过 (Day 46-52)
│   ├── day46-lora-qlora/
│   ├── day47-sft-dpo/
│   ├── day48-vllm/
│   ├── day49-kv-cache-pagedattention/
│   └── day50-model-gateway-router/
│
├── 08-final-projects/       # Phase 9: Final Projects (Day 53-60)
│   ├── day51-enterprise-agent-platform/     # ★ 项目一
│   ├── day52-investment-research-platform/  # ★ 项目二
│   ├── day53-architecture-review/
│   └── day54-final-boss/
│
└── docs/
    ├── architecture/         # 架构图
    ├── notes/                # 学习笔记
    ├── interview/            # 面试题库+答案
    └── weekly-review/        # 每周复盘
```

---

## 🗺️ 60天总路线

```
Agent Journey 60D v3.0
═══════════════════════════════════════════════════════
目标：Senior Agent Engineer / Agent Platform Architect
定位：Java企业级架构 + Agent编排
═══════════════════════════════════════════════════════

Phase 1  Day 1-3    LLM Foundation（压缩）
Phase 2  Day 4-7    Agent Core + Tool Calling
Phase 3  Day 8-14   LangChain快速过 + LangGraph深一周
Phase 4  Day 15-22  RAG 全栈
Phase 5  Day 23-31  MCP + A2A + Multi-Agent
Phase 6  Day 32-38  Production Agent（Java优势发力）
Phase 7  Day 39-45  Evaluation + GraphRAG
Phase 8  Day 46-52  LLM Engineering（P2快速过）
Phase 9  Day 53-60  Final Projects + 面试准备
```

---

## 🚀 快速开始

### 1. 环境准备

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install openai pydantic langchain langchain-openai langchain-core langgraph
```

### 2. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env 填入你的 API Key
```

### 3. 开始闯关

```bash
# 从 Day 1 开始
cd 01-newbie-village/day01-llm-foundation/
cat README.md  # 阅读任务单
python sync_chat.py  # 运行代码
```

---

## 📊 技术栈

### 核心技术
- **Python**: 3.12+, async/await, type hints
- **Agent框架**: LangGraph (L4), LangChain (L3)
- **协议**: MCP (L3), A2A (L3)
- **RAG**: Milvus, Hybrid Search, Reranker, GraphRAG

### 你的Java优势
- **Java控制平面**: Spring Boot + Agent Runtime
- **生产级**: Observability, Security, Multi-tenant
- **消息队列**: RocketMQ / Kafka

### 工具
- **模型**: OpenAI / Qwen / DeepSeek / vLLM
- **评估**: RAGAS
- **部署**: Docker, Kubernetes

---

## 🏆 闯关规则

### 每日流程
```
📚 阅读官方文档 (20%)
   ↓
💻 敲代码 (60%)
   ↓
📝 写README + Boss答案 (20%)
   ↓
🔀 Git Commit
   ↓
⭐ 自我评分
   ↓
🔓 解锁下一关
```

### 评分体系
| 维度 | 权重 | 说明 |
|------|------|------|
| Knowledge | 20% | 知识理解深度 |
| Engineering | 60% | 代码质量 + 功能实现 |
| Architecture | 10% | 架构设计能力 |
| Boss | 10% | 面试表达 |

### 通关标准
- **≥90分**: 完美通关
- **75-89分**: 通关
- **60-74分**: 勉强通关，需补强
- **<60分**: 重新闯关

---

## ⭐ 最终毕业标准

不是"我看完60天课程"，而是：

1. **GitHub 上有两个完整项目**
2. **能坐在面试官面前，不看资料，从架构层面解释**：
   - Agent Runtime 原理
   - LangGraph 核心设计
   - RAG 全链路
   - MCP / A2A 协议
   - Multi-Agent 编排
   - 生产级 Agent 系统设计

---

## 📝 当前进度

| 阶段 | 天数 | 状态 |
|------|------|------|
| Phase 1+2: 新手村 + Agent核心 | Day 1-7 | ✅ 完成 |
| Phase 3: LangChain + LangGraph | Day 8-14 | ✅ 完成 |
| Phase 4: RAG 全栈 | Day 15-22 | ⬜ 待填充 |
| Phase 5: MCP + A2A + Multi-Agent | Day 23-31 | ⬜ 待填充 |
| Phase 6: Production Agent | Day 32-38 | ⬜ 待填充 |
| Phase 7: Evaluation + GraphRAG | Day 39-45 | ⬜ 待填充 |
| Phase 8: LLM Engineering | Day 46-52 | ⬜ 待填充 |
| Phase 9: Final Projects | Day 53-60 | ⬜ 待填充 |

---

**准备好了吗？从 Day 1 开始你的 Agent Journey！**
