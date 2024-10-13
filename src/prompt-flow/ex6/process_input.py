from promptflow import tool

def add_one(input_text: str) -> str:
    return f"{input_text} one"

def add_two(input_text: str) -> str:
    return f"{input_text} two"

def add_three(input_text: str) -> str:
    return f"{input_text} three"

@tool
def process_input(step: str, input_text: str) -> dict:
    """입력 텍스트를 처리하고 지정된 단계를 수행합니다."""
    if step == "one":
        result = add_one(input_text)
    elif step == "two":
        result = add_two(input_text)
    elif step == "three":
        result = add_three(input_text)
        parts = result.split()
        return {
            "original_input": parts[0],
            "with_one": " ".join(parts[:2]),
            "with_two": " ".join(parts[:3]),
            "final_result": result
        }
    else:
        raise ValueError(f"Unknown step: {step}")
    
    return {"result": result}

# 테스트용 코드
if __name__ == "__main__":
    user_input = "Hello"
    step1 = process_input("one", user_input)
    step2 = process_input("two", step1["result"])
    final_result = process_input("three", step2["result"])
    print(final_result)