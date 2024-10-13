Prompt Flow를 사용하여 사용자 입력을 순차적으로 처리하는 간단한 예제를 구현합니다. 입력 텍스트에 "one", "two", "three"를 차례로 추가하여 최종 결과를 생성합니다.

## 실행 명령어

프로젝트를 실행하려면 다음 명령어를 사용하세요:

```bash
pf flow test --flow . --inputs user_input="Hello"
```

이 명령어는 현재 디렉토리의 `flow.dag.yaml` 파일을 기반으로 플로우를 테스트 실행합니다.

## 예상 출력

성공적으로 실행되면 다음과 같은 출력을 볼 수 있습니다:

```json
{
  "final_result": {
    "original_input": "Hello",
    "with_one": "Hello one",
    "with_two": "Hello one two",
    "final_result": "Hello one two three"
  }
}
```