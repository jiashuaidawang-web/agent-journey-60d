"""
Day 20: Reranker Demo.

演示重排序（两阶段检索）。

Usage:
    python two_stage_retrieval.py
"""


def two_stage_retrieval_demo():
    """两阶段检索演示。"""
    from sentence_transformers import SentenceTransformer, CrossEncoder
    import numpy as np

    print("=" * 60)
    print("Two-Stage Retrieval Demo")
    print("=" * 60)

    # 知识库
    documents = [
        "贵州茅台是白酒行业龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
        "中国白酒行业CR5持续提升，高端化趋势明显",
        "动力电池需求随新能源车增长而增长",
        "互联网行业监管政策趋严",
        "高端白酒具有品牌壁垒",
        "新能源车渗透率持续提升",
    ]

    query = "白酒龙头企业有哪些"

    # 阶段1：召回（Bi-Encoder）
    print("\n📦 阶段1：召回（Bi-Encoder）...")
    bi_encoder = SentenceTransformer("BAAI/bge-m3")
    doc_embeddings = bi_encoder.encode(documents)
    query_embedding = bi_encoder.encode([query])

    # 计算相似度
    similarities = np.dot(doc_embeddings, query_embedding[0])
    similarities = similarities / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    # Top-K 召回
    recall_k = 5
    recall_indices = np.argsort(similarities)[::-1][:recall_k]
    recalled_docs = [documents[i] for i in recall_indices]

    print(f"   Top {recall_k} 召回:")
    for i, idx in enumerate(recall_indices):
        print(f"   [{i+1}] {documents[idx]} (相似度: {similarities[idx]:.4f})")

    # 阶段2：精排（Cross-Encoder）
    print(f"\n📦 阶段2：精排（Cross-Encoder）...")

    try:
        reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")

        # 构建 (query, doc) 对
        pairs = [(query, doc) for doc in recalled_docs]

        # 计算分数
        rerank_scores = reranker.predict(pairs)

        # 排序
        rerank_indices = np.argsort(rerank_scores)[::-1]

        print(f"   Top 3 精排结果:")
        for i in range(min(3, len(rerank_indices))):
            idx = rerank_indices[i]
            print(f"   [{i+1}] {recalled_docs[idx]} (Rerank: {rerank_scores[idx]:.4f})")

    except Exception as e:
        print(f"   ⚠️ Reranker 加载失败: {e}")
        print("   使用原始召回结果")

    print("\n✅ 两阶段检索演示完成")


if __name__ == "__main__":
    two_stage_retrieval_demo()
