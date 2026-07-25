"""
Day 26: Skill Architecture.

实现 Agent → Skill → Tool 三层架构。

Usage:
    python skill_framework.py
"""


class Tool:
    """工具基类（原子操作）。"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def execute(self, **kwargs):
        raise NotImplementedError


class Skill:
    """技能基类（业务能力）。"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tools: list[Tool] = []

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def execute(self, **kwargs):
        raise NotImplementedError


class SkillRegistry:
    """技能注册表。"""

    def __init__(self):
        self._skills: dict[str, Skill] = {}

    def register(self, skill: Skill):
        self._skills[skill.name] = skill

    def get(self, name: str) -> Skill | None:
        return self._skills.get(name)

    def list_skills(self):
        return list(self._skills.values())


class Agent:
    """智能体：调用 Skill。"""

    def __init__(self, name: str, skill_registry: SkillRegistry):
        self.name = name
        self.registry = skill_registry

    def execute_skill(self, skill_name: str, **kwargs):
        skill = self.registry.get(skill_name)
        if skill is None:
            return f"技能 '{skill_name}' 不存在"
        return skill.execute(**kwargs)


# 具体实现
class HttpTool(Tool):
    """HTTP 工具。"""

    def __init__(self):
        super().__init__("http_request", "发送 HTTP 请求")

    def execute(self, **kwargs):
        url = kwargs.get("url", "")
        return f"HTTP GET {url} → 200 OK"


class DatabaseTool(Tool):
    """数据库工具。"""

    def __init__(self):
        super().__init__("db_query", "查询数据库")

    def execute(self, **kwargs):
        query = kwargs.get("query", "")
        return f"DB Query: {query} → [results]"


class IndustryResearchSkill(Skill):
    """行业研究技能。"""

    def __init__(self):
        super().__init__("industry_research", "研究行业概况")
        self.add_tool(HttpTool())
        self.add_tool(DatabaseTool())

    def execute(self, **kwargs):
        industry = kwargs.get("industry", "")
        # 调用多个 Tool
        result1 = self.tools[0].execute(url=f"https://api.industry.com/{industry}")
        result2 = self.tools[1].execute(query=f"SELECT * FROM industries WHERE name='{industry}'")
        return f"行业研究完成: {industry}\n  {result1}\n  {result2}"


class CompanyResearchSkill(Skill):
    """公司研究技能。"""

    def __init__(self):
        super().__init__("company_research", "研究公司信息")
        self.add_tool(HttpTool())
        self.add_tool(DatabaseTool())

    def execute(self, **kwargs):
        company = kwargs.get("company", "")
        result1 = self.tools[0].execute(url=f"https://api.company.com/{company}")
        result2 = self.tools[1].execute(query=f"SELECT * FROM companies WHERE name='{company}'")
        return f"公司研究完成: {company}\n  {result1}\n  {result2}"


def skill_framework_demo():
    """Skill 框架演示。"""
    print("=" * 60)
    print("Skill Architecture Demo")
    print("=" * 60)

    # 创建 Registry
    registry = SkillRegistry()

    # 注册 Skills
    registry.register(IndustryResearchSkill())
    registry.register(CompanyResearchSkill())

    print(f"\n✅ 注册 {len(registry.list_skills())} 个技能:")
    for skill in registry.list_skills():
        print(f"   - {skill.name}: {skill.description}")

    # 创建 Agent
    agent = Agent("research_agent", registry)

    # 调用 Skill
    print(f"\n🔧 Agent 调用技能:")
    result = agent.execute_skill("industry_research", industry="白酒")
    print(f"   {result}")

    result = agent.execute_skill("company_research", company="贵州茅台")
    print(f"   {result}")


if __name__ == "__main__":
    skill_framework_demo()
