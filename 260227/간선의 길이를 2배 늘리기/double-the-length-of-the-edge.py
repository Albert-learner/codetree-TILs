# Please write your code here.
import sys
import heapq

INF = 10 ** 30

n, m = map(int, input().split())
edges = []
adj = [[] for _ in range(n + 1)]

for eid in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    adj[u].append((v, w, eid))
    adj[v].append((u, w, eid))

def dijkstra(double_eid=-1, need_parent=False):
    dist = [INF] * (n + 1)
    parent_node = [-1] * (n + 1)
    parent_edge = [-1] * (n + 1)

    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        d, x = heapq.heappop(pq)
        if d != dist[x]:
            continue
        for nx, w, eid in adj[x]:
            ww = w * 2 if eid == double_eid else w
            nd = d + ww

            if nd < dist[nx]:
                dist[nx] = nd
                if need_parent:
                    parent_node[nx] = x
                    parent_edge[nx] = eid
                heapq.heappush(pq, (nd, nx))
            elif need_parent and nd == dist[nx]:
                if x < parent_node[nx] or parent_node[nx] == -1:
                    parent_node[nx] = x
                    parent_edge[nx] = eid

    if need_parent:
        return dist, parent_node, parent_edge
    return dist

base_dist, par_node, par_edge = dijkstra(need_parent=True)
base = base_dist[n]

path_edges = []
cur = n
while cur != 1:
    eid = par_edge[cur]
    if eid == -1:
        print(0)
        sys.exit(0)
    path_edges.append(eid)
    cur = par_node[cur]

best_increase = 0
for eid in path_edges:
    dist2 = dijkstra(double_eid=eid, need_parent=False)
    best_increase = max(best_increase, dist2[n] - base)

print(best_increase)