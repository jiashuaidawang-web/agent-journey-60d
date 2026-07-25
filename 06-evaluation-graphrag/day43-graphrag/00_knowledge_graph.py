"""
Day 43: GraphRAG Demo.

演示 GraphRAG 的核心概念。

Usage:
    python knowledge_graph.py
"""


class Entity:
    """实体（节点）。"""

    def __init__(self, id: str, name: str, type: str):
        self.id = id
        self.name = name
        self.type = type  # Person, Company, Industry, etc.

    def __repr__(self):
        return f"Entity({self.name}, {self.type})"


class Relationship:
    """关系（边）。"""

    def __init__(self, source: Entity, target: Entity, relation: str):
        self.source = source
        self.target = target
        self.relation = relation

    def __repr__(self):
        return f"Relationship({self.source.name} -[{self.relation}]-> {self.target.name})"


class KnowledgeGraph:
    """知识图谱。"""

    def __init__(self):
        self.entities: dict[str, Entity] = {}
        self.relationships: list[Relationship] = []

    def add_entity(self, id: str, name: str, type: str) -> Entity:
        entity = Entity(id, name, type)
        self.entities[id] = entity
        return entity

    def add_relationship(self, source_id: str, target_id: str, relation: str):
        source = self.entities.get(source_id)
        target = self.entities.get(target_id)
        if source and target:
            rel = Relationship(source, target, relation)
            self.relationships.append(rel)

    def get_entity(self, id: str) -> Entity | None:
        return self.entities.get(id)

    def get_relationships(self, entity_id: str) -> list[Relationship]:
        return [r for r in self.relationships
                if r.source.id == entity_id or r.target.id == entity_id]

    def query(self, entity_name: str, depth: int = 1) -> dict:
        """查询实体及其关系。"""
        # 查找实体
        entity = None
        for e in self.entities.values():
            if e.name == entity_name:
                entity = e
                break

        if entity is None:
            return {"entity": None, "relationships": []}

        # 获取关系
        relationships = self.get_relationships(entity.id)

        return {
            "entity": entity,
            "relationships": relationships,
        }

    def display(self):
        """展示图谱。"""
        print(f"\n📊 知识图谱:")
        print(f"   实体数: {len(self.entities)}")
        print(f"   关系数: {len(self.relationships)}")

        print(f"\n   实体:")
        for entity in self.entities.values():
            print(f"   - {entity.name} ({entity.type})")

        print(f"\n   关系:")
        for rel in self.relationships:
            print(f"   - {rel.source.name} -[{rel.relation}]-> {rel.target.name}")


def knowledge_graph_demo():
    """知识图谱演示。"""
    print("=" * 60)
    print("Knowledge Graph Demo")
    print("=" * 60)

    kg = KnowledgeGraph()

    # 添加实体
    print("\n📦 添加实体:")
    kg.add_entity("mooutai", "贵州茅台", "Company")
    kg.add_entity("wuliangye", "五粮液", "Company")
    kg.add_entity("ningde", "宁德时代", "Company")
    kg.add_entity("baijiu", "白酒", "Industry")
    kg.add_entity("battery", "动力电池", "Industry")

    # 添加关系
    print("📦 添加关系:")
    kg.add_relationship("mooutai", "baijiu", "属于行业")
    kg.add_relationship("wuliangye", "baijiu", "属于行业")
    kg.add_relationship("ningde", "battery", "属于行业")
    kg.add_relationship("mooutai", "wuliangye", "竞争对手")

    # 展示
    kg.display()

    # 查询
    print(f"\n🔍 查询 '贵州茅台':")
    result = kg.query("贵州茅台")
    if result["entity"]:
        print(f"   实体: {result['entity']}")
        print(f"   关系:")
        for rel in result["relationships"]:
            print(f"   - {rel}")

    return kg


if __name__ == "__main__":
    knowledge_graph_demo()
