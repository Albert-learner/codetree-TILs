n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())

# Please write your code here.
import heapq

INF = 10 ** 30
g = [[] for _ in range(n + 1)]
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))

dist = [INF] * (n + 1)
dist[A] = 0

pq = [(0, A)]
while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    if u == B:  
        break
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[B])