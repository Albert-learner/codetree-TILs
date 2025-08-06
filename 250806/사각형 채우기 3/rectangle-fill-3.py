n = int(input())

# Please write your code here.
dp = [0] * (n + 1)
dp[0] = 1
if n >= 1:
    dp[1] = 2

for i in range(2, n + 1):
    dp[i] = 2 * dp[i - 1] + 3 * dp[i - 2]
    for j in range(i - 3, -1, -1):
        dp[i] = dp[i] + 2 * dp[j]


print(dp[n] % 1000000007)