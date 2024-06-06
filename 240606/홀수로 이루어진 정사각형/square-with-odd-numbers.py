N = int(input())

for i in range(0, 2 * N, 2):
    for j in range(11, N * 2 - 1 + 11, 2):
        print(i + j, end = ' ')
    print()