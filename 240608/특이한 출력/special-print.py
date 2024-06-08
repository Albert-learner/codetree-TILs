N = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if (i + j) % 4 == 0:
            print(f"({i}, {j})")
        else:
            print(f"({i}, {j})", end = ' ')