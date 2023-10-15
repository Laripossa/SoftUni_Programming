number_of_lines = int(input())

opening = 0
closing = 0
is_balanced = True

for lines in range(number_of_lines):
    random = input()
    if random == "(":
        opening += 1
        is_balanced = False
        if closing == opening - 2:
            is_balanced = False
            break
    elif random == ")":
        if is_balanced:
            is_balanced = False
            break
        else:
            closing += 1
            is_balanced = True

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

