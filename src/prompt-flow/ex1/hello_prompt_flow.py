from promptflow.core import tool

@tool
def greet(name: str) -> str:
    return f"안녕하세요, {name}님! Prompt Flow에 오신 것을 환영합니다!"

# flow 데코레이터 대신 일반 함수로 변경
def simple_greeting(user_name: str) -> dict:
    greeting = greet(user_name)
    return {"greeting": greeting}

# 예시 실행
if __name__ == "__main__":
    user_name = "홍길동"
    result = simple_greeting(user_name)
    print(result["greeting"])
    # 안녕하세요, 홍길동님! Prompt Flow에 오신 것을 환영합니다!