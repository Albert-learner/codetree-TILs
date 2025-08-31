n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
INF = 10 ** 9
dp = [INF] * n
dp[0] = 0

for i in range(n):
    if dp[i] == INF:
        continue

    for step in range(1, num[i] + 1):
        ni = i + step
        if ni < n:
            dp[ni] = min(dp[ni], dp[i] + 1)

print(dp[-1] if dp[-1] != INF else -1)