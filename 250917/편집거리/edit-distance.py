A = input()
B = input()

# Please write your code here.
n, m = len(A), len(B)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i

for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    ai = A[i - 1]
    for j in range(1, m + 1):
        bj = B[j - 1]
        cost = 0 if ai == bj else 1
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

print(dp[n][m])