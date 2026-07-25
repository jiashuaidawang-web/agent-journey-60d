"""
Mini Agent Runtime - Model Abstraction.

模型抽象层：定义 Model 接口 + OpenAI 实现。

Java 类比:
    Model 接口    ≈  interface ChatModel { ChatResponse chat(ChatRequest) }
    OpenAIModel   ≈  OpenAIChatModel implements ChatModel
"""

from __future__ import annotations

import json
import time
from abc import ABC, abstractmethod


class Model(ABC):
    """模型抽象接口。"""

    @abstractmethod
    def chat(self, messages: list[dict]) -> dict:
        """发送聊天请求。

        Args:
            messages: 消息列表

        Returns:
            {
                "content": str,          # 回复内容
                "tool_calls": list|null,  # 工具调用
                "input_tokens": int,
                "output_tokens": int,
            }
        """
        ...

    @abstractmethod
    def chat_with_tools(self, messages: list[dict], tools: list[dict]) -> dict:
        """带工具的聊天请求。"""
        ...


class OpenAIModel(Model):
    """OpenAI 兼容模型实现。"""

    def __init__(self, api_key: str, model_name: str = "gpt-4o-mini",
                 base_url: str = "https://api.openai.com/v1", temperature: float = 0.7):
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = base_url
        self.temperature = temperature

        from openai import OpenAI
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def chat(self, messages: list[dict]) -> dict:
        """基础聊天（不带工具）。"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=self.temperature,
        )

        return {
            "content": response.choices[0].message.content or "",
            "tool_calls": None,
            "input_tokens": response.usage.prompt_tokens if response.usage else 0,
            "output_tokens": response.usage.completion_tokens if response.usage else 0,
        }

    def chat_with_tools(self, messages: list[dict], tools: list[dict]) -> dict:
        """带工具的聊天。"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=self.temperature,
        )

        assistant_message = response.choices[0].message
        tool_calls = None

        if assistant_message.tool_calls:
            tool_calls = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in assistant_message.tool_calls
            ]

        return {
            "content": assistant_message.content or "",
            "tool_calls": tool_calls,
            "input_tokens": response.usage.prompt_tokens if response.usage else 0,
            "output_tokens": response.usage.completion_tokens if response.usage else 0,
        }
