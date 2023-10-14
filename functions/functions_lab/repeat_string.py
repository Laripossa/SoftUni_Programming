def repeated_string(string, times):
    for time in range(times):
        print(string, end="")


string = input()
times = int(input())
repeated_string(string, times)