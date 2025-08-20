N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
dp = [0] * (M + 1)
for i in range(1, M + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = max(dp[i], dp[i - coin] + 1)

print(dp[M] if dp[M] != 0 else -1)