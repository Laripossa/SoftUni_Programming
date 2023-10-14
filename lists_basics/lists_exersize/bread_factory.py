events = input().split("|")
energy = 100
coins = 100
gained_energy = 0
day_completed = True

for event in events:
    # event_items = event.split("-")
    # type_of_event = event_items[0]
    # event_coins = int(event_items[1])
    type_of_event, event_value = event.split("-")
    if type_of_event == "rest":
        current_energy = energy
        energy += int(event_value)
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
        # if energy + event_value > 100:
        #     gained_energy += event_value - abs(energy - event_value)
        #     energy = 100
        # else:
        #     energy += event_value
        #     gained_energy += event_value
    elif type_of_event == "order":
        if energy >= 30:
            energy -= 30
            coins += int(event_value)
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        ingredient = type_of_event
        if coins >= int(event_value):
            coins -= int(event_value)
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")