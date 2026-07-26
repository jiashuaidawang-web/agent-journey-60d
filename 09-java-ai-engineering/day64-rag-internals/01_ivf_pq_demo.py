"""
Day 64: IVF-PQ 演示 - 倒排索引 + 乘积量化加速向量检索

功能：
1. 生成随机向量
2. IVF 聚类
3. PQ 量化
4. 对比暴力检索

示例：
    python 01_ivf_pq_demo.py
    python 01_ivf_pq_demo.py --num-vectors 100000 --dim 768

实际实现需要：
- faiss
- numpy

作者：Agent Journey 60D
日期：Day 64
"""

import argparse
import time

import numpy as np


class IVFIndex:
    """IVF 倒排索引

    核心思想：
    - 用 K-Means 对向量空间聚类
    - 每个向量分配到最近的聚类
    - 搜索时只查询最近的 nprobe 个聚类
    """

    def __init__(self, dim: int, nlist: int = 100):
        self.dim = dim
        self.nlist = nlist  # 聚类数量
        self.centroids: Optional[np.ndarray] = None  # 聚类中心
        self.inverted_lists: dict[int, list[int]] = {}  # 聚类 -> 向量 ID 列表

    def train(self, vectors: np.ndarray) -> None:
        """训练聚类

        Args:
            vectors: 向量矩阵 (N, D)
        """
        # TODO: 使用 K-Means 聚类
        # self.centroids = kmeans(vectors, self.nlist)
        pass

    def add(self, vectors: np.ndarray) -> None:
        """添加向量

        Args:
            vectors: 向量矩阵 (N, D)
        """
        # TODO: 将每个向量分配到最近的聚类
        pass

    def search(self, query: np.ndarray, k: int = 10, nprobe: int = 10) -> list[tuple[int, float]]:
        """搜索 Top-K 最近邻

        Args:
            query: 查询向量 (D,)
            k: 返回数量
            nprobe: 查询的聚类数量

        Returns:
            [(id, distance), ...]
        """
        # TODO: 实现 IVF 搜索
        # 1. 找到最近的 nprobe 个聚类
        # 2. 在这些聚类内暴力检索
        # 3. 返回 Top-K
        return []


class PQIndex:
    """PQ 乘积量化

    核心思想：
    - 将 D 维向量分成 m 段
    - 每段用 K-Means 聚类，得到 256 个中心
    - 每段用 1 字节编码（聚类 ID）
    - 距离计算用查表法
    """

    def __init__(self, dim: int, m: int = 8, k: int = 256):
        self.dim = dim
        self.m = m  # 分段数
        self.k = k  # 每段聚类数
        self.codebooks: Optional[np.ndarray] = None  # (m, k, dim/m)
        self.codes: Optional[np.ndarray] = None  # (N, m)

    def train(self, vectors: np.ndarray) -> None:
        """训练 PQ

        Args:
            vectors: 向量矩阵 (N, D)
        """
        # TODO: 对每段进行 K-Means 聚类
        pass

    def encode(self, vectors: np.ndarray) -> np.ndarray:
        """编码向量为 PQ 码

        Args:
            vectors: 向量矩阵 (N, D)

        Returns:
            PQ 码 (N, m)
        """
        # TODO: 每段找最近的聚类中心
        pass

    def search(self, query: np.ndarray, k: int = 10) -> list[tuple[int, float]]:
        """搜索 Top-K 最近邻

        Args:
            query: 查询向量 (D,)
            k: 返回数量

        Returns:
            [(id, distance), ...]
        """
        # TODO: 用查表法计算距离
        return []


def benchmark(vectors: np.ndarray, queries: np.ndarray) -> dict:
    """对比暴力检索 vs IVF vs PQ

    Args:
        vectors: 向量矩阵 (N, D)
        queries: 查询矩阵 (Q, D)

    Returns:
        性能对比结果
    """
    results = {}

    # 暴力检索
    print("📊 暴力检索...")
    # start = time.time()
    # ... 暴力检索
    # results["brute"] = {"time": ..., "recall": 1.0}

    # IVF
    print("📊 IVF 检索...")
    # ivf = IVFIndex(vectors.shape[1])
    # ivf.train(vectors)
    # ivf.add(vectors)
    # results["ivf"] = {"time": ..., "recall": ...}

    # PQ
    print("📊 PQ 检索...")
    # pq = PQIndex(vectors.shape[1])
    # pq.train(vectors)
    # results["pq"] = {"time": ..., "recall": ...}

    return results


def main():
    parser = argparse.ArgumentParser(description="IVF-PQ 演示")
    parser.add_argument("--num-vectors", type=int, default=100000, help="向量数量")
    parser.add_argument("--dim", type=int, default=768, help="向量维度")
    parser.add_argument("--num-queries", type=int, default=100, help="查询数量")
    args = parser.parse_args()

    print(f"📊 生成 {args.num_vectors} 个 {args.dim} 维随机向量")
    # vectors = np.random.randn(args.num_vectors, args.dim).astype(np.float32)
    # queries = np.random.randn(args.num_queries, args.dim).astype(np.float32)

    # results = benchmark(vectors, queries)
    # print("\n性能对比：")
    # for name, metrics in results.items():
    #     print(f"  {name}: {metrics['time']:.2f}ms, recall={metrics['recall']:.2%}")


if __name__ == "__main__":
    main()
