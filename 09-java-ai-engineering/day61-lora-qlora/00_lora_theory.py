"""
Day 61: LoRA/QLoRA 微调实战 - LoRA 数学原理可视化

本文件可视化 LoRA 的低秩分解数学原理：
- 模拟权重矩阵 W
- 生成低秩矩阵 A 和 B
- 计算 BA 并可视化
- 对比参数量

核心公式：
- 原始：h = Wx
- LoRA：h = Wx + BAx = (W + BA)x
- W 冻结，A 和 B 可训练
"""

import numpy as np
from typing import Tuple


# === LoRA 数学原理演示 ===

class LoRATheory:
    """
    LoRA 数学原理演示
    - 模拟权重矩阵 W
    - 生成低秩矩阵 A 和 B
    - 计算 BA 并可视化
    """

    def __init__(self, d: int = 1024, k: int = 1024, rank: int = 16):
        """
        Args:
            d: 输出维度
            k: 输入维度
            rank: LoRA 秩
        """
        self.d = d
        self.k = k
        self.rank = rank

        # 原始权重矩阵 W（模拟预训练权重）
        self.W = np.random.randn(d, k) * 0.02

        # LoRA 矩阵 A（高斯初始化）
        self.A = np.random.randn(rank, k) * 0.02

        # LoRA 矩阵 B（零初始化）
        self.B = np.zeros((d, rank))

    def count_parameters(self) -> dict:
        """计算参数量"""
        return {
            "W": self.W.size,                           # d * k
            "A": self.A.size,                           # rank * k
            "B": self.B.size,                           # d * rank
            "lora_total": self.A.size + self.B.size,    # rank * (d + k)
            "compression_ratio": 1 - (self.A.size + self.B.size) / self.W.size
        }

    def forward(self, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        前向传播

        Args:
            x: 输入向量

        Returns:
            (原始输出, LoRA 输出)
        """
        # 原始输出
        h_original = self.W @ x

        # LoRA 输出
        h_lora = self.W @ x + self.B @ self.A @ x

        return h_original, h_lora

    def get_delta_W(self) -> np.ndarray:
        """获取 LoRA 更新矩阵 BA"""
        return self.B @ self.A

    def visualize_matrix_stats(self):
        """可视化矩阵统计信息"""
        print("📊 矩阵统计信息：")
        print(f"   W: shape={self.W.shape}, mean={self.W.mean():.6f}, std={self.W.std():.6f}")
        print(f"   A: shape={self.A.shape}, mean={self.A.mean():.6f}, std={self.A.std():.6f}")
        print(f"   B: shape={self.B.shape}, mean={self.B.mean():.6f}, std={self.B.std():.6f}")
        print(f"   BA: shape={(self.B @ self.A).shape}")
        print()


# === 主函数 ===

def main():
    """
    主函数：演示 LoRA 数学原理

    运行方式：
        python 00_lora_theory.py

    预期输出：
        📐 LoRA 数学原理可视化
        📊 原始权重矩阵 W: 1024x1024 = 1,048,576 参数
        📊 LoRA 矩阵 A: 16x1024 = 16,384 参数
        📊 LoRA 矩阵 B: 1024x16 = 16,384 参数
        📊 压缩率: 96.9%
    """
    print("=" * 60)
    print("📐 LoRA 数学原理可视化")
    print("=" * 60)
    print()

    # 创建 LoRA 实例
    lora = LoRATheory(d=1024, k=1024, rank=16)

    # 打印参数量
    params = lora.count_parameters()
    print("📊 参数量统计：")
    print(f"   原始权重矩阵 W: {lora.d}x{lora.k} = {params['W']:,} 参数")
    print(f"   LoRA 矩阵 A: {lora.rank}x{lora.k} = {params['A']:,} 参数")
    print(f"   LoRA 矩阵 B: {lora.d}x{lora.rank} = {params['B']:,} 参数")
    print(f"   LoRA 总参数: {params['lora_total']:,}")
    print(f"   压缩率: {params['compression_ratio']*100:.1f}%")
    print()

    # 可视化矩阵统计
    lora.visualize_matrix_stats()

    # 前向传播演示
    print("🔄 前向传播演示：")
    x = np.random.randn(1024)  # 输入向量
    h_original, h_lora = lora.forward(x)
    print(f"   输入 x: shape={x.shape}")
    print(f"   原始输出 h=Wx: shape={h_original.shape}")
    print(f"   LoRA 输出 h=Wx+BAx: shape={h_lora.shape}")
    print(f"   输出差异 (L2 norm): {np.linalg.norm(h_original - h_lora):.6f}")
    print()

    # 不同 rank 的对比
    print("📊 不同 rank 的压缩率对比：")
    print(f"   {'Rank':<10} {'参数量':<15} {'压缩率':<10}")
    print(f"   {'-'*35}")
    for rank in [4, 8, 16, 32, 64]:
        lora_temp = LoRATheory(d=1024, k=1024, rank=rank)
        params_temp = lora_temp.count_parameters()
        print(f"   {rank:<10} {params_temp['lora_total']:<15,} {params_temp['compression_ratio']*100:.1f}%")
    print()

    print("✅ LoRA 数学原理可视化完成")
    print()
    print("核心结论：")
    print("  1. LoRA 通过低秩分解大幅减少可训练参数")
    print("  2. rank=16 时，压缩率可达 96.9%")
    print("  3. 参数量从 d*k 降到 r*(d+k)")


if __name__ == "__main__":
    main()
