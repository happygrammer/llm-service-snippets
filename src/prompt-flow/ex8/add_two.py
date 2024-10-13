from promptflow import tool

@tool
def add_two(input_text: str) -> dict:
    """'two'를 추가합니다."""
    result = f"{input_text} two"
    return {"result": result}