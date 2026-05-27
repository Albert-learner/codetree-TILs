n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b, w in edges:
    graph[a].append((b, w))
    reverse_graph[b].append((a, w))
    indegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

topo = []
while q:
    cur = q.popleft()
    topo.append(cur)

    for nxt, w in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

dist = [-1] * (n + 1)
dist[1] = 0

for cur in topo:
    if dist[cur] == -1:
        continue

    for nxt, w in graph[cur]:
        if dist[nxt] < dist[cur] + w:
            dist[nxt] = dist[cur] + w

visited_node = [False] * (n + 1)
visited_edge = set()

q = deque([n])
visited_node[n] = True

while q:
    cur = q.popleft()

    for prev, w in reverse_graph[cur]:

        if dist[prev] + w == dist[cur]:
            visited_edge.add((prev, cur))

            if not visited_node[prev]:
                visited_node[prev] = True
                q.append(prev)

print(dist[n], len(visited_edge))