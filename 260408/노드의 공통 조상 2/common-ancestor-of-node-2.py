n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

LOG = (n).bit_length()

parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [0] * (n + 1)
visited = [False] * (n + 1)

stack = [1]
visited[1] = True
parent[0][1] = 0
depth[1] = 0

while stack:
    u = stack.pop()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[0][v] = u
            depth[v] = depth[u] + 1
            stack.append(v)

for j in range(1, LOG):
    for i in range(1, n + 1):
        parent[j][i] = parent[j - 1][parent[j - 1][i]]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for j in range(LOG):
        if diff & (1 << j):
            a = parent[j][a]

    if a == b:
        return a

    for j in range(LOG - 1, -1, -1):
        if parent[j][a] != parent[j][b]:
            a = parent[j][a]
            b = parent[j][b]

    return parent[0][a]

for a, b in queries:
    print(lca(a, b))