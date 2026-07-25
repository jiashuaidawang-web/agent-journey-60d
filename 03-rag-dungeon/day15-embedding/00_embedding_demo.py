"""
Day 15: Embedding Demo.

演示文本嵌入：文本 → 向量。

Usage:
    python embedding_demo.py
"""


def embedding_demo():
    """嵌入演示。"""
    from sentence_transformers import SentenceTransformer

    print("=" * 60)
    print("Embedding Demo")
    print("=" * 60)

    # 1. 加载模型
    print("\n📦 加载 BGE-M3 模型...")
    model = SentenceTransformer("BAAI/bge-m3")
    print("✅ 模型加载完成")

    # 2. 文本向量化
    texts = [
        "苹果是一种水果",
        "香蕉是黄色的水果",
        "汽车有四个轮子",
        "今天天气很好",
        "Python 是编程语言",
    ]

    print(f"\n📝 文本向量化:")
    embeddings = model.encode(texts)

    for text, emb in zip(texts, embeddings):
        print(f"   '{text}' → 向量维度: {len(emb)}, 前5维: {emb[:5].round(3)}")

    print(f"\n📊 向量维度: {embeddings.shape}")

    return embeddings


def embedding_search_demo():
    """嵌入搜索演示。"""
    from sentence_transformers import SentenceTransformer
    import numpy as np

    model = SentenceTransformer("BAAI/bge-m3")

    # 知识库
    knowledge_base = [
        "贵州茅台是白酒龙头，股价1680元",
        "宁德时代是动力电池龙头，股价210元",
        "比亚迪是新能源车龙头，股价280元",
        "腾讯是互联网龙头，股价380元",
        "阿里巴巴是电商龙头，股价80美元",
    ]

    print("\n" + "=" * 60)
    print("Embedding Search Demo")
    print("=" * 60)

    # 编码知识库
    kb_embeddings = model.encode(knowledge_base)

    # 查询
    queries = [
        "白酒龙头股有哪些",
        "电池龙头股",
        "电商公司股价",
    ]

    for query in queries:
        print(f"\n🔍 查询: '{query}'")

        # 编码查询
        query_embedding = model.encode([query])

        # 计算相似度
        similarities = np.dot(kb_embeddings, query_embedding[0])
        similarities = similarities / (
            np.linalg.norm(kb_embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        # 排序
        top_k = 3
        top_indices = np.argsort(similarities)[::-1][:top_k]

        print(f"   Top {top_k} 结果:")
        for i, idx in enumerate(top_indices):
            print(f"   [{i+1}] {knowledge_base[idx]} (相似度: {similarities[idx]:.4f})")


if __name__ == "__main__":
    embedding_demo()
    embedding_search_demo()
