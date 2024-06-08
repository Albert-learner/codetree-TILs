N = int(input())

for i in range(N):
    print(' ' * (2 * i), end = '')

    for j in range(N - i, 0, -1):
        print(j, end = ' ')
    print()