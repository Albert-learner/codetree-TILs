n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
INT_MAX = 10 ** 18

merged = [
    [0] * (n + 1) 
    for _ in range(n + 1)
]

dp = [
    [0] * (n + 1) 
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    merged[i][i] = arr[i]
    for j in range(i + 1, n + 1):
        merged[i][j] = merged[i][j - 1] + arr[j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = INT_MAX

for i in range(1, n + 1):
    dp[i][i] = 0

for gap in range(2, n + 1):
    for i in range(1, n - gap + 2):
        j = i + gap - 1

        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + merged[i][k] + merged[k + 1][j]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][n])

