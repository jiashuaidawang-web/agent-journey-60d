"""
================================================================================
Day 2 - 意图分类器 | 01_intent_classifier.py
================================================================================

【学习目标】
实现 IntentClassifier：输入自然语言 → 输出结构化意图

【前置知识】
- 00_pydantic_models.py（Pydantic 模型）

【操作步骤】
1. 运行: python 01_intent_classifier.py "帮我分析贵州茅台"
2. 观察输出：意图类型 + 实体 + 置信度

【预期输出】
📝 输入: 帮我分析贵州茅台

✅ 分类结果:
   Intent:     stock_analysis
   Entity:     贵州茅台
   Confidence: 0.95

📦 JSON 输出:
   {"intent":"stock_analysis","entity":"贵州茅台","confidence":0.95}

【验证标准】
□ 能看到意图分类结果
□ 能看到 JSON 输出
□ 尝试不同输入（天气、计算），观察分类结果

【代码要点】
- response_format={"type": "json_object"}: JSON Mode
- json.loads(): 解析 JSON
- IntentResult(**result_dict): Pydantic 验证

================================================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from pydantic_models import IntentResult
from model_config import ModelConfig


def classify_intent(user_input: str) -> IntentResult:
    """意图分类器。

    使用 OpenAI Structured Outputs 保证输出格式。

    Args:
        user_input: 用户自然语言输入

    Returns:
        结构化的 IntentResult
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ 请先安装依赖: pip install openai")
        sys.exit(1)

    config = ModelConfig.from_env()

    if not config.api_key or config.api_key == "your-key-here":
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        sys.exit(1)

    client = OpenAI(**config.get_client_kwargs())

    # System Prompt 定义意图分类规则
    system_prompt = """你是一个意图分类器。根据用户输入，识别其意图。

支持的意图类型：
- stock_analysis: 股票分析（包含股票名称）
- weather: 天气查询（包含城市名）
- calculation: 数学计算（包含表达式）
- unknown: 未知意图

请输出 JSON 格式：
{
  "intent": "意图类型",
  "entity": "提取的实体（股票名/城市名/表达式）",
  "confidence": 0.0-1.0 的置信度
}"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    # 使用 Structured Output
    response = client.chat.completions.create(
        model=config.model_name,
        messages=messages,
        temperature=0.0,  # 分类任务用低温
        max_tokens=256,
        response_format={"type": "json_object"},
    )

    result_json = response.choices[0].message.content
    result_dict = json.loads(result_json)

    # 用 Pydantic 验证
    intent_result = IntentResult(**result_dict)

    return intent_result


def main():
    """命令行入口。"""
    user_input = sys.argv[1] if len(sys.argv) > 1 else "帮我分析贵州茅台"

    print(f"📝 输入: {user_input}\n")

    result = classify_intent(user_input)

    print(f"✅ 分类结果:")
    print(f"   Intent:     {result.intent}")
    print(f"   Entity:     {result.entity}")
    print(f"   Confidence: {result.confidence}")
    print()
    print(f"📦 JSON 输出:")
    print(f"   {result.model_dump_json()}")


if __name__ == "__main__":
    main()
