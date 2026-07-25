"""
Day 49: KV Cache Demo.

演示 KV Cache 原理。

Usage:
    python kv_cache_demo.py
"""


def kv_cache_demo():
    """KV Cache 演示。"""
    print("=" * 60)
    print("KV Cache Demo")
    print("=" * 60)

    print("\n📦 KV Cache 原理:")
    print("   问题：生成式模型每生成一个 token 都要计算所有历史 token 的 Attention")
    print("   解决：缓存已计算的 Key 和 Value")

    print("\n📦 生成过程:")
    print("   输入: '贵州茅台是'")
    print("   生成 '白' 时:")
    print("     - 使用缓存的 KV（贵、州、茅、台、是）")
    print("     - 只计算 '白' 的 KV")
    print("   '白' 的 Attention = Query_白 × [KV_贵, KV_州, KV_茅, KV_台, KV_是]")

    print("\n📦 无 KV Cache:")
    print("   每步都重新计算所有 KV")
    print("   时间复杂度: O(n²)")

    print("\n📦 有 KV Cache:")
    print("   只计算新 token 的 KV")
    print("   时间复杂度: O(n)")

    print("\n✅ KV Cache 演示完成")


def paged_attention_demo():
    """PagedAttention 演示。"""
    print("\n" + "=" * 60)
    print("PagedAttention Demo")
    print("=" * 60)

    print("\n📦 传统 KV Cache 的问题:")
    print("   - 每个请求预分配连续显存")
    print("   - 产生显存碎片")
    print("   - 利用率低（20-40%）")

    print("\n📦 PagedAttention 原理:")
    print("   - 将 KV Cache 分页管理")
    print("   - 类似操作系统虚拟内存分页")
    print("   - 每个请求的 KV Cache 可以非连续存储")

    print("\n📦 优势:")
    print("   - 避免显存碎片")
    print("   - 显存利用率 >90%")
    print("   - 支持动态分配")

    print("\n✅ PagedAttention 演示完成")


if __name__ == "__main__":
    kv_cache_demo()
    paged_attention_demo()
