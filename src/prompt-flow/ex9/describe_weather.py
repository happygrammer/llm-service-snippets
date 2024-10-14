from promptflow.core import tool

@tool
def describe_weather(fahrenheit):
    if fahrenheit < 32:
        description = "It's freezing cold!"
    elif 32 <= fahrenheit < 50:
        description = "It's cold."
    elif 50 <= fahrenheit < 70:
        description = "It's cool and pleasant."
    elif 70 <= fahrenheit < 85:
        description = "It's warm and nice."
    else:
        description = "It's hot!"

    return {"temperature": fahrenheit, "description": description}

def main(fahrenheit):
    return describe_weather(fahrenheit)
