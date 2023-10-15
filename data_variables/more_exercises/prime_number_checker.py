from math import sqrt


def isprime(number: int) -> bool:
    a = 2
    while a <= sqrt(number):
        if number % a < 1:
            return False
        a = a + 1
    return True


input_number = int(input())
print(isprime(input_number))
