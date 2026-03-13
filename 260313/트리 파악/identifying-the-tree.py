n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n + 1)
parent = [0] * (n + 1)

queue = deque([1])
parent[1] = -1

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        parent[nxt] = cur
        depth[nxt] = depth[cur] + 1
        queue.append(nxt)

total_moves = 0
for node in range(2, n + 1):
    if len(graph[node]) == 1:
        total_moves += depth[node]

print(1 if total_moves % 2 == 1 else 0)