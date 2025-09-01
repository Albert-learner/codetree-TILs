n = int(input())
red = [0]
blue = [0]

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
dp = [[0] * (n + 1) for _ in range(2 * n + 1)]

for i in range(1, 2 * n + 1):
    dp[i][0] = dp[i - 1][0] + blue[i]

for i in range(1, 2 * n + 1):
    for j in range(1, n + 1):
        if i < j:
            continue

        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + red[i]
            continue

        dp[i][j] = max(dp[i - 1][j - 1] + red[i], dp[i - 1][j] + blue[i])

print(dp[2 * n][n])