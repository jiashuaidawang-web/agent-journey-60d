"""
Day 19: BM25 + Hybrid Retrieval.

演示 BM25 和混合检索。

Usage:
    python hybrid_retrieval.py
"""


def bm25_demo():
    """BM25 演示。"""
    try:
        from rank_bm25 import BM25Okapi
    except ImportError:
        print("⚠️ rank_bm25 未安装，使用模拟实现")
        return bm25_mock_demo()

    print("=" * 60)
    print("BM25 Demo")
    print("=" * 60)

    # 文档集合
    documents = [
        "贵州茅台是白酒行业龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
        "中国白酒行业CR5持续提升，高端化趋势明显",
        "动力电池需求随新能源车增长而增长",
    ]

    # 分词（简化：按字切分）
    tokenized_docs = [list(doc) for doc in documents]

    # 创建 BM25
    bm25 = BM25Okapi(tokenized_docs)

    # 查询
    queries = ["白酒龙头", "电池龙头", "新能源"]

    for query in queries:
        print(f"\n🔍 查询: '{query}'")
        tokenized_query = list(query)

        # 获取分数
        scores = bm25.get_scores(tokenized_query)

        # 排序
        top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]

        print(f"   Top 3 结果:")
        for i, idx in enumerate(top_indices):
            print(f"   [{i+1}] {documents[idx]} (BM25: {scores[idx]:.4f})")


def bm25_mock_demo():
    """BM25 模拟演示。"""
    print("=" * 60)
    print("BM25 Mock Demo")
    print("=" * 60)

    documents = [
        "贵州茅台是白酒行业龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
    ]

    # 模拟 BM25 分数（基于关键词匹配）
    query = "白酒龙头"
    scores = []
    for doc in documents:
        score = sum(1 for word in query if word in doc)
        scores.append(score)

    print(f"\n🔍 查询: '{query}'")
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    for i, idx in enumerate(top_indices):
        print(f"   [{i+1}] {documents[idx]} (匹配词数: {scores[idx]})")


def hybrid_retrieval_demo():
    """混合检索演示。"""
    from sentence_transformers import SentenceTransformer
    import numpy as np

    print("\n" + "=" * 60)
    print("Hybrid Retrieval Demo")
    print("=" * 60)

    model = SentenceTransformer("BAAI/bge-m3")

    documents = [
        "贵州茅台是白酒行业龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
        "中国白酒行业CR5持续提升",
        "动力电池需求随新能源车增长",
    ]

    # Dense 检索
    doc_embeddings = model.encode(documents)

    query = "白酒龙头企业"
    query_embedding = model.encode([query])

    # Dense 分数
    dense_scores = np.dot(doc_embeddings, query_embedding[0])
    dense_scores = dense_scores / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    # Sparse 分数（模拟 BM25）
    sparse_scores = []
    for doc in documents:
        score = sum(1 for word in query if word in doc)
        sparse_scores.append(score)
    sparse_scores = np.array(sparse_scores)

    # RRF 融合
    def rrf_fusion(dense_scores, sparse_scores, k=60):
        """Reciprocal Rank Fusion。"""
        n = len(dense_scores)
        final_scores = np.zeros(n)

        # Dense 排名
        dense_rank = np.argsort(np.argsort(-dense_scores))
        # Sparse 排名
        sparse_rank = np.argsort(np.argsort(-sparse_scores))

        for i in range(n):
            final_scores[i] = 1 / (k + dense_rank[i]) + 1 / (k + sparse_rank[i])

        return final_scores

    final_scores = rrf_fusion(dense_scores, sparse_scores)

    # 结果
    print(f"\n🔍 查询: '{query}'")

    print(f"\n   Dense 排名:")
    dense_top = np.argsort(dense_scores)[::-1][:3]
    for i, idx in enumerate(dense_top):
        print(f"   [{i+1}] {documents[idx]} (分数: {dense_scores[idx]:.4f})")

    print(f"\n   Sparse 排名:")
    sparse_top = np.argsort(sparse_scores)[::-1][:3]
    for i, idx in enumerate(sparse_top):
        print(f"   [{i+1}] {documents[idx]} (分数: {sparse_scores[idx]:.4f})")

    print(f"\n   Hybrid (RRF) 排名:")
    final_top = np.argsort(final_scores)[::-1][:3]
    for i, idx in enumerate(final_top):
        print(f"   [{i+1}] {documents[idx]} (融合分数: {final_scores[idx]:.4f})")


if __name__ == "__main__":
    bm25_demo()
    hybrid_retrieval_demo()
