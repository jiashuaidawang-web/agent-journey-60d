"""
================================================================================
Day 56 - 模型选型决策代码 | 02_model_decision.py
================================================================================

【学习目标】
实现模型选型决策代码，根据业务需求选择模型

【前置知识】
- 00_model_platforms.py（平台对比）
- 01_ollama_integration.py（本地模型接入）

【操作步骤】
1. 阅读本文件，理解决策逻辑
2. 添加自己的决策规则
3. 运行代码，观察输出

【预期输出】
🎯 模型选型决策
├── 需求: 国内合规 → 推荐: 阿里百炼
├── 需求: 低成本 → 推荐: DeepSeek
├── 需求: 隐私优先 → 推荐: Ollama
└── 需求: 最强能力 → 推荐: OpenAI

【验证标准】
□ 能实现决策逻辑
□ 能覆盖多种场景
□ 能解释决策依据

【代码要点】
- 决策树逻辑
- 多维度评分
- 场景匹配

================================================================================
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ModelRequirement:
    """模型需求。"""
    compliance: Optional[str] = None      # 合规要求: 国内 / 海外
    budget: Optional[str] = None          # 预算: 低 / 中 / 高
    privacy: Optional[str] = None         # 隐私: 高 / 中 / 低
    chinese_ability: Optional[int] = None # 中文能力: 1-5
    tool_calling: Optional[bool] = None   # 工具调用: True / False
    multimodal: Optional[bool] = None     # 多模态: True / False
    latency: Optional[str] = None         # 延迟: 低 / 中 / 高


@dataclass
class ModelOption:
    """模型选项。"""
    name: str
    price_level: str
    chinese_ability: int
    tool_calling: bool
    multimodal: bool
    compliance: str
    score: int = 0


def get_all_models() -> List[ModelOption]:
    """获取所有可用模型。"""
    return [
        ModelOption("OpenAI GPT-4o", "$$$", 3, True, True, "海外"),
        ModelOption("DeepSeek V3", "$", 5, True, False, "海外"),
        ModelOption("阿里百炼 Qwen3", "¥", 5, True, True, "国内"),
        ModelOption("智谱 GLM-4", "¥", 4, True, False, "国内"),
        ModelOption("月之暗面 Kimi", "¥", 4, True, False, "海外"),
        ModelOption("硅基流动", "$", 4, True, False, "海外"),
        ModelOption("Ollama Llama", "免费", 3, True, False, "本地"),
    ]


def calculate_score(model: ModelOption, req: ModelRequirement) -> int:
    """根据需求计算模型得分。"""
    score = 0

    # 合规性（一票否决）
    if req.compliance == "国内" and model.compliance != "国内":
        return -100

    # 预算匹配
    if req.budget == "低" and model.price_level in ["$", "免费"]:
        score += 30
    elif req.budget == "中" and model.price_level in ["¥", "$$"]:
        score += 20
    elif req.budget == "高":
        score += 10

    # 隐私要求
    if req.privacy == "高" and model.compliance == "本地":
        score += 40
    elif req.privacy == "中" and model.compliance in ["国内", "本地"]:
        score += 20

    # 中文能力
    if req.chinese_ability:
        score += model.chinese_ability * 5

    # 工具调用
    if req.tool_calling and model.tool_calling:
        score += 20

    # 多模态
    if req.multimodal and model.multimodal:
        score += 15

    return score


def select_model(req: ModelRequirement) -> Optional[str]:
    """根据需求选择最佳模型。"""
    models = get_all_models()
    best_model = None
    best_score = -1000

    for model in models:
        score = calculate_score(model, req)
        if score > best_score:
            best_score = score
            best_model = model

    return best_model.name if best_model else None


def demo_scenarios():
    """演示多种场景的模型选择。"""
    scenarios = [
        ("国内合规场景", ModelRequirement(
            compliance="国内",
            budget="中",
            chinese_ability=5,
            tool_calling=True
        )),
        ("低成本场景", ModelRequirement(
            budget="低",
            chinese_ability=4,
            tool_calling=True
        )),
        ("隐私优先场景", ModelRequirement(
            privacy="高",
            chinese_ability=3,
            tool_calling=True
        )),
        ("最强能力场景", ModelRequirement(
            budget="高",
            chinese_ability=4,
            tool_calling=True,
            multimodal=True
        )),
        ("本地开发场景", ModelRequirement(
            privacy="高",
            budget="低",
            chinese_ability=3
        )),
    ]

    print("🎯 模型选型决策：")
    print("-" * 60)
    for name, req in scenarios:
        model = select_model(req)
        print(f"├── 场景: {name}")
        print(f"│   需求: 合规={req.compliance}, 预算={req.budget}, 隐私={req.privacy}")
        print(f"│   推荐: {model}")
        print()


def main():
    """主函数：展示模型选型决策。"""
    print("=" * 60)
    print("🎯 模型选型决策")
    print("=" * 60)
    print()

    demo_scenarios()

    print("=" * 60)
    print("✅ 模型选型决策演示完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
