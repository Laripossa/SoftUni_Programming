def calculate_factorial_num(number):
    for current_number in range(1, number):
        number *= current_number
    return number


def factorial_division(number :int, number2: int) -> float:
    first_factorial = calculate_factorial_num(number)
    second_factorial = calculate_factorial_num(number2)
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
result = factorial_division(first_number, second_number)
print(f"{result:.2f}")