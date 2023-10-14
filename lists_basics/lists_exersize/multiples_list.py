factor = int(input())
count = int(input())
multiples_list = []

for multiply_by in range(1, count + 1):
    current_result = factor * multiply_by
    multiples_list.append(current_result)

print(multiples_list)