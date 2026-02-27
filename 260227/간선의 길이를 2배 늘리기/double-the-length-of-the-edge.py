INF = 10**30

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
                # (보통 이 문제는 최단경로가 유일한 케이스로 출제되지만)
                # 동률일 때는 "부모 정점 번호가 더 작은" 쪽으로 고정해서 경로를 안정적으로 만듭니다.
                if x < parent_node[nx] or parent_node[nx] == -1:
                    parent_node[nx] = x
                    parent_edge[nx] = eid

    if need_parent:
        return dist, parent_node, parent_edge
    return dist

# 1) 원래 최단거리 + (한 가지) 최단경로 복원
base_dist, par_node, par_edge = dijkstra(need_parent=True)
base = base_dist[n]

# 최단경로(1 -> n)에 포함된 간선 id들 추출
path_edges = []
cur = n
while cur != 1:
    eid = par_edge[cur]
    if eid == -1:
        # 문제에서 도달 가능이 보장되는 편이지만, 혹시라도 안전장치
        print(0)
        sys.exit(0)
    path_edges.append(eid)
    cur = par_node[cur]

# 2) 경로 위의 간선 하나씩 2배로 늘려보고, 최단거리 증가량의 최댓값 계산
best_increase = 0
for eid in path_edges:
    dist2 = dijkstra(double_eid=eid, need_parent=False)
    best_increase = max(best_increase, dist2[n] - base)

print(best_increase)