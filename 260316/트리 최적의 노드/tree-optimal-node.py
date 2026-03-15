n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

def BFS(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    far_node = start
    far_dist = 0
    for i in range(1, n + 1):
        if dist[i] > far_dist:
            far_dist = dist[i]
            far_node = i

    return far_node, far_dist

u, _ = BFS(1)
v, diameter = BFS(u)

print((diameter + 1) // 2)