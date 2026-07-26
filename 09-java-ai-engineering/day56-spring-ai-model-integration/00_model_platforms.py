"""
================================================================================
Day 56 - 主流模型平台对比 | 00_model_platforms.py
================================================================================

【学习目标】
整理主流模型平台对比表，理解各平台特点和接入方式

【前置知识】
- Day 55 Spring AI 总览

【操作步骤】
1. 阅读本文件，理解各平台特点
2. 整理自己的对比表
3. 运行代码，观察输出

【预期输出】
📊 主流模型平台对比
├── OpenAI: GPT-4o / GPT-5 | 价格: $$$ | 中文: ⭐⭐⭐
├── DeepSeek: V3 | 价格: $ | 中文: ⭐⭐⭐⭐⭐
├── 阿里百炼: Qwen3 | 价格: ¥ | 中文: ⭐⭐⭐⭐⭐
└── Ollama: Llama / Qwen | 价格: 免费 | 中文: 取决于模型

【验证标准】
□ 能说出各平台特点
□ 能对比各平台优劣势
□ 能根据场景选择模型

【代码要点】
- dataclass 定义平台数据
- 对比表展示各维度
- 决策树逻辑

================================================================================
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ModelPlatform:
    """模型平台数据模型。"""
    name: str                          # 平台名称
    models: List[str]                  # 代表模型
    price_level: str                   # 价格水平: $ / $$ / $$$
    chinese_ability: int               # 中文能力: 1-5
    tool_calling: bool                 # 是否支持工具调用
    multimodal: bool                   # 是否支持多模态
    compliance: str                    # 合规性: 国内 / 海外
    access_type: str                   # 接入方式: 官方SDK / OpenAI兼容
    base_url: str = ""                 # API 地址


def get_all_platforms() -> List[ModelPlatform]:
    """获取所有主流模型平台信息。"""
    return [
        ModelPlatform(
            name="OpenAI",
            models=["GPT-4o", "GPT-4o-mini", "GPT-5"],
            price_level="$$$",
            chinese_ability=3,
            tool_calling=True,
            multimodal=True,
            compliance="海外",
            access_type="官方SDK / OpenAI兼容",
            base_url="https://api.openai.com/v1"
        ),
        ModelPlatform(
            name="DeepSeek",
            models=["DeepSeek V3", "DeepSeek R1"],
            price_level="$",
            chinese_ability=5,
            tool_calling=True,
            multimodal=False,
            compliance="海外",
            access_type="OpenAI兼容",
            base_url="https://api.deepseek.com/v1"
        ),
        ModelPlatform(
            name="阿里百炼",
            models=["通义千问 Qwen3", "Qwen2.5"],
            price_level="¥",
            chinese_ability=5,
            tool_calling=True,
            multimodal=True,
            compliance="国内",
            access_type="官方SDK",
            base_url="https://dashscope.aliyuncs.com"
        ),
        ModelPlatform(
            name="智谱",
            models=["GLM-4", "GLM-4-Flash"],
            price_level="¥",
            chinese_ability=4,
            tool_calling=True,
            multimodal=False,
            compliance="国内",
            access_type="OpenAI兼容",
            base_url="https://open.bigmodel.cn/api/paas/v4"
        ),
        ModelPlatform(
            name="月之暗面",
            models=["Kimi"],
            price_level="¥",
            chinese_ability=4,
            tool_calling=True,
            multimodal=False,
            compliance="海外",
            access_type="OpenAI兼容",
            base_url="https://api.moonshot.cn/v1"
        ),
        ModelPlatform(
            name="硅基流动",
            models=["聚合 API"],
            price_level="$",
            chinese_ability=4,
            tool_calling=True,
            multimodal=False,
            compliance="海外",
            access_type="OpenAI兼容",
            base_url="https://api.siliconflow.cn/v1"
        ),
        ModelPlatform(
            name="Ollama",
            models=["Llama", "Mistral", "Qwen", "CodeLlama"],
            price_level="免费",
            chinese_ability=3,
            tool_calling=True,
            multimodal=False,
            compliance="本地",
            access_type="本地API",
            base_url="http://localhost:11434"
        ),
    ]


def display_platforms(platforms: List[ModelPlatform]):
    """展示模型平台对比表。"""
    print("📊 主流模型平台对比：")
    print("-" * 60)
    for p in platforms:
        stars = "⭐" * p.chinese_ability
        print(f"├── {p.name}: {', '.join(p.models[:2])}")
        print(f"│   价格: {p.price_level} | 中文: {stars}")
        print(f"│   合规: {p.compliance} | 工具调用: {'✅' if p.tool_calling else '❌'}")
        print()


def show_decision_tree():
    """展示模型选型决策树。"""
    print("🎯 模型选型决策树：")
    print("""
├── 需要国内合规？
│   ├── 是 → 阿里百炼 / 百度 / 智谱
│   └── 否 → 继续
│
├── 需要最强能力？
│   ├── 是 → OpenAI GPT-4o / GPT-5
│   └── 否 → 继续
│
├── 需要性价比？
│   ├── 是 → DeepSeek V3 / 硅基流动
│   └── 否 → 继续
│
├── 需要本地部署？
│   ├── 是 → Ollama + Llama / Qwen
│   └── 否 → 继续
│
└── 需要长文本？
    ├── 是 → Kimi / Claude 4
    └── 否 → 根据预算选择
""")


def main():
    """主函数：展示主流模型平台对比。"""
    print("=" * 60)
    print("📊 主流模型平台对比")
    print("=" * 60)
    print()

    platforms = get_all_platforms()
    display_platforms(platforms)
    show_decision_tree()

    print("=" * 60)
    print("✅ 模型平台对比完成")
    print("=" * 60)


if __name__ == "__main__":
    main()
