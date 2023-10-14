lines = int(input())
left_capacity = 255
litres_in_tank = 0

for times in range(lines):
    pour_in = int(input())
    if left_capacity - pour_in < 0:
        print("Insufficient capacity!")
        continue
    if left_capacity > 0:
        litres_in_tank += pour_in
        left_capacity -= pour_in

print(litres_in_tank)

