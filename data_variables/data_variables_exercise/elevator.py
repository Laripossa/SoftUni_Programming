number_of_people = int(input())
capacity = int(input())

total_courses = 0
full_courses = number_of_people // capacity
total_courses += full_courses
remainder = number_of_people % capacity

if remainder != 0:
    total_courses += 1

print(total_courses)