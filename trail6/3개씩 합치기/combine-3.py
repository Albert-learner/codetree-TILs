n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
INF = 10 ** 18

dp = [[0] * n for _ in range(n)]

for length in range(2, n):
    for l in range(n - length):
        r = l + length
        dp[l][r] = INF

        for k in range(l + 1, r):
            dp[l][r] = min(
                dp[l][r],
                dp[l][k] + dp[k][r] + arr[l] * arr[k] * arr[r] 
            )

print(dp[0][n - 1])