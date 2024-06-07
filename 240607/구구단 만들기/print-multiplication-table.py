a, b = map(int, input().split())

for num in range(1, 10):
    for n in range(b, a - 1, -2):
        if n == 2:
            print(f"{n} * {num} = {n * num}")
        else:
            print(f"{n} * {num} = {n * num} /", end = ' ')