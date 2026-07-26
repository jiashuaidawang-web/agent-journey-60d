"""
================================================================================
Day 58 - 动态切模型 Advisor | 03_model_router_advisor.py
================================================================================

【学习目标】
实现动态切模型 Advisor，理解模型路由机制

【前置知识】
- 00_advisor_chain.py（责任链基础）
- 01_logging_advisor.py（日志 Advisor）

【操作步骤】
1. 阅读本文件，理解模型路由实现
2. 扩展路由策略
3. 运行代码，观察输出

【预期输出】
🎯 动态切模型 Advisor
├── VIP 用户 → gpt-4o
└── 普通用户 → gpt-4o-mini

【验证标准】
□ 能实现模型路由
□ 能根据用户等级选择模型
□ 能处理降级策略

【代码要点】
- 用户等级: VIP / PREMIUM / NORMAL
- 模型映射: 等级 → 模型
- 降级策略: 主模型故障时切换

================================================================================
"""

import sys
import time
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class UserLevel(Enum):
    """用户等级。"""
    VIP = "VIP"
    PREMIUM = "PREMIUM"
    NORMAL = "NORMAL"


@dataclass
class AdvisorRequest:
    """Advisor 请求。"""
    user_text: str
    system_text: str = ""
    advise_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AdvisorResponse:
    """Advisor 响应。"""
    user_text: str
    system_text: str = ""
    advise_context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChatClientResponse:
    """ChatClient 响应。"""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class Advisor:
    """Advisor 接口。"""

    def before(self, request: AdvisorRequest, chain: 'AdvisorChain') -> AdvisorResponse:
        return chain.next_before(request)

    def after(self, response: ChatClientResponse, chain: 'AdvisorChain') -> ChatClientResponse:
        return chain.next_after(response)

    def get_order(self) -> int:
        return 0


class AdvisorChain:
    """Advisor 责任链。"""

    def __init__(self, advisors: List[Advisor]):
        self.advisors = sorted(advisors, key=lambda a: a.get_order())
        self.before_index = 0
        self.after_index = len(self.advisors) - 1

    def next_before(self, request: AdvisorRequest) -> AdvisorResponse:
        if self.before_index < len(self.advisors):
            advisor = self.advisors[self.before_index]
            self.before_index += 1
            return advisor.before(request, self)
        return AdvisorResponse(
            user_text=request.user_text,
            system_text=request.system_text,
            advise_context=request.advise_context
        )

    def next_after(self, response: ChatClientResponse) -> ChatClientResponse:
        if self.after_index >= 0:
            advisor = self.advisors[self.after_index]
            self.after_index -= 1
            return advisor.after(response, self)
        return response


class ModelRouterAdvisor(Advisor):
    """动态切模型 Advisor。

    根据用户等级、任务类型、成本等因素动态选择模型。
    """

    # 用户等级 → 模型映射
    LEVEL_MODEL_MAP = {
        UserLevel.VIP: "gpt-4o",
        UserLevel.PREMIUM: "gpt-4o-mini",
        UserLevel.NORMAL: "ollama-llama"
    }

    # 任务类型 → 模型映射
    TASK_MODEL_MAP = {
        "code-generation": "gpt-4o",
        "translation": "deepseek-v3",
        "chat": "gpt-4o-mini"
    }

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        """前置处理：选择模型。"""
        print(f"   🎯 [ModelRouter] 选择模型...")

        # 获取用户等级
        user_level = self._get_user_level(request)
        print(f"      用户等级: {user_level.value}")

        # 根据用户等级选择模型
        model = self.LEVEL_MODEL_MAP.get(user_level, "gpt-4o-mini")
        print(f"      选择模型: {model}")

        # 设置目标模型
        request.advise_context['target_model'] = model
        request.advise_context['user_level'] = user_level.value

        return chain.next_before(request)

    def _get_user_level(self, request: AdvisorRequest) -> UserLevel:
        """获取用户等级。"""
        # 从上下文获取用户 ID，查询用户等级
        user_id = request.advise_context.get('userId')
        if user_id:
            # 模拟从数据库查询
            level_map = {
                "user-vip": UserLevel.VIP,
                "user-premium": UserLevel.PREMIUM,
            }
            return level_map.get(user_id, UserLevel.NORMAL)
        return UserLevel.NORMAL

    def get_order(self) -> int:
        return 15


