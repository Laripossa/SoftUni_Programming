group_size = int(input())
days_of_adventure = int(input())
day_count = 1
coins = 0

for day in range(days_of_adventure):
    if day_count % 10 == 0:
        group_size -= 2
    if day_count % 15 == 0:
        group_size += 5

    coins += 50
    coins -= 2 * group_size

    if day_count % 3 == 0:
        coins -= 3 * group_size
        if day_count % 5 == 0:
            coins -= 2 * group_size
    if day_count % 5 == 0:
        coins += 20 * group_size
    day_count += 1

coins_pp = int(coins / group_size)

print(f"{group_size} companions received {coins_pp} coins each.")

