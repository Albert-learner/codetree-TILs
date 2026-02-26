n, m, x = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 18

graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for u, v, w in edges:
    graph[u].append((v, w))
    rev_graph[v].append((u, w))

def dijkstra(start, g):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  

    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d != dist[u]:
            continue

        for v, w in g[u]:
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

dist_from_x = dijkstra(x, graph)
dist_to_x = dijkstra(x, rev_graph)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dist_to_x[i] + dist_from_x[i])

print(ans)