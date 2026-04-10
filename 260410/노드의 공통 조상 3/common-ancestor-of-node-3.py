n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_nodes, to_nodes = zip(*edges)
from_nodes = list(from_nodes)
to_nodes = list(to_nodes)

q = int(input())

queries = [tuple(map(int, input().split())) for _ in range(q)]
a, b, c = zip(*queries)
a = list(a)
b = list(b)
c = list(c)

# Please write your code here.
import sys
from collections import deque

adj = [[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

LOG = (n).bit_length()

parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)

visited = [False] * (n + 1)
dq = deque([1])
visited[1] = True
parent[0][1] = 0
depth[1] = 0


while dq:
    u = dq.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            parent[0][v] = u
            depth[v] = depth[u] + 1
            dq.append(v)

for k in range(1, LOG):
    for v in range(1, n + 1):
        parent[k][v] = parent[k - 1][parent[k - 1][v]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]
    bit = 0
    while diff:
        if diff & 1:
            u = parent[bit][u]
        diff >>= 1
        bit += 1

    if u == v:
        return u

    for k in range(LOG - 1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]

answer = []
for x, y, z in queries:
    ans = lca(lca(x, y), z)
    answer.append(str(ans))

print("\n".join(answer))