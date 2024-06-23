input_str = input()

firsts, seconds = 0, 0
for i in range(len(input_str) - 1):
    if input_str[i:i + 2] == "ee":
        firsts += 1
    elif input_str[i:i + 2] == "eb":
        seconds += 1

print(firsts, seconds)