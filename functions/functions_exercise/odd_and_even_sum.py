def odd_even_sums(some_number: str):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)
    return sum_of_even_digits, sum_of_odd_digits


number = input()
sum_of_even, sum_of_odd = odd_even_sums(number)
print(f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}")