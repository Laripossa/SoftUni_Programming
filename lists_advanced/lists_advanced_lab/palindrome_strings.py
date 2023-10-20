words_list = input().split()
wanted_palindrome = input()

found_palind = [word for word in words_list if word == wanted_palindrome]
found = len(found_palind)

all_palind = [word for word in words_list if word == word[::-1]]
print(all_palind)
print(f"Found palindrome {found} times")