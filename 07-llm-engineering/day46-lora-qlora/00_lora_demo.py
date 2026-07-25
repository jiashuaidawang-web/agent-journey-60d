"""
Day 46: LoRA Demo.

演示 LoRA 原理（简化版）。

Usage:
    python lora_demo.py
"""


def lora_principle_demo():
    """LoRA 原理演示。"""
    print("=" * 60)
    print("LoRA Principle Demo")
    print("=" * 60)

    import numpy as np

    # 模拟原始权重矩阵（冻结）
    W = np.random.randn(4, 4)
    print(f"\n📦 原始权重 W (冻结):")
    print(f"   形状: {W.shape}")
    print(f"   参数数: {W.size}")

    # LoRA：低秩矩阵 A 和 B
    rank = 2  # 秩
    A = np.random.randn(4, rank) * 0.01
    B = np.random.randn(rank, 4) * 0.01

    print(f"\n📦 LoRA 矩阵:")
    print(f"   A 形状: {A.shape}, 参数数: {A.size}")
    print(f"   B 形状: {B.shape}, 参数数: {B.size}")
    print(f"   可训练参数: {A.size + B.size}")
    print(f"   原始参数: {W.size}")
    print(f"   参数减少: {(1 - (A.size + B.size) / W.size) * 100:.1f}%")

    # 计算 ΔW = A × B
    delta_W = A @ B
    print(f"\n📦 ΔW = A × B:")
    print(f"   形状: {delta_W.shape}")

    # 新权重 = W + ΔW
    W_new = W + delta_W
    print(f"\n📦 新权重 W' = W + ΔW:")
    print(f"   形状: W_new.shape}")

    print("\n✅ LoRA 原理演示完成")
    print("\n💡 关键点:")
    print("   - 原始权重 W 冻结，不训练")
    print("   - 只训练低秩矩阵 A 和 B")
    print("   - 参数大幅减少，显存占用低")


def qlora_principle_demo():
    """QLoRA 原理演示。"""
    print("\n" + "=" * 60)
    print("QLoRA Principle Demo")
    print("=" * 60)

    print("\n📦 QLoRA vs LoRA:")
    print("   LoRA:")
    print("     - 基础模型: FP16 (16-bit)")
    print("     - LoRA 部分: FP16 (16-bit)")
    print("   QLoRA:")
    print("     - 基础模型: NF4 (4-bit 量化)")
    print("     - LoRA 部分: BF16 (16-bit)")
    print("     - 进一步降低显存")

    print("\n📦 显存对比 (7B 模型):")
    print("   全量微调: ~100GB")
    print("   LoRA:     ~30GB")
    print("   QLoRA:    ~10GB")

    print("\n✅ QLoRA 原理演示完成")


if __name__ == "__main__":
    lora_principle_demo()
    qlora_principle_demo()
