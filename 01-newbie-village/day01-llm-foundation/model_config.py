"""
Model configuration for agent-journey-60d.

Abstraction over model providers — similar to Java's ServiceProvider interface.
"""

from pydantic import BaseModel, Field
from typing import Optional


class ModelConfig(BaseModel):
    """模型配置 — 支持多provider切换."""

    api_key: str = Field(..., description="API密钥")
    base_url: str = Field(
        default="https://api.openai.com/v1",
        description="OpenAI兼容的API地址",
    )
    model_name: str = Field(default="gpt-4o", description="模型名称")
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, gt=0)
    timeout: int = Field(default=60, gt=0, description="请求超时秒数")

    def get_client_kwargs(self) -> dict:
        """获取客户端初始化参数."""
        return {
            "api_key": self.api_key,
            "base_url": self.base_url,
            "timeout": self.timeout,
        }


class ChatParams(BaseModel):
    """聊天请求参数."""

    messages: list[dict] = Field(..., description="消息列表")
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    stream: bool = Field(default=False)
    response_format: Optional[dict] = None  # JSON schema
