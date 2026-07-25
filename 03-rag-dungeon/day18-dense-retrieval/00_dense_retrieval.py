"""
Day 18: Dense Retrieval.

实现基于 Embedding 的语义检索。

Usage:
    python dense_retrieval.py
"""


def dense_retrieval_demo():
    """稠密检索演示。"""
    from sentence_transformers import SentenceTransformer
    import numpy as np

    print("=" * 60)
    print("Dense Retrieval Demo")
    print("=" * 60)

    # 1. 加载嵌入模型
    print("\n📦 加载嵌入模型...")
    model = SentenceTransformer("BAAI/bge-m3")

    # 2. 知识库
    documents = [
        "贵州茅台是白酒行业龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
        "腾讯是互联网龙头，股价380元",
        "阿里巴巴是电商龙头，股价80美元",
        "中国白酒行业CR5持续提升",
        "动力电池需求随新能源车增长",
        "互联网行业监管政策趋严",
    ]

    print(f"\n📚 知识库: {len(documents)} 条文档")

    # 3. 文档嵌入
    print("\n🔢 生成文档嵌入...")
    doc_embeddings = model.encode(documents)
    print(f"   嵌入维度: {doc_embeddings.shape}")

    # 4. 查询
    queries = [
        "白酒龙头股有哪些",
        "电池龙头股",
        "互联网公司股价",
    ]

    for query in queries:
        print(f"\n🔍 查询: '{query}'")

        # 查询嵌入
        query_embedding = model.encode([query])

        # 计算相似度
        similarities = np.dot(doc_embeddings, query_embedding[0])
        similarities = similarities / (
            np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        # Top-K
        k = 3
        top_indices = np.argsort(similarities)[::-1][:k]

        print(f"   Top {k} 结果:")
        for i, idx in enumerate(top_indices):
            print(f"   [{i+1}] {documents[idx]} (相似度: {similarities[idx]:.4f})")


if __name__ == "__main__":
    dense_retrieval_demo()
