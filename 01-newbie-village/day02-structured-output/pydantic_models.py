"""
================================================================================
Day 2 - Pydantic 模型定义 | pydantic_models.py
================================================================================

【学习目标】
理解 Pydantic 模型：Agent 系统常用的结构化输出模型

【前置知识】
- Day 1 LLM Foundation

【操作步骤】
1. 运行: python pydantic_models.py
2. 观察输出：模型的 JSON 序列化和校验

【预期输出】
IntentResult: {"intent":"stock_analysis","entity":"贵州茅台","confidence":0.95}
ToolCall: {"tool_name":"stock_tool","arguments":{"stock":"贵州茅台"},"reasoning":"用户要分析股票"}
✅ 校验生效: 1 validation error for IntentResult...

【验证标准】
□ 能看到模型的 JSON 输出
□ 能看到校验错误（confidence > 1 时报错）
□ 理解 BaseModel + Field 的用法

【代码要点】
- BaseModel: Pydantic 基类
- Field: 字段定义和校验
- Literal: 限定取值范围
- model_dump_json(): 序列化为 JSON

================================================================================
"""

from pydantic import BaseModel, Field
from typing import Literal


class IntentResult(BaseModel):
    """意图识别结果。"""

    intent: str = Field(..., description="意图类型")
    entity: str | None = Field(None, description="提取的实体")
    confidence: float = Field(..., ge=0.0, le=1.0, description="置信度")


class ToolCall(BaseModel):
    """工具调用。

    LLM 决定调用工具时，输出这个结构。
    """

    tool_name: str = Field(..., description="工具名称")
    arguments: dict = Field(default_factory=dict, description="工具参数")
    reasoning: str | None = Field(None, description="为什么选择这个工具")


class ToolResult(BaseModel):
    """工具执行结果。"""

    tool_name: str = Field(..., description="工具名称")
    success: bool = Field(..., description="是否成功")
    result: str = Field(..., description="执行结果")
    error: str | None = Field(None, description="错误信息")


class AgentResponse(BaseModel):
    """Agent 最终响应。"""

    content: str = Field(..., description="回复内容")
    tool_calls: list[ToolCall] = Field(default_factory=list, description="工具调用列表")
    finished: bool = Field(default=False, description="是否完成")


# 常用意图类型（Literal 限定取值）
IntentType = Literal[
    "stock_analysis",
    "weather",
    "calculation",
    "search",
    "unknown",
]


class StrictIntentResult(BaseModel):
    """严格的意图识别结果（使用 Literal）。"""

    intent: IntentType = Field(..., description="意图类型")
    entity: str | None = Field(None, description="提取的实体")
    confidence: float = Field(..., ge=0.0, le=1.0, description="置信度")


# 测试
if __name__ == "__main__":
    # 测试 IntentResult
    result = IntentResult(intent="stock_analysis", entity="贵州茅台", confidence=0.95)
    print(f"IntentResult: {result.model_dump_json()}")

    # 测试 ToolCall
    call = ToolCall(tool_name="stock_tool", arguments={"stock": "贵州茅台"}, reasoning="用户要分析股票")
    print(f"ToolCall: {call.model_dump_json()}")

    # 测试校验
    try:
        bad_result = IntentResult(intent="test", confidence=1.5)  # confidence > 1 应该报错
    except Exception as e:
        print(f"✅ 校验生效: {e}")
