def add(a: int, b: int) -> int:
    result = a + b
    return result


def subtract(a: int, b: int) -> int:
    result = a - b
    return result


def divide(a: int, b: int) -> int:
    result = a / b
    return result


def multiply(a: int, b: int) -> int:
    result = a * b
    return result

function = input()
a = int(input())
b = int(input())

if function == "add":
    print(add(a, b))
elif function == "subtract":
    print(subtract(a, b))
elif function == "divide":
    print(divide(a, b))
elif function == "multiply":
    print(multiply(a, b))