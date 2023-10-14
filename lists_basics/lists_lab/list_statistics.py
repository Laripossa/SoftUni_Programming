amount_of_numbers = int(input())
positives = []
negatives = []

for digits in range(amount_of_numbers):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

print(positives)
print(negatives)
print("Count of positives:", len(positives))
print("Sum of negatives:", len(negatives))