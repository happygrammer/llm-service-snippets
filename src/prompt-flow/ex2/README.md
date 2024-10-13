# Prompt Flow Greeting Tool

Prompt Flow를 사용하여 사용자에게 인사말을 생성하는 도구를 구현한 예제입니다.

## 사용 방법

1. `greeting_template.j2` 파일을 수정하여 원하는 인사말 템플릿을 작성합니다.

2. 스크립트를 실행합니다:
   ```
   python greeting_tool.py
   ```

3. 스크립트는 사용자 이름을 입력받아 인사말을 생성하고 출력합니다.

## 주요 기능

- Jinja2 템플릿 엔진을 사용하여 동적으로 인사말 생성
- Prompt Flow의 `@tool` 데코레이터를 사용하여 도구 함수 정의
- 사용자 이름을 입력받아 개인화된 인사말 생성

## 파일 구조

- `greeting_tool.py`: 주요 Python 스크립트
- `greeting_template.j2`: Jinja2 템플릿 파일
