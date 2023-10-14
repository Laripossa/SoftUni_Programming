# year = int(input())
# is_happy = False
#
# while not is_happy:
#     year += 1
#     is_happy = True
#     for digit in str(year):
#         if str(year).count(digit) != 1:
#             is_happy = False
#             break
#
# print(year)

#

year = int(input())
is_happy = False

while not is_happy:
    year_as_str = str(year)
    set_year = set(year_as_str)
    length = len(year_as_str)
    if len(set_year) != length:
        year += 1
    else:
        is_happy = True

print(set_year)
print(year)