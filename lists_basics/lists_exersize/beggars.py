money_string = input().split(", ")
count_of_beggars = int(input())
money_digits = []

for current_money in money_string:
    money_digits.append(int(current_money))

final_sums = []
starting_index = 0

while starting_index < count_of_beggars:
    current_beggar_sum = 0
    for current_index in range(starting_index, len(money_digits), count_of_beggars):
        current_beggar_sum += money_digits[current_index]
    final_sums.append(current_beggar_sum)
    starting_index += 1

print(final_sums)