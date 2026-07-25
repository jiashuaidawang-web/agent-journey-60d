"""
Day 22: RAG Pipeline.

整合 Day 15-21 的完整 RAG Pipeline。

流程：
    查询 → 重写 → 混合检索 → 精排 → 组装上下文 → LLM 生成

Usage:
    python rag_pipeline.py
"""


class RAGPipeline:
    """完整 RAG Pipeline。"""

    def __init__(self):
        from sentence_transformers import SentenceTransformer, CrossEncoder
        from langchain_openai import ChatOpenAI

        # 嵌入模型
        self.embed_model = SentenceTransformer("BAAI/bge-m3")

        # Reranker
        try:
            self.reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")
        except Exception:
            self.reranker = None

        # LLM
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        # 知识库
        self.documents = []
        self.embeddings = None

    def add_documents(self, documents: list[str]):
        """添加文档到知识库。"""
        self.documents.extend(documents)
        self.embeddings = self.embed_model.encode(self.documents)

    def rewrite_query(self, query: str) -> str:
        """查询重写。"""
        from langchain_core.messages import HumanMessage

        prompt = f"""将以下查询改写为更适合检索的形式：
查询：{query}
改写后："""

        rewritten = self.llm.invoke([HumanMessage(content=prompt)]).content
        return rewritten

    def hybrid_search(self, query: str, top_k: int = 10) -> list[tuple[int, float]]:
        """混合检索（Dense + BM25）。"""
        import numpy as np

        if self.embeddings is None:
            return []

        # Dense 检索
        query_embedding = self.embed_model.encode([query])
        dense_scores = np.dot(self.embeddings, query_embedding[0])
        dense_scores = dense_scores / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        # BM25（简化：关键词匹配）
        sparse_scores = []
        for doc in self.documents:
            score = sum(1 for word in query if word in doc)
            sparse_scores.append(score)
        sparse_scores = np.array(sparse_scores, dtype=float)

        # RRF 融合
        final_scores = self._rrf_fusion(dense_scores, sparse_scores)

        # Top-K
        top_indices = np.argsort(final_scores)[::-1][:top_k]
        return [(idx, final_scores[idx]) for idx in top_indices]

    def _rrf_fusion(self, dense_scores, sparse_scores, k=60):
        """RRF 融合。"""
        import numpy as np
        n = len(dense_scores)
        final_scores = np.zeros(n)

        dense_rank = np.argsort(np.argsort(-dense_scores))
        sparse_rank = np.argsort(np.argsort(-sparse_scores))

        for i in range(n):
            final_scores[i] = 1 / (k + dense_rank[i]) + 1 / (k + sparse_rank[i])

        return final_scores

    def rerank(self, query: str, doc_indices: list[int], top_k: int = 3) -> list[int]:
        """重排序。"""
        if self.reranker is None:
            return doc_indices[:top_k]

        docs = [self.documents[i] for i in doc_indices]
        pairs = [(query, doc) for doc in docs]
        scores = self.reranker.predict(pairs)

        # 排序
        rerank_indices = np.argsort(scores)[::-1][:top_k]
        return [doc_indices[i] for i in rerank_indices]

    def assemble_context(self, doc_indices: list[int]) -> str:
        """组装上下文。"""
        context = "\n".join([f"[{i+1}] {self.documents[idx]}" for i, idx in enumerate(doc_indices)])
        return context

    def generate(self, query: str, context: str) -> str:
        """LLM 生成回答。"""
        from langchain_core.messages import HumanMessage

        prompt = f"""根据以下上下文回答问题：

上下文：
{context}

问题：{query}
回答："""

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content

    def query(self, user_query: str) -> dict:
        """完整 RAG 流程。"""
        print("=" * 60)
        print("RAG Pipeline")
        print("=" * 60)

        print(f"\n🔍 原始查询: {user_query}")

        # 1. 查询重写
        print("\n📦 步骤1：查询重写...")
        rewritten = self.rewrite_query(user_query)
        print(f"   改写后: {rewritten}")

        # 2. 混合检索
        print("\n📦 步骤2：混合检索...")
        search_results = self.hybrid_search(rewritten, top_k=10)
        doc_indices = [idx for idx, _ in search_results]
        print(f"   召回 {len(doc_indices)} 条文档")

        # 3. 重排序
        print("\n📦 步骤3：重排序...")
        reranked_indices = self.rerank(rewritten, doc_indices, top_k=3)
        print(f"   精排 Top 3:")
        for i, idx in enumerate(reranked_indices):
            print(f"   [{i+1}] {self.documents[idx]}")

        # 4. 组装上下文
        context = self.assemble_context(reranked_indices)

        # 5. LLM 生成
        print("\n📦 步骤4：LLM 生成...")
        answer = self.generate(rewritten, context)
        print(f"   回答: {answer}")

        return {
            "query": user_query,
            "rewritten": rewritten,
            "documents": [self.documents[i] for i in reranked_indices],
            "answer": answer,
        }


def main():
    """运行 RAG Pipeline。"""
    rag = RAGPipeline()

    # 添加知识库
    rag.add_documents([
        "贵州茅台是白酒行业龙头，市占率超过50%，股价1680元",
        "宁德时代是动力电池龙头，全球市占率37%，股价210元",
        "比亚迪是新能源车龙头，2023年销量302万辆，股价280元",
        "中国白酒行业CR5持续提升，高端化趋势明显",
        "动力电池需求随新能源车增长而增长",
        "高端白酒具有品牌壁垒，护城河深厚",
        "新能源车渗透率持续提升，2024年超过35%",
    ])

    # 查询
    result = rag.query("白酒龙头企业有哪些")

    print("\n" + "=" * 60)
    print("最终结果")
    print("=" * 60)
    print(f"问题: {result['query']}")
    print(f"回答: {result['answer']}")


if __name__ == "__main__":
    main()
