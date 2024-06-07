a, b = map(int, input().split())

for j in range(2, 9, 2):
    for i in range(b, a - 1, -1):
        if i == a:
            print(f"{i} * {j} = {i * j}")
        else:
            print(f"{i} * {j} = {i * j} /", end = ' ')