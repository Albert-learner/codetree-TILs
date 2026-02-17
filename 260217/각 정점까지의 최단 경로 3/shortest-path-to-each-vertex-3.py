n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

graph = [[] for _ in range(n + 1)]
for u, v, w in edges:
    graph[u].append((v, w))

INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]
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
for i in range(2, n + 1):
    out.append(str(dist[i] if dist[i] != INF else -1))

print("\n".join(out))