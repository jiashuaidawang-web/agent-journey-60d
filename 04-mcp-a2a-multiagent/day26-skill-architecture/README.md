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
├── skill_framework.py       # Skill 框架
├── investment_skills.py     # 投研 Skills
├── requirements.txt
└── boss-answer.md
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
