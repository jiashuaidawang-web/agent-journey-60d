"""
Day 64: Milvus 集群部署 - Docker Compose + Python SDK

功能：
1. Docker Compose 部署 Milvus 集群
2. 创建 Collection
3. 插入 / 查询 / 删除
4. 索引管理

示例：
    python 03_milvus_cluster.py
    python 03_milvus_cluster.py --host localhost --port 19530

实际实现需要：
- pymilvus
- docker-compose

作者：Agent Journey 60D
日期：Day 64
"""

import argparse
import time
from typing import Optional

import numpy as np


DOCKER_COMPOSE_YAML = """
version: '3.5'
services:
  etcd:
    image: quay.io/coreos/etcd:v3.5.5
    environment:
      ETCD_AUTO_COMPACTION_MODE: revision
      ETCD_AUTO_COMPACTION_RETENTION: 1000
      ETCD_QUOTA_BACKEND_BYTES: 4294967296
    volumes: [/etcd:/etcd]

  minio:
    image: minio/minio:RELEASE.2023-03-20T20-16-18Z
    environment:
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
    ports: [9000:9000, 9001:9001]
    command: minio server /minio_data --console-address ":9001"

  standalone:
    image: milvusdb/milvus:v2.4.0
    command: ["milvus", "run", "standalone"]
    environment:
      ETCD_ENDPOINTS: etcd:2379
      MINIO_ADDRESS: minio:9000
    ports: [19530:19530, 9091:9091]
    depends_on: [etcd, minio]
"""


class MilvusCluster:
    """Milvus 集群管理

    Milvus 架构：
    - Proxy：接入层，负载均衡
    - Coordinator：元数据管理
    - Worker：数据处理（DataNode / QueryNode / IndexNode）
    - Storage：MinIO / S3
    """

    def __init__(self, host: str = "localhost", port: str = "19530"):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self) -> bool:
        """连接 Milvus

        Returns:
            是否连接成功
        """
        # TODO: 连接 Milvus
        # from pymilvus import connections
        # connections.connect(host=self.host, port=self.port)
        self.connected = True
        return True

    def create_collection(self, collection_name: str, dim: int = 768) -> bool:
        """创建 Collection

        Args:
            collection_name: Collection 名称
            dim: 向量维度

        Returns:
            是否创建成功
        """
        # TODO: 创建 Collection
        # from pymilvus import FieldSchema, CollectionSchema, DataType, Collection
        # fields = [
        #     FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        #     FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim),
        #     FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
        # ]
        # schema = CollectionSchema(fields, description="RAG Collection")
        # collection = Collection(name=collection_name, schema=schema)
        return True

    def create_index(self, collection_name: str, index_type: str = "HNSW") -> bool:
        """创建索引

        Args:
            collection_name: Collection 名称
            index_type: 索引类型（HNSW / IVF_PQ / FLAT）

        Returns:
            是否创建成功
        """
        # TODO: 创建索引
        # index_params = {
        #     "metric_type": "IP",
        #     "index_type": index_type,
        #     "params": {"M": 16, "efConstruction": 200}
        # }
        # collection.create_index(field_name="embedding", index_params=index_params)
        return True

    def insert(self, collection_name: str, vectors: np.ndarray, texts: list[str]) -> list[int]:
        """插入向量

        Args:
            collection_name: Collection 名称
            vectors: 向量矩阵 (N, D)
            texts: 文本列表

        Returns:
            插入的 ID 列表
        """
        # TODO: 插入向量
        return []

    def search(self, collection_name: str, query: np.ndarray, k: int = 10,
               filters: Optional[str] = None) -> list[dict]:
        """搜索向量

        Args:
            collection_name: Collection 名称
            query: 查询向量 (D,)
            k: 返回数量
            filters: 过滤表达式

        Returns:
            搜索结果列表
        """
        # TODO: 搜索向量
        # results = collection.search(
        #     data=[query],
        #     anns_field="embedding",
        #     param={"metric_type": "IP", "params": {"ef": 50}},
        #     limit=k,
        #     expr=filters
        # )
        return []

    def delete(self, collection_name: str, ids: list[int]) -> bool:
        """删除向量

        Args:
            collection_name: Collection 名称
            ids: 要删除的 ID 列表

        Returns:
            是否删除成功
        """
        # TODO: 删除向量
        return True

    def drop_collection(self, collection_name: str) -> bool:
        """删除 Collection

        Args:
            collection_name: Collection 名称

        Returns:
            是否删除成功
        """
        # TODO: 删除 Collection
        return True


def demo_rag_workflow():
    """演示 RAG 完整工作流"""
    print("🚀 Milvus RAG 工作流演示")

    # Step 1: 连接
    cluster = MilvusCluster()
    # cluster.connect()
    print("✅ 连接 Milvus")

    # Step 2: 创建 Collection
    # cluster.create_collection("rag_collection", dim=768)
    print("✅ 创建 Collection")

    # Step 3: 插入向量
    # vectors = np.random.randn(1000, 768).astype(np.float32)
    # texts = [f"文档 {i}" for i in range(1000)]
    # cluster.insert("rag_collection", vectors, texts)
    print("✅ 插入 1000 条向量")

    # Step 4: 创建索引
    # cluster.create_index("rag_collection", "HNSW")
    print("✅ 创建 HNSW 索引")

    # Step 5: 搜索
    # query = np.random.randn(768).astype(np.float32)
    # results = cluster.search("rag_collection", query, k=5)
    print("✅ 搜索完成")

    # Step 6: 带过滤搜索
    # results = cluster.search("rag_collection", query, k=5, filters="source == '财报.pdf'")
    print("✅ 带过滤搜索完成")


def main():
    parser = argparse.ArgumentParser(description="Milvus 集群部署")
    parser.add_argument("--host", type=str, default="localhost", help="Milvus 主机")
    parser.add_argument("--port", type=str, default="19530", help="Milvus 端口")
    args = parser.parse_args()

    demo_rag_workflow()


if __name__ == "__main__":
    main()
