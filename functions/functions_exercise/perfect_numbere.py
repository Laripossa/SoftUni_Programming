def is_perfect(num: int) -> str:
    divisors_sum = 0
    for current_divisor in range(1, num):
        if num % current_divisor == 0:
            divisors_sum += current_divisor

    if divisors_sum == num:
        return "We have a perfect number!"
    return "It's not so perfect."
        

number = int(input())
print(is_perfect(number))