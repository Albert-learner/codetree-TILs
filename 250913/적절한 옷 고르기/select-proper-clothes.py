N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
INF = -(10 ** 15)
avail = [[] for _ in range(M + 1)]
for i in range(N):
    for day in range(s[i], e[i] + 1):
        avail[day].append(i)

dp = [[INF] * N for _ in range(M + 1)]

for j in avail[1]:
    dp[1][j] = 0

for day in range(2, M + 1):
    for j in avail[day]:
        best = INF
        for k in avail[day - 1]:
            if dp[day - 1][k] == INF:
                continue
            cand = dp[day - 1][k] + abs(v[j] - v[k])
            if cand > best:
                best = cand
        dp[day][j] = best

ans = max(dp[M][j] for j in avail[M])
print(ans)