n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return False

    parent[fb] = fa
    return True

edges.sort(key = lambda x: x[2])
mst_weight = 0
mst_adj = [[] for _ in range(n + 1)]
cnt = 0

for u, v, w in edges:
    if union(u, v):
        mst_weight += w
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))
        cnt += 1

        if cnt == n - 1:
            break

def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    far_node = start
    max_dist = 0

    while q:
        u = q.popleft()

        if dist[u] > max_dist:
            max_dist = dist[u]
            far_node = u

        for v, w in mst_adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                q.append(v)

    return far_node, max_dist

x, _ = bfs(1)
y, diameter = bfs(x)

print(mst_weight)
print(diameter)