def sum_numbers(n1, n2):
    return n1 + n2


def subtract(sum, n3):
    return sum - n3


def add_and_subtract(n1, n2, n3):
    sum_of_first_and_second = sum_numbers(n1, n2)
    final_result = subtract(sum_of_first_and_second, n3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))