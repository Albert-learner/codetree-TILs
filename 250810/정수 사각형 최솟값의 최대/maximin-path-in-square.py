n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
NEG = -10 ** 18
dp = [[NEG] * n for _ in range(n)]
dp[0][0] = grid[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        best = NEG
        if i > 0:
            best = max(best, min(dp[i - 1][j], grid[i][j]))
        if j > 0:
            best = max(best, min(dp[i][j - 1], grid[i][j]))
        dp[i][j] = best

print(dp[n - 1][n - 1])