fires_to_put_out = input().split("#")
available_water = int(input())
total_effort = 0
total_fire = 0
print("Cells:")

for fire in fires_to_put_out:
    type_of_fire, water_needed_as_str = fire.split(" = ")
    water_needed = int(water_needed_as_str)
    if type_of_fire == "High" and 81 <= water_needed <= 125:
        if available_water >= water_needed:
            available_water -= water_needed
            total_effort += 0.25 * water_needed
            total_fire += water_needed
            print(f" - {water_needed}")
    elif type_of_fire == "Medium" and 51 <= water_needed <= 80:
        if available_water >= water_needed:
            available_water -= water_needed
            total_effort += 0.25 * water_needed
            total_fire += water_needed
            print(f" - {water_needed}")
    elif type_of_fire == "Low" and 1 <= water_needed <= 50:
        if available_water >= water_needed:
            available_water -= water_needed
            total_effort += 0.25 * water_needed
            total_fire += water_needed
            print(f" - {water_needed}")
    else:
        continue

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")