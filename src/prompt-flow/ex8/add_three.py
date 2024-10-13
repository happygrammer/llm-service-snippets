from promptflow import tool

@tool
def add_three(input_text: str) -> dict:
    """'three'를 추가하고 최종 결과를 반환합니다."""
    result = f"{input_text} three"
    parts = result.split()
    return {
        "original_input": parts[0],
        "with_one": " ".join(parts[:2]),
        "with_two": " ".join(parts[:3]),
        "final_result": result
    }