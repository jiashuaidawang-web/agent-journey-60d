"""
Day 15: Similarity Demo.

演示相似度计算：Cosine Similarity。

Usage:
    python similarity_demo.py
"""


def cosine_similarity_demo():
    """Cosine Similarity 演示。"""
    import numpy as np

    print("=" * 60)
    print("Cosine Similarity Demo")
    print("=" * 60)

    def cosine_sim(a, b):
        """计算 Cosine Similarity。"""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # 模拟向量（实际中由 Embedding 模型生成）
    vectors = {
        "苹果": np.array([0.8, 0.6, 0.1, 0.2]),
        "香蕉": np.array([0.7, 0.7, 0.2, 0.1]),
        "水果": np.array([0.9, 0.5, 0.1, 0.3]),
        "汽车": np.array([0.1, 0.2, 0.8, 0.9]),
        "电脑": np.array([0.2, 0.1, 0.7, 0.8]),
    }

    # 计算相似度矩阵
    print("\n📊 相似度矩阵:")
    names = list(vectors.keys())

    # 表头
    print(f"{'':>8}", end="")
    for name in names:
        print(f"{name:>8}", end="")
    print()

    # 矩阵
    for name_a in names:
        print(f"{name_a:>8}", end="")
        for name_b in names:
            sim = cosine_sim(vectors[name_a], vectors[name_b])
            print(f"{sim:>8.4f}", end="")
        print()

    # 分析
    print("\n💡 观察:")
    print("   - 苹果 vs 香蕉: 高相似度（都是水果）")
    print("   - 苹果 vs 水果: 高相似度（上下位关系）")
    print("   - 苹果 vs 汽车: 低相似度（不相关）")
    print("   - 汽车 vs 电脑: 中等相似度（都是人造物品）")


def semantic_vs_literal():
    """语义相似 vs 字面相似。"""
    from sentence_transformers import SentenceTransformer
    import numpy as np

    print("\n" + "=" * 60)
    print("语义相似 vs 字面相似")
    print("=" * 60)

    model = SentenceTransformer("BAAI/bge-m3")

    # 语义相似但字面不同
    pairs = [
        ("如何学习Python", "Python学习方法"),      # 语义相似
        ("苹果手机", "iPhone"),                    # 语义相同
        ("今天天气很好", "今天天气很差"),           # 字面相似但语义相反
        ("贵州茅台", "茅台酒"),                    # 语义相同
    ]

    for text_a, text_b in pairs:
        emb_a = model.encode([text_a])
        emb_b = model.encode([text_b])

        sim = np.dot(emb_a[0], emb_b[0]) / (
            np.linalg.norm(emb_a[0]) * np.linalg.norm(emb_b[0])
        )

        print(f"\n   '{text_a}' vs '{text_b}'")
        print(f"   相似度: {sim:.4f}")


if __name__ == "__main__":
    cosine_similarity_demo()
    semantic_vs_literal()
