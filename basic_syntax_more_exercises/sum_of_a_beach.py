received_word = input()
letters_in_the_word = []
sand = ["S", "a", "n", "d"]
water = ["W", "a", "t", "e", "r"]
fish = ["F", "i", "s", "h"]
sun = ["S", "u", "n"]
times_count = 0

for char in received_word:
    letters_in_the_word.append(char)

current_letter = letters_in_the_word

for sand_char in letters_in_the_word:
    if sand_char in sand:
        sand.remove(sand_char)

    if not sand:
        times_count += 1
        letters_in_the_word = current_letter
        break

for water_char in letters_in_the_word:
    if water_char in water:
        water.remove(water_char)

    if not water:
        times_count += 1
        letters_in_the_word = current_letter
        break

for fish_char in letters_in_the_word:
    if fish_char in fish:
        fish.remove(fish_char)

    if not fish:
        times_count += 1
        letters_in_the_word = current_letter
        break

for sun_char in letters_in_the_word:
    if sun_char in sun:
        sun.remove(sun_char)

    if not sun:
        times_count += 1
        letters_in_the_word = current_letter
        break

print(times_count)

