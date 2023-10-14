def sorting(some_list: list) -> list:
    sorted_list = sorted(some_list)
    return sorted_list


numbers_list = list(map(int, input().split()))
result = sorting(numbers_list)
print(result)
