"""
Day 47: SFT / DPO Demo.

演示 SFT 和 DPO 原理。

Usage:
    python sft_dpo_demo.py
"""


def sft_demo():
    """SFT 演示。"""
    print("=" * 60)
    print("SFT Demo")
    print("=" * 60)

    # SFT 数据格式
    sft_data = [
        {
            "instruction": "请分析以下股票",
            "input": "贵州茅台",
            "output": "贵州茅台是白酒行业龙头，市占率超过50%...",
        },
        {
            "instruction": "请计算以下数学题",
            "input": "123 * 456",
            "output": "123 * 456 = 56088",
        },
    ]

    print("\n📦 SFT 数据格式:")
    for i, item in enumerate(sft_data):
        print(f"\n   样本 {i+1}:")
        print(f"   - instruction: {item['instruction']}")
        print(f"   - input: {item['input']}")
        print(f"   - output: {item['output']}")

    print("\n💡 SFT 原理:")
    print("   - 使用标注数据（问题-答案对）微调")
    print("   - 模型学习特定格式和风格")
    print("   - 类似'带答案的学习'")


def dpo_demo():
    """DPO 演示。"""
    print("\n" + "=" * 60)
    print("DPO Demo")
    print("=" * 60)

    # DPO 数据格式
    dpo_data = [
        {
            "prompt": "请分析贵州茅台",
            "chosen": "贵州茅台是白酒行业龙头，市占率超过50%，基本面稳健...",
            "rejected": "贵州茅台是一家公司。",
        },
    ]

    print("\n📦 DPO 数据格式:")
    for i, item in enumerate(dpo_data):
        print(f"\n   样本 {i+1}:")
        print(f"   - prompt: {item['prompt']}")
        print(f"   - chosen (好答案): {item['chosen'][:50]}...")
        print(f"   - rejected (差答案): {item['rejected']}")

    print("\n💡 DPO 原理:")
    print("   - 使用偏好数据（好答案 vs 差答案）")
    print("   - 直接优化模型，无需 Reward Model")
    print("   - 比 RLHF 更简单、更稳定")


def rlhf_vs_dpo():
    """RLHF vs DPO 对比。"""
    print("\n" + "=" * 60)
    print("RLHF vs DPO")
    print("=" * 60)

    comparison = """
   RLHF（Reinforcement Learning from Human Feedback）:
   ┌─────────────────────────────────────────────────┐
   │ SFT → Reward Model 训练 → PPO 微调              │
   └─────────────────────────────────────────────────┘
   - 需要训练 Reward Model
   - PPO 训练不稳定
   - 流程复杂

   DPO（Direct Preference Optimization）:
   ┌─────────────────────────────────────────────────┐
   │ SFT → DPO 微调（直接优化）                       │
   └─────────────────────────────────────────────────┘
   - 无需 Reward Model
   - 训练简单稳定
   - 效果更好
"""
    print(comparison)


if __name__ == "__main__":
    sft_demo()
    dpo_demo()
    rlhf_vs_dpo()
