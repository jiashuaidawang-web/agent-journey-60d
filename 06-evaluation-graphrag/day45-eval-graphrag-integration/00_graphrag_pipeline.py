"""
Day 45: GraphRAG Pipeline.

整合 GraphRAG 和评测的完整 Pipeline。

Usage:
    python graphrag_pipeline.py
"""


class GraphRAGPipeline:
    """GraphRAG Pipeline。"""

    def __init__(self):
        self.entities = {}
        self.relationships = []
        self.documents = []

    def add_document(self, doc_id: str, text: str, entities: list[dict]):
        """添加文档。"""
        self.documents.append({"id": doc_id, "text": text})

        # 添加实体
        for entity in entities:
            self.entities[entity["id"]] = entity

    def add_relationship(self, source_id: str, target_id: str, relation: str):
        """添加关系。"""
        self.relationships.append({
            "source": source_id,
            "target": target_id,
            "relation": relation,
        })

    def query(self, query: str) -> dict:
        """查询。"""
        # 1. 实体匹配
        matched_entities = []
        for eid, entity in self.entities.items():
            if entity["name"] in query:
                matched_entities.append(entity)

        # 2. 图检索（查找相关实体和关系）
        related = []
        for entity in matched_entities:
            for rel in self.relationships:
                if rel["source"] == entity["id"] or rel["target"] == entity["id"]:
                    related.append(rel)

        # 3. 生成上下文
        context = self._build_context(matched_entities, related)

        # 4. 模拟 LLM 生成
        answer = f"基于知识图谱的回答: 找到 {len(matched_entities)} 个实体, {len(related)} 个关系"

        return {
            "query": query,
            "entities": matched_entities,
            "relationships": related,
            "context": context,
            "answer": answer,
        }

    def _build_context(self, entities, relationships) -> str:
        """构建上下文。"""
        context = "实体:\n"
        for entity in entities:
            context += f"  - {entity['name']} ({entity['type']})\n"

        context += "\n关系:\n"
        for rel in relationships:
            source = self.entities.get(rel["source"], {}).get("name", "?")
            target = self.entities.get(rel["target"], {}).get("name", "?")
            context += f"  - {source} -[{rel['relation']}]-> {target}\n"

        return context

    def evaluate(self, test_cases: list[dict]) -> dict:
        """评测。"""
        results = []

        for case in test_cases:
            result = self.query(case["query"])
            # 简单评测：检查是否找到相关实体
            found = len(result["entities"])
            expected = case.get("expected_entities", 1)
            score = min(found / expected, 1.0) if expected > 0 else 0

            results.append({
                "query": case["query"],
                "score": score,
            })

        avg_score = sum(r["score"] for r in results) / len(results) if results else 0

        return {
            "avg_score": avg_score,
            "details": results,
        }


def graphrag_pipeline_demo():
    """GraphRAG Pipeline 演示。"""
    print("=" * 60)
    print("GraphRAG Pipeline Demo")
    print("=" * 60)

    pipeline = GraphRAGPipeline()

    # 添加文档
    print("\n📦 构建知识图谱:")
    pipeline.add_document("doc1", "贵州茅台是白酒龙头", [
        {"id": "moutai", "name": "贵州茅台", "type": "Company"},
        {"id": "baijiu", "name": "白酒", "type": "Industry"},
    ])
    pipeline.add_document("doc2", "五粮液是白酒企业", [
        {"id": "wuliangye", "name": "五粮液", "type": "Company"},
    ])

    # 添加关系
    pipeline.add_relationship("moutai", "baijiu", "属于")
    pipeline.add_relationship("wuliangye", "baijiu", "属于")
    pipeline.add_relationship("moutai", "wuliangye", "竞争对手")

    print(f"   实体数: {len(pipeline.entities)}")
    print(f"   关系数: {len(pipeline.relationships)}")

    # 查询
    print(f"\n🔍 查询:")
    result = pipeline.query("白酒龙头企业")
    print(f"   查询: {result['query']}")
    print(f"   找到实体: {[e['name'] for e in result['entities']]}")
    print(f"   回答: {result['answer']}")

    # 评测
    print(f"\n📊 评测:")
    test_cases = [
        {"query": "白酒龙头企业", "expected_entities": 1},
        {"query": "五粮液", "expected_entities": 1},
    ]
    eval_result = pipeline.evaluate(test_cases)
    print(f"   平均得分: {eval_result['avg_score']:.2f}")

    print("\n✅ GraphRAG Pipeline 完成")


if __name__ == "__main__":
    graphrag_pipeline_demo()
