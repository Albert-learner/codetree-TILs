n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

MOD = 1000000007

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for x, y in edges:
    graph[x].append(y)
    indegree[y] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

dp = [0] * (n + 1)
dp[1] = 1

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        dp[nxt] = (dp[nxt] + dp[cur]) % MOD
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(dp[n])