initial_string = input()
vowels_list = ['a', 'o', 'u', 'e', 'i']

without_vowels = [char for char in initial_string if char.lower() not in vowels_list]
print(''.join(without_vowels))