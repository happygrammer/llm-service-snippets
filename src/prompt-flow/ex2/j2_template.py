import os
from jinja2 import Environment, FileSystemLoader
from promptflow.core import tool

# 현재 스크립트의 절대 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__))

# Jinja2 환경 설정
env = Environment(loader=FileSystemLoader(current_dir))

# 템플릿 파일의 존재 여부를 확인합니다
template_path = os.path.join(current_dir, 'greeting_template.j2')
if not os.path.exists(template_path):
    raise FileNotFoundError(f"Template file not found: {template_path}")

template = env.get_template('greeting_template.j2')

@tool
def greet(name: str) -> str:
    return template.render(name=name)

def simple_greeting(user_name: str) -> dict:
    greeting = greet(user_name)
    return {"greeting": greeting}

# 예시 실행
if __name__ == "__main__":
    user_name = "홍길동"
    result = simple_greeting(user_name)
    print(result["greeting"])
    # 안녕하세요, 홍길동님! Prompt Flow에 오신 것을 환영합니다!