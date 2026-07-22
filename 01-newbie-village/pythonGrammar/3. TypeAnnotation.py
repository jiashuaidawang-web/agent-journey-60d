from typing import List,Dict,Optional

# List[str] 等价 Java的List<String>
# Dict[str, int] 等价 Java的Map<String, Integer>
# Optional[str] 等价 Java的@Nullable String，表示可以是None


def build_agent_content(
        sys_prompt: str,
        history_prompt: List[Dict[str,str]],
        max_token_limit: Optional[int] = None
)->List[Dict[str,str]]:
    """组装LLM的上下文，类比Java的DTO组装"""
    content = [{"role":"system","content":"system_prompt"}]
    if max_token_limit and len(str(sys_prompt)) > max_token_limit:
        content = content[-5:]
    return content

# 写一个parse_tool_call函数，输入是dict类型，返回Optional[dict]，如果输入没有name字段就返回None。


def parse_tool_call(name:dict) -> Optional[dict]:
    if not name:
        return None
    elif name["role"] == "system_prompt":
        return ["name","user"]