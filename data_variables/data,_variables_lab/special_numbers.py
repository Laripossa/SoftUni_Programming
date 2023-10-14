n = int(input())

for number in range(1,n + 1):
    current_number = str(number)
    digits_sum = 0
    for digit in current_number:
        digits_sum += int(digit)

    is_special = False
    if digits_sum in [5,7,11]:
        is_special = True
    print(f"{number} -> {is_special}")