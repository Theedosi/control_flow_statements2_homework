def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp<0:
        "Freezing"
    if temp>0 and temp<=10:
        "Very Cold"
    if temp>=11 and temp<=20:
        "Cold"
    if temp>=21 and temp<=30:
        "Normal"
    if temp>=31 and temp<=40:
         "Hot"
    if temp>40:
        "Very Hot"