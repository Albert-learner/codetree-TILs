N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [0] * (M + 1)

for i in range(N):
    wi, vi = w[i], v[i]
    for cap in range(M, wi - 1, -1):
        dp[cap] = max(dp[cap], dp[cap - wi] + vi)

print(dp[M])