"""
Day 39: Generation Evaluation.

演示生成质量评测。

Usage:
    python generation_eval.py
"""


def faithfulness_score(answer: str, context: str) -> float:
    """Faithfulness：回答是否基于上下文。

    简化版：检查回答中的关键信息是否在上下文中。
    """
    # 提取关键信息（简化：按空格分词）
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    # 计算重叠
    overlap = len(answer_words & context_words)
    total = len(answer_words)

    return overlap / total if total > 0 else 0


def answer_relevance_score(answer: str, query: str) -> float:
    """Answer Relevance：回答是否切题。

    简化版：检查回答中是否包含查询关键词。
    """
    query_words = set(query.lower().split())
    answer_words = set(answer.lower().split())

    overlap = len(query_words & answer_words)
    total = len(query_words)

    return overlap / total if total > 0 else 0


def generation_eval_demo():
    """生成评测演示。"""
    print("=" * 60)
    print("Generation Evaluation Demo")
    print("=" * 60)

    eval_data = [
        {
            "query": "白酒龙头企业有哪些",
            "context": "贵州茅台是白酒行业龙头，市占率超过50%。五粮液是第二大白酒企业。",
            "answer": "白酒龙头企业包括贵州茅台和五粮液。",
        },
        {
            "query": "贵州茅台股价",
            "context": "贵州茅台当前股价1680元，PE 30倍。",
            "answer": "贵州茅台股价1680元。",
        },
        {
            "query": "动力电池龙头",
            "context": "宁德时代是动力电池龙头，全球市占率37%。",
            "answer": "比亚迪是新能源车龙头。",  # 错误答案
        },
    ]

    print(f"\n📊 生成评测结果:")
    print(f"{'Query':<20} {'Faith.':<10} {'Relev.':<10}")
    print("-" * 40)

    for data in eval_data:
        query = data["query"]
        context = data["context"]
        answer = data["answer"]

        faith = faithfulness_score(answer, context)
        relev = answer_relevance_score(answer, query)

        print(f"{query:<20} {faith:<10.4f} {relev:<10.4f}")

    print("\n💡 说明:")
        print("   Faithfulness: 回答是否基于上下文")
        print("   Relevance: 回答是否切题")


if __name__ == "__main__":
    generation_eval_demo()
