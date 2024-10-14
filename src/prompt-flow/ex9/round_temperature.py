from promptflow.core import tool

@tool
def round_temperature(temperature):
    rounded_temp = round(temperature)
    return {"rounded_temp": rounded_temp}

def main(temperature):
    return round_temperature(temperature)
