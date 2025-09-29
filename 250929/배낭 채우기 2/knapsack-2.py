N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [0] * (M + 1)

for wi, vi in zip(w, v):
    for cap in range(wi, M + 1):
        dp[cap] = max(dp[cap], dp[cap - wi] + vi)

print(dp[M])