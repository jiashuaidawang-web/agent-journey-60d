"""
Day 32: Observability Demo.

演示 Agent 系统的可观测性。

Usage:
    python trace_demo.py
"""


class Trace:
    """追踪。"""

    def __init__(self, trace_id: str):
        self.trace_id = trace_id
        self.spans: list[Span] = []

    def add_span(self, span):
        self.spans.append(span)

    def to_dict(self):
        return {
            "trace_id": self.trace_id,
            "spans": [s.to_dict() for s in self.spans],
            "total_duration": sum(s.duration for s in self.spans),
        }


class Span:
    """步骤。"""

    def __init__(self, name: str, input_data: dict = None, output_data: dict = None):
        self.name = name
        self.input_data = input_data or {}
        self.output_data = output_data or {}
        self.duration = 0
        self.tokens = 0
        self.status = "success"
        self.error = None

    def set_duration(self, duration: float):
        self.duration = duration

    def set_tokens(self, tokens: int):
        self.tokens = tokens

    def set_error(self, error: str):
        self.error = error
        self.status = "error"

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "tokens": self.tokens,
            "status": self.status,
            "error": self.error,
        }


class AgentTracer:
    """Agent 追踪器。"""

    def __init__(self):
        self.traces: dict[str, Trace] = {}

    def start_trace(self, trace_id: str) -> Trace:
        trace = Trace(trace_id)
        self.traces[trace_id] = trace
        return trace

    def add_span(self, trace_id: str, name: str, **kwargs):
        span = Span(name, **kwargs)
        if trace_id in self.traces:
            self.traces[trace_id].add_span(span)
        return span

    def get_trace(self, trace_id: str) -> Trace | None:
        return self.traces.get(trace_id)

    def summary(self):
        return {
            "total_traces": len(self.traces),
            "total_spans": sum(len(t.spans) for t in self.traces.values()),
            "total_tokens": sum(
                sum(s.tokens for s in t.spans) for t in self.traces.values()
            ),
        }


def trace_demo():
    """Trace 演示。"""
    print("=" * 60)
    print("Trace Demo")
    print("=" * 60)

    tracer = AgentTracer()

    # 模拟 Agent 执行
    trace = tracer.start_trace("trace_001")

    # 步骤1：查询重写
    span1 = tracer.add_span("trace_001", "query_rewrite",
                            input_data={"query": "白酒龙头"})
    span1.set_duration(0.5)
    span1.set_tokens(100)

    # 步骤2：向量检索
    span2 = tracer.add_span("trace_001", "vector_search",
                            input_data={"query_rewrite": "白酒龙头企业"})
    span2.set_duration(0.3)
    span2.set_tokens(0)

    # 步骤3：LLM 生成
    span3 = tracer.add_span("trace_001", "llm_generate",
                            input_data={"context": "..."})
    span3.set_duration(2.0)
    span3.set_tokens(500)

    # 打印 Trace
    trace_data = trace.to_dict()
    print(f"\n📋 Trace: {trace_data['trace_id']}")
    print(f"   总耗时: {trace_data['total_duration']:.2f}s")
    print(f"\n   Steps:")
    for span in trace_data["spans"]:
        print(f"   - {span['name']}: {span['duration']:.2f}s, {span['tokens']} tokens, {span['status']}")

    # 汇总
    summary = tracer.summary()
    print(f"\n📊 汇总:")
    print(f"   Trace 数: {summary['total_traces']}")
    print(f"   Span 数: {summary['total_spans']}")
    print(f"   总 Token: {summary['total_tokens']}")


if __name__ == "__main__":
    trace_demo()
