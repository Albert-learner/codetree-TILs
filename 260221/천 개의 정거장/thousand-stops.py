A, B, N = map(int, input().split())

bus_fare = []
stop_count = []
bus_stops = []

for _ in range(N):
    fare, count = map(int, input().split())
    bus_fare.append(fare)
    stop_count.append(count)
    bus_stops.append(list(map(int, input().split())))

# Please write your code here.
import heapq

POINT_MAX = 1000
node_id = POINT_MAX + 1  

ride_id = [] 
for i in range(N):
    cnt = stop_count[i]
    ids = list(range(node_id, node_id + cnt))
    node_id += cnt
    ride_id.append(ids)

V = node_id  
adj = [[] for _ in range(V)]

# add edges
for i in range(N):
    fare = bus_fare[i]
    stops = bus_stops[i]
    ids = ride_id[i]
    cnt = len(stops)

    for p in range(cnt):
        cur_ride = ids[p]
        s = stops[p]

        adj[s].append((cur_ride, fare, 0))

        adj[cur_ride].append((s, 0, 0))

        if p + 1 < cnt:
            adj[cur_ride].append((ids[p + 1], 0, 1))

INF = (10 ** 30, 10 ** 30)
dist = [INF] * V
dist[A] = (0, 0)

pq = [(0, 0, A)] 
while pq:
    c, t, u = heapq.heappop(pq)
    if (c, t) != dist[u]:
        continue
    if u == B: 
        break
    for v, dc, dt in adj[u]:
        nc, nt = c + dc, t + dt
        if (nc, nt) < dist[v]:
            dist[v] = (nc, nt)
            heapq.heappush(pq, (nc, nt, v))

ans = dist[B]
if ans == INF:
    print("-1 -1")
else:
    print(ans[0], ans[1])