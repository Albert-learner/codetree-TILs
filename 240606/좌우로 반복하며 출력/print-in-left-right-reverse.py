N = int(input())

for i in range(1, N + 1):
    if i % 2 == 1:
        print(*[j for j in range(1, N + 1)], end = '')
    else:
        print(*[j for j in range(N, 0, -1)], end = '')