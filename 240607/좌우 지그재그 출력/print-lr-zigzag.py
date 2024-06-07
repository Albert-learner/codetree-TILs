N = int(input())

for i in range(1, N + 1):
    if i % 2 == 1:
        for j in range(N * i - (N - 1), N * i + 1):
            print(j, end = ' ')
    else:
        for j in range(N * i, N * i - N, -1):
            print(j, end = ' ')
    print()