class CostAwareModelRouterAdvisor(Advisor):
    """成本感知模型路由 Advisor。

    在用户等级基础上，考虑成本因素。
    """

    # 模型价格（每 1M tokens）
    MODEL_PRICE = {
        "gpt-4o": 2.5,
        "gpt-4o-mini": 0.15,
        "deepseek-v3": 0.1,
        "ollama-llama": 0.0
    }

    def before(self, request: AdvisorRequest, chain: AdvisorChain) -> AdvisorResponse:
        """前置处理：成本感知选择模型。"""
        print(f"   💰 [CostAwareRouter] 成本感知选择模型...")

        user_level = request.adviseContext().get('userLevel', 'NORMAL')
        budget = request.adviseContext().get('budget', 'unlimited')

        # 根据用户等级和预算选择模型
        if user_level == 'VIP':
            model = "gpt-4o"
        elif budget == 'low':
            model = "ollama-llama"
        elif budget == 'medium':
            model = "deepseek-v3"
        else:
            model = "gpt-4o-mini"

        price = self.MODEL_PRICE.get(model, 0)
        print(f"      选择模型: {model} (${price}/1M tokens)")

        request.advise_context['target_model'] = model
        return chain.next_before(request)

    def get_order(self) -> int:
        return 16


def demo_user_level_routing():
    """演示基于用户等级的模型路由。"""
    print("🎯 基于用户等级的模型路由：")
    print("-" * 40)

    advisor = ModelRouterAdvisor()

    test_cases = [
        ("user-vip", "VIP 用户"),
        ("user-premium", "PREMIUM 用户"),
        ("user-normal", "普通用户"),
    ]

    for user_id, description in test_cases:
        print(f"📤 {description} ({user_id})：")
        request = AdvisorRequest(
            user_text="你好",
            advise_context={"userId": user_id}
        )
        chain = AdvisorChain([advisor])
        chain.next_before(request)
        print(f"     目标模型: {request.advise_context.get('target_model')}")
        print()


def demo_cost_aware_routing():
    """演示成本感知的模型路由。"""
    print("💰 成本感知的模型路由：")
    print("-" * 40)

    test_cases = [
        ("VIP", "unlimited", "VIP 用户，无限制"),
        ("NORMAL", "low", "普通用户，低预算"),
        ("NORMAL", "medium", "普通用户，中等预算"),
        ("NORMAL", "unlimited", "普通用户，无限制"),
    ]

    for level, budget, description in test_cases:
        print(f"📤 {description}：")
        print(f"      等级: {level}, 预算: {budget}")

        if level == "VIP":
            model = "gpt-4o"
        elif budget == "low":
            model = "ollama-llama"
        elif budget == "medium":
            model = "deepseek-v3"
        else:
            model = "gpt-4o-mini"

        print(f"      选择模型: {model}")
        print()


def show_java_code():
    """展示 Java 实现。"""
    print("💻 Java 实现：")
    print("-" * 40)
    print("""
public class ModelRouterAdvisor implements Advisor {

    private final Map<String, ChatClient> modelMap;

    public ModelRouterAdvisor(
        @Qualifier("openAiClient") ChatClient openAiClient,
        @Qualifier("ollamaClient") ChatClient ollamaClient
    ) {
        this.modelMap = Map.of(
            "gpt-4o", openAiClient,
            "ollama-llama", ollamaClient
        );
    }

    @Override
    public AdvisorResponse before(AdvisorRequest request, AdvisorChain chain) {
        String userId = (String) request.adviseContext().get("userId");
        String userLevel = getUserLevel(userId);

        // 根据用户等级选择模型
        String model = switch (userLevel) {
            case "VIP" -> "gpt-4o";
            case "PREMIUM" -> "gpt-4o-mini";
            default -> "ollama-llama";
        };

        // 设置目标模型
        request.adviseContext().put("targetModel", model);
        return chain.nextBefore(request);
    }

    private String getUserLevel(String userId) {
        // 从数据库或缓存获取用户等级
        return "VIP";
    }

    @Override
    public int getOrder() {
        return 15;
    }
}
""")


def main():
    """主函数：展示动态切模型 Advisor。"""
    print("=" * 60)
    print("🎯 动态切模型 Advisor")
    print("=" * 60)
    print()

    demo_user_level_routing()
    demo_cost_aware_routing()
    show_java_code()

    print("=" * 60)
    print("✅ 动态切模型 Advisor 演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
