n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
from_list, to_list = zip(*edges) if m > 0 else ([], [])

# Please write your code here.
import heapq
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1

pq = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

answer = []
while pq:
    cur = heapq.heappop(pq)
    answer.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            heapq.heappush(pq, nxt)

if len(answer) != n:
    print(-1)
else:
    print(*answer)