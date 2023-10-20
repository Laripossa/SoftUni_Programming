wagons_count = int(input())
train = [0 for wagon in range(wagons_count)]
command = input()

while command != "End":
    command_as_list = command.split()
    if command_as_list[0] == "add":
        last_wagon = len(train) - 1
        people = int(command_as_list[1])
        train[last_wagon] += people
    elif command_as_list[0] == "insert":
        people = int(command_as_list[2])
        wagon = int(command_as_list[1])
        train[wagon] += people
    elif command_as_list[0] == "leave":
        people = int(command_as_list[2])
        wagon = int(command_as_list[1])
        train[wagon] -= people

    command = input()

print(train)
