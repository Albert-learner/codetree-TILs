# Please write your code here.
import sys
import heapq

INF = 10**18

n, m = map(int, input().split())
rev = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j, d = map(int, input().split())
    rev[j].append((i, d))

dist = [INF] * (n + 1)
dist[n] = 0
pq = [(0, n)]

while pq:
    cur_d, u = heapq.heappop(pq)
    if cur_d != dist[u]:
        continue
    for v, w in rev[u]:
        nd = cur_d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(max(dist[1:n]))