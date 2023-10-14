def minimum_number(some_list: list) -> int:
    return min(some_list)


def maximum_number(some_list: list) -> int:
    return max(some_list)


def sum_numbers(some_list: list) -> int:
    return sum(some_list)


numbers_list = list(map(int, input().split()))
min_num = minimum_number(numbers_list)
max_num = maximum_number(numbers_list)
sum_of_nums = sum_numbers(numbers_list)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_of_nums}")