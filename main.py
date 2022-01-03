def calculator(num1, num2, operator):
    if operator == "+":
        return int(num1) + int(num2)
    elif operator == "-":
        return int(num1) - int(num2)
    elif operator == "*":
        return int(num1) * int(num2)
    else:
        return int(num1) / int(num2)


