# Please write your code here.
import heapq

INF = 10**30

def dijkstra(start, adj, n):
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

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

A, B = map(int, input().split())

distA = dijkstra(A, adj, n)
distB = dijkstra(B, adj, n)

if distA[B] >= INF:
    print(-1)
    print()
    sys.exit(0)

path = [A]
u = A
target = distA[B]

while u != B:
    best_v = None
    best_w = None
    du = distA[u]
    for v, w in adj[u]:
        if du + w + distB[v] == target:
            if best_v is None or v < best_v:
                best_v = v
                best_w = w

    if best_v is None:
        break

    u = best_v
    path.append(u)

print(distA[B])
print(*path)