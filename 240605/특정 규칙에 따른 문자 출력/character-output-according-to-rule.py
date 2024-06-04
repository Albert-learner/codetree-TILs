N = int(input())

grid = [[' ' for _ in range(N)] for _ in range(2 * N - 1)]

for i in range(N):
    x, y = 2 * N - 1 - i, i
    for j in range(N):
        nx, ny = x - 1, y
        grid[nx][ny] = '@'
        x, y = nx, ny

for i in range(2 * N - 1):
    for j in range(N):
        print(grid[i][j], end = ' ')
    print()