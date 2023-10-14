def is_palindrome(some_number: str) -> bool:
    return some_number == some_number[::-1]


numbers_list = input().split(", ")
for number in numbers_list:
    print(is_palindrome(number))