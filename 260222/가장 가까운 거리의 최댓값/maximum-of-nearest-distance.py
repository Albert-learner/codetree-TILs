n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 30

g = [[] for _ in range(n + 1)]
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))

dist = [INF] * (n + 1)
pq = []
for src in (a, b, c):
    dist[src] = 0
    heapq.heappush(pq, (0, src))

while pq:
    d, x = heapq.heappop(pq)
    if d != dist[x]:
        continue
    for nx, w in g[x]:
        nd = d + w
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(pq, (nd, nx))

ans = 0
for i in range(1, n + 1):
    if dist[i] > ans:
        ans = dist[i]

print(ans)