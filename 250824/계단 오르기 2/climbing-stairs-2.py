n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
NEG = -10 ** 18
dp = [[NEG] * 4 for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n + 1):
    for k in range(4):
        if dp[i][k] == NEG:
            continue

        if k < 3 and i + 1 <= n:
            dp[i + 1][k + 1] = max(dp[i + 1][k + 1], dp[i][k] + coin[i + 1])

        if i + 2 <= n:
            dp[i + 2][k] = max(dp[i + 2][k], dp[i][k] + coin[i + 2])

print(max(dp[n]))