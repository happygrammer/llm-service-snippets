from promptflow.core import tool

@tool
def convert_to_fahrenheit(celsius):
    celsius = float(celsius)  # 문자열을 float로 변환
    fahrenheit = (celsius * 9/5) + 32
    return {"fahrenheit": fahrenheit}

def main(celsius):
    return convert_to_fahrenheit(celsius)