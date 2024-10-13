  'flow.dag.yaml' 파일에서 정의된 워크플로우에 따라 입력 텍스트에 "one", "two", "three"를 차례로 추가합니다. 프로젝트는 메인 YAML 파일과 개별 노드 YAML 파일들('nodes/' 디렉토리 내)로 구성되어 있으며, 'process_input.py'에서 실제 텍스트 처리 로직을 수행합니다.
  
  실행하려면 Prompt Flow를 설치한 후 아래 명령어를 입력하세요.
  
```
pf flow test --flow . --inputs user_input="Hello"
```

  이 프로젝트는 Prompt Flow의 기본 사용법과 모듈화된 워크플로우 구성 방법을 보여주는 예제입니다.