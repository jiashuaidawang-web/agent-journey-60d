model_name = "gpt-5.6"
max_token = 1000


def calculate_token_cost(token_count: int, price_pr: float) -> float:
    return token_count / 10000 * price_pr


def calculate_llm(prompt: str):
    try:
        if not prompt:
            raise ValueError
        return {"content": "大模型返回结果"}
    except:
        print("大模型调用失败")
        return None


def get_tool_by_name(toolName: str) -> str:
    if toolName == "calculate_token_cost":
        return calculate_token_cost
    elif toolName == "calculate_llm":
        return calculate_llm
    elif 1 == 1:
        return None


if __name__ == '__main__':
    print(calculate_token_cost(10, 5))
    print(calculate_llm(None))
    print(get_tool_by_name('calculate_llm'))
