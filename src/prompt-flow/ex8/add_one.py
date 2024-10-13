from promptflow import tool

@tool
def add_one(input_text: str) -> dict:
    """'one'을 추가합니다."""
    result = f"{input_text} one"
    return {"result": result}