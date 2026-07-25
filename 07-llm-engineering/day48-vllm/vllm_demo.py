"""
Day 48: vLLM Demo.

演示 vLLM 使用。

Usage:
    python vllm_demo.py
"""


def vllm_demo():
    """vLLM 演示。"""
    print("=" * 60)
    print("vLLM Demo")
    print("=" * 60)

    try:
        import vllm
        print(f"✅ vLLM 版本: {vllm.__version__}")
    except ImportError:
        print("⚠️ vLLM 未安装")
        print("   安装: pip install vllm")

    print("\n📦 vLLM 启动方式:")
    print("   python -m vllm.entrypoints.openai.api_server \\")
    print("       --model Qwen2.5-7B \\")
    print("       --port 8000")

    print("\n📦 调用方式（OpenAI 兼容 API）:")
    print("   from openai import OpenAI")
    print("   client = OpenAI(base_url='http://localhost:8000/v1')")
    print("   response = client.chat.completions.create(")
    print("       model='Qwen2.5-7B',")
    print("       messages=[{'role': 'user', 'content': 'Hello'}]")
    print("   )")

    print("\n📦 核心优化:")
    print("   - PagedAttention: 分页管理 KV Cache")
    print("   - Continuous Batching: 连续批处理")
    print("   - Prefix Caching: 前缀缓存")
    print("   - Tensor Parallelism: 张量并行")

    return True


if __name__ == "__main__":
    vllm_demo()
