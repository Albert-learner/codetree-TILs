N, M = map(int, input().split())
red1, red2 = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Please write your code here.
import heapq

INF = 10 ** 30

adj = [[] for _ in range(N + 1)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

def dijkstra(start: int):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, x = heapq.heappop(pq)
        if d != dist[x]:
            continue
        for nx, w in adj[x]:
            nd = d + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))
    return dist

dist1 = dijkstra(red1)
dist2 = dijkstra(red2)

d12 = dist1[red2]
if d12 >= INF:
    print(-1)
    sys.exit(0)

ans = INF
for s in range(1, N + 1):
    if s == red1 or s == red2:
        continue  
    if dist1[s] >= INF or dist2[s] >= INF:
        continue 
    ans = min(ans, dist1[s] + dist2[s] + d12)

print(-1 if ans >= INF else ans)