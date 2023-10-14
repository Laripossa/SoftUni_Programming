numbers_string_list = input().split()
numbers_to_remove = int(input())
numbers_int_list = []

for number in numbers_string_list:
    current_number = int(number)
    numbers_int_list.append(current_number)

for removals in range(numbers_to_remove):
    numbers_int_list.remove(min(numbers_int_list))

print(", ".join(map(str, numbers_int_list)))