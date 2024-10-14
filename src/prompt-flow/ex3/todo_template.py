import os
from jinja2 import Environment, FileSystemLoader
from promptflow.core import tool
from typing import List, Dict

current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir))

# 템플릿 파일 확인
template_path = os.path.join(current_dir, 'todo_template.j2')
if not os.path.exists(template_path):
    raise FileNotFoundError(f"Template file not found: {template_path}")

template = env.get_template('todo_template.j2')

@tool
def format_todo_list(todos: List[Dict[str, str]]) -> str:
    return template.render(todos=todos)

def manage_todo_list(action: str, task: str = "", todos: List[Dict[str, str]] = []) -> Dict[str, str]:
    if action == "add":
        todos.append({"task": task, "status": "미완료"})
        message = f"Task '{task}' added to the list."
    elif action == "complete":
        for todo in todos:
            if todo["task"] == task:
                todo["status"] = "완료"
                message = f"Task '{task}' marked as complete."
                break
        else:
            message = f"Task '{task}' not found in the list."
    elif action == "list":
        formatted_list = format_todo_list(todos)
        message = f"Current Todo List:\n{formatted_list}"
    else:
        message = "Invalid action. Use 'add', 'complete', or 'list'."

    return {"message": message, "todos": todos}

# 예시 실행
if __name__ == "__main__":
    todos = []

    # 추가
    result = manage_todo_list("add", "apple", todos)
    print(result["message"])

    # 추가
    result = manage_todo_list("add", "banana", result["todos"])
    print(result["message"])

    # 추가된 항목에 대한 리스트 출력
    result = manage_todo_list("list", todos=result["todos"])
    print(result["message"])

    # 완료로 상태 업데이트
    result = manage_todo_list("complete", "apple", result["todos"])
    print(result["message"])

    # 리스트 출력
    result = manage_todo_list("list", todos=result["todos"])
    print(result["message"])

"""
Task 'apple' added to the list.
Task 'banana' added to the list.
Current Todo List:

- apple (미완료)

- banana (미완료)

Task 'apple' marked as complete.
Current Todo List:

- apple (완료)

- banana (미완료)
"""