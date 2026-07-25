"""
Day 1: Model Configuration Abstraction.

支持多 Provider: OpenAI / 通义千问 / DeepSeek / 智谱
从环境变量加载配置。

Java 类比: 相当于 application.yml + @ConfigurationProperties
"""

import os
from pydantic import BaseModel, Field


class ModelConfig(BaseModel):
    """模型配置抽象。

    支持任意 OpenAI 兼容 API 的模型。
    """

    api_key: str = Field(..., description="API Key")
    base_url: str = Field("https://api.openai.com/v1", description="API Base URL")
    model_name: str = Field("gpt-4o-mini", description="模型名称")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="温度")
    max_tokens: int = Field(2048, gt=0, description="最大输出 Token 数")
    timeout: int = Field(60, gt=0, description="超时时间(秒)")

    def get_client_kwargs(self) -> dict:
        """返回 OpenAI client 构造参数。"""
        return {
            "api_key": self.api_key,
            "base_url": self.base_url,
            "timeout": self.timeout,
        }

    @classmethod
    def from_env(cls) -> "ModelConfig":
        """从环境变量加载配置。

        支持的环境变量:
        - OPENAI_API_KEY
        - OPENAI_BASE_URL
        - MODEL_NAME
        - MODEL_TEMPERATURE
        - MODEL_MAX_TOKENS
        - MODEL_TIMEOUT
        """
        return cls(
            api_key=os.getenv("OPENAI_API_KEY", ""),
            base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
            model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            temperature=float(os.getenv("MODEL_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("MODEL_MAX_TOKENS", "2048")),
            timeout=int(os.getenv("MODEL_TIMEOUT", "60")),
        )

    def __str__(self) -> str:
        # 脱敏显示 api_key
        masked_key = self.api_key[:8] + "..." + self.api_key[-4:] if len(self.api_key) > 12 else "***"
        return (
            f"ModelConfig(model={self.model_name}, base_url={self.base_url}, "
            f"temp={self.temperature}, max_tokens={self.max_tokens}, key={masked_key})"
        )


class ChatParams(BaseModel):
    """聊天请求参数。"""

    messages: list[dict] = Field(..., description="消息列表")
    temperature: float | None = None
    max_tokens: int | None = None
    stream: bool = Field(default=False)
    response_format: dict | None = None  # JSON schema


# 常用模型预设
MODEL_PRESETS = {
    "gpt-4o": {
        "model_name": "gpt-4o",
        "base_url": "https://api.openai.com/v1",
    },
    "gpt-4o-mini": {
        "model_name": "gpt-4o-mini",
        "base_url": "https://api.openai.com/v1",
    },
    "qwen-plus": {
        "model_name": "qwen-plus",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    },
    "deepseek-chat": {
        "model_name": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
    },
    "glm-4-flash": {
        "model_name": "glm-4-flash",
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
    },
}
