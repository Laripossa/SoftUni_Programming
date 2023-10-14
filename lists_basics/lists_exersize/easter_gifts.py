gifts_list = input().split()

while True:
    command = input().split()

    if command[0] == "No":
        break
    elif command[0] == "OutOfStock":
        current_gift = command[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == current_gift:
                gifts_list[i] = "None"
    elif command[0] == "Required":
        current_gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = current_gift
    elif command[0] == "JustInCase":
        current_gift = command[1]
        gifts_list[-1] = current_gift

# for gift in gifts_list:
#     if gift == "None":
#         gifts_list.remove(gift)
filtered = [gift for gift in gifts_list if gift != "None"]
print(" ".join(filtered))
