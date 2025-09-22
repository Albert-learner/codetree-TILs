n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def can_path(lo, hi):
    if not (lo <= grid[0][0] <= hi and lo <= grid[n - 1][n - 1] <= hi):
        return False

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not (lo <= grid[i][j] <= hi):
                dp[i][j] = False
                continue

            if i == 0 and j == 0:
                dp[i][j] = True
            else:
                from_up = dp[i - 1][j] if i > 0 else False
                from_left = dp[i][j - 1] if j > 0 else False
                dp[i][j] = from_up or from_left

    return dp[-1][-1]

vals = sorted({grid[i][j] for i in range(n) for j in range(n)})
k = len(vals)

ans = 10 ** 9
i = j = 0

while i < k and j < k:
    if can_path(vals[i], vals[j]):
        ans = min(ans, vals[j] - vals[i])
        i += 1
    else:
        j += 1

print(ans)