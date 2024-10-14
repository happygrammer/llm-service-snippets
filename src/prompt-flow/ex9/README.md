# 온도 변환 Flow

섭씨를 화씨로 변환하고 날씨 설명을 제공하는 간단한 prompt flow를 보여줍니다. 온도 변환, 반올림, 날씨 설명을 위한 세 개의 Python 스크립트를 포함합니다.

실행 방법:

```
pf flow test --flow . --inputs celsius_temp="25"
```

```
pf flow test --flow . --inputs celsius_temp="25"
Prompt flow service has started...
WARNING:root:'from promptflow import tool' is deprecated and will be removed in the future. Use 'from promptflow.core import tool' instead.
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Start executing nodes in thread pool mode.
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Start to run 3 nodes with concurrency level 16.
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Executing node convert_to_fahrenheit. node run id: 1dd1a8eb-4097-4470-b452-8b77c49f0b77_convert_to_fahrenheit_0
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Node convert_to_fahrenheit completes.
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Executing node round_temperature. node run id: 1dd1a8eb-4097-4470-b452-8b77c49f0b77_round_temperature_0
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Node round_temperature completes.
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Executing node describe_weather. node run id: 1dd1a8eb-4097-4470-b452-8b77c49f0b77_describe_weather_0
2024-10-14 22:15:52 +0900    3924 execution.flow     INFO     Node describe_weather completes.
You can view the trace detail from the following URL:
http://127.0.0.1:23333/v1.0/ui/traces/?#collection=ex9&uiTraceId=0x3c57fe0e3b998af374e1872a1fb6f60f
{
    "weather_description": {
        "temperature": 77,
        "description": "It's warm and nice."
    }
}
```