"""
Day 21: HyDE Demo.

演示 HyDE（Hypothetical Document Embeddings）。

Usage:
    python hyde_demo.py
"""


def hyde_demo():
    """HyDE 演示。"""
    from sentence_transformers import SentenceTransformer
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage
    import numpy as np

    print("=" * 60)
    print("HyDE Demo")
    print("=" * 60)

    # 知识库
    documents = [
        "贵州茅台是白酒行业龙头，市占率超过50%",
        "宁德时代是动力电池龙头，全球市占率37%",
        "比亚迪是新能源车龙头，2023年销量302万辆",
        "中国白酒行业CR5持续提升，高端化趋势明显",
        "动力电池需求随新能源车增长而增长",
    ]

    # 嵌入模型
    model = SentenceTransformer("BAAI/bge-m3")
    doc_embeddings = model.encode(documents)

    # 查询
    query = "白酒龙头企业"
    print(f"\n🔍 原始查询: '{query}'")

    # 方法1：直接检索（普通）
    print("\n📦 方法1：直接检索...")
    query_embedding = model.encode([query])
    similarities = np.dot(doc_embeddings, query_embedding[0])
    similarities = similarities / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(query_embedding)
    )
    top_indices = np.argsort(similarities)[::-1][:3]

    print(f"   Top 3 结果:")
    for i, idx in enumerate(top_indices):
        print(f"   [{i+1}] {documents[idx]} (相似度: {similarities[idx]:.4f})")

    # 方法2：HyDE（生成假设文档）
    print("\n📦 方法2：HyDE...")

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    # 生成假设文档
    hyde_prompt = f"""根据以下查询，生成一段假设的相关文档（50-100字）：
查询：{query}
假设文档："""

    hypothetical_doc = llm.invoke([HumanMessage(content=hyde_prompt)]).content
    print(f"   假设文档: {hypothetical_doc}")

    # 用假设文档的向量搜索
    hyde_embedding = model.encode([hypothetical_doc])
    hyde_similarities = np.dot(doc_embeddings, hyde_embedding[0])
    hyde_similarities = hyde_similarities / (
        np.linalg.norm(doc_embeddings, axis=1) * np.linalg.norm(hyde_embedding)
    )
    hyde_top_indices = np.argsort(hyde_similarities)[::-1][:3]

    print(f"   Top 3 结果:")
    for i, idx in enumerate(hyde_top_indices):
        print(f"   [{i+1}] {documents[idx]} (相似度: {hyde_similarities[idx]:.4f})")

    # 对比
    print("\n📊 对比:")
    print(f"   直接检索 Top1: {documents[top_indices[0]]}")
    print(f"   HyDE 检索 Top1: {documents[hyde_top_indices[0]]}")

    print("\n✅ HyDE 演示完成")


def query_rewrite_demo():
    """Query Rewrite 演示。"""
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage

    print("\n" + "=" * 60)
    print("Query Rewrite Demo")
    print("=" * 60)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    queries = [
        "白酒龙头",
        "电池龙头股",
        "互联网公司",
    ]

    for query in queries:
        print(f"\n🔍 原始查询: '{query}'")

        rewrite_prompt = f"""将以下查询改写为更完整、更适合检索的形式：
查询：{query}
改写后："""

        rewritten = llm.invoke([HumanMessage(content=rewrite_prompt)]).content
        print(f"   改写后: {rewritten}")


if __name__ == "__main__":
    hyde_demo()
    query_rewrite_demo()
