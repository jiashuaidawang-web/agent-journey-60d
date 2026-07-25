"""
Day 22: RAG Evaluation.

RAG 系统评测。

Usage:
    python rag_evaluation.py
"""


def rag_evaluation_demo():
    """RAG 评测演示。"""
    print("=" * 60)
    print("RAG Evaluation Demo")
    print("=" * 60)

    # 模拟数据
    ground_truth = [
        {"query": "白酒龙头", "relevant_docs": [0, 3, 5]},
        {"query": "电池龙头", "relevant_docs": [1, 4]},
        {"query": "新能源车", "relevant_docs": [2, 6]},
    ]

    # 模拟检索结果
    retrieval_results = [
        {"query": "白酒龙头", "retrieved_docs": [0, 1, 3, 5]},
        {"query": "电池龙头", "retrieved_docs": [1, 2, 4]},
        {"query": "新能源车", "retrieved_docs": [2, 4, 6]},
    ]

    # 计算指标
    def precision_at_k(retrieved, relevant, k):
        """Precision@K。"""
        retrieved_k = retrieved[:k]
        relevant_count = len(set(retrieved_k) & set(relevant))
        return relevant_count / k

    def recall_at_k(retrieved, relevant, k):
        """Recall@K。"""
        retrieved_k = retrieved[:k]
        relevant_count = len(set(retrieved_k) & set(relevant))
        return relevant_count / len(relevant) if relevant else 0

    def mrr(retrieved, relevant):
        """Mean Reciprocal Rank。"""
        for i, doc in enumerate(retrieved):
            if doc in relevant:
                return 1 / (i + 1)
        return 0

    def ndcg_at_k(retrieved, relevant, k):
        """NDCG@K。"""
        dcg = 0
        for i, doc in enumerate(retrieved[:k]):
            if doc in relevant:
                dcg += 1 / (i + 1)

        # IDCG
        idcg = sum(1 / (i + 1) for i in range(min(len(relevant), k)))

        return dcg / idcg if idcg > 0 else 0

    print("\n📊 评测结果:")
    print(f"{'Query':<12} {'P@3':<8} {'R@3':<8} {'MRR':<8} {'NDCG@3':<8}")
    print("-" * 44)

    for gt, rt in zip(ground_truth, retrieval_results):
        query = gt["query"]
        relevant = gt["relevant_docs"]
        retrieved = rt["retrieved_docs"]

        p = precision_at_k(retrieved, relevant, 3)
        r = recall_at_k(retrieved, relevant, 3)
        m = mrr(retrieved, relevant)
        n = ndcg_at_k(retrieved, relevant, 3)

        print(f"{query:<12} {p:<8.4f} {r:<8.4f} {m:<8.4f} {n:<8.4f}")

    # 汇总
    avg_p = sum(precision_at_k(rt["retrieved_docs"], gt["relevant_docs"], 3)
                for gt, rt in zip(ground_truth, retrieval_results)) / len(ground_truth)
    avg_r = sum(recall_at_k(rt["retrieved_docs"], gt["relevant_docs"], 3)
                for gt, rt in zip(ground_truth, retrieval_results)) / len(ground_truth)

    print("-" * 44)
    print(f"{'Average':<12} {avg_p:<8.4f} {avg_r:<8.4f}")

    print("\n✅ 评测完成")


if __name__ == "__main__":
    rag_evaluation_demo()
