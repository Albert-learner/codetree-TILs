n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for x, y in edges:
    graph[x].append(y)
    indegree[y] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

topo = []

while q:
    cur = q.popleft()
    topo.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

dp = [-1] * (n + 1)
nxt_node = [0] * (n + 1)

dp[n] = 1

for cur in reversed(topo):
    if cur == n:
        continue

    best_len = -1
    best_next = 0

    for nxt in graph[cur]:
        if dp[nxt] == -1:
            continue

        cand = dp[nxt] + 1

        if cand > best_len:
            best_len = cand
            best_next = nxt
        elif cand == best_len and nxt < best_next:
            best_next = nxt

    dp[cur] = best_len
    nxt_node[cur] = best_next

if dp[1] == -1:
    print(-1)
else:
    path = []
    cur = 1

    while cur != 0:
        path.append(cur)

        if cur == n:
            break

        cur = nxt_node[cur]

    print(dp[1])
    print(*path)