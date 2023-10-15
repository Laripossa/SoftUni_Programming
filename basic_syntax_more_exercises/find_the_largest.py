initial_number_as_str = input()
digits_list = []

for digit in initial_number_as_str:
    current_digit = int(digit)
    digits_list.append(current_digit)

digits_list.sort(reverse=True)

for number in digits_list:
    print(number, end="")
