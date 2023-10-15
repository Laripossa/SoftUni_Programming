numbers_list = list(map(int, input().split(", ")))
zeroes_count = 0
new_list = []

for current_number in numbers_list:
    if current_number == 0:
        zeroes_count += 1
    else:
        new_list.append(current_number)

for zeroes in range(zeroes_count):
    new_list.append(0)

print(new_list)