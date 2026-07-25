"""
Day 51: Enterprise Agent Platform.

企业级 Agent 平台主程序。

Usage:
    python enterprise_agent_platform.py
"""


import uuid
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Tenant:
    """租户。"""

    def __init__(self, tenant_id: str, name: str, tier: str = "basic"):
        self.tenant_id = tenant_id
        self.name = name
        self.tier = tier
        self.quota = self._get_quota(tier)
        self.usage = {"token_count": 0, "api_calls": 0}

    def _get_quota(self, tier: str) -> dict:
        quotas = {
            "basic": {"token_limit": 100_000, "api_call_limit": 1_000},
            "pro": {"token_limit": 1_000_000, "api_call_limit": 10_000},
            "enterprise": {"token_limit": 10_000_000, "api_call_limit": 100_000},
        }
        return quotas.get(tier, quotas["basic"])

    def check_quota(self, tokens: int = 0) -> tuple[bool, str]:
        if self.usage["token_count"] + tokens > self.quota["token_limit"]:
            return False, "Token 配额不足"
        if self.usage["api_calls"] + 1 > self.quota["api_call_limit"]:
            return False, "API 调用配额不足"
        return True, "通过"


class Task:
    """任务。"""

    def __init__(self, tenant_id: str, input_data: dict):
        self.task_id = str(uuid.uuid4())
        self.tenant_id = tenant_id
        self.input_data = input_data
        self.output_data = None
        self.status = TaskStatus.PENDING
        self.cost = 0
        self.tokens = 0
        self.created_at = datetime.now()
        self.completed_at = None

    def complete(self, output_data: str, tokens: int, cost: float):
        self.output_data = output_data
        self.tokens = tokens
        self.cost = cost
        self.status = TaskStatus.COMPLETED
        self.completed_at = datetime.now()


class AgentPlatform:
    """Agent 平台。"""

    def __init__(self):
        self.tenants: dict[str, Tenant] = {}
        self.tasks: list[Task] = []
        self.total_cost = 0

    def register_tenant(self, tenant_id: str, name: str, tier: str = "basic") -> Tenant:
        """注册租户。"""
        tenant = Tenant(tenant_id, name, tier)
        self.tenants[tenant_id] = tenant
        return tenant

    def submit_task(self, tenant_id: str, input_data: dict) -> str:
        """提交任务。"""
        tenant = self.tenants.get(tenant_id)
        if tenant is None:
            raise ValueError(f"租户 {tenant_id} 不存在")

        # 配额检查
        can_access, reason = tenant.check_quota(tokens=1000)
        if not can_access:
            raise PermissionError(reason)

        # 创建任务
        task = Task(tenant_id, input_data)
        self.tasks.append(task)

        # 执行任务
        self._execute_task(task, tenant)

        return task.task_id

    def _execute_task(self, task: Task, tenant: Tenant):
        """执行任务。"""
        task.status = TaskStatus.RUNNING

        # 模拟 Agent 执行
        tokens_used = 500
        cost = tokens_used * 0.00015 / 1000

        result = f"处理完成: {task.input_data}"
        task.complete(result, tokens_used, cost)

        # 更新租户使用量
        tenant.usage["token_count"] += tokens_used
        tenant.usage["api_calls"] += 1
        self.total_cost += cost

    def get_tenant_usage(self, tenant_id: str) -> dict:
        """获取租户使用情况。"""
        tenant = self.tenants.get(tenant_id)
        if tenant is None:
            return {}

        return {
            "tenant_id": tenant_id,
            "name": tenant.name,
            "tier": tenant.tier,
            "token_used": tenant.usage["token_count"],
            "token_limit": tenant.quota["token_limit"],
            "api_calls": tenant.usage["api_calls"],
            "token_percentage": tenant.usage["token_count"] / tenant.quota["token_limit"] * 100,
        }

    def get_platform_stats(self) -> dict:
        """获取平台统计。"""
        return {
            "total_tenants": len(self.tenants),
            "total_tasks": len(self.tasks),
            "total_cost": self.total_cost,
            "completed_tasks": sum(1 for t in self.tasks if t.status == TaskStatus.COMPLETED),
        }


def enterprise_agent_platform_demo():
    """Enterprise Agent Platform 演示。"""
    print("=" * 60)
    print("Enterprise Agent Platform Demo")
    print("=" * 60)

    platform = AgentPlatform()

    # 注册租户
    print("\n📦 注册租户:")
    platform.register_tenant("tenant_001", "小公司", "basic")
    platform.register_tenant("tenant_002", "中公司", "pro")
    platform.register_tenant("tenant_003", "大公司", "enterprise")
    print("   注册 3 个租户")

    # 提交任务
    print("\n📤 提交任务:")
    for tenant_id in ["tenant_001", "tenant_002", "tenant_003"]:
        task_id = platform.submit_task(tenant_id, {"query": "分析贵州茅台"})
        print(f"   {tenant_id}: 任务 {task_id[:8]}... 提交成功")

    # 租户使用情况
    print("\n📊 租户使用情况:")
    for tenant_id in ["tenant_001", "tenant_002", "tenant_003"]:
        usage = platform.get_tenant_usage(tenant_id)
        print(f"   {usage['name']} ({usage['tier']}):")
        print(f"     Token: {usage['token_used']:,} / {usage['token_limit']:,} ({usage['token_percentage']:.2f}%)")

    # 平台统计
    print("\n🏢 平台统计:")
    stats = platform.get_platform_stats()
    print(f"   租户数: {stats['total_tenants']}")
    print(f"   任务数: {stats['total_tasks']}")
    print(f"   总成本: ${stats['total_cost']:.6f}")
    print(f"   完成数: {stats['completed_tasks']}")

    print("\n✅ Enterprise Agent Platform 演示完成")


if __name__ == "__main__":
    enterprise_agent_platform_demo()
