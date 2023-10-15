key = int(input())
lines_following = int(input())
message = []

for line in range(lines_following):
    letter = input()
    new_char_number = ord(letter) + key
    new_char = chr(new_char_number)
    message.append(new_char)

print("".join(message))