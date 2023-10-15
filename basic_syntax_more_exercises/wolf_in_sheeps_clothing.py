animals_list = input().split(", ")

reversed_animal_list = animals_list[::-1]

if reversed_animal_list[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for index in range(len(reversed_animal_list)):
        if animals_list[index] == "wolf":
            print(f"Oi! Sheep number {len(animals_list) - (1 + index)}! You are about to be eaten by a wolf!")


