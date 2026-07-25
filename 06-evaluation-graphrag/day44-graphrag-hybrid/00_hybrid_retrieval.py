"""
Day 44: GraphRAG Hybrid Demo.

演示 Graph + Vector 混合检索。

Usage:
    python hybrid_retrieval.py
"""


def hybrid_retrieval_demo():
    """混合检索演示。"""
    print("=" * 60)
    print("GraphRAG Hybrid Demo")
    print("=" * 60)

    # 模拟数据
    query = "白酒龙头企业"

    # 向量检索结果（按相似度排序）
    vector_results = [
        {"id": 1, "text": "贵州茅台是白酒龙头", "score": 0.95},
        {"id": 2, "text": "五粮液是白酒企业", "score": 0.88},
        {"id": 3, "text": "白酒行业CR5提升", "score": 0.82},
    ]

    # 图检索结果（按关系排序）
    graph_results = [
        {"id": 1, "text": "贵州茅台 -[龙头]-> 白酒", "hops": 1},
        {"id": 4, "text": "贵州茅台 -[竞争对手]-> 五粮液", "hops": 1},
        {"id": 5, "text": "白酒 -[包含]-> 泸州老窖", "hops": 2},
    ]

    print(f"\n🔍 查询: '{query}'")

    print(f"\n📦 向量检索结果:")
    for r in vector_results:
        print(f"   [{r['id']}] {r['text']} (相似度: {r['score']:.2f})")

    print(f"\n📦 图检索结果:")
    for r in graph_results:
        print(f"   [{r['id']}] {r['text']} (跳数: {r['hops']})")

    # RRF 融合
    print(f"\n📦 混合检索结果 (RRF 融合):")

    def rrf_fusion(vector_results, graph_results, k=60):
        scores = {}
        for i, r in enumerate(vector_results):
            scores[r["id"]] = scores.get(r["id"], 0) + 1 / (k + i)
        for i, r in enumerate(graph_results):
            scores[r["id"]] = scores.get(r["id"], 0) + 1 / (k + i)
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)

    fused = rrf_fusion(vector_results, graph_results)

    print(f"   融合排序:")
    for doc_id, score in fused[:5]:
        print(f"   - 文档 {doc_id}: {score:.4f}")

    print("\n✅ 混合检索完成")


if __name__ == "__main__":
    hybrid_retrieval_demo()
