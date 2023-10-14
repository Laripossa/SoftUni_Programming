first_number = int(input())
second_number = int(input())
current_number = first_number

while current_number <= second_number:
    print(f'{chr(current_number)}', end=" ")
    current_number += 1