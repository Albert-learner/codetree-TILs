n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            continue

        for x in range(i + 1, n):
            for y in range(j + 1, m):
                if grid[x][y] > grid[i][j]:
                    dp[x][y] = max(dp[x][y], dp[i][j] + 1)

max_cnts = 0
for i in range(n):
    for j in range(m):
        max_cnts = max(max_cnts, dp[i][j])

print(max_cnts)