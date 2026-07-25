"""
================================================================================
Day 3 - Prompt 对比实验 | 01_prompt_experiment.py
================================================================================

【学习目标】
对比不同 Prompt 的效果：准确率、Token 消耗、延迟

【前置知识】
- 00_context_builder.py（Context 组装）

【操作步骤】
1. 运行: python 01_prompt_experiment.py
2. 观察输出：3种 Prompt 的对比结果

【预期输出】
Prompt 对比实验
任务: 请解释什么是 Spring Boot 的自动配置原理

────────────────────────────────────────
📝 A: 无 Prompt（Zero-shot）
────────────────────────────────────────
⏱️  耗时: 1.20s
📊 Tokens: input=20, output=150, total=170
📄 输出长度: 150 字

────────────────────────────────────────
📝 B: 角色 + 指令
────────────────────────────────────────
⏱️  耗时: 1.50s
📊 Tokens: input=50, output=120, total=170
📄 输出长度: 120 字

────────────────────────────────────────
📝 C: Few-shot + CoT
────────────────────────────────────────
⏱️  耗时: 2.10s
📊 Tokens: input=150, output=200, total=350
📄 输出长度: 200 字

📊 实验汇总:
Prompt             耗时(s)    Input      Output     Total
A                   1.20       20         150        170
B                   1.50       50         120        170
C                   2.10       150        200        350

💡 结论:
   - Zero-shot 最简洁，但输出质量不稳定
   - 角色+指令 能显著提升输出质量
   - Few-shot + CoT 适合复杂推理任务，但 Token 消耗更大

【验证标准】
□ 能看到 3 种 Prompt 的对比
□ 理解 Prompt 对输出质量和 Token 消耗的影响

【代码要点】
- Zero-shot：无示例
- Few-shot：给 2-5 个示例
- CoT（Chain-of-Thought）：让模型一步步推理

================================================================================
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from model_config import ModelConfig


def run_prompt_experiment():
    """运行 Prompt 对比实验。"""
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ 请先安装依赖: pip install openai")
        sys.exit(1)

    config = ModelConfig.from_env()
    client = OpenAI(**config.get_client_kwargs())

    # 同一个任务，3种 Prompt
    task = "请解释什么是 Spring Boot 的自动配置原理"

    prompts = {
        "A: 无 Prompt（Zero-shot）": task,

        "B: 角色 + 指令": """你是一个有10年经验的Java架构师。
请用简洁的语言解释 Spring Boot 的自动配置原理。
要求：不超过150字，用列表形式输出。""",

        "C: Few-shot + CoT": """你是一个Java架构师。
请解释 Spring Boot 的自动配置原理。

示例：
问：什么是 Spring IOC？
答：1. 控制反转 2. 依赖注入 3. Bean 容器管理

请按以下步骤思考：
1. 先说明自动配置的目的
2. 解释 @EnableAutoConfiguration 的作用
3. 说明 spring.factories / AutoConfigurationImportSelector 的机制
4. 总结条件装配 @Conditional 的作用

请用中文回答，不超过200字。""",
    }

    results = {}

    print("=" * 60)
    print("Prompt 对比实验")
    print("=" * 60)
    print(f"任务: {task}\n")

    for name, prompt in prompts.items():
        print(f"\n{'─' * 40}")
        print(f"📝 {name}")
        print(f"{'─' * 40}")

        start_time = time.time()

        response = client.chat.completions.create(
            model=config.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=512,
        )

        elapsed = time.time() - start_time
        result = response.choices[0].message.content
        tokens = response.usage

        results[name] = {
            "time": elapsed,
            "input_tokens": tokens.prompt_tokens,
            "output_tokens": tokens.completion_tokens,
            "total_tokens": tokens.total_tokens,
            "result_length": len(result),
        }

        print(f"⏱️  耗时: {elapsed:.2f}s")
        print(f"📊 Tokens: input={tokens.prompt_tokens}, output={tokens.completion_tokens}, total={tokens.total_tokens}")
        print(f"📄 输出长度: {len(result)} 字")
        print(f"📤 输出:\n{result[:200]}...")

    # 汇总对比
    print(f"\n{'=' * 60}")
    print("📊 实验汇总")
    print(f"{'=' * 60}")
    print(f"{'Prompt':<20} {'耗时(s)':<10} {'Input':<10} {'Output':<10} {'Total':<10}")
    print(f"{'─' * 60}")

    for name, r in results.items():
        short_name = name.split("：")[0] if "：" in name else name[:10]
        print(f"{short_name:<20} {r['time']:<10.2f} {r['input_tokens']:<10} {r['output_tokens']:<10} {r['total_tokens']:<10}")

    print(f"\n💡 结论:")
    print(f"   - Zero-shot 最简洁，但输出质量不稳定")
    print(f"   - 角色+指令 能显著提升输出质量")
    print(f"   - Few-shot + CoT 适合复杂推理任务，但 Token 消耗更大")


if __name__ == "__main__":
    run_prompt_experiment()
