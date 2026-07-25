"""
Day 16: Milvus Demo.

演示 Milvus 向量的基本操作。

Usage:
    python milvus_demo.py
"""


def milvus_demo():
    """Milvus 演示。"""
    from pymilvus import (
        connections,
        FieldSchema,
        CollectionSchema,
        DataType,
        Collection,
    )
    import numpy as np

    print("=" * 60)
    print("Milvus Demo")
    print("=" * 60)

    # 1. 连接
    print("\n📡 连接 Milvus...")
    connections.connect("default", host="localhost", port="19530")

    # 2. 定义 Schema
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=500),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
    ]
    schema = CollectionSchema(fields=fields, description="RAG 知识库")

    # 3. 创建 Collection
    collection = Collection(name="rag_knowledge", schema=schema)
    print(f"✅ Collection 创建完成: {collection.name}")

    # 4. 插入数据
    print("\n📥 插入数据...")
    texts = [
        "贵州茅台是白酒龙头",
        "宁德时代是动力电池龙头",
        "比亚迪是新能源车龙头",
    ]
    # 模拟嵌入向量（实际应由嵌入模型生成）
    embeddings = np.random.rand(3, 768).tolist()

    data = [texts, embeddings]
    collection.insert(data)
    print(f"✅ 插入 {len(texts)} 条数据")

    # 5. 创建索引
    print("\n📊 创建索引...")
    index_params = {
        "metric_type": "COSINE",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128},
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    print("✅ 索引创建完成")

    # 6. 搜索
    print("\n🔍 向量搜索...")
    collection.load()
    query_embedding = np.random.rand(1, 768).tolist()

    search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
    results = collection.search(
        data=query_embedding,
        anns_field="embedding",
        param=search_params,
        limit=3,
        output_fields=["text"],
    )

    print(f"   搜索结果:")
    for hits in results:
        for hit in hits:
            print(f"   - {hit.entity.get('text')} (距离: {hit.distance:.4f})")

    # 清理
    collection.drop()
    print("\n✅ 演示完成")


if __name__ == "__main__":
    milvus_demo()
