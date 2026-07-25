"""
Day 39: RAG Evaluation.

演示 RAG 系统的评测。

Usage:
    python retrieval_eval.py
"""


def precision_at_k(retrieved: list[int], relevant: list[int], k: int) -> float:
    """Precision@K。"""
    retrieved_k = retrieved[:k]
    relevant_count = len(set(retrieved_k) & set(relevant))
    return relevant_count / k if k > 0 else 0


def recall_at_k(retrieved: list[int], relevant: list[int], k: int) -> float:
    """Recall@K。"""
    retrieved_k = retrieved[:k]
    relevant_count = len(set(retrieved_k) & set(relevant))
    return relevant_count / len(relevant) if relevant else 0


def mrr(retrieved: list[int], relevant: list[int]) -> float:
    """Mean Reciprocal Rank。"""
    for i, doc in enumerate(retrieved):
        if doc in relevant:
            return 1 / (i + 1)
    return 0


def ndcg_at_k(retrieved: list[int], relevant: list[int], k: int) -> float:
    """NDCG@K。"""
    dcg = 0
    for i, doc in enumerate(retrieved[:k]):
        if doc in relevant:
            dcg += 1 / (i + 1)

    idcg = sum(1 / (i + 1) for i in range(min(len(relevant), k)))
    return dcg / idcg if idcg > 0 else 0


def retrieval_eval_demo():
    """检索评测演示。"""
    print("=" * 60)
    print("Retrieval Evaluation Demo")
    print("=" * 60)

    # 评测数据集
    eval_data = [
        {
            "query": "白酒龙头",
            "relevant_docs": [0, 3, 5],
            "retrieved_docs": [0, 1, 3, 5, 2],
        },
        {
            "query": "电池龙头",
            "relevant_docs": [1, 4],
            "retrieved_docs": [1, 2, 4, 0, 3],
        },
        {
            "query": "新能源车",
            "relevant_docs": [2, 6],
            "retrieved_docs": [2, 4, 6, 1, 0],
        },
    ]

    print(f"\n📊 检索评测结果:")
    print(f"{'Query':<12} {'P@3':<8} {'R@3':<8} {'MRR':<8} {'NDCG@3':<8}")
    print("-" * 44)

    for data in eval_data:
        query = data["query"]
        relevant = data["relevant_docs"]
        retrieved = data["retrieved_docs"]

        p = precision_at_k(retrieved, relevant, 3)
        r = recall_at_k(retrieved, relevant, 3)
        m = mrr(retrieved, relevant)
        n = ndcg_at_k(retrieved, relevant, 3)

        print(f"{query:<12} {p:<8.4f} {r:<8.4f} {m:<8.4f} {n:<8.4f}")

    # 汇总
    avg_p = sum(precision_at_k(d["retrieved_docs"], d["relevant_docs"], 3) for d in eval_data) / len(eval_data)
    avg_r = sum(recall_at_k(d["retrieved_docs"], d["relevant_docs"], 3) for d in eval_data) / len(eval_data)
    avg_m = sum(mrr(d["retrieved_docs"], d["relevant_docs"]) for d in eval_data) / len(eval_data)
    avg_n = sum(ndcg_at_k(d["retrieved_docs"], d["relevant_docs"], 3) for d in eval_data) / len(eval_data)

    print("-" * 44)
    print(f"{'Average':<12} {avg_p:<8.4f} {avg_r:<8.4f} {avg_m:<8.4f} {avg_n:<8.4f}")


if __name__ == "__main__":
    retrieval_eval_demo()
