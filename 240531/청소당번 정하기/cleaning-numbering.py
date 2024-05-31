N = int(input())

a, b, c = 0, 0, 0
for day in range(1, N + 1):
    if day % 12 == 0:
        c += 1
    elif day % 3 == 0:
        b += 1
    elif day % 2 == 0:
        a += 1

print(a, b, c)