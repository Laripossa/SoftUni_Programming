def smallest(some_numbers: list) -> int:
    return min(some_numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
smallest_element = smallest([first_num, second_num, third_num])
print(smallest_element)