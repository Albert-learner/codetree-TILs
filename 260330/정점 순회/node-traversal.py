n, s, d = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

if n == 1:
    print(0)
    sys.exit()

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
order = []
stack = [s]
parent[s] = -1

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        parent[nxt] = cur
        stack.append(nxt)

max_depth = [0] * (n + 1)

for cur in reversed(order):
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        max_depth[cur] = max(max_depth[cur], max_depth[nxt] + 1)

need_edges = 0
for node in range(1, n + 1):
    if node == s:
        continue

    if max_depth[node] >= d:
        need_edges += 1

print(need_edges * 2)