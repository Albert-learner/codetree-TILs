n, m = map(int, input().split())
v1, v2, e = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 18

adj = [[] for _ in range(n + 1)]
for a, b, c in edges:
    adj[a].append((b, c))
    adj[b].append((a, c))

def dijkstra(start: int):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

dist1 = dijkstra(v1)
dist2 = dijkstra(v2)
distE = dijkstra(e)

ans = INF
for k in range(1, n + 1):
    if dist1[k] == INF or dist2[k] == INF or distE[k] == INF:
        continue
    ans = min(ans, dist1[k] + dist2[k] + distE[k])

print(-1 if ans == INF else ans)