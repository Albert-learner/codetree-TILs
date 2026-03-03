n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 30
adj = [[] for _ in range(n + 1)]
for a, b, d in edges:
    adj[a].append((b, d))
    adj[b].append((a, d))

dist = [INF] * (n + 1)
dist[n] = 0
pq = [(0, n)]

while pq:
    cur_d, u = heapq.heappop(pq)
    if cur_d != dist[u]:
        continue

    for v, w in adj[u]:
        nd = cur_d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(max(dist[1:]))