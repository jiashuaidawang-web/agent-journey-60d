''''
 Boss 题里已经画出了架构：

  "帮我分析贵州茅台"
      ↓
  Intent_classifier.py（意图分类器）
      ↓
  {"intent": "stock_analysis", "entity": "贵州茅台", "confidence": 0.9}
      ↓
  02_router.py（路由器）← 你在这里
      ↓
  stock_analysis_handler() / weather_handler() / ...
'''

from pydantic_models import IntentResult
from Intent_classifier import classify_intent

def route(user_input: str) -> IntentResult:
    intent = classify_intent(user_input)
    if intent.intent == "stock_analysis":
        return handle_stock(intent.entity)
    elif intent.intent == "weather":
        return handle_weather(intent.entity)
    else:
        return handle_unknow()





def handle_stock(user_input: str) -> IntentResult:
    return f"📈 正在分析股票: {user_input}（后续接入实时行情）"


def handle_weather(user_input: str) -> IntentResult:
    return f"📈 正在查询天气: {user_input}（后续接入实时行情）"

def handle_unknow() -> IntentResult:
    return f"📈 不知道什么模型）"


if __name__ == '__main__':
    route("棒我差寻一下N长鑫今天是什么情况")