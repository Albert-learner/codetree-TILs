n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

adj = [[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

INF = 10 ** 15

dp = [[0, 0, 0] for _ in range(n + 1)]
def DFS(u, parent):
    dp[u][0] = 1
    dp[u][1] = INF
    dp[u][2] = 0

    children = []
    for v in adj[u]:
        if v == parent:
            continue

        DFS(v, u)
        children.append(v)

    if not children:
        dp[u][0] = 1
        dp[u][1] = INF
        dp[u][2] = 0
        return

    dp0 = 1
    for v in children:
        dp0 += min(dp[v][0], dp[v][1], dp[v][2])
    dp[u][0] = dp0

    dp2 = 0
    for v in children:
        dp2 += min(dp[v][0], dp[v][1])
    dp[u][2] = dp2

    total = 0
    extra = INF
    for v in children:
        best = min(dp[v][0], dp[v][1])
        total += best
        extra = min(extra, dp[v][0] - best)

    dp[u][1] = total + extra

DFS(1, 0)

print(min(dp[1][0], dp[1][1]))