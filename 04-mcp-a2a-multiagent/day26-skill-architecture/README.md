# Day 26: Skill Architecture（技能架构）

> **今日目标**: 掌握 Skill 架构：Agent → Skill → Tool
> **核心问题**: 为什么要引入 Skill 层？

---

## 🎯 今日目标

1. 理解 Skill 层的作用
2. 实现 Agent → Skill → Tool 三层架构
3. 实现 Investment Research Skills
4. 理解 Skill 和 Tool 的区别

---

## 📚 必学知识

### 1. 为什么需要 Skill 层？

```
Agent（智能体）
    ↓
Skill（技能）—— 业务逻辑封装
    ↓
Tool（工具）—— 原子操作
```

**问题**：
- Tool 是原子操作（如 HTTP 请求、数据库查询）
- Agent 需要的是业务能力（如"研究行业"、"分析公司"）
- Skill 层封装业务逻辑，调用多个 Tool

### 2. Skill vs Tool

| 维度 | Tool | Skill |
|------|------|-------|
| 粒度 | 原子操作 | 业务能力 |
| 例子 | HTTP 请求、数据库查询 | 行业研究、公司分析 |
| 调用 | LLM 直接调用 | Agent 调用，内部调用多个 Tool |
| 复用性 | 高 | 中 |

### 3. Investment Research Skills

| Skill | 作用 | 调用 Tools |
|-------|------|------------|
| IndustryResearchSkill | 行业研究 | search_industry, get_market_data |
| CompanyResearchSkill | 公司研究 | search_company, get_financial_data |
| FinancialAnalysisSkill | 财务分析 | calculate, get_financial_data |
| MarketSentimentSkill | 市场情绪 | search_news, analyze_sentiment |

---

## 🔗 官方资料

| 知识点 | 地址 |
|--------|------|
| LangGraph Skills | https://langchain-ai.github.io/langgraph/concepts/ |

---

## 🧠 学习深度

### 必须掌握（L3）
- [ ] Skill 层设计
- [ ] Agent → Skill → Tool 三层架构
- [ ] Investment Research Skills 实现

---

## 💻 今日编码任务

### 文件结构

```
day26-skill-architecture/
├── README.md
├── 00_skill_framework.py     # Skill 框架
├── requirements.txt
└── 99-boss-answer.md
```

### Task 1: skill_framework.py（60min）

实现 Skill 框架：
- Skill 基类
- Skill Registry
- Agent 调用 Skill

### Task 2: investment_skills.py（60min）

实现投研 Skills：
- IndustryResearchSkill
- CompanyResearchSkill
- FinancialAnalysisSkill

---

## 🐉 今日 Boss

1. **Skill 层的作用是什么？**
2. **Skill 和 Tool 的区别？**
3. **为什么 Agent 不直接调用 Tool？**

---

## ⭐ 通关评分（100分）

| 项目 | 分值 |
|------|------|
| skill_framework.py | 50分 |
| investment_skills.py | 30分 |
| Boss 答案 | 20分 |

---

## 🔓 解锁条件

- [ ] 代码能运行
- [ ] Boss 3题完成
- [ ] 总分 ≥ 60分

**解锁后进入 Day 27: A2A Protocol**

---

## 🤖 Codex / Claude Code 任务

### 今天 AI 可以帮你
- 解释 Skill 层的设计思想
- 解释 Agent → Skill → Tool 三层架构
- 帮你调试 Skill 框架代码报错
- 对比 Skill 和 Tool 的优劣

### 今天 AI 不能帮你
- 替你理解概念（你必须自己理解）
- 替你写完整代码（你必须自己敲）
- 替你回答 Boss（你必须自己想）

### 正确用法
> "我理解面向对象的继承和多态，Skill 基类 + 具体 Skill 的封装方式我不太熟。请用 Java 的接口和实现类类比解释 Skill 框架的设计，然后给我一个最小示例。"

### 错误用法
> "帮我写一个完整的 Skill 框架。"

---

## 📝 GitHub 提交规范

### 提交结构
```
04-mcp-a2a-multiagent/
└── day26-skill-architecture/
    ├── README.md           # 学习总结
    ├── LEARNING_FLOW.md    # 学习流程
    ├── 00_skill_framework.py # Skill 框架
    ├── requirements.txt
    └── 99-boss-answer.md   # Boss 答案
```

### README.md 必须包含
```markdown
# Day 26 学习总结

## 今天学到了什么
（用自己的话写，不要抄文档）

## 原来以为是什么 vs 现在理解是什么
| 概念 | 原来以为 | 现在理解 |
|------|----------|----------|
| Skill | ... | ... |
| Tool | ... | ... |

## 遇到的坑
（记录踩过的坑）

## 代码运行截图
（贴终端输出）
```

### Commit 规范
```bash
git add 04-mcp-a2a-multiagent/day26-skill-architecture/
git commit -m "feat(day26): Skill Architecture - Skill 框架和投研 Skills 完成"
```

---

## 📊 今日检查清单

- [ ] 读了 LangGraph Skills 相关资料
- [ ] 写了 00_skill_framework.py
- [ ] 运行了所有代码
- [ ] 写了 README 学习总结
- [ ] 写了 99-boss-answer.md
- [ ] Git Commit

**今日积分**: ⭐ 理论__分 | 💻 编码__分 | 🐉 Boss__分 = ___/100
