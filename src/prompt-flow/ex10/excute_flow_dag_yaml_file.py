from promptflow.client import PFClient
from promptflow.entities import Run
import yaml
import os

def load_flow_inputs(flow_file: str) -> dict:
    with open(flow_file, 'r') as f:
        flow_dag = yaml.safe_load(f)
    return {k: v['type'] for k, v in flow_dag.get('inputs', {}).items()}

def execute_flow(flow_dir: str, inputs: dict) -> dict:
    # PFClient 초기화
    client = PFClient()

    # flow 경로 설정
    flow_path = os.path.abspath(flow_dir)

    # flow 실행
    run: Run = client.test(flow=flow_path, inputs=inputs)

    # 결과 반환
    return run

if __name__ == "__main__":
    # flow 디렉토리 (flow.dag.yaml 파일이 있는 디렉토리)
    # current path를 flow 디렉토리로 설정

    flow_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../ex9"))
    print(flow_dir)


    # flow.dag.yaml에서 입력 정보 로드
    flow_file = os.path.join(flow_dir, "flow.dag.yaml")
    input_schema = load_flow_inputs(flow_file)

    # 사용자로부터 입력 받기
    inputs = {}
    for input_name, input_type in input_schema.items():
        value = input(f"Enter value for {input_name} ({input_type}): ")
        inputs[input_name] = value

    # flow 실행
    results = execute_flow(flow_dir, inputs)

    # 결과 출력
    print("\nResults:")
    for key, value in results.items():
        print(f"{key}: {value}")