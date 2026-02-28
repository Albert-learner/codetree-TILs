n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 10 ** 30

adj = [[] for _ in range(n + 1)]
for idx, (u, v, w) in enumerate(edges):
    adj[u].append((v, w))
    adj[v].append((u, w))

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

dist1 = dijkstra(1)
distN = dijkstra(n)
D = dist1[n]

sp_out = [[] for _ in range(n + 1)]  
dag_edges = [] 

for idx, (u, v, w) in enumerate(edges):
    if dist1[u] + w == dist1[v] and dist1[u] + w + distN[v] == D:
        sp_out[u].append((v, idx))
        dag_edges.append((u, v, idx))
    elif dist1[v] + w == dist1[u] and dist1[v] + w + distN[u] == D:
        sp_out[v].append((u, idx))
        dag_edges.append((v, u, idx))

nodes = list(range(1, n + 1))
nodes.sort(key=lambda x: dist1[x])

cnt1 = [0] * (n + 1)
cnt1[1] = 1
for u in nodes:
    if cnt1[u] == 0:
        continue
    for v, _ in sp_out[u]:
        cnt1[v] += cnt1[u]

total = cnt1[n] 

cnt2 = [0] * (n + 1)
cnt2[n] = 1
for u in reversed(nodes):
    for v, _ in sp_out[u]:
        cnt2[u] += cnt2[v]

answer = 0
for u, v, _ in dag_edges:
    if cnt1[u] * cnt2[v] == total:
        answer += 1

print(answer)