n, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
depth = [0] * (n + 1)
order = []

stack = [r]
parent[r] = -1

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        parent[nxt] = cur
        depth[nxt] = depth[cur] + 1
        stack.append(nxt)

children = [[] for _ in range(n + 1)]
for v in range(1, n + 1):
    if parent[v] > 0:
        children[parent[v]].append(v)

central = -1
cur = r
while True:
    if len(children[cur]) >= 2:
        central = cur
        break
    
    if len(children[cur]) == 0:
        central = cur
        break

    cur = children[cur][0]

subtree_size = [1] * (n + 1)
for cur in reversed(order):
    for ch in children[cur]:
        subtree_size[cur] += subtree_size[ch]

sizes = []
for nxt in graph[central]:
    if parent[nxt] == central:
        sizes.append(subtree_size[nxt])
    else:
        sizes.append(n - subtree_size[central])

print(max(sizes) - min(sizes))