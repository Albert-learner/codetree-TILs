n = int(input())

# Please write your code here.
dp = [0] * 1000
dp[0], dp[1], dp[2] = 1, 2, 3

for i in range(3, n):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n - 1] % 10007)