N = int(input())

cnts = 1
grid = [[] * N for _ in range(N)]
for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            grid[i].append(cnts + j)
        cnts = grid[i][-1] + 2
    else:
        for j in range(0, N * 2, 2):
            grid[i].append(cnts + j)
        cnts = grid[i][-1] + 1

for row in grid:
    print(*row)