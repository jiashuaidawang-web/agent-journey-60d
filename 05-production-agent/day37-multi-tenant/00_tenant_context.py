"""
Day 37: Multi-tenant Demo.

演示多租户隔离。

Usage:
    python tenant_context.py
"""


class TenantContext:
    """租户上下文（类似 Java ThreadLocal）。"""

    _current_tenant = None

    @classmethod
    def set_current_tenant(cls, tenant_id: str):
        cls._current_tenant = tenant_id

    @classmethod
    def get_current_tenant(cls) -> str | None:
        return cls._current_tenant

    @classmethod
    def clear(cls):
        cls._current_tenant = None


class DataIsolation:
    """数据隔离。"""

    def __init__(self):
        # 模拟数据库
        self.data: dict[str, list[dict]] = {
            "tenant_001": [
                {"id": 1, "name": "文档A"},
                {"id": 2, "name": "文档B"},
            ],
            "tenant_002": [
                {"id": 3, "name": "文档C"},
            ],
        }

    def query(self, tenant_id: str) -> list[dict]:
        """查询（自动过滤租户）。"""
        return self.data.get(tenant_id, [])

    def insert(self, tenant_id: str, item: dict):
        """插入（自动添加租户 ID）。"""
        if tenant_id not in self.data:
            self.data[tenant_id] = []
        self.data[tenant_id].append(item)


class QuotaIsolation:
    """配额隔离。"""

    def __init__(self):
        self.quotas: dict[str, dict] = {
            "tenant_001": {"token_limit": 100_000, "token_used": 0},
            "tenant_002": {"token_limit": 1_000_000, "token_used": 0},
        }

    def check_quota(self, tenant_id: str, tokens: int) -> tuple[bool, str]:
        """检查配额。"""
        quota = self.quotas.get(tenant_id)
        if quota is None:
            return False, "租户不存在"

        if quota["token_used"] + tokens > quota["token_limit"]:
            return False, "配额不足"

        return True, "通过"

    def consume(self, tenant_id: str, tokens: int):
        """消耗配额。"""
        if tenant_id in self.quotas:
            self.quotas[tenant_id]["token_used"] += tokens


def tenant_context_demo():
    """租户上下文演示。"""
    print("=" * 60)
    print("Multi-tenant Demo")
    print("=" * 60)

    # 租户上下文
    print("\n📦 租户上下文:")
    TenantContext.set_current_tenant("tenant_001")
    print(f"   当前租户: {TenantContext.get_current_tenant()}")

    # 数据隔离
    print("\n📦 数据隔离:")
    data_isolation = DataIsolation()

    for tenant_id in ["tenant_001", "tenant_002"]:
        items = data_isolation.query(tenant_id)
        print(f"   {tenant_id}: {len(items)} 条数据")

    # 配额隔离
    print("\n📦 配额隔离:")
    quota_isolation = QuotaIsolation()

    for tenant_id in ["tenant_001", "tenant_002"]:
        can_access, reason = quota_isolation.check_quota(tenant_id, 50_000)
        status = "✅ 通过" if can_access else "❌ 拒绝"
        print(f"   {tenant_id} 请求 50K Token: {status} ({reason})")


if __name__ == "__main__":
    tenant_context_demo()
