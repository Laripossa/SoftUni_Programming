def characters_between(first: str, second: str) -> list:
    characters = []
    for current_character in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_character))
    return characters


first_character = input()
second_character = input()
result = characters_between(first_character, second_character)
print(" ".join(result))