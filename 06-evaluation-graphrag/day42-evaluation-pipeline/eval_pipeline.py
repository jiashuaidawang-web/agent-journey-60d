"""
Day 42: Evaluation Pipeline.

演示评测流水线。

Usage:
    python eval_pipeline.py
"""


class EvaluationPipeline:
    """评测流水线。"""

    def __init__(self):
        self.metrics = []
        self.results = []

    def add_metric(self, name: str, func):
        """添加评测指标。"""
        self.metrics.append({"name": name, "func": func})

    def run(self, dataset: list[dict]) -> dict:
        """运行评测。"""
        print("=" * 60)
        print("Evaluation Pipeline")
        print("=" * 60)

        print(f"\n📊 数据集: {len(dataset)} 条")
        print(f"📊 指标: {len(self.metrics)} 个")

        # 执行 RAG
        print(f"\n🔄 执行 RAG...")
        predictions = []
        for item in dataset:
            # 模拟 RAG 执行
            prediction = {
                "query": item["query"],
                "answer": f"回答: {item['query']}",
                "contexts": [f"上下文: {item['query']}"],
            }
            predictions.append(prediction)

        # 计算指标
        print(f"🔄 计算指标...")
        scores = {}
        for metric in self.metrics:
            metric_scores = []
            for pred, gt in zip(predictions, dataset):
                score = metric["func"](pred, gt)
                metric_scores.append(score)
            avg_score = sum(metric_scores) / len(metric_scores) if metric_scores else 0
            scores[metric["name"]] = avg_score

        # 生成报告
        print(f"\n📋 评测报告:")
        for name, score in scores.items():
            bar = "█" * int(score * 20)
            print(f"   {name:<20} {score:.4f} {bar}")

        return scores


def eval_pipeline_demo():
    """评测流水线演示。"""
    pipeline = EvaluationPipeline()

    # 添加指标
    pipeline.add_metric("answer_relevance", lambda pred, gt: 0.85)
    pipeline.add_metric("faithfulness", lambda pred, gt: 0.90)
    pipeline.add_metric("context_recall", lambda pred, gt: 0.80)

    # 评测数据集
    dataset = [
        {"query": "白酒龙头", "ground_truth": "贵州茅台"},
        {"query": "电池龙头", "ground_truth": "宁德时代"},
        {"query": "新能源车", "ground_truth": "比亚迪"},
    ]

    # 运行评测
    scores = pipeline.run(dataset)

    return scores


if __name__ == "__main__":
    eval_pipeline_demo()
