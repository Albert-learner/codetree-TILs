n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys

INF = sys.maxsize

dp = [[INF] * n for _ in range(1 << n)]

dp[1][0] = 0

for mask in range(1 << n):
    for cur in range(n):
        if dp[mask][cur] == INF:
            continue

        if ((mask >> cur) & 1) == 0:
            continue

        for nxt in range(n):
            if (mask >> nxt) & 1:
                continue

            if dist[cur][nxt] == 0:
                continue

            next_mask = mask | (1 << nxt)
            dp[next_mask][nxt] = min(
                dp[next_mask][nxt],
                dp[mask][cur] + dist[cur][nxt]
            )

full = (1 << n) - 1
answer = INF

for last in range(1, n):
    if dist[last][0] == 0:
        continue

    answer = min(answer, dp[full][last] + dist[last][0])

print(answer)
