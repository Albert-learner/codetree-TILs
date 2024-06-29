N = int(input())
grids = [list(map(int, input().split())) for _ in range(N)]

coins = []
for i in range(N):
    for j in range(N - 2):
        coins.append(grids[i][j: j + 3].count(1))

print(max(coins))