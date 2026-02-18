n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import sys
import heapq

INF = 10 ** 18

graph = [[] for _ in range(n + 1)]
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

dist = [INF] * (n + 1)
dist[k] = 0
pq = [(0, k)]

while pq:
    cur_d, u = heapq.heappop(pq)
    if cur_d != dist[u]:
        continue

    for v, w in graph[u]:
        nd = cur_d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

out = []
for i in range(1, n + 1):
    out.append(str(dist[i] if dist[i] != INF else -1))
print("\n".join(out))