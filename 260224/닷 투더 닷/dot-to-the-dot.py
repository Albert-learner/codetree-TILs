n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

adj = [[] for _ in range(n + 1)]
c_values = set()
for u, v, L, C in edges:
    adj[u].append((v, L, C))
    adj[v].append((u, L, C))
    c_values.add(C)

INF = 10 ** 30

def dijkstra(min_c):
    dist = [INF] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        if u == n:
            return d
        for v, w, c in adj[u]:
            if c < min_c:
                continue
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return INF

best_num = None  
best_den = None  

for A in c_values:
    B = dijkstra(A)
    if B >= INF:
        continue

    num = B * A + x
    den = A

    if best_num is None:
        best_num, best_den = num, den
    else:
        if num * best_den < best_num * den:
            best_num, best_den = num, den

print(best_num // best_den)
