"""
Day 16: FAISS Demo.

演示 FAISS 向量搜索库的使用。

Usage:
    python faiss_demo.py
"""


def faiss_demo():
    """FAISS 演示。"""
    import numpy as np

    print("=" * 60)
    print("FAISS Demo")
    print("=" * 60)

    try:
        import faiss
    except ImportError:
        print("⚠️ FAISS 未安装，使用模拟实现")
        return faiss_mock_demo()

    # 1. 准备数据
    d = 768  # 向量维度
    nb = 1000  # 数据库大小
    nq = 5  # 查询数量

    print(f"\n📊 生成模拟数据: {nb} 条, 维度 {d}")
    np.random.seed(42)
    xb = np.random.random((nb, d)).astype('float32')
    xq = np.random.random((nq, d)).astype('float32')

    # 2. 创建索引（Flat = 精确搜索）
    print("\n📦 创建 FLAT 索引...")
    index_flat = faiss.IndexFlatIP(d)  # Inner Product
    index_flat.add(xb)
    print(f"✅ 索引大小: {index_flat.ntotal}")

    # 3. 搜索
    print("\n🔍 搜索...")
    k = 5
    distances, indices = index_flat.search(xq, k)

    print(f"   查询0 的 Top {k} 结果:")
    for i in range(k):
        print(f"   [{i+1}] id={indices[0][i]}, 相似度={distances[0][i]:.4f}")

    # 4. IVF 索引（更快）
    print("\n📦 创建 IVF 索引...")
    nlist = 100  # 聚类数
    quantizer = faiss.IndexFlatIP(d)
    index_ivf = faiss.IndexIVFFlat(quantizer, d, nlist)
    index_ivf.train(xb)
    index_ivf.add(xb)
    index_ivf.nprobe = 10  # 搜索时访问的聚类数

    distances_ivf, indices_ivf = index_ivf.search(xq, k)
    print(f"   IVF 搜索完成")

    # 5. HNSW 索引（最快）
    print("\n📦 创建 HNSW 索引...")
    index_hnsw = faiss.IndexHNSWFlat(d, 32)
    index_hnsw.add(xb)

    distances_hnsw, indices_hnsw = index_hnsw.search(xq, k)
    print(f"   HNSW 搜索完成")

    print("\n✅ 演示完成")


def faiss_mock_demo():
    """FAISS 未安装时的模拟演示。"""
    import numpy as np

    print("\n📦 模拟 FAISS 演示...")

    # 模拟数据
    d = 768
    nb = 1000
    nq = 5

    np.random.seed(42)
    xb = np.random.random((nb, d)).astype('float32')
    xq = np.random.random((nq, d)).astype('float32')

    # 计算相似度
    similarities = np.dot(xb, xq[0])
    top_k = 5
    top_indices = np.argsort(similarities)[::-1][:top_k]

    print(f"\n🔍 查询0 的 Top {top_k} 结果:")
    for i, idx in enumerate(top_indices):
        print(f"   [{i+1}] id={idx}, 相似度={similarities[idx]:.4f}")

    print("\n✅ 模拟演示完成")
    print("💡 提示: 安装 FAISS 运行完整演示: pip install faiss-cpu")


if __name__ == "__main__":
    faiss_demo()
