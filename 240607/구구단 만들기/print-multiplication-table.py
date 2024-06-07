a, b = map(int, input().split())

for num in range(1, 10):
    if a != b:
        for n in range(b, a - 1, -2):
            if n == a:
                print(f"{n} * {num} = {n * num}")
            else:
                print(f"{n} * {num} = {n * num} /", end = ' ')
    else:
        print(f"{a} * {num} = {a * num}")