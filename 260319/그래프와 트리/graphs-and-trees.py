n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
tree_cnts = 0

for start in range(1, n + 1):
    if visited[start]:
        continue

    queue = deque([start])
    visited[start] = True

    vertex_cnts = 0
    degree_sum = 0

    while queue:
        cur = queue.popleft()
        vertex_cnts += 1
        degree_sum += len(graph[cur])

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    edge_cnts = degree_sum // 2

    if edge_cnts == vertex_cnts - 1:
        tree_cnts += 1

print(tree_cnts)