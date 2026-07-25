"""
Day 41: RAGAS Demo.

演示 RAGAS 框架的使用。

Usage:
    python ragas_demo.py
"""


def ragas_metrics_demo():
    """RAGAS 指标演示。"""
    print("=" * 60)
    print("RAGAS Metrics Demo")
    print("=" * 60)

    # RAGAS 指标说明
    metrics = {
        "faithfulness": {
            "description": "回答是否基于上下文",
            "dimension": "生成质量",
            "range": "0-1",
            "higher_better": True,
        },
        "answer_relevancy": {
            "description": "回答是否切题",
            "dimension": "生成质量",
            "range": "0-1",
            "higher_better": True,
        },
        "context_recall": {
            "description": "上下文是否覆盖答案所需信息",
            "dimension": "检索质量",
            "range": "0-1",
            "higher_better": True,
        },
        "context_precision": {
            "description": "上下文是否相关，没有噪声",
            "dimension": "检索质量",
            "range": "0-1",
            "higher_better": True,
        },
    }

    print("\n📊 RAGAS 指标:")
    for name, info in metrics.items():
        print(f"\n   {name}:")
        print(f"      描述: {info['description']}")
        print(f"      维度: {info['dimension']}")
        print(f"      范围: {info['range']}")

    # 模拟评测结果
    print(f"\n📊 模拟评测结果:")
    eval_results = {
        "faithfulness": 0.92,
        "answer_relevancy": 0.88,
        "context_recall": 0.85,
        "context_precision": 0.90,
    }

    for metric, score in eval_results.items():
        bar = "█" * int(score * 20)
        print(f"   {metric:<20} {score:.2f} {bar}")

    # 综合评分
    avg_score = sum(eval_results.values()) / len(eval_results)
    print(f"\n   综合评分: {avg_score:.2f}")

    return eval_results


def ragas_evaluation_flow():
    """RAGAS 评测流程。"""
    print("\n" + "=" * 60)
    print("RAGAS Evaluation Flow")
    print("=" * 60)

    flow = [
        "1. 构建评测数据集",
        "   - questions: 用户问题列表",
        "   - contexts: 检索到的上下文列表",
        "   - answers: 生成的回答列表",
        "   - ground_truths: 标准答案列表",
        "",
        "2. 选择评测指标",
        "   - faithfulness",
        "   - answer_relevancy",
        "   - context_recall",
        "   - context_precision",
        "",
        "3. 运行评测",
        "   result = evaluate(dataset, metrics=[...])",
        "",
        "4. 分析结果",
        "   - 各指标得分",
        "   - 综合评分",
        "   - 问题分析",
    ]

    print("\n📋 评测流程:")
    for line in flow:
        print(f"   {line}")


if __name__ == "__main__":
    ragas_metrics_demo()
    ragas_evaluation_flow()
