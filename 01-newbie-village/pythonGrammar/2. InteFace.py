from typing import Protocol


# 1. Protocol：完全等价Java的Interface，定义ModelProvider规范

class Iface(Protocol):
    async def chat(self, message: list, tools: list = None) -> dict:
        """所有模型实现类必须实现这个方法"""


# 2. 实现类：类比Java的implements
class OpenAIProvider:
    async def OpenAI(self, message: list, tools: list = None) -> dict:
        return {"tools": "openAi返回结果", "tool_calls": []}


class KimiProvider:
    async def Kimi(self, message: list, tools: list = None) -> dict:
        return {"tools": "kimi返回结果", "tool_calls": ""}


class BaseTool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class CaculatorTool(BaseTool):
    def __init__(self):
        super().__init__("Caculator", "计算两个数的和")

    def execute(self, a: float, b: float) -> float:
        return a + b



# 定义一个Tool Protocol，要求所有工具必须有name、description属性和execute方法，然后实现一个WeatherTool。


class ToolProtocol(Protocol):
    async def execute(self,name:str,description:str):
        ...

class WeathToolProtocal(ToolProtocol):
    def __init__(self):
        pass

    def execute(self,name:str,description:str):
        print(name)
        print(description)



class Tool(Protocol):
    name: str
    description: str
    async def execute(self,**kwargs) -> dict:
        pass


class WeatherTool(Tool):
    name = "天气"
    description = "查询指定城市的天气信息"
    async def execute(self,**kwargs) -> dict:
        city = kwargs.get("city","北京")
        return {"city":"北京","天气":"晴空万里"}


to = WeatherTool()
print((to.execute(city = "上海")))
print(isinstance(to, WeatherTool))
print(isinstance(to, WeatherTool))


if __name__ == "__main__":
    tool = CaculatorTool()
    print(tool.execute(1,2))
