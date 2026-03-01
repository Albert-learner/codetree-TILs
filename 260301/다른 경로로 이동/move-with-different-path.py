n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 30

g = [[] for _ in range(n + 1)]
for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))

def dijkstra(start, banned=None):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if banned is not None:
                a, b = (u, v) if u < v else (v, u)
                if (a, b) in banned:
                    continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

dist1 = dijkstra(1)
distN = dijkstra(n)
best = dist1[n]

banned_edges = set()
cur = 1
while cur != n:
    nxt_choice = None
    for nxt, w in g[cur]:
        if dist1[cur] + w == dist1[nxt] and dist1[cur] + w + distN[nxt] == best:
            if nxt_choice is None or nxt < nxt_choice:
                nxt_choice = nxt
                w_choice = w
    a, b = (cur, nxt_choice) if cur < nxt_choice else (nxt_choice, cur)
    banned_edges.add((a, b))
    cur = nxt_choice

distB = dijkstra(1, banned=banned_edges)
print(-1 if distB[n] >= INF else distB[n])