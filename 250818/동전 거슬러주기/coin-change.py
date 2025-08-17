N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.
INF = 10000
dp = [INF] * (M + 1)
dp[0] = 0

for i in range(1, M + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[M] if dp[M] != INF else -1)