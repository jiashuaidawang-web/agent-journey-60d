from typing import Dict
from pydantic import BaseModel

# 定义toolcall结构,返回javaDTO
class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, str]
    call_id: str | None = None

toolCall  = ToolCall(name="toolCall", arguments={"a":"1"})
print(toolCall.model_dump())

