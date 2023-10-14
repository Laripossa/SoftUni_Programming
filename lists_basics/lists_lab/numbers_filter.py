amount = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(amount):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)