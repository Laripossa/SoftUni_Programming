# Read the sequences of numbers and string
numbers_list = input().split()
initial_text = input()
# Initialize two empty lists
work_text = initial_text
final_message = []
digit_sums = []

# Calculate the sums of the digits of each number
for current_number in numbers_list:
    sum_of_number = 0
    for digit in current_number:
        sum_of_number += int(digit)
    #     Add the sums to the list
    digit_sums.append(sum_of_number)

# Loop trough the list of sums to find the desired characters
for current_sum in digit_sums:
    # Ensure the index is valid
    index = current_sum % len(work_text)
    # Append the desired character
    final_message.append(work_text[index])
    # Remove the added character from the text
    work_text = work_text[:index] + work_text[index + 1:]


print("".join(final_message))
