n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[float("inf")] * n for _ in range(n)]
dp[0][n - 1] = grid[0][n - 1]

for i in range(n):
    for j in range(n - 1, -1, -1):
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
        if j < n - 1:
            dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j])

print(dp[n - 1][0])