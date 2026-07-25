"""
Day 36: Tenant Management.

演示租户管理（Java 控制平面核心功能）。

Usage:
    python tenant_management.py
"""


class Tenant:
    """租户。"""

    def __init__(self, tenant_id: str, name: str, tier: str = "basic"):
        self.tenant_id = tenant_id
        self.name = name
        self.tier = tier  # basic, pro, enterprise
        self.quota = self._get_quota(tier)
        self.usage = {
            "token_count": 0,
            "api_calls": 0,
            "storage_mb": 0,
        }

    def _get_quota(self, tier: str) -> dict:
        """根据套餐获取配额。"""
        quotas = {
            "basic": {
                "token_limit": 100_000,      # 10万 Token/月
                "api_call_limit": 1_000,     # 1000 次调用/月
                "storage_limit_mb": 100,     # 100MB 存储
            },
            "pro": {
                "token_limit": 1_000_000,    # 100万 Token/月
                "api_call_limit": 10_000,    # 1万次调用/月
                "storage_limit_mb": 1_000,   # 1GB 存储
            },
            "enterprise": {
                "token_limit": 10_000_000,   # 1000万 Token/月
                "api_call_limit": 100_000,   # 10万次调用/月
                "storage_limit_mb": 10_000,  # 10GB 存储
            },
        }
        return quotas.get(tier, quotas["basic"])

    def check_quota(self, tokens: int = 0, api_calls: int = 0) -> tuple[bool, str]:
        """检查配额。"""
        if self.usage["token_count"] + tokens > self.quota["token_limit"]:
            return False, "Token 配额不足"

        if self.usage["api_calls"] + api_calls > self.quota["api_call_limit"]:
            return False, "API 调用配额不足"

        return True, "通过"

    def record_usage(self, tokens: int = 0, api_calls: int = 0):
        """记录使用量。"""
        self.usage["token_count"] += tokens
        self.usage["api_calls"] += api_calls

    def usage_percentage(self) -> dict:
        """使用率。"""
        return {
            "token": self.usage["token_count"] / self.quota["token_limit"] * 100,
            "api_calls": self.usage["api_calls"] / self.quota["api_call_limit"] * 100,
        }


class TenantManager:
    """租户管理器。"""

    def __init__(self):
        self.tenants: dict[str, Tenant] = {}

    def create_tenant(self, tenant_id: str, name: str, tier: str = "basic") -> Tenant:
        """创建租户。"""
        tenant = Tenant(tenant_id, name, tier)
        self.tenants[tenant_id] = tenant
        return tenant

    def get_tenant(self, tenant_id: str) -> Tenant | None:
        return self.tenants.get(tenant_id)

    def check_access(self, tenant_id: str, tokens: int = 0) -> tuple[bool, str]:
        """检查访问权限。"""
        tenant = self.get_tenant(tenant_id)
        if tenant is None:
            return False, "租户不存在"

        return tenant.check_quota(tokens=tokens, api_calls=1)


def tenant_management_demo():
    """租户管理演示。"""
    print("=" * 60)
    print("Tenant Management Demo")
    print("=" * 60)

    manager = TenantManager()

    # 创建租户
    print("\n📦 创建租户:")
    basic = manager.create_tenant("tenant_001", "小公司", "basic")
    pro = manager.create_tenant("tenant_002", "中公司", "pro")
    enterprise = manager.create_tenant("tenant_003", "大公司", "enterprise")

    for tenant in [basic, pro, enterprise]:
        print(f"   - {tenant.name} ({tenant.tier}): Token 配额 {tenant.quota['token_limit']:,}")

    # 模拟使用
    print("\n📊 模拟使用:")
    basic.record_usage(tokens=50_000, api_calls=500)
    pro.record_usage(tokens=500_000, api_calls=5_000)
    enterprise.record_usage(tokens=5_000_000, api_calls=50_000)

    for tenant in [basic, pro, enterprise]:
        usage = tenant.usage_percentage()
        print(f"   - {tenant.name}: Token 使用率 {usage['token']:.1f}%, API 使用率 {usage['api_calls']:.1f}%")

    # 配额检查
    print("\n🔒 配额检查:")
    for tenant in [basic, pro, enterprise]:
        can_access, reason = manager.check_access(tenant.tenant_id, tokens=60_000)
        status = "✅ 通过" if can_access else "❌ 拒绝"
        print(f"   - {tenant.name} 请求 60K Token: {status} ({reason})")


if __name__ == "__main__":
    tenant_management_demo()
