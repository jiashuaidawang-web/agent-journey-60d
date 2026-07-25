"""
Day 52: Investment Research Platform.

AI 投研多 Agent 平台主程序。

Usage:
    python investment_research_platform.py
"""


class Tool:
    """工具基类。"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def execute(self, **kwargs):
        raise NotImplementedError


class Skill:
    """技能基类。"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tools: list[Tool] = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def execute(self, **kwargs):
        raise NotImplementedError


# 投研工具
class IndustryResearchTool(Tool):
    def __init__(self):
        super().__init__("industry_research", "研究行业概况")

    def execute(self, **kwargs):
        industry = kwargs.get("industry", "")
        return f"{industry}行业概况：市场规模持续增长，龙头企业市占率提升"


class CompanyResearchTool(Tool):
    def __init__(self):
        super().__init__("company_research", "研究公司信息")

    def execute(self, **kwargs):
        company = kwargs.get("company", "")
        return f"{company}：行业龙头，基本面稳健"


class FinancialAnalysisTool(Tool):
    def __init__(self):
        super().__init__("financial_analysis", "分析财务数据")

    def execute(self, **kwargs):
        company = kwargs.get("company", "")
        return f"{company}财务数据：营收增长15%，净利润增长18%"


class MarketSentimentTool(Tool):
    def __init__(self):
        super().__init__("market_sentiment", "分析市场情绪")

    def execute(self, **kwargs):
        return "市场情绪：投资者信心指数上升，资金流入明显"


class RiskAnalysisTool(Tool):
    def __init__(self):
        super().__init__("risk_analysis", "分析风险因素")

    def execute(self, **kwargs):
        return "风险因素：政策风险、市场风险、经营风险"


# 投研 Skills
class IndustryResearchSkill(Skill):
    def __init__(self):
        super().__init__("industry_research_skill", "行业研究技能")
        self.add_tool(IndustryResearchTool())

    def execute(self, **kwargs):
        return self.tools[0].execute(**kwargs)


class CompanyResearchSkill(Skill):
    def __init__(self):
        super().__init__("company_research_skill", "公司研究技能")
        self.add_tool(CompanyResearchTool())
        self.add_tool(FinancialAnalysisTool())

    def execute(self, **kwargs):
        result1 = self.tools[0].execute(**kwargs)
        result2 = self.tools[1].execute(**kwargs)
        return f"{result1}\n{result2}"


class MarketSentimentSkill(Skill):
    def __init__(self):
        super().__init__("market_sentiment_skill", "市场情绪技能")
        self.add_tool(MarketSentimentTool())

    def execute(self, **kwargs):
        return self.tools[0].execute(**kwargs)


class RiskAnalysisSkill(Skill):
    def __init__(self):
        super().__init__("risk_analysis_skill", "风险分析技能")
        self.add_tool(RiskAnalysisTool())

    def execute(self, **kwargs):
        return self.tools[0].execute(**kwargs)


# 专业 Agent
class Agent:
    """Agent。"""

    def __init__(self, name: str, skill: Skill):
        self.name = name
        self.skill = skill

    def execute(self, **kwargs):
        return f"[{self.name}] {self.skill.execute(**kwargs)}"


# Supervisor Agent
class SupervisorAgent:
    """协调 Agent。"""

    def __init__(self):
        self.agents: dict[str, Agent] = {}

    def register_agent(self, name: str, agent: Agent):
        self.agents[name] = agent

    def execute(self, query: str) -> dict:
        """执行投研任务。"""
        print(f"\n📋 Supervisor 接收任务: {query}")

        results = {}

        # 根据查询调用不同 Agent
        if "行业" in query:
            results["industry"] = self.agents["industry"].execute(industry="白酒")
        if "公司" in query or "企业" in query:
            results["company"] = self.agents["company"].execute(company="贵州茅台")
        if "市场" in query or "情绪" in query:
            results["market"] = self.agents["market"].execute()
        if "风险" in query:
            results["risk"] = self.agents["risk"].execute()

        return results

    def generate_report(self, results: dict) -> str:
        """生成投研报告。"""
        report = "# 投研报告\n\n"

        if "industry" in results:
            report += "## 行业分析\n"
            report += results["industry"] + "\n\n"

        if "company" in results:
            report += "## 公司分析\n"
            report += results["company"] + "\n\n"

        if "market" in results:
            report += "## 市场情绪\n"
            report += results["market"] + "\n\n"

        if "risk" in results:
            report += "## 风险分析\n"
            report += results["risk"] + "\n\n"

        return report


def investment_research_platform_demo():
    """Investment Research Platform 演示。"""
    print("=" * 60)
    print("Investment Research Platform Demo")
    print("=" * 60)

    # 创建 Supervisor
    supervisor = SupervisorAgent()

    # 注册专业 Agent
    supervisor.register_agent("industry", Agent("行业研究员", IndustryResearchSkill()))
    supervisor.register_agent("company", Agent("公司研究员", CompanyResearchSkill()))
    supervisor.register_agent("market", Agent("市场分析师", MarketSentimentSkill()))
    supervisor.register_agent("risk", Agent("风险分析师", RiskAnalysisSkill()))

    print("\n✅ Supervisor 创建完成，注册 4 个 Agent")

    # 执行投研任务
    query = "请分析白酒行业龙头企业贵州茅台"
    results = supervisor.execute(query)

    # 打印结果
    print("\n📊 投研结果:")
    for agent_name, result in results.items():
        print(f"\n   {agent_name}:")
        print(f"   {result}")

    # 生成报告
    report = supervisor.generate_report(results)
    print("\n📄 投研报告:")
    print(report)

    print("\n✅ Investment Research Platform 演示完成")


if __name__ == "__main__":
    investment_research_platform_demo()
