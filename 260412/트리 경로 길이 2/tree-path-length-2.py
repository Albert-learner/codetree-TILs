n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

q = int(input())

queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
import sys
from collections import deque

adj = [[] for _ in range(n + 1)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

LOG = (n).bit_length()
parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)
dist = [0] * (n + 1)

visited = [False] * (n + 1)
dq = deque([1])
visited[1] = True

while dq:
    u = dq.popleft()
    for v, w in adj[u]:
        if not visited[v]:
            visited[v] = True
            depth[v] = depth[u] + 1
            parent[0][v] = u
            dist[v] = dist[u] + w
            dq.append(v)

for k in range(1, LOG):
    for v in range(1, n + 1):
        parent[k][v] = parent[k - 1][parent[k - 1][v]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]
    for k in range(LOG):
        if diff & (1 << k):
            u = parent[k][u]

    if u == v:
        return u

    for k in range(LOG - 1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]

answer = []
for u, v in queries:
    w = lca(u, v)
    total = dist[u] + dist[v] - 2 * dist[w]
    answer.append(str(total))

print("\n".join(answer))