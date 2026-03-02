n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 30

adj = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]

for u, v, wA, wB in edges:
    adj[u].append((v, wA, wB))
    rev[v].append((u, wA, wB))

def dijkstra_to_N(use_A: bool):
    dist = [INF] * (n + 1)
    dist[n] = 0
    pq = [(0, n)]
    while pq:
        d, x = heapq.heappop(pq)
        if d != dist[x]:
            continue
        for prev, wA, wB in rev[x]:
            w = wA if use_A else wB
            nd = d + w
            if nd < dist[prev]:
                dist[prev] = nd
                heapq.heappush(pq, (nd, prev))
    return dist

distA = dijkstra_to_N(True)
distB = dijkstra_to_N(False)

reachable = [d < INF for d in distA]

warnDist = [INF] * (n + 1)
warnDist[1] = 0
pq = [(0, 1)]

while pq:
    wcnt, u = heapq.heappop(pq)
    if wcnt != warnDist[u]:
        continue
    if u == n:
        break

    if not reachable[u]:
        continue

    for v, wA, wB in adj[u]:
        if not reachable[v]:
            continue  

        wa = 1 if distA[u] != wA + distA[v] else 0
        wb = 1 if distB[u] != wB + distB[v] else 0

        cost = wa + wb
        nw = wcnt + cost
        if nw < warnDist[v]:
            warnDist[v] = nw
            heapq.heappush(pq, (nw, v))

print(warnDist[n])