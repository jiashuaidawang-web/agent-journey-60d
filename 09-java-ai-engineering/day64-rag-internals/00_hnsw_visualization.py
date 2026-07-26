"""
Day 64: HNSW 可视化 - 构建层级图并展示搜索过程

功能：
1. 生成随机向量
2. 构建 HNSW 图
3. 可视化层级结构
4. 展示搜索路径

示例：
    python 00_hnsw_visualization.py
    python 00_hnsw_visualization.py --num-vectors 1000 --dim 128

实际实现需要：
- hnswlib / faiss
- matplotlib / plotly

作者：Agent Journey 60D
日期：Day 64
"""

import argparse
import random
from typing import Optional

import numpy as np


class HNSWNode:
    """HNSW 节点"""
    def __init__(self, id: int, vector: np.ndarray, level: int):
        self.id = id
        self.vector = vector
        self.level = level
        self.neighbors: dict[int, list[int]] = {}  # level -> neighbor ids


class HNSWIndex:
    """HNSW 索引

    核心思想：
    - 构建多层图结构（类似跳表）
    - 高层图节点少，用于快速定位
    - 底层图节点多，用于精确搜索
    """

    def __init__(self, dim: int, m: int = 16, ef_construction: int = 200):
        self.dim = dim
        self.m = m
        self.ef_construction = ef_construction
        self.nodes: dict[int, HNSWNode] = {}
        self.max_level = 0
        self.entry_point: Optional[int] = None

    def _random_level(self) -> int:
        """随机生成节点层级（指数衰减）"""
        import math
        level = 0
        while random.random() < 1 / math.e and level < self.max_level + 1:
            level += 1
        return level

    def insert(self, id: int, vector: np.ndarray) -> None:
        """插入向量

        Args:
            id: 向量 ID
            vector: 向量值
        """
        # TODO: 实现 HNSW 插入逻辑
        # 1. 随机生成层级
        # 2. 从最高层搜索最近邻
        # 3. 在每一层建立连接
        pass

    def search(self, query: np.ndarray, k: int = 10, ef_search: int = 50) -> list[tuple[int, float]]:
        """搜索 Top-K 最近邻

        Args:
            query: 查询向量
            k: 返回数量
            ef_search: 搜索宽度

        Returns:
            [(id, distance), ...] 按距离升序
        """
        # TODO: 实现 HNSW 搜索逻辑
        # 1. 从最高层开始
        # 2. 每层贪心搜索
        # 3. 返回 Top-K
        return []

    def get_layer_stats(self) -> dict[int, int]:
        """统计每层节点数

        Returns:
            {layer: count}
        """
        stats: dict[int, int] = {}
        for node in self.nodes.values():
            for level in range(node.level + 1):
                stats[level] = stats.get(level, 0) + 1
        return stats


def visualize_hnsw(index: HNSWIndex) -> None:
    """可视化 HNSW 层级结构

    Args:
        index: HNSW 索引
    """
    # TODO: 使用 matplotlib / plotly 可视化
    # 绘制每层节点和连接
    stats = index.get_layer_stats()
    print("📊 HNSW 图层级统计：")
    for level, count in sorted(stats.items()):
        print(f"  Layer {level}: {count} nodes")


def demo_search(index: HNSWIndex, query: np.ndarray) -> None:
    """演示搜索过程

    Args:
        index: HNSW 索引
        query: 查询向量
    """
    print(f"\n🔍 搜索查询向量（dim={len(query)}）")
    # results = index.search(query, k=5)
    # for id, dist in results:
    #      print(f"  Node {id}: distance={dist:.4f}")


def main():
    parser = argparse.ArgumentParser(description="HNSW 可视化")
    parser.add_argument("--num-vectors", type=int, default=1000, help="向量数量")
    parser.add_argument("--dim", type=int, default=128, help="向量维度")
    args = parser.parse_args()

    print(f"📊 构建 HNSW 索引（{args.num_vectors} 向量，{args.dim} 维）")
    index = HNSWIndex(dim=args.dim)

    # 生成随机向量
    # for i in range(args.num_vectors):
    #     vector = np.random.randn(args.dim).astype(np.float32)
    #     index.insert(i, vector)

    visualize_hnsw(index)

    # 演示搜索
    # query = np.random.randn(args.dim).astype(np.float32)
    # demo_search(index, query)


if __name__ == "__main__":
    main()
