number_of_str = int(input())
special_word = input()
full_list = []
special_list = []

for _ in range(number_of_str):
    current_string = input()
    full_list.append(current_string)
    if special_word in current_string:
        special_list.append(current_string)

print(full_list)
print(special_list)