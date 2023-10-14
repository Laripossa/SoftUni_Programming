def is_valid(some_pass: str) -> list:
    message = []
    if len(some_pass) < 6 or len(some_pass) > 10:
        message.append("Password must be between 6 and 10 characters")
    if not some_pass.isalnum():
        message.append("Password must consist only of letters and digits")
    digits_count = 0
    for char in some_pass:
        if char.isdigit():
            digits_count += 1
    if digits_count < 2:
        message.append("Password must have at least 2 digits")
    return message


password = input()
validated_password = is_valid(password)
if len(validated_password) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_password))