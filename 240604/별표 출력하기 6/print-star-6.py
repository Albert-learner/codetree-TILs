N = int(input())

size = 2 * N - 1
pattern = [[' ' for _ in range(size)] for _ in range(size)]

for i in range(N):
    for j in range(i, size - i):
        pattern[i][j] = '*'
        pattern[size - i - 1][j] = '*'

for row in pattern:
    print(' '.join(row